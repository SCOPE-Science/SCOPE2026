from math import isqrt


def is_kth_power(n, k):
    lo, hi = 1, 1
    while hi ** k < n:
        hi *= 2
    while lo <= hi:
        m = (lo + hi) // 2
        v = m ** k
        if v == n:
            return True
        if v < n:
            lo = m + 1
        else:
            hi = m - 1
    return False


def F(n, k):
    return 1 if is_kth_power(n, k) else n


def G(n, k):
    return n ** k


def primes_upto(n):
    ps=[]
    for x in range(2,n+1):
        if all(x%p for p in ps if p*p<=x): ps.append(x)
    return ps

ps=primes_upto(1000)
cm=0
inj=0
witness=0
const=0
for k in range(2,9):
    for a in range(1,121):
        for b in range(1,121):
            assert G(a*b,k)==G(a,k)*G(b,k)
            cm += 1
    vals=[G(n,k) for n in range(1,501)]
    assert len(vals)==len(set(vals))
    inj += len(vals)
    for a in range(1,121):
        for b in range(a+1,121):
            r=next(p for p in ps if (a*b)%p)
            assert not is_kth_power(a*r,k)
            assert not is_kth_power(b*r,k)
            assert F(a*r,k)==a*r and F(b*r,k)==b*r
            assert F(a*r,k)!=F(b*r,k)
            witness += 1
    for n in range(1,2001):
        assert F(G(n,k),k)==1
        const += 1
print('VERIFY_OK')
print(f'complete_multiplicativity_checks={cm}')
print(f'injective_value_checks={inj}')
print(f'quasi_injective_constructive_witness_checks={witness}')
print(f'constant_composition_checks={const}')
