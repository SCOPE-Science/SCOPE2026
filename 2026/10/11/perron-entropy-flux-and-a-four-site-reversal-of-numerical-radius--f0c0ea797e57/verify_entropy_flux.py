"""Numerical sanity checks for the entropy-flux formula (not a proof of the limits)."""
from decimal import Decimal, localcontext


def four_slope(a, b, c):
    with localcontext() as ctx:
        ctx.prec = 65
        a, b, c = Decimal(str(a)), Decimal(str(b)), Decimal(str(c))
        s = a*a + b*b + c*c
        r2 = (s + (s*s - 4*a*a*c*c).sqrt())/2
        r = r2.sqrt()
        y = (a/r, Decimal(1), (r2-a*a)/(b*r))
        y = y + (c*y[2]/r,)
        den = sum(z*z for z in y)
        weights = (a,b,c)
        flux = sum(weights[j]*y[j]*y[j+1]*(y[j]/y[j+1]).ln()
                   for j in range(3))/den
        return flux/2, r/2


def tridiagonal_perron(a, b, c):
    # Independent power iteration on the positive matrix I + W/(a+b+c).
    from math import sqrt, log
    v = [0.5]*4
    z = float(a+b+c)
    for _ in range(3000):
        new = [v[0] + a*v[1]/z,
               v[1] + (a*v[0]+b*v[2])/z,
               v[2] + (b*v[1]+c*v[3])/z,
               v[3] + c*v[2]/z]
        norm = sqrt(sum(t*t for t in new))
        new = [t/norm for t in new]
        if max(abs(u-w) for u,w in zip(new,v)) < 5e-16:
            v=new
            break
        v=new
    flux = sum(w*v[j]*v[j+1]*log(v[j]/v[j+1])
               for j,w in enumerate((a,b,c)))
    return flux/2


if __name__ == '__main__':
    for b, direction in [('0.01', 1), ('1', 1), ('4', -1), ('100', -1)]:
        d, _ = four_slope(2, b, 1)
        assert d*direction > 0
        assert abs(float(d)-tridiagonal_perron(2,float(b),1)) < 2e-11
    print('ENTROPY_FLUX_NUMERIC_CHECK_OK')
