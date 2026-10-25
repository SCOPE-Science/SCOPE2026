"""Independent exact-arithmetic checks for weighted dimer adsorption on wheel graphs.

Run: python verify_wheel.py. Python standard library only. Analytical proofs are in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from functools import lru_cache


def exact_event_probability(rim_size, spoke_rate):
    """Dynamic programming on all possible remaining edge sets, not using path recurrence."""
    t = Fraction(spoke_rate)
    edges = []
    for j in range(1, rim_size + 1):
        edges.append((0, j, t))
        edges.append((j, 1 + j % rim_size, Fraction(1)))

    @lru_cache(None)
    def state(occupied):
        available = [(x, y, rate) for x, y, rate in edges
                     if not ((occupied >> x) & 1 or (occupied >> y) & 1)]
        if not available:
            return Fraction(0) if occupied & 1 else Fraction(1)
        total = sum(rate for _, _, rate in available)
        return sum(rate * state(occupied | (1 << x) | (1 << y)) / total
                   for x, y, rate in available)
    return state(0)


def recurrence(spoke_rate, max_m):
    a = 1 + Fraction(spoke_rate)
    out = [Fraction(1)]
    for m in range(1, max_m + 1):
        out.append(sum(out[j] * out[m-1-j] for j in range(m)) /
                   (2*a*m - 1))
    return out


def hypergeometric_series(spoke_rate, max_m):
    a = 1 + Fraction(spoke_rate)
    b = -1 / (2*a)
    c = 1 / (4*a*a)
    u = [Fraction(1)]
    v = [Fraction(1)]
    for n in range(1, max_m + 1):
        u.append(u[-1] * c / (n*(b+n-1)))
        v.append(v[-1] * c / (n*(b+n)))
    f = [Fraction(1)]
    for n in range(1, max_m + 1):
        f.append(v[n] - sum(u[j]*f[n-j] for j in range(1, n+1)))
    return f, u


def dominant_root(spoke_rate):
    with localcontext() as ctx:
        ctx.prec = 70
        a = Decimal(1) + Decimal(spoke_rate.numerator)/Decimal(spoke_rate.denominator)
        b = -Decimal(1)/(2*a)
        c = Decimal(1)/(4*a*a)
        def u(z):
            term = Decimal(1)
            result = term
            for j in range(1, 150):
                term *= c*z / (Decimal(j)*(b+j-1))
                result += term
                if abs(term) < Decimal('1e-65'):
                    break
            return result
        low,high=Decimal(0),Decimal(4)*a
        assert u(low)>0 and u(high)<0
        for _ in range(210):
            mid=(low+high)/2
            if u(mid)>0:low=mid
            else:high=mid
        return (low+high)/2


def main():
    checks=0
    for rate in (Fraction(1,2), Fraction(1), Fraction(2)):
        q=recurrence(rate, 35)
        f,u=hypergeometric_series(rate, 35)
        for j in range(36):
            assert q[j]==f[j], (rate,j)
            checks+=1
        assert all(x<0 for x in u[1:]);checks+=1
        for n in range(3,11):
            expected=Fraction(0) if n%2 else q[(n-2)//2]/(1+rate)
            actual=exact_event_probability(n,rate)
            assert actual==expected,(rate,n,actual,expected)
            checks+=1
        rho=dominant_root(rate)
        assert rho>1
        with localcontext() as ctx:
            ctx.prec=70
            a=Decimal(1)+Decimal(rate.numerator)/Decimal(rate.denominator)
            ratio=Decimal(q[20].numerator)/Decimal(q[20].denominator)/(2*a/(rho**21))
            assert abs(ratio-1)<Decimal('1e-16'),(rate,rho,ratio)
            checks+=1
        print('rate',str(rate),'dominant root',str(rho),'asymptotic ratio m=20',str(ratio))
    print('PASS:',checks,'independent exact/numerical assertions')

if __name__=='__main__':main()
