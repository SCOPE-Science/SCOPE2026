"""Exact checks for reciprocal-dyad and directed-cycle covariance in row-regular random digraphs.
Standard-library Python 3; run with: python verify.py
"""
from itertools import combinations, permutations, product
from fractions import Fraction
from math import factorial

# Sparse three-variable polynomial arithmetic, exponent order: (n,k,ell).
class Poly:
    def __init__(self, terms):
        self.t = {e: c for e,c in terms.items() if c}
    @staticmethod
    def scalar(v): return Poly({(0,0,0):v})
    def __add__(self, other):
        if not isinstance(other,Poly): other=Poly.scalar(other)
        t=self.t.copy()
        for e,c in other.t.items(): t[e]=t.get(e,0)+c
        return Poly(t)
    __radd__=__add__
    def __neg__(self):return Poly({e:-c for e,c in self.t.items()})
    def __sub__(self,other):return self+-other if isinstance(other,Poly) else self+(-other)
    def __rsub__(self,other):return -self+other
    def __mul__(self,other):
        if not isinstance(other,Poly):other=Poly.scalar(other)
        t={}
        for e,c in self.t.items():
            for f,d in other.t.items():
                g=tuple(e[i]+f[i] for i in range(3));t[g]=t.get(g,0)+c*d
        return Poly(t)
    __rmul__=__mul__
    def __pow__(self,p):
        assert isinstance(p,int) and p>=0
        out=Poly.scalar(1)
        for _ in range(p):out=out*self
        return out
    def __eq__(self,other):return self.t==(other.t if isinstance(other,Poly) else Poly.scalar(other).t)

n=Poly({(1,0,0):1});k=Poly({(0,1,0):1});ell=Poly({(0,0,1):1})
# Multiply the three-class overlap identity by 2*k^2*(n-2)^2.
L=(n-ell)*2*k*(n-2)*((k-1)*(n-1)-k*(n-2))
L+=2*(n-2)*((k-1)*(n-1)**2-k**2*(n-2))
L+=(ell-3)*((k-1)**2*(n-1)**2-k**2*(n-2)**2)
R=(k-n+1)**2*(ell-2*n+1)
assert L==R, 'polynomial identity failure'
print('POLYNOMIAL_IDENTITY_PASS', len(L.t), 'nonzero monomials')

# Directly compute a mixed expectation from arbitrary overlapping prescribed arc sets.
# Independent rows choose uniform k-subsets of n-1 potential neighbors.
def prob_requirements(req,n,k):
    ans=Fraction(1)
    for u, out in enumerate(req):
        t=len(out)
        if t>k:return Fraction(0)
        ans*=Fraction(factorial(k)*factorial(n-1-t), factorial(k-t)*factorial(n-1))
    return ans

def exact_formula(n,k,ell):
    nfall=factorial(n)//factorial(n-ell)
    return Fraction(-nfall*k**ell*(n-k-1)**2*(2*n-ell-1),2*(n-1)**(ell+2)*(n-2)**2)

def from_overlap_events(n,k,ell):
    arr=list(range(n))
    cycles=[tup for tup in permutations(arr,ell) if tup[0]==min(tup)]
    pairs=list(combinations(arr,2))
    p=Fraction(k,n-1)
    indep=p**(ell+2)
    total=Fraction(0)
    for cyc in cycles:
        edges=[(cyc[i],cyc[(i+1)%ell]) for i in range(ell)]
        for u,v in pairs:
            req=[set() for _ in range(n)]
            for a,b in edges+[(u,v),(v,u)]:req[a].add(b)
            total+=prob_requirements(req,n,k)-indep
    return total

checked=0
for N in range(3,8):
    for K in range(1,N):
        for E in range(3,N+1):
            actual=from_overlap_events(N,K,E)
            expected=exact_formula(N,K,E)
            assert actual==expected,(N,K,E,actual,expected)
            checked+=1
print('EVENT_EXACT_PROBABILITY_PASS', checked, 'strata')

# Enumerate all full digraphs for low n, independently of the event formula.
checked=0
for N in range(3,6):
    for K in range(1,N):
        opts=[list(combinations((v for v in range(N) if v!=u),K)) for u in range(N)]
        sample_size=1
        for op in opts:sample_size*=len(op)
        cycles={E:[t for t in permutations(range(N),E) if t[0]==min(t)] for E in range(3,N+1)}
        mean2=0; mean={E:0 for E in cycles}; mixed={E:0 for E in cycles}
        for choice in product(*opts):
            arcs=[set(t) for t in choice]
            C2=sum(v in arcs[u] and u in arcs[v] for u in range(N) for v in range(u+1,N))
            mean2+=C2
            for E,cycs in cycles.items():
                count=sum(all(t[(i+1)%E] in arcs[t[i]] for i in range(E)) for t in cycs)
                mean[E]+=count; mixed[E]+=C2*count
        for E in cycles:
            actual=Fraction(mixed[E],sample_size)-Fraction(mean2*mean[E],sample_size**2)
            assert actual==exact_formula(N,K,E),(N,K,E,actual)
            checked+=1
print('EXHAUSTIVE_DIGRAPHS_PASS',checked,'strata')
print('VERIFY_OK')
