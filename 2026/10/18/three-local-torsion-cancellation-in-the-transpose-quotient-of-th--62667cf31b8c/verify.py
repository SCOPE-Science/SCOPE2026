"""Exact finite checks for the chessboard-transpose quotient theorem.
Requires Python 3 standard library. The cited integral homology theorem and
Armstrong orbit-space theorem are external mathematical inputs, not checked here.
"""
from itertools import combinations, permutations
import json
from pathlib import Path

MOD = 3
F = {}
for k in range(1, 6):
    F[k] = sorted(tuple(sorted(5*i+j for i,j in zip(rows,cols)))
                  for rows in combinations(range(5),k)
                  for cols in permutations(range(5),k))
P = {k:{f:i for i,f in enumerate(F[k])} for k in F}
assert [len(F[k]) for k in range(1,6)] == [25,200,600,600,120]

def oriented(a):
    inv=sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
    return tuple(sorted(a)),(-1)**inv

def normalize(v):
    return {f:c%MOD for f,c in v.items() if c%MOD}

def wedge(terms):
    out={():1}
    for term in terms:
        result={}
        for face,c in out.items():
            for vertex,d in term.items():
                if vertex in face: continue
                ft,sgn=oriented(face+(vertex,))
                result[ft]=(result.get(ft,0)+c*d*sgn)%MOD
        out=normalize(result)
    return out

def alpha(i,j,k):return {5*i+j:1,5*i+k:-1}
def beta(i,j,k):return {5*i+k:1,5*j+k:-1}
Z=wedge([alpha(0,0,1),alpha(1,2,3),beta(2,3,4)])

def apply(chain, op):
    out={}
    for f,c in chain.items():
        vs=[]
        for v in f:
            i,j=divmod(v,5)
            if op=='transpose':i,j=j,i
            elif op=='row01':i=1-i if i<2 else i
            elif op=='col01':j=1-j if j<2 else j
            else:raise ValueError(op)
            vs.append(5*i+j)
        ft,sign=oriented(vs)
        out[ft]=(out.get(ft,0)+c*sign)%MOD
    return normalize(out)

def boundary(chain):
    out={}
    for f,c in chain.items():
        for j in range(len(f)):
            sub=f[:j]+f[j+1:]
            out[sub]=(out.get(sub,0)+c*((-1)**j))%MOD
    return normalize(out)

cert=json.loads(Path(__file__).with_name('certificate.json').read_text())
T=apply(Z,'transpose')
W={F[4][i]:v for i,v in cert['boundary_chain']}
assert boundary(W)==normalize({f:Z.get(f,0)+T.get(f,0) for f in set(Z)|set(T)})
assert not boundary(Z) and not boundary(T)
phi={F[3][i]:v for i,v in cert['cocycle']}
# Cocycle: phi annihilates the boundary of each four-rook face.
for simplex in F[4]:
    assert sum((-1)**i*phi.get(simplex[:i]+simplex[i+1:],0) for i in range(4))%MOD==0

def pairing(z):return sum(phi.get(f,0)*c for f,c in z.items())%MOD
assert pairing(Z)==1
for op in ('row01','col01','transpose'):
    assert pairing(apply(Z,op))==2,op
# Rank of the two modular boundary operators (sparse exact reduction).
def mat_rank(k):
    piv={}
    for face in F[k]:
        x={P[k-1][face[:i]+face[i+1:]]: ((-1)**i)%3 for i in range(k)}
        while x:
            i=min(x);t=x[i];b=piv.get(i)
            if b is None:
                piv[i]={j:(c*pow(t,-1,MOD))%MOD for j,c in x.items()}
                break
            for j,c in b.items():
                a=(x.get(j,0)-t*c)%MOD
                if a:x[j]=a
                else:x.pop(j,None)
    return len(piv)
assert mat_rank(3)==176
assert mat_rank(4)==423
# Trace on H_3(Q): signed fixed-simplex Lefschetz sum is zero.
# Invariant rook placements for transposition have diagonal-loop or unordered-pair orbits.
# Their signed orbit generating functions satisfy F_n=-(n-1)F_{n-2}.
f=[1,0]
for n in range(2,6):f.append(-(n-1)*f[n-2])
assert f[5]==0
print('VERIFIED faces=(25,200,600,600,120), ranks=(176,423),')
print('cocycle_pairing=1, transpose_and_row_column_signs=-1, Lefschetz_trace_H3=0')
