"""Independent finite checks for exact periods of divisor-sum/LCM quotients."""
from math import gcd, lcm
from fractions import Fraction


def factors(n):
    out = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            j = 0
            while n % d == 0:
                n //= d
                j += 1
            out[d] = j
        d += 1 if d == 2 else 2
    if n > 1:
        out[n] = 1
    return out


def sigma_power(n, alpha):
    z = 1
    for p, e in factors(n).items():
        z *= sum(p**(alpha*j) for j in range(e+1))
    return z


def exact_g(n, k, alpha):
    values = list(range(n, n+k+1))
    mul = 1
    whole_lcm = 1
    for j in values:
        mul *= sigma_power(j, alpha)
        whole_lcm = lcm(whole_lcm, j)
    den = sigma_power(whole_lcm, alpha)
    assert mul % den == 0
    return mul // den


def expected_period(k):
    t = 1
    for p in range(2, k+1):
        if len(factors(p)) != 1 or factors(p).get(p) != 1:
            continue
        pp = p
        while pp*p <= k:
            pp *= p
        if (k+1) % pp:
            t *= pp
    return t


def count_p(n, p, j, k):
    m = p**j
    return sum((n+i) % m == 0 for i in range(k+1))


def g_from_local_counts(n,k,alpha):
    z = Fraction(1)
    for p in range(2,k+1):
        if factors(p)!={p:1}:
            continue
        pp=p
        e=1
        while pp*p<=k:
            pp*=p
            e+=1
        for j in range(1,e+1):
            numer=sum(p**(alpha*t) for t in range(j+1))
            denom=sum(p**(alpha*t) for t in range(j))
            z*=Fraction(numer,denom)**(count_p(n,p,j,k)-1)
    assert z.denominator==1
    return z.numerator


def run():
    n_exact=0
    for alpha in (0,1,2):
        for k in range(1,11):
            t=expected_period(k)
            values=[exact_g(n,k,alpha) for n in range(1,t+1)]
            # Verify that *every* proper divisor candidate fails, not only a fixed list.
            for d in range(1,t):
                if t%d==0:
                    assert any(values[i]!=values[(i+d)%t] for i in range(t))
            for n in range(1, min(5*t,500)+1):
                x=exact_g(n,k,alpha)
                assert x==values[(n-1)%t]
                assert x==g_from_local_counts(n,k,alpha)
                n_exact+=1
    # Different positive multiplicative function, prime-power factors f(p^a)=exp(a^2).
    # Use integer f(p^a)=2**(a*a) to test non-multiplicative-in-exponent f.
    def f(n):
        z=1
        for _,a in factors(n).items():z*=2**(a*a)
        return z
    exotic=0
    for k in range(1,10):
        t=expected_period(k)
        vals=[]
        for n in range(1,t+1):
            mul=1;lc=1
            for u in range(n,n+k+1):
                mul*=f(u);lc=lcm(lc,u)
            assert mul%f(lc)==0
            vals.append(mul//f(lc))
        for d in range(1,t):
            if t%d==0:assert any(vals[i]!=vals[(i+d)%t] for i in range(t))
        exotic+=t
    print('VERIFY_OK: tested', n_exact, 'exact sigma_alpha comparisons (alpha=0,1,2),', exotic,
          'non-geometric prime-power function states; all claimed periods were minimal')

if __name__=='__main__':
    run()
