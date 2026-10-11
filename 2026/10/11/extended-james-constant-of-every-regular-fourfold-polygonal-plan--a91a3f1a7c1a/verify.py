import math

TOL=3e-10

def norm_poly(z,n):
    alpha=math.pi/(4*n)
    x,y=z
    return max(abs(x*math.cos(2*k*alpha)+y*math.sin(2*k*alpha)) for k in range(2*n))

def e(th):
    return (math.cos(th),math.sin(th))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def sub(a,b): return (a[0]-b[0],a[1]-b[1])
def mul(c,a): return (c*a[0],c*a[1])

def euc(a): return math.hypot(a[0],a[1])

sharp=0
samples=0
for n in range(1,41):
    alpha=math.pi/(4*n)
    sec=1/math.cos(alpha)
    target=math.sqrt(2)*sec
    u=mul(sec,e(alpha))
    v=mul(sec,e(alpha+math.pi/2))
    assert abs(norm_poly(u,n)-1)<TOL
    assert abs(norm_poly(v,n)-1)<TOL
    t=math.tan(alpha)
    c=math.sqrt(2/(1+t*t))
    x=mul(c,u)
    y=mul(c*t,v)
    assert abs(norm_poly(x,n)**2+norm_poly(y,n)**2-2)<2e-9
    a=norm_poly(add(x,y),n)
    b=norm_poly(sub(x,y),n)
    assert abs(a-target)<2e-9 and abs(b-target)<2e-9
    sharp+=1

    # Deterministic admissible sample family. The analytic proof, not these samples,
    # supplies the universal upper bound.
    for i in range(1,41):
        th=2*math.pi*i/41
        p=e(th)
        np=norm_poly(p,n)
        p=mul(1/np,p)
        for j in range(1,17):
            ph=2*math.pi*j/17
            q=e(ph)
            nq=norm_poly(q,n)
            q=mul(1/nq,q)
            r=j/17
            scale=math.sqrt(2/(1+r*r))
            xx=mul(scale,p)
            yy=mul(scale*r,q)
            val=min(norm_poly(add(xx,yy),n),norm_poly(sub(xx,yy),n))
            assert val <= target+2e-9
            samples+=1

print(f'VERIFY_OK polygons={sharp} admissible_samples={samples} formula=sqrt(2)*sec(pi/(4n))')
