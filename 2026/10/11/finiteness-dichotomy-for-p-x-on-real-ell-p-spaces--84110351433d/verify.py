import math

def finite_terms(p,b):
    A = 1.0 + (1.0 + abs(b)**p)**(2.0/p)
    D = A - ((1.0-b)**p + 1.0)**(2.0/p)
    N = A - ((1.0+b)**p + 1.0)**(2.0/p)
    return N,D

def bisect_root(p,lo,hi):
    flo = finite_terms(p,lo)[1]
    fhi = finite_terms(p,hi)[1]
    assert flo*fhi < 0.0
    for _ in range(100):
        mid = (lo+hi)/2.0
        fm = finite_terms(p,mid)[1]
        if flo*fm <= 0.0:
            hi = mid
            fhi = fm
        else:
            lo = mid
            flo = fm
    return (lo+hi)/2.0

checked=[]
for p in [1.0,1.1,1.5,1.9]:
    assert finite_terms(p,0.0)[1] < 0.0
    assert finite_terms(p,1.0)[1] > 0.0
    r = bisect_root(p,0.0,1.0)
    N0,_ = finite_terms(p,r)
    assert N0 < 0.0
    b = r - 1e-7
    N,D = finite_terms(p,b)
    assert N < 0.0 and D < 0.0
    assert N/D > 1e5
    checked.append((p,r,N/D))

for p in [2.1,3.0,4.0,10.0,100.0]:
    assert finite_terms(p,-1.0)[1] < 0.0
    assert finite_terms(p,0.0)[1] > 0.0
    r = bisect_root(p,-1.0,0.0)
    N0,_ = finite_terms(p,r)
    assert N0 > 0.0
    b = r + 1e-7
    N,D = finite_terms(p,b)
    assert N > 0.0 and D > 0.0
    assert N/D > 1e5
    checked.append((p,r,N/D))

# p = infinity: exact branch up to floating evaluation.
rinf = 1.0-math.sqrt(2.0)
for eps in [1e-3,1e-5,1e-7]:
    b = rinf + eps
    D = 2.0-(1.0-b)**2
    N = 1.0
    assert D > 0.0
assert 1.0/(2.0-(1.0-(rinf+1e-7))**2) > 1e6

# p = 2: direct Euclidean quotient equals -1 for nonorthogonal samples.
def euclid_sq(v):
    return v[0]*v[0]+v[1]*v[1]

for x,y in [
    ((1.0,0.0),(0.3,1.0)),
    ((1.0,2.0),(-0.4,0.7)),
    ((2.0,-1.0),(0.5,1.5)),
]:
    A = euclid_sq(x)+euclid_sq(y)
    num = A-euclid_sq((x[0]+y[0],x[1]+y[1]))
    den = A-euclid_sq((x[0]-y[0],x[1]-y[1]))
    assert abs(den) > 1e-12
    assert abs(num/den + 1.0) < 1e-12

print("VERIFY_OK finite_p_samples=9 hilbert=-1 infinity_pole=1-sqrt2 quotient_blowup>1e5")
