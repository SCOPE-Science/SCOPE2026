"""Independent arithmetic spot checks for the Hamming-cube positivity threshold.
The accompanying proof, not these finite tests, establishes the theorem.
Uses Python 3 standard library only.
"""
from math import comb, exp, log

def krawtchouk(d, k, r):
    return sum((-1)**j * comb(r, j) * comb(d-r, k-j)
               for j in range(max(0, k-d+r), min(k, r)+1))

def h(d, r, z):
    return sum(krawtchouk(d, k, r) * z**(k*k) for k in range(d+1))

def root(d):
    lo = 1/d
    hi = 1/d + 1/(d**3)
    assert h(d,d,lo)>0 and h(d,d,hi)<0, (d,h(d,d,lo),h(d,d,hi))
    for _ in range(75):
        mid=(lo+hi)/2
        if h(d,d,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2

if __name__=='__main__':
    for d in range(3,33):
        z=root(d)
        t=-log(z)/4
        z_safe=z*(1-1e-7)
        assert all(h(d,r,z_safe)>0 for r in range(d+1)),d
        assert all(h(d,r,z)>0 for r in range(d)), d
        if d<=16:
            print('dimension',d,'time',format(t,'.15f'),
                  'asymptotic_scaled_difference',format((log(d)/4-t)*d*d,'.10f'))
    print('All finite spot checks passed. Infinite statement uses analytic bounds.')
