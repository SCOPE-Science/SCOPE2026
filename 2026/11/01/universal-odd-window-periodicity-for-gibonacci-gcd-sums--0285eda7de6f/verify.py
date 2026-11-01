"""Finite tests accompanying a theorem on gcds of Gibonacci windows.
Run with Python 3; no third-party dependencies.
"""
from math import gcd, lcm


def sequence(a, b, bound):
    terms = [a, b]
    for _ in range(bound):
        terms.append(terms[-1] + terms[-2])
    return terms


def norm(x, y):
    return y*y - x*y - x*x


def finite_gcd(values):
    out = 0
    for value in values:
        out = gcd(out, value)
    return out


def period_mod(a, b, m):
    start = (a % m, b % m)
    x, y = start
    for t in range(1, m*m+1):
        x, y = y, (x+y) % m
        if (x,y) == start:
            return t
    raise AssertionError('No modular period')


def values(terms, k):
    x = terms[k+1]-terms[1]
    y = terms[k+2]-terms[2]
    a = gcd(x,y)
    b = gcd(terms[k]*terms[k+1]-terms[0]*terms[1],
            terms[k+1]**2-terms[1]**2,
            terms[k+2]**2-terms[2]**2)
    return a, b


seed_count = length_count = period_checks = norm_checks = 0
examples = {}
for a in range(-6,7):
    for b in range(-6,7):
        if (a,b) == (0,0):
            continue
        d = gcd(a,b)
        u,v = a//d, b//d
        mu = norm(u,v)
        assert mu != 0
        m = 2*abs(mu)
        t = lcm(2,period_mod(u,v,m))
        # Test a bounded range of all odd lengths, and the shifted periods.
        top = 60+t+16
        term = sequence(a,b,top+20)
        for k in range(1,60,2):
            a0,b0 = values(term,k)
            a1,b1 = values(term,k+t)
            assert (a0,b0) == (a1,b1),(a,b,k,t)
            period_checks+=1
            # Compute genuine (not formula-defined) window sums in 12 positions.
            starts = 12
            raw_a = finite_gcd(sum(term[n+1:n+k+1]) for n in range(starts))
            raw_b = finite_gcd(sum(z*z for z in term[n+1:n+k+1]) for n in range(starts))
            assert (a0,b0) == (raw_a,raw_b),(a,b,k)
            assert a0 % d == 0 and b0 % (d*d) == 0
            assert m % (a0//d) == 0 and m % (b0//(d*d)) == 0
            x,y = term[k],term[k+1]
            delta = ((term[k+2]**2-term[2]**2)
                    -2*(term[k+1]**2-term[1]**2)
                    -(x*y-a*b))
            assert delta == 2*d*d*mu
            length_count+=1
        for i in range(0,55):
            assert norm(term[i],term[i+1]) == (-1)**i*d*d*mu
            norm_checks+=1
        if (a,b) in [(-1,3),(0,1),(1,4),(2,1),(4,6)]:
            examples[str((a,b))] = {'mu':mu,'modulus':m,'common_period_bound':t,
                'first_odd_values': [(k,values(term,k)) for k in range(1,18,2)]}
        seed_count+=1
print(f'PASS: {seed_count} nonzero seeds; {length_count} exact window-GCD comparisons; '
      f'{period_checks} shifted-period comparisons; {norm_checks} norm identities.')
for name,e in examples.items(): print(name,e)
print('Finite checks are examples, not proofs of all odd lengths or all integer initial values.')
