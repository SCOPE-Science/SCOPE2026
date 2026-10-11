import math

def vp_kernel(n, t):
    s=math.sin(t/2)
    if abs(s)<1e-14:
        return 3.0*n
    return (math.sin(n*t)**2-math.sin(n*t/2)**2)/(n*s*s)

def three_kernel(t):
    return 1 + 2*math.cos(t)

def closed_A(m):
    x=math.pi/m
    if m%3==0:
        return 1/3+(2*math.sqrt(3)/m)*(math.cos(x)/math.sin(x))
    if m%3==1:
        return 1/3+2/(3*m)+(4/m)*math.sin(math.pi/3-x/3)/math.sin(x)
    return 1/3-2/(3*m)+(4/m)*math.sin(math.pi/3+x/3)/math.sin(x)

max_decimation=max_closed=max_csc=0.0
checks=0
for n in range(1,41):
    for m in range(4,121):
        N=n*m
        lhs=sum(abs(vp_kernel(n,2*math.pi*r/N)) for r in range(N))/N
        rhs=sum(abs(three_kernel(2*math.pi*s/m)) for s in range(m))/m
        max_decimation=max(max_decimation,abs(lhs-rhs))
        max_closed=max(max_closed,abs(rhs-closed_A(m)))
        checks+=1
for n in range(1,40):
    for j in range(1,40):
        x=(j+0.371)/(47*n)
        lhs=sum(1/(math.sin(x+math.pi*q/n)**2) for q in range(n))
        rhs=n*n/(math.sin(n*x)**2)
        max_csc=max(max_csc,abs(lhs-rhs)/max(1.0,abs(rhs)))
assert max_decimation<2e-11,max_decimation
assert max_closed<2e-13,max_closed
assert max_csc<2e-12,max_csc
print(f'VERIFY_OK cases={checks} decimation_maxerr={max_decimation:.3e} closed_maxerr={max_closed:.3e} csc_relerr={max_csc:.3e}')
