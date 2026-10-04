from math import log, pi, fsum

# Classical dilogarithm series, rapidly convergent for the two negative rational arguments used here.
def li2(z, tol=1e-17):
    n = 1
    term = z
    vals = []
    while True:
        add = term/(n*n)
        vals.append(add)
        if abs(add) < tol:
            return fsum(vals)
        n += 1
        term *= z
        if n > 100000:
            raise RuntimeError('series did not converge')

def G(w):
    if 0.0 <= w <= 1.0:
        return 1.0 - 2.0/(w+2.0)*(1.0 + log((w+2.0)/2.0))
    if w <= 1.5:
        return (4.0-3.0*w-2.0*log(3.0/(2.0*w))+4.0*log((w+2.0)/3.0))/(w+2.0)
    if w <= 2.0:
        return (w-2.0+4.0*log((w+2.0)/(2.0*w)))/(w+2.0)
    raise ValueError(w)

def simpson(a,b,n):
    if n % 2: n += 1
    h=(b-a)/n
    s=G(a)+G(b)
    s += 4.0*fsum(G(a+(2*j-1)*h) for j in range(1,n//2+1))
    s += 2.0*fsum(G(a+2*j*h) for j in range(1,n//2))
    return s*h/3.0

L2,L3,L7=log(2.0),log(3.0),log(7.0)
closed=(pi*pi/3.0 + 6.0*li2(-0.75) - 2.0*li2(-0.5)
        + L2*L2 + 3.0*L3*L3 - 6.0*L2*L3
        + 14.0*L7 - 20.0*L2 - 12.0*L3)
# Split at the two published junctions.
direct=simpson(0.0,1.0,40000)+simpson(1.0,1.5,30000)+simpson(1.5,2.0,30000)
expected=0.058879779905129229
err=abs(closed-direct)
assert abs(closed-expected) < 3e-15, (closed,expected)
assert err < 2e-13, (closed,direct,err)
print('VERIFY_OK closed={:.17g} direct={:.17g} abs_diff={:.3g}'.format(closed,direct,err))
