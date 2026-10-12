"""Independent finite coalescent merger enumeration and covariance-profile checks."""
from fractions import Fraction as F
from math import comb, log


def theory(n,r):
    return sum((F(4*k*comb(n-r-1,k-2), comb(n-1,k-1)*k*k*(k-1)*(k-1))
                for k in range(2,n-r+2)),F(0))


def enumerated_counts(n):
    # Propagate *exact* state probabilities, enumerating all pair-merger transitions.
    state = {tuple((i,) for i in range(n)): F(1)}
    a = {}
    for k in range(n,1,-1):
        assert all(len(s)==k for s in state)
        a[k] = {r:sum((w*sum(len(block)==r for block in s)
                         for s,w in state.items()), F(0))
                for r in range(1,n)}
        next_state = {}
        for s,w in state.items():
            for i in range(k):
                for j in range(i+1,k):
                    merged = tuple(sorted(s[i]+s[j]))
                    nxt = tuple(sorted([x for h,x in enumerate(s) if h!=i and h!=j] + [merged]))
                    next_state[nxt] = next_state.get(nxt,F(0)) + w/F(comb(k,2))
        assert sum(next_state.values(),F(0))==1
        state=next_state
    return a

checks=0
for n in range(2,9):
    d=enumerated_counts(n)
    for r in range(1,n):
        direct = sum((F(4)*d[k][r]/(k*k*(k-1)*(k-1)) for k in d),F(0))
        assert direct == theory(n,r),(n,r,direct,theory(n,r))
        checks+=1
    C=[theory(n,r) for r in range(1,n)]
    for j in range(n-1):
        for i in range(len(C)-j):
            diff=sum(((-1)**h*comb(j,h)*C[i+h] for h in range(j+1)),F(0))
            assert diff>0,(n,j,i,diff)
            checks+=1
    # Deterministic tree identities: sum_r r L_r = n H and sum_r L_r = total tree length.
    vH=sum((F(4,k*k*(k-1)*(k-1)) for k in range(2,n+1)),F(0))
    covHL=sum((F(4,k*(k-1)*(k-1)) for k in range(2,n+1)),F(0))
    assert sum((F(r)*C[r-1] for r in range(1,n)),F(0))==n*vH
    assert sum(C,F(0))==covHL
    checks+=2
    assert C[0]==F(4,n)
    assert C[-1]==F(2,n-1)
    checks+=2

print('EXACT_OK n=2..8, theory_vs_merger_enumeration, strict_finite_differences, endpoints; checks=',checks)
for n in [500,1000,2000]:
    for alpha in [0.0,0.2,0.5,0.8,1.0]:
        r = max(1,min(n-1,round(alpha*n)))
        # Stable iterative k-level expected W to avoid huge factorials.
        q=1.0
        total=0.0
        # q for k=2: E W2,r = 2/(n-1) for every r.
        # each k uses direct product over r-1 (may be large; large n cost acceptable)
        for k in range(2,n-r+2):
            ratio=1.0
            for x in range(r-1):
                ratio *= (n-k-x)/(n-1-x)
            total += 4*ratio/((n-r)*k*(k-1))
        a=alpha
        limiting=4*(1-a+a*log(a))/(1-a)**2 if 0<a<1 else (4.0 if a==0 else 2.0)
        print(f'n={n} r={r} n_cov={n*total:.8f} target={limiting:.8f} absolute_error={abs(n*total-limiting):.4g}')
