"""Exact finite single-site random sequential adsorption checks; standard library only."""
from functools import lru_cache
from fractions import Fraction
from math import exp

def moments(n,hub_even=False,all_spokes=False, lam=1):
    N=2*n+1
    ns=[0]*N
    for v in range(2*n):
        for w in ((v-1)%(2*n),(v+1)%(2*n)):ns[v]|=1<<w
    for v in range(2*n):
        if all_spokes or (hub_even and v%2==0):
            ns[v]|=1<<(2*n);ns[2*n]|=1<<v
    rates=[1]*(2*n)+[lam]
    @lru_cache(None)
    def f(mask):
        if not mask:return (Fraction(0),Fraction(0))
        r=sum(rates[v] for v in range(N) if mask>>v&1)
        a=b=Fraction(0)
        for v in range(N):
            if not mask>>v&1:continue
            x,y=f(mask&~((1<<v)|ns[v]))
            p=Fraction(rates[v],r)
            a+=p*(1+x)
            b+=p*(1+2*x+y)
        return a,b
    return f((1<<N)-1)
def base_moments(n):
    N=2*n;ns=[(1<<((v-1)%N)) |(1<<((v+1)%N)) for v in range(N)]
    @lru_cache(None)
    def f(mask):
        if not mask:return(Fraction(0),Fraction(0))
        r=mask.bit_count();a=b=Fraction(0)
        for v in range(N):
            if mask>>v&1:
                x,y=f(mask&~((1<<v)|ns[v]));a+=(1+x)/r;b+=(1+2*x+y)/r
        return a,b
    return f((1<<N)-1)


def run_checks():
    import itertools
    from math import exp
    tests=0
    for m in range(2,7):
        mu, second=base_moments(m)
        for lam in (1,2):
            for gear, wheel in ((True,False),(False,True)):
                u, sq=moments(m,hub_even=gear,all_spokes=wheel,lam=lam)
                assert (u>mu) if gear else (u<mu)
                assert sq-u*u>0
                tests+=3
                if wheel:
                    p=Fraction(lam,2*m+lam)
                    assert u == (1-p)*mu+p
                    assert sq-u*u == (1-p)*(second-mu*mu)+p*(1-p)*(mu-1)**2
                    tests+=2
    # The hub acceptance event is checked independently against chronological
    # deposition on the augmented and unaugmented graphs for every ordering.
    for m in (2,3):
        n=2*m
        for perm in itertools.permutations(range(n+1)):
            rim=[set(((i-1)%n,(i+1)%n)) for i in range(n)]
            base=set()
            for x in perm:
                if x<n and not any(v in base for v in rim[x]):base.add(x)
            first_even=min(perm.index(i) for i in base if i%2==0) if any(i%2==0 for i in base) else len(perm)
            for wheel in (False,True):
                nbr=[set(y) for y in rim]+[set()]
                for i in range(n):
                    if wheel or i%2==0:
                        nbr[i].add(n);nbr[n].add(i)
                occupied=set()
                for x in perm:
                    if not any(v in occupied for v in nbr[x]):occupied.add(x)
                if wheel:
                    expected=1 if perm[0]==n else len(base)
                else:
                    expected=m+1 if perm.index(n)<first_even else len(base)
                assert len(occupied)==expected,(m,perm,wheel,base,occupied)
                tests+=1
    print('VERIFICATION_OK exact_recursion_and_exhaustive_eventwise_checks=',tests)
    print('asymptotic_coefficients',{'gear_mean':exp(-2),'wheel_mean':-(1-exp(-2))/2,
     'gear_var_per_pair':exp(-4),'wheel_var_per_pair':(1-exp(-2))**2/2})

if __name__=='__main__':
    run_checks()
