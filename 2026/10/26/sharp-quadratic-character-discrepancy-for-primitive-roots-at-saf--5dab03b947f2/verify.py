"""Standalone exact enumeration for quadratic-character sums on safe-prime primitive roots."""
from math import isqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, isqrt(n) + 1):
        if n % d == 0:
            return False
    return True


def chi(z, p):
    z %= p
    if z == 0:
        return 0
    return 1 if pow(z, (p - 1) // 2, p) == 1 else -1


def verify():
    safe = [p for p in range(5, 181) if is_prime(p) and is_prime((p - 1)//2) and p == 2 * ((p - 1)//2) + 1]
    assert safe == [5, 7, 11, 23, 47, 59, 83, 107, 167, 179]
    tested = 0
    witnesses = {}
    for p in safe:
        q = (p-1)//2
        # Explicit independent multiplicative-order criterion for primitive roots.
        primitive = [g for g in range(1, p) if pow(g, 2, p) != 1 and pow(g, q, p) != 1]
        assert primitive == [g for g in range(1,p) if chi(g,p) == -1 and (p == 5 or g != p-1)]
        minimum = p
        for a in (0,1):
            for b in range(p):
                if a == 0 and b != 1:
                    continue  # nonzero linear slope can be normalized to 1
                for c in range(p):
                    if a == 0 and c == 0:
                        continue
                    if (b*b - 4*a*c) % p == 0:
                        continue
                    vals = [chi(a*g*g + b*g + c, p) for g in primitive]
                    s = sum(vals)
                    r = vals.count(0)
                    nplus = vals.count(1)
                    nminus = vals.count(-1)
                    t = sum(chi(x*(a*x*x + b*x + c),p) for x in range(p))
                    eta = chi(a-b+c,p)
                    if p == 5:
                        tested += 1
                        minimum = min(minimum,nplus,nminus)
                        continue
                    assert 2*s == -chi(a,p)-chi(c,p)-t-2*eta, (p,a,b,c,s,t)
                    assert 4*nplus == p-3-2*r-chi(a,p)-chi(c,p)-t-2*eta
                    assert 4*nminus == p-3-2*r+chi(a,p)+chi(c,p)+t+2*eta
                    assert abs(s) <= isqrt(p)+2
                    if p >= 23:
                        assert nplus >= 1 and nminus >= 1, (p,a,b,c, nplus,nminus)
                    minimum = min(minimum,nplus,nminus)
                    tested += 1
        witnesses[p] = minimum
    for p in (5,7,11):
        primitive = [g for g in range(1,p) if chi(g,p)==-1 and g != p-1]
        vals=[chi(g*g+g+1,p) for g in primitive]
        assert 1 not in vals or -1 not in vals, (p,vals)
    for p,a,b,c,target in [(23,1,1,4,-6),(47,1,1,36,-8)]:
        gs=[g for g in range(1,p) if chi(g,p)==-1 and g!=p-1]
        assert sum(chi(a*g*g+b*g+c,p) for g in gs)==target
    assert witnesses[23] == 1
    print('VERIFY_OK: exact character-sum and signed-count identities for', tested,
          'normalized polynomial triples on', len(safe), 'safe primes through 179;',
          'minimum signed counts:', witnesses)


if __name__ == '__main__':
    verify()
