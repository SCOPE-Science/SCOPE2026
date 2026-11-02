"""Independent exact-arithmetic checks for mixed Wythoff representation counts."""
from math import isqrt, log

SCALE = 10**60
SQRT5_LO = isqrt(5*SCALE*SCALE)

def low_wythoff(k):
    lo = (k*(SCALE+SQRT5_LO))//(2*SCALE)
    hi = (k*(SCALE+SQRT5_LO+1))//(2*SCALE)
    assert lo == hi, (k,lo,hi)
    return lo

def floor_alpha(k):
    lo = (k*(SQRT5_LO-SCALE))//(2*SCALE)
    hi = (k*(SQRT5_LO+1-SCALE))//(2*SCALE)
    assert lo == hi, (k,lo,hi)
    return lo

N=750
u={low_wythoff(k) for k in range(1,N+1)}
v={low_wythoff(k)+k for k in range(1,N+1)}
alpha=(5**.5-1)/2
beta=(3-5**.5)/2
max_err=0.
for n in range(1,N+1):
    direct=sum(1 for m in u if m<n and n-m in v)
    symbolic=sum((floor_alpha(m+1)-floor_alpha(m))*(1-(floor_alpha(n-m+1)-floor_alpha(n-m))) for m in range(1,n))
    assert direct == symbolic, (n,direct,symbolic)
    t=(n*alpha)%1
    profile=beta-t if t<beta else t-beta if t<2*beta else beta
    delta=abs(direct-n*profile)
    max_err=max(max_err,delta)
    assert delta < 8*log(n+2), (n,delta)
assert all(low_wythoff(k)+k > low_wythoff(k) for k in range(1,N+1))
print(f'VERIFY_OK n_range=1..{N} independent_definitions=yes exact_membership_arithmetic=yes maximum_profile_error={max_err:.6f}')
