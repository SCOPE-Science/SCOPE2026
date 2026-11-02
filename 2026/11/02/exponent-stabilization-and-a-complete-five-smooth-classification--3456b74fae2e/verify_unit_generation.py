"""Exact finite checks for least integer generators of modular unit groups."""
from math import gcd

def factor(n):
    r = {}; p = 2
    while p * p <= n:
        while n % p == 0:
            r[p] = r.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1: r[n] = r.get(n, 0) + 1
    return r

def reduced_modulus(n):
    m = 1
    for p, e in factor(n).items():
        m *= p ** min(e, 3 if p == 2 else 2)
    return m

def phi(n):
    v = n
    for p in factor(n): v = v // p * (p - 1)
    return v

def least_generator_bound(n):
    if n <= 2: return 1
    generated = {1}
    target = phi(n)
    for a in range(2, n + 1):
        if gcd(a, n) != 1 or a % n in generated: continue
        old = generated.copy()
        new = old.copy()
        v = a % n
        while v not in old:
            new.update((x * v) % n for x in old)
            v = (v * a) % n
        generated = new
        if len(generated) == target: return a
    raise AssertionError('no bound')

def direct_subgroup_size(n, B):
    if n == 1: return 1
    generators = [a for a in range(1, B + 1) if gcd(a, n) == 1]
    group = {1 % n}; todo = [1 % n]
    while todo:
        x = todo.pop()
        for g in generators:
            y = (x * g) % n
            if y not in group:
                group.add(y); todo.append(y)
    return len(group)

TABLE = {
    (0, 0): (1, 1, 3, 5),
    (1, 0): (2, 5, 7, 13),
    (0, 1): (2, 3, 11, 11),
    (1, 1): (7, 11, 13, 17),
}

def run():
    cases=0
    for a in range(4):
        for b in range(3):
            for c in range(3):
                n=2**a * 3**b * 5**c
                claimed=TABLE[(b > 0, c > 0)][a]
                result=least_generator_bound(n)
                assert result==claimed,(a,b,c,n,result,claimed)
                assert direct_subgroup_size(n,claimed)==phi(n),(a,b,c,'upper')
                if claimed>1:assert direct_subgroup_size(n,claimed-1)<phi(n),(a,b,c,'lower')
                cases+=1
    stability_cases=0
    for n in range(1,2001):
        assert least_generator_bound(n)==least_generator_bound(reduced_modulus(n)),n
        stability_cases+=1
    print('VERIFY_OK table_cases=%d stability_cases=%d subgroup_methods=2 exact_integer=yes'%(cases,stability_cases))
    for n in (4,8,42,126,30,60,120):print('CASE',n,'G=',least_generator_bound(n))

if __name__=='__main__': run()
