from collections import Counter

def formula_counts(p,a,b):
    assert 1 <= a < b
    finite = p**b*(p-2) if a == 1 else p**(3*a+b-4)*(p-1)*(p-2)
    infinity = p**(3*a+b-3)*(p-1)*(p-2)
    if b == a+1:
        infinity += p**(4*a-3)*(p-1)**2
    return infinity, finite

def fixed_fiber_counts(p,a,b):
    pa = p**a
    pb = p**b
    gap = b-a
    counts = Counter()

    for alpha in range(pa):
        if alpha % p == 0:
            continue
        for beta in range(pa):
            for c in range(pa):
                gamma = c * p**gap
                for delta in range(pb):
                    if delta % p == 0:
                        continue

                    fixed = []
                    for x in range(pa):
                        for y in range(pb):
                            if (alpha*x + beta*y - x) % pa:
                                continue
                            if (gamma*x + delta*y - y) % pb:
                                continue
                            fixed.append((x,y))

                    if len(fixed) != p:
                        continue

                    nz = [z for z in fixed if z != (0,0)]
                    x,y = nz[0]
                    if x == 0:
                        label = "infinity"
                    else:
                        k = (x // p**(a-1)) % p
                        ell = (y // p**(b-1)) % p
                        label = (ell * pow(k,-1,p)) % p
                    counts[label] += 1

    return counts

tests = [
    (2,1,2),
    (2,1,3),
    (2,2,3),
    (3,1,2),
    (3,1,3),
    (3,2,3),
    (5,1,2),
]

for p,a,b in tests:
    actual = fixed_fiber_counts(p,a,b)
    m_inf,m_t = formula_counts(p,a,b)

    expected = Counter()
    if m_inf:
        expected["infinity"] = m_inf
    if m_t:
        for t in range(p):
            expected[t] = m_t

    assert actual == expected, (p,a,b,actual,expected)

    if (a,b) == (1,2):
        total = m_inf + p*m_t
        published = p*(2*p**3 - 4*p**2 + 1)
        assert total == published

    print({
        "p":p,
        "a":a,
        "b":b,
        "fibers":dict(actual),
        "total_order_p_fixed":sum(actual.values()),
    })

print("VERIFY_OK")
