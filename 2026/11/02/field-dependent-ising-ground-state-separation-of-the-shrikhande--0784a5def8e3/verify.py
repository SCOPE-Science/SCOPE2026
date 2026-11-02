#!/usr/bin/env python3
"""Finite exact independent ground-state census for two 16-site spin networks."""
from collections import defaultdict
from fractions import Fraction
from itertools import product

SIDE=4
N=SIDE*SIDE
STEP={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
TARGET={
  'Shrikhande':([0,6,12,18,24,26,30,30,32],[1,16,72,96,16,432,32,816,42]),
  'Rook':([0,6,12,18,24,26,28,30,32],[1,16,72,96,24,432,1224,816,90]),
}

def vertex_graph(kind):
    e=set()
    for u in range(N):
        i,j=divmod(u,SIDE)
        for v in range(u+1,N):
            x,y=divmod(v,SIDE)
            if kind=='Shrikhande':
                isedge=((x-i)%4,(y-j)%4) in STEP
            else:
                isedge=(x==i or y==j)
            if isedge:e.add((u,v))
    assert len(e)==48
    nbr=[0]*N
    for u,v in e:
        nbr[u]|=1<<v
        nbr[v]|=1<<u
    assert all(n.bit_count()==6 for n in nbr)
    # Exact strong regularity: A^2=4I+2(ones matrix).
    for u in range(N):
        for v in range(N):
            common=(nbr[u]&nbr[v]).bit_count()
            assert common==(6 if u==v else 2)
    return nbr

def enumerate_gray(nbr):
    # Incremental updates after one bit flip; never inspect all edges of a state.
    count=[defaultdict(int) for _ in range(N+1)]
    prev=0
    r=cut=0
    count[0][0]=1
    for k in range(1,1<<N):
        mask=k^(k>>1)
        changed=mask^prev
        assert changed.bit_count()==1
        v=changed.bit_length()-1
        ones=(nbr[v]&prev).bit_count()
        if prev&(1<<v):
            cut+=2*ones-6
            r-=1
        else:
            cut+=6-2*ones
            r+=1
        count[r][cut]+=1
        prev=mask
    assert sum(sum(d.values()) for d in count)==(1<<N)
    return count

def row_contributions(kind):
    hh=[]
    for a in range(16):
        if kind=='Shrikhande':
            hh.append(sum(((a>>j)^(a>>((j+1)%4)))&1 for j in range(4)))
        else:
            hh.append(sum(((a>>j)^(a>>k))&1 for j in range(4) for k in range(j+1,4)))
    cross={}
    for a in range(16):
        for b in range(16):
            if kind=='Shrikhande':
                cross[a,b]=sum(((a>>j)^(b>>j))&1 for j in range(4))+sum(((a>>j)^(b>>((j+1)%4)))&1 for j in range(4))
            else:
                cross[a,b]=sum(((a>>j)^(b>>j))&1 for j in range(4))
    return hh,cross

def enumerate_rows(kind):
    # Independent row-by-row formula: no graph-edge list and no Gray-code updates.
    hh,cross=row_contributions(kind)
    count=[defaultdict(int) for _ in range(N+1)]
    for a,b,c,d in product(range(16),repeat=4):
        r=a.bit_count()+b.bit_count()+c.bit_count()+d.bit_count()
        cut=hh[a]+hh[b]+hh[c]+hh[d]
        if kind=='Shrikhande':
            cut+=cross[a,b]+cross[b,c]+cross[c,d]+cross[d,a]
        else:
            cut+=cross[a,b]+cross[a,c]+cross[a,d]+cross[b,c]+cross[b,d]+cross[c,d]
        count[r][cut]+=1
    assert sum(sum(x.values()) for x in count)==(1<<N)
    return count

def ground_profile(count):
    best=[max(d) for d in count]
    multiplicity=[count[r][best[r]] for r in range(17)]
    return best,multiplicity

def phase(count, h):
    best,multiplicity=ground_profile(count)
    optimum=max(Fraction(best[r])-h*r for r in range(17))
    rs=[r for r in range(17) if Fraction(best[r])-h*r==optimum]
    return rs,sum(multiplicity[r] for r in rs)

def check():
    expected={
      'Shrikhande':[(Fraction(0),[8],42),(Fraction(1),[6,8],74),(Fraction(2),[6],32),(Fraction(3),[4,6],48),(Fraction(4),[4],16),(Fraction(6),[0,1,2,3,4],201),(Fraction(7),[0],1)],
      'Rook':[(Fraction(0),[8],90),(Fraction(1),[8],90),(Fraction(2),[4,5,6,7,8],2586),(Fraction(3),[4],24),(Fraction(6),[0,1,2,3,4],209),(Fraction(7),[0],1)]
    }
    for kind in TARGET:
        nbr=vertex_graph(kind)
        a=enumerate_gray(nbr)
        b=enumerate_rows(kind)
        assert a==b,kind
        B,C=ground_profile(a)
        witnesses=({'Shrikhande':{4:0x0505,5:0x0345,6:0x152c,7:0x070f,8:0x0f0f},
                    'Rook':{4:0x1248,5:0x112c,6:0x116a,7:0x136c,8:0x33cc}})[kind]
        for r,mask in witnesses.items():
            assert mask.bit_count()==r
            interior_edges=sum((nbr[u]&mask).bit_count() for u in range(N) if mask&(1<<u))//2
            assert 6*r-2*interior_edges==B[r]
        for r in range(17):
            assert sum(a[r].values())==__import__('math').comb(16,r)
        eb,ec=TARGET[kind]
        assert B[:9]==eb,(kind,B)
        assert C[:9]==ec,(kind,C)
        assert B==B[::-1] and C==C[::-1]
        for h,rs,n in expected[kind]:
            got=phase(a,h)
            assert got==(rs,n),(kind,h,got,(rs,n))
        for r in range(9):
            assert sum(a[r].values())==__import__('math').comb(16,r)
        print(kind, 'half cut extrema',B[:9],'half degeneracies',C[:9])
    print('VERIFY_OK 65536 configurations/graph; two independent enumeration algorithms; exact spectra and plateaux')

if __name__=='__main__':check()
