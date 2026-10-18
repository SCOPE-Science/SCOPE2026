"""Reproduce finite one-point type counts for weak-order parameter posets."""
from itertools import product


def compositions(n, h):
    if h == 1:
        yield (n,)
    else:
        for first in range(1, n-h+2):
            for tail in compositions(n-first, h-1):
                yield (first,) + tail


def predicted(sizes):
    a = [(1 << k)-1 for k in sizes]
    t = 1 + 2*sum(a) + sum(a[i]*a[j] for i in range(len(a)) for j in range(i+1,len(a)))
    o = 1 + 2*sum(sizes) + sum(sizes[i]*sizes[j] for i in range(len(sizes)) for j in range(i+1,len(sizes)))
    return t,o


def exhaustive(sizes):
    levels = tuple(i for i,k in enumerate(sizes) for _ in range(k))
    n = len(levels)
    if n > 8:
        raise ValueError("Bound exhaustive tests to eight points")
    total = 0
    orbits = set()
    for states in product(range(3), repeat=n):
        down = [i for i,v in enumerate(states) if v==1]
        up = [i for i,v in enumerate(states) if v==2]
        if any(levels[i] >= levels[j] for i in down for j in up):
            continue
        if any(levels[i] < levels[j] and ((states[i]==2 and states[j]!=2) or (states[j]==1 and states[i]!=1))
               for i in range(n) for j in range(n)):
            continue
        total += 1
        signature = tuple((sum(states[i] == 1 for i in range(n) if levels[i]==lvl),
                           sum(states[i] == 2 for i in range(n) if levels[i]==lvl))
                          for lvl in range(len(sizes)))
        orbits.add(signature)
    return total,len(orbits)


def check():
    checks = 0
    for n in range(1,9):
        for h in range(1,min(n,5)+1):
            comp = list(compositions(n,h))
            for c in comp:
                a = predicted(c)
                b = exhaustive(c)
                assert a==b,(c,a,b)
                checks+=1
            vals = [(predicted(c),c) for c in comp]
            mins_t = min(v[0][0] for v in vals)
            maxs_t = max(v[0][0] for v in vals)
            mins_o = min(v[0][1] for v in vals)
            maxs_o = max(v[0][1] for v in vals)
            q,r=divmod(n,h)
            balanced = (q,)*(h-r)+(q+1,)*r
            extreme = (n-h+1,)+(1,)*(h-1)
            assert predicted(balanced)[0]==mins_t
            assert predicted(balanced)[1]==maxs_o
            assert predicted(extreme)[0]==maxs_t
            assert predicted(extreme)[1]==mins_o
    assert predicted((2,3,3)) == (126,38)
    assert predicted((6,1,1)) == (258,30)
    print(f'VERIFY_OK: {checks} size compositions through eight points, direct ternary assignments and type orbit signatures')


if __name__ == '__main__':
    check()


def egf_checks():
    # Arrays store n! times the ordinary Taylor coefficient (EGF convention).
    from math import factorial, log
    N = 30
    def mul(u, v):
        return [sum(comb(n, k)*u[k]*v[n-k] for k in range(n+1)) for n in range(N+1)]
    from math import comb
    W=[0]*(N+1)
    W[0]=1
    for n in range(1,N+1):
        W[n]=sum(comb(n,k)*W[n-k] for k in range(1,n+1))
    A=[0]+[(1<<n)-1 for n in range(1,N+1)]
    C=[0]+[n for n in range(1,N+1)]
    W2=mul(W,W);W3=mul(W2,W)
    AW2=mul(A,W2)
    AA_W3=mul(mul(A,A),W3)
    CW2=mul(C,W2)
    CC_W3=mul(mul(C,C),W3)
    ST=[W[n]+2*AW2[n]+AA_W3[n] for n in range(N+1)]
    SO=[W[n]+2*CW2[n]+CC_W3[n] for n in range(N+1)]
    for n in range(1,11):
        brute_t=brute_o=brute_w=0
        for h in range(1,n+1):
            for c in compositions(n,h):
                weight=factorial(n)
                for k in c: weight//=factorial(k)
                t,o=predicted(c)
                brute_w+=weight
                brute_t+=weight*t
                brute_o+=weight*o
        assert W[n]==brute_w and ST[n]==brute_t and SO[n]==brute_o,(n,ST[n],brute_t)
    rho=log(2)
    for n in (15,30):
        avg_t=ST[n]/W[n]
        avg_o=SO[n]/W[n]
        print(f'EGF_CHECK n={n}: E_types={avg_t:.6f}, E_orbits={avg_o:.6f}, ratio={avg_t/avg_o:.6f}, limiting_ratio={rho**-2:.6f}')
    print('EGF_VERIFY_OK: exact species coefficients through n=10')


if __name__=='__main__':
    egf_checks()
