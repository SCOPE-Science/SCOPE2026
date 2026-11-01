"""Finite exact diagnostics for repeated Minkowski averages of orthotope skeleta."""
from itertools import product, combinations
from math import comb, sqrt
from fractions import Fraction

def test_sumsets():
    checked=0
    cases=[]
    for d,q,m in [(2,3,1),(2,3,2),(2,2,3),(3,2,1),(3,2,2),(3,2,3),(4,1,2),(4,2,2)]:
        V=list(product(range(-q,q+1),repeat=d))
        for k in range(d):
            S={p for p in V if sum(abs(v)!=q for v in p)<=k}
            sums={(0,)*d}
            for _ in range(m):
                sums={tuple(a+b for a,b in zip(u,v)) for u in sums for v in S}
            universe=product(range(-m*q,m*q+1),repeat=d)
            predicted={z for z in universe if sum((v+m*q)%(2*q)!=0 for v in z)<=min(d,m*k)}
            assert sums==predicted, (d,k,q,m,len(sums),len(predicted))
            checked+=len(predicted)
            cases.append((d,k,m,q,len(sums)))
    return checked,cases

def cell_sets(d,m,j):
    # A cell coordinate is a vertex (0, index) or open interval (1, index).
    out=[]
    for free in combinations(range(d),j):
        fs=set(free)
        for coord in product(*[range(m) if i in fs else range(m+1) for i in range(d)]):
            out.append(tuple((int(i in fs),coord[i]) for i in range(d)))
    return out

def rank_mod2(cols):
    pivots={}
    for col in cols:
        while col:
            pivot=col.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=col;break
            col ^= pivots[pivot]
    return len(pivots)

def boundary_rank(cells_j,cells_j_minus,d):
    if not cells_j:return 0
    idminus={c:i for i,c in enumerate(cells_j_minus)}
    cols=[]
    for c in cells_j:
        bits=0
        for i,(typ,index) in enumerate(c):
            if typ:
                for v in (index,index+1):
                    cc=c[:i]+((0,v),)+c[i+1:]
                    bits ^= 1<<idminus[cc]
        cols.append(bits)
    return rank_mod2(cols)

def test_topology():
    checks=[]
    for d in range(2,5):
        for m in range(1,4 if d<=3 else 3):
            allcells=[cell_sets(d,m,j) for j in range(d+1)]
            ranks=[0]+[boundary_rank(allcells[j],allcells[j-1],d) for j in range(1,d+1)]
            for t in range(d):
                bs=[]
                for j in range(t+1):
                    b=len(allcells[j])-ranks[j]-(ranks[j+1] if j<t else 0)
                    if j==0:b-=1
                    bs.append(b)
                expected=sum((-1)**(j-t-1)*comb(d,j)*m**j*(m+1)**(d-j) for j in range(t+1,d+1))
                assert bs[t]==expected and all(b==0 for b in bs[:-1]),(d,m,t,bs,expected)
                checks.append((d,m,t,expected))
    return checks

def test_metric():
    # Independent exhaustive lattice nearest-set distances for dimensions <=3.
    count=0
    for d,m,k,axes in [(2,2,0,(1,3)),(2,2,1,(1,3)),(3,2,1,(2,3,5)),(3,2,0,(2,3,5)),(3,3,1,(1,2,3)),(3,3,0,(1,2,3))]:
        r=max(0,d-m*k)
        caps=sorted(axes)[:r]
        assert sum(a*a for a in caps)>=0
        # Grid midpoints are exact distance-maximizers.
        y=tuple(Fraction(a, m)*(1 if m%2==1 else 1) for a in axes)
        # For odd m midpoint a/m is on cell midpoint; for even m also.
        distances=[]
        for axis,z in zip(axes,y):
            G=[Fraction(axis*(-m+2*i),m) for i in range(m+1)]
            dist=min(abs(z-g) for g in G)
            distances.append(dist)
        # y=a/m for odd m? In m=3, a/3 IS GRID (-a,-a/3,a/3,a) -> choose y=0 instead.
        y=tuple(Fraction(0) if m%2 else Fraction(a,m) for a in axes)
        distances=[]
        for axis,z in zip(axes,y):
            G=[Fraction(axis*(-m+2*i),m) for i in range(m+1)]
            distances.append(min(abs(z-g) for g in G))
        closest_sq=sum(sorted(a*a for a in distances)[:r])
        claimed_sq=Fraction(sum(a*a for a in caps),m*m)
        assert closest_sq==claimed_sq,(d,m,k,distances,closest_sq,claimed_sq)
        count+=1
    return count

if __name__=='__main__':
    checked,cases=test_sumsets()
    topo=test_topology()
    metric=test_metric()
    print('exact sumset membership points:',checked,'cases:',len(cases))
    print('cellular mod2 topology cases:',len(topo),'examples:',topo[-8:])
    print('metric deep-hole tests:',metric)
    print('PASS')
