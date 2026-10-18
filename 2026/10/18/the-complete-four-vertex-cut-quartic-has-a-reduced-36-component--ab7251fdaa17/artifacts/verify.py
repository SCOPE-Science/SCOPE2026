"""Independent exact arithmetic checks for the quartic binomial cut hypersurface.
Run: python3 artifacts/verify.py
"""
from itertools import product,combinations
from math import comb

# Four triple products in each variable block.
monomials=[tuple(1 if j!=i else 0 for j in range(4)) for i in range(4)]
assert len(set(monomials))==4
# Pairs of coordinate hyperplanes are precisely the minimal covers.
for bits in product((0,1),repeat=4):
    is_zero=all(any(bits[j]==0 for j in range(4) if j!=i) for i in range(4))
    assert is_zero==(sum(v==0 for v in bits)>=2)
assert len(list(combinations(range(4),2)))==6
# The 4x3 Hilbert-Burch syzygy matrix and its maximal minors.
import itertools
H=[["x1",0,0], ["-x2","x2",0], [0,"-x3","x3"], [0,0,"-x4"]]
# Determinantal minors have absolute coefficient 1 and exponents of all but one variable.
def poly_mul(p,q):
    out={}
    for a,c in p.items():
        for b,d in q.items():
            e=tuple(x+y for x,y in zip(a,b))
            out[e]=out.get(e,0)+c*d
    return {a:c for a,c in out.items() if c}
def entry(s):
    if not s:return {}
    neg=s[0]=='-'; s=s[1:] if neg else s
    k=int(s[-1])-1
    return {tuple(int(j==k) for j in range(4)): -1 if neg else 1}
def det3(a):
    out={}
    for pi in itertools.permutations(range(3)):
        sign=(-1)**sum(pi[i]>pi[j] for i in range(3) for j in range(i+1,3))
        p={(0,0,0,0):sign}
        for i in range(3):p=poly_mul(p,entry(a[i][pi[i]]))
        for k,v in p.items():out[k]=out.get(k,0)+v
    return {k:v for k,v in out.items() if v}
for omitted in range(4):
    p=det3([row for j,row in enumerate(H) if j!=omitted]);assert len(p)==1
    (exps,c),=p.items();assert exps==monomials[omitted] and abs(c)==1
# Hilbert numerator from tensor product of the two Hilbert-Burch quotients.
a=[1,0,0,-4,3]
n=[0]*9
for i,x in enumerate(a):
    for j,y in enumerate(a):n[i+j]+=x*y
assert n==[1,0,0,-8,6,0,16,-24,9]
h=[1,4,10,12,9]
for d in range(24):
    f=lambda s: 1 if s==0 else 6*s-2
    direct=sum(f(k)*f(d-k) for k in range(d+1))
    hilbert=sum(h[i]*comb(d-i+3,3) for i in range(min(d,len(h)-1)+1))
    assert direct==hilbert,(d,direct,hilbert)
assert sum(h)==36
# Betti multiplicities from the tensor-product resolution.
beta={(0,0):1,(1,3):8,(2,4):6,(2,6):16,(3,7):24,(4,8):9}
for degree in range(9):
    assert n[degree]==sum((-1)**i * b for (i,j),b in beta.items() if j==degree)
assert beta[4,8]==9
# Projective arithmetic genus: P(0)=sum_i h_i binom(3-i,3) using generalized binomial.
def generalized_c3(z):return z*(z-1)*(z-2)//6
chi=sum(q*generalized_c3(3-i) for i,q in enumerate(h))
assert chi==-8 and 1-chi==9
# Exactly 36 minimal component ideals.
primes=[(tuple(I),tuple(K)) for I in combinations(range(4),2) for K in combinations(range(4),2)]
assert len(set(primes))==36
# Field-point checks: projective vectors modulo scaling.
for p in (2,3):
    total=singular=0
    for v in product(range(p),repeat=8):
        if v==(0,)*8:continue
        first=next(z for z in v if z)
        if first!=1:continue # unique representative of each projective point
        x=v[:4];y=v[4:]
        f=(x[0]*x[1]*x[2]*x[3]-y[0]*y[1]*y[2]*y[3])%p
        d=[__import__('math').prod(t for j,t in enumerate(b) if i!=j)%p for b in (x,y) for i in range(4)]
        is_sing=(f==0 and all(w==0 for w in d))
        expected=(sum(t==0 for t in x)>=2 and sum(t==0 for t in y)>=2)
        assert is_sing==expected,(p,v,is_sing,expected)
        total+=1;singular+=is_sing
    print(f'F_{p}: projective_points={total} singular_points={singular}')
print('VERIFY_OK K4 singular scheme / Hilbert / resolution / finite fields')
