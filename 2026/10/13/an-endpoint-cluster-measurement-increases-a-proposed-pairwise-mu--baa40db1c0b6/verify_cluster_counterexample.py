from fractions import Fraction
import sympy as sp
from itertools import product, combinations

N=4
basis=list(product([0,1], repeat=N))
idx={x:i for i,x in enumerate(basis)}

def cluster_rho(measured=None):
    # exact density matrix for C4, or a normalized post-Z-measurement branch on qubit 1.
    if measured is None:
        allowed=basis; norm=Fraction(1,16)
    else:
        allowed=[x for x in basis if x[0]==measured]; norm=Fraction(1,8)
    rho=[[Fraction(0) for _ in range(16)] for _ in range(16)]
    def sign(x):
        return -1 if (x[0]*x[1]+x[1]*x[2]+x[2]*x[3])%2 else 1
    for x in allowed:
        for y in allowed:
            rho[idx[x]][idx[y]]=norm*sign(x)*sign(y)
    return rho

def reduce(rho, keep):
    keep=tuple(keep); drop=tuple(i for i in range(N) if i not in keep)
    out_basis=list(product([0,1],repeat=len(keep)))
    oi={x:i for i,x in enumerate(out_basis)}
    m=len(out_basis)
    out=[[Fraction(0) for _ in range(m)] for _ in range(m)]
    for a in out_basis:
      for b in out_basis:
        s=Fraction(0)
        for d in product([0,1],repeat=len(drop)):
          x=[0]*N; y=[0]*N
          for j,q in enumerate(keep): x[q]=a[j]; y[q]=b[j]
          for j,q in enumerate(drop): x[q]=d[j]; y[q]=d[j]
          s += rho[idx[tuple(x)]][idx[tuple(y)]]
        out[oi[a]][oi[b]]=s
    return sp.Matrix([[sp.Rational(v.numerator,v.denominator) for v in row] for row in out])

def spectrum(M):
    ev=M.eigenvals()
    vals=[]
    for v,m in ev.items(): vals += [sp.simplify(v)]*m
    return sorted(vals,key=lambda z: float(z))

def S_from_spectrum(vals):
    # All spectra here contain only 0, 1/4, 1/2, 1; use exact base-2 entropies.
    ans=sp.Integer(0)
    for v in vals:
        if v==0: continue
        if v==1: term=0
        elif v==sp.Rational(1,2): term=sp.Rational(1,2)
        elif v==sp.Rational(1,4): term=sp.Rational(1,2)
        else: raise AssertionError(f'unexpected eigenvalue {v}')
        ans += term
    return sp.simplify(ans)

def pair_MI(rho,i,j):
    si=S_from_spectrum(spectrum(reduce(rho,[i])))
    sj=S_from_spectrum(spectrum(reduce(rho,[j])))
    sij=S_from_spectrum(spectrum(reduce(rho,[i,j])))
    return sp.simplify(si+sj-sij), spectrum(reduce(rho,[i,j]))

rho=cluster_rho()
expected_initial={(0,1):1,(2,3):1,(0,2):0,(0,3):0,(1,2):0,(1,3):0}
initial={}
for p in combinations(range(4),2):
    mi,spec=pair_MI(rho,*p); initial[p]=mi
    assert mi==expected_initial[p], (p,mi,spec)
assert sum(initial.values(),sp.Integer(0))==2
M0=sp.Rational(1,6)*sum(initial.values(),sp.Integer(0)) # M_Fr=(1/6) sum I
assert M0==sp.Rational(1,3)

for z in [0,1]:
    rz=cluster_rho(z)
    post={}
    for p in combinations(range(4),2):
        mi,spec=pair_MI(rz,*p); post[p]=mi
    for p in [(1,2),(1,3),(2,3)]: assert post[p]==1, (z,p,post[p])
    for p in [(0,1),(0,2),(0,3)]: assert post[p]==0, (z,p,post[p])
    assert sum(post.values(),sp.Integer(0))==3
    Mz=sp.Rational(1,6)*sum(post.values(),sp.Integer(0))
    assert Mz==sp.Rational(1,2)

print('VERIFY_OK initial_M=1/3 branch_M=1/2 average_post=1/2 gap=1/6 ratio=3/2')
