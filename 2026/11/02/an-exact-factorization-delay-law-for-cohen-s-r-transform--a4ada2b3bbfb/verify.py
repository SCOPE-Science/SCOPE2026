import sympy as s
from sympy import symbols, Poly
from functools import lru_cache
from itertools import product
from math import prod
x=s.symbols('x')

def polynormal(p,poly):
    P=Poly(poly,x,modulus=p)
    return tuple(int(v)%p for v in P.all_coeffs())

def fromtuple(coeffs):
    return s.Add(*(c*x**(len(coeffs)-1-i) for i,c in enumerate(coeffs)))

@lru_cache(None)
def offspring(p, f):
    n=len(f)-1
    assert f[0]==1
    R=0
    # coeff f highest degree first
    for i,c in enumerate(f):
        m=n-i
        R += c * 2**i * x**i * (x*x+1)**m
    P=Poly(R,x,modulus=p)
    assert P.degree()==2*n and P.LC()==1
    factors, mult=s.factor_list(P,modulus=p)[1],[]
    fs=[]
    for fp, exp in factors:
        fs += [polynormal(p,fp.as_expr())]*exp
    if len(fs)==1:
        assert len(fs[0])==2*n+1
        return None
    assert len(fs)==2 and all(len(z)==n+1 for z in fs) and len(set(fs))==2,(p,f,fs)
    return tuple(fs)

def mu(n): return int(s.mobius(n))
def e2(n):
    v=0
    while n%2==0: v+=1;n//=2
    return v

def prediction(p,n):
    e=e2(p**n-1)
    count=[]
    for v in range(e+1):
        a=0
        for d in s.divisors(n):
            d=int(d)
            ed=e2(p**d-1)
            od=(p**d-1)//(2**ed)
            if v==0:b=od
            elif v<=ed:b=od*2**(v-1)
            else:b=0
            a+=mu(n//d)*b
        assert a%n==0,(p,n,v,a)
        count.append(a//n)
    return list(reversed(count))

def main():
    total=0
    for p,n in [(3,2),(3,3),(3,4),(3,5),(5,2),(5,3),(7,2),(7,3),(11,2)]:
        e=e2(p**n-1)
        polys=[]
        for cs in product(range(p), repeat=n):
            f=(1,)+cs
            if Poly(fromtuple(f),x,modulus=p).is_irreducible:
                polys.append(f)
        @lru_cache(None)
        def mincost(f):
            # finite breadth-first, avoids any cycle from periodic branch
            frontier={f}
            for cost in range(e+2):
                foll=set()
                for g in frontier:
                    children=offspring(p,g)
                    if children is None:
                        return cost
                    foll.update(children)
                frontier=foll
            raise AssertionError((p,n,f))
        actual=[0]*(e+1)
        periodic_count=0
        for f in polys:
            j=mincost(f)
            assert j<=e,(p,n,f,j)
            actual[j]+=1
            if j==e:
                periodic_count+=1
            children=offspring(p,f)
            if j==0:
                assert children is None
            elif j<e:
                assert children is not None and all(mincost(g)==j-1 for g in children),(p,n,f,j,children)
            else:
                assert children is not None and sorted([mincost(g) for g in children])==[e-1,e],(p,n,f,children)
        theory=prediction(p,n)
        assert actual==theory,(p,n,actual,theory)
        N=len(polys)
        exactmean=sum(j*actual[j] for j in range(e+1))+actual[e] # randomized extra unit when periodic
        den=sum(mu(n//int(d))*(p**int(d)) for d in s.divisors(n))
        assert den==n*N
        etarget=sum(mu(n//int(d))*(p**int(d)-1)*(e-e2(p**int(d)-1)+1) for d in s.divisors(n))
        assert exactmean*n==etarget,(p,n,exactmean,n,etarget)
        if n%2: assert exactmean==N
        else: assert exactmean<N
        total+=N
        print(f'p={p},n={n},e={e},irreducibles={N},counts_by_splits={actual},mean={exactmean}/{N}')
    print(f'CHECK_OK total_irreducibles={total}, complete_finite_field_polynomial_factorizations=1, random_branch_transition_certificates=1')
if __name__=='__main__':main()

# Additional exact arithmetic cross-checks for proper prime powers.  These
# verify all count and mean identities, not polynomial factorization there.
if __name__=='__main__':
    cases=0
    for q in (9,25,27,49,81,125):
        for n in range(2,26):
            a=prediction(q,n)
            e=e2(q**n-1)
            assert len(a)==e+1
            den=sum(mu(n//int(d))*q**int(d) for d in s.divisors(n))
            assert den % n==0 and sum(a)==den//n
            lhs=(sum(j*a[j] for j in range(e+1))+a[e])*n
            rhs=sum(mu(n//int(d))*(q**int(d)-1)*(e-e2(q**int(d)-1)+1) for d in s.divisors(n))
            assert lhs==rhs,(q,n,lhs,rhs)
            if n%2:assert lhs==den
            else:assert lhs<den
            cases+=1
    print('PRIME_POWER_ARITHMETIC_OK parameter_pairs=',cases)
