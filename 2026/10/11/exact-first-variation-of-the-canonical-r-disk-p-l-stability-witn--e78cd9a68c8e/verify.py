import math


def close(a, b, tol=2e-10):
    if abs(a-b) > tol * max(1.0, abs(a), abs(b)):
        raise AssertionError((a,b,a-b))


def params(r,w):
    s=0.5*(math.sqrt(4*r*r-(r-w)**2)-math.sqrt(3.0)*(r-w))
    u=s/(2*r)
    c=math.sqrt(1-u*u)
    return s,u,c


def segment(r,t):
    return r*r*math.asin(t/(2*r))-t*math.sqrt(4*r*r-t*t)/4


def exact_terms(r,w,x):
    s,u,c=params(r,w)
    z=x/(2*r)
    d=math.sqrt(1-z*z)
    dx=x*(c*d-u*z)
    dy=x*(u*d+c*z)
    vx=s/2+dx
    vy=dy
    a_direct=math.hypot(vx+s/2,vy)
    b_direct=math.hypot(vx,vy-math.sqrt(3)*s/2)
    tri_new=abs((0+s/2)*(vy-0)-(math.sqrt(3)*s/2-0)*(vx+s/2))/2
    tri_old=math.sqrt(3)*s*s/4
    D_direct=tri_new-tri_old
    a=s*d+c*x
    b2=s*s+x*x+s*x*((c-math.sqrt(3)*u)*d-(u+math.sqrt(3)*c)*z)
    b=math.sqrt(b2)
    D=s*x*((math.sqrt(3)*c-u)*d-(math.sqrt(3)*u+c)*z)/4
    close(a,a_direct)
    close(b,b_direct)
    close(D,D_direct)
    eps=D+segment(r,a)+segment(r,b)-2*segment(r,s)
    return eps,a,b,D


def slope(r,w):
    s,u,c=params(r,w)
    L=r*(2*u*u+math.sqrt(3)*u*(1-2*u*u)/c)/2
    alt=s*math.sin(2*math.asin(u)+math.pi/3)/(2*c)
    close(L,alt)
    return L


def ccan(r,w):
    s,u,c=params(r,w)
    L=slope(r,w)
    return c/(2*L)


for r,w in [(1.0,1.0),(1.0,0.5),(2.0,0.7),(10.0,1.0)]:
    s,u,c=params(r,w)
    close(w,r*(1+math.sqrt(3)*u-c))
    L=slope(r,w)
    if not L>0:
        raise AssertionError('nonpositive slope')
    eps,_,_,_=exact_terms(r,w,1e-4*r)
    if abs(eps/(1e-4*r)-L) > 4e-4*max(1.0,abs(L)):
        raise AssertionError(('slope check',r,w,eps/(1e-4*r),L))

close(ccan(1.0,1.0),math.sqrt(3)/2)
if abs(ccan(100000.0,1.0)-1.0) > 2e-5:
    raise AssertionError(('classical limit',ccan(100000.0,1.0)))

print('VERIFY_OK')
