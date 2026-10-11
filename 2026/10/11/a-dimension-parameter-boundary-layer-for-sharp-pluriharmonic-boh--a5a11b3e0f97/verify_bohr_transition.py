import math

def S(x):
    return -math.log1p(-x) - x

def T(n):
    return math.log1p(1.0/n) - 1.0/n

def root_radius(n, alpha):
    a = 1.0-alpha
    tau = n*a
    target = 1.0 + 2.0*tau*T(n)
    lo, hi = 0.0, 1.0-1e-15
    for _ in range(160):
        mid=(lo+hi)/2
        if mid + 2.0*tau*S(mid) < target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/(2*n)

def limit_x(tau):
    if tau == 0.0:
        return 1.0
    lo, hi=0.0, 1.0-1e-15
    for _ in range(160):
        mid=(lo+hi)/2
        if mid+2.0*tau*S(mid) < 1.0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

print("FIXED_ALPHA")
for alpha in (0.2,0.5,0.8):
    a=1-alpha
    for n in (100,400,1600):
        r=root_radius(n,alpha)
        leading=(n**1.5)*math.sqrt(a)*r
        second=(n**2)*(r-(a**-0.5)*n**-1.5)
        print(alpha,n,f"{leading:.12f}",f"{second:.12f}")
print("TRANSITION")
for tau in (0.25,1.0,4.0):
    xi=limit_x(tau)
    for n in (100,400,1600):
        alpha=1.0-tau/n
        x=n*root_radius(n,alpha)
        print(tau,n,f"{x:.12f}",f"{xi:.12f}",f"{x-xi:.3e}")
