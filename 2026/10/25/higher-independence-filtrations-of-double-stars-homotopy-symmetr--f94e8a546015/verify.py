"""Exact finite checks for higher independence complexes of double stars.
Only standard Python; no external documents or runtime dependencies.
"""
from itertools import combinations, permutations, product
from math import comb


def graph(a,b):
    n=a+b+2
    A=range(2,2+a); B=range(2+a,n)
    edges=[(0,1)]+[(0,x) for x in A]+[(1,x) for x in B]
    return n,edges

def allowed(S,edges,r):
    parent={v:v for v in S}
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    for u,v in edges:
        if u in parent and v in parent:
            x,y=find(u),find(v)
            parent[x]=y
    sizes={}
    for v in S:
        z=find(v);sizes[z]=sizes.get(z,0)+1
    return max(sizes.values(), default=0)<=r

def faces(a,b,r):
    n,edges=graph(a,b)
    return {tuple(S) for k in range(n+1) for S in combinations(range(n),k) if allowed(S,edges,r)}

def gf2rank(cols):
    piv={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else: piv[p]=v;break
    return len(piv)

def bettis(F):
    bysize={}
    for f in F:bysize.setdefault(len(f),[]).append(f)
    ranks={}
    for k in range(1,max(bysize)+1):
        lower={f:i for i,f in enumerate(bysize.get(k-1,[]))}
        cols=[]
        for f in bysize.get(k,[]):
            v=0
            for x in f:
                ff=tuple(y for y in f if y!=x)
                v ^= (1<<lower[ff])
            cols.append(v)
        ranks[k]=gf2rank(cols)
    return {k-1:len(fs)-ranks.get(k,0)-ranks.get(k+1,0)
            for k,fs in bysize.items() if k and len(fs)-ranks.get(k,0)-ranks.get(k+1,0)}

def parity_in_face(face,g):
    p=[g[x] for x in face];return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def reduced_lefschetz(F,g):
    out=-1
    for face in F:
        if face and tuple(sorted(g[x] for x in face))==face:
            out+=(-1 if len(face)%2==0 else 1)*parity_in_face(face,g)
    return out

def wedge_character(g,n,k):
    # coefficient of t**k in det(I+t*g on augmentation lattice)
    # det(I+t*g on natural permutation module) divided by (1+t).
    leaf=[g[x]-2 for x in range(2,n)]
    N=n-2;seen=set();poly=[1]+[0]*N
    for i in range(N):
        if i in seen: continue
        x=i;l=0
        while x not in seen:
            seen.add(x);l+=1;x=leaf[x]
        # factor 1-(-t)**l
        for deg in range(N,l-1,-1):poly[deg]-=(-1)**l*poly[deg-l]
    # divide by (1+t) coefficientwise
    quotient=[0]*N
    for j in range(N):quotient[j]=poly[j]-(quotient[j-1] if j else 0)
    return quotient[k]

def actions(a,b):
    n,_=graph(a,b)
    for pa in permutations(range(a)):
        for pb in permutations(range(b)):
            g=list(range(n))
            for i,x in enumerate(pa):g[2+i]=2+x
            for i,x in enumerate(pb):g[2+a+i]=2+a+x
            yield g,False
            if a==b:
                h=g[:];h[0],h[1]=1,0
                for i in range(a):
                    h[2+i]=2+a+pa[i]
                    h[2+a+i]=2+pb[i]
                yield h,True

checks=0;faces_seen=0;char_checks=0
for a in range(1,4):
    for b in range(1,4):
        n=a+b+2;N=a+b
        for r in range(1,n+1):
            F=faces(a,b,r);faces_seen+=len(F)-1
            expected={} if r==1 or r>=n else {r-1:comb(N-1,r-2)}
            observed=bettis(F)
            assert observed==expected,(a,b,r,'betti',observed,expected)
            checks+=1
            for g,swap in actions(a,b):
                assert {tuple(sorted(g[x] for x in f)) for f in F}==F,(a,b,r,'not automorphism')
                got=reduced_lefschetz(F,g)
                if not expected: want=0
                else:
                    tr=wedge_character(g,n,r-2)*(-1 if swap else 1)
                    want=(-1)**(r-1)*tr
                assert got==want,(a,b,r,'character',g,got,want)
                char_checks+=1
print('VERIFY_OK configs=%s nonempty_faces=%s signed_lefschetz_checks=%s'%(checks,faces_seen,char_checks))
