"""Independent finite checks of Apéry-set length spectra for explicit generator families."""
import heapq, math
from fractions import Fraction

def ap_dist(G,m=None):
    if m is None: m=min(G)
    D=[10**20]*m
    D[0]=0
    H=[(0,0)]
    while H:
        d,r=heapq.heappop(H)
        if d!=D[r]: continue
        for g in G:
            rr=(r+g)%m; dd=d+g
            if dd<D[rr]: D[rr]=dd; heapq.heappush(H,(dd,rr))
    return D

def data(G):
    m=min(G); D=ap_dist(G); A=sorted(D)
    # The Apéry values in a residue are exactly the shortest-path distances.
    atom=[]
    for g in G:
        others=[h for h in G if h!=g]
        if g==m or not others or ap_dist(others,m)[g%m]>g:
            atom.append(g)
    L={0:{0}}
    for w in A[1:]:
        lengths=set()
        for g in atom:
            if 0<=w-g and w-g in L:
                lengths|={v+1 for v in L[w-g]}
        assert lengths,(m,G,w)
        L[w]=lengths
    return D,atom,L,{Fraction(max(v),min(v)) for v in L.values() if 0 not in v}|{Fraction(1)}

def family(m,kind):
    if kind=='unit':
        return [m,m+1]+[4*m+j for j in range(5,m)]
    if kind=='three_halves':
        return [m,m+1]+[m+j for j in range(5,m)]
    if kind=='two':
        return [m,m+1]+[2*m+j for j in range(5,m-1)]+[2*m-1]

kinds={'unit':{Fraction(1)},'three_halves':{Fraction(1),Fraction(3,2)},'two':{Fraction(1),Fraction(2)}}
for m in range(7,100):
    for kind,target in kinds.items():
        G=family(m,kind)
        D,atoms,L,R=data(G)
        assert len(G)==m-3 and len(atoms)==m-3,(m,kind,atoms,G)
        assert R==target,(m,kind,R,target)
        if kind=='unit':
            expected=[0]+[j*(m+1) for j in range(1,5)]+[4*m+j for j in range(5,m)]
        elif kind=='three_halves':
            expected=[0, m+1, 2*m+2,3*m+3,3*m+4]+[m+j for j in range(5,m)]
        else:
            expected=[0,m+1,2*m+2,3*m+3,4*m+4]+[2*m+j for j in range(5,m-1)]+[2*m-1]
        assert D==expected,(m,kind,D,expected)
print('VERIFICATION_OK: 279 family instances, multiplicities 7..99; exact Apéry values, atom counts, factorization-length spectra')
for k in kinds:
    G=family(9,k);D,A,L,R=data(G)
    print(k,'G=',G,'R=',sorted(map(str,R)),'nonunique_lengths=',{v:sorted(ls) for v,ls in L.items() if len(ls)>1})
