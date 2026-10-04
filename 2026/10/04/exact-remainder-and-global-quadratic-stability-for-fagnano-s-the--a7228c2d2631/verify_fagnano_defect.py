import math, random


def angles_from_sides(a,b,c):
    A=math.acos((b*b+c*c-a*a)/(2*b*c))
    B=math.acos((c*c+a*a-b*b)/(2*c*a))
    C=math.pi-A-B
    return A,B,C

def check(a,b,c,x,y,z):
    A,B,C=angles_from_sides(a,b,c)
    if max(A,B,C) >= math.pi/2-1e-13:
        raise ValueError('triangle must be acute')
    u = x*math.cos(A)+(c-z)*math.cos(C)
    p = x*math.sin(A)-(c-z)*math.sin(C)
    v = y*math.cos(B)+(a-x)*math.cos(A)
    q = y*math.sin(B)-(a-x)*math.sin(A)
    w = z*math.cos(C)+(b-y)*math.cos(B)
    r = z*math.sin(C)-(b-y)*math.sin(B)
    ZX=math.hypot(u,p); XY=math.hypot(v,q); YZ=math.hypot(w,r)
    per=ZX+XY+YZ
    area=0.25*math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))
    p0=8*area*area/(a*b*c)
    defect=(ZX-u)+(XY-v)+(YZ-w)
    exact_err=abs((per-p0)-defect)
    D=max(a,b,c)
    Q=p*p+q*q+r*r
    stab1=(per-p0)-Q/(2*D)
    x0=c*math.cos(B); y0=a*math.cos(C); z0=b*math.cos(A)
    weighted=(math.sin(A)*(x-x0))**2+(math.sin(B)*(y-y0))**2+(math.sin(C)*(z-z0))**2
    stab2=(per-p0)-weighted/(2*D)
    return exact_err, stab1, stab2, (per-p0), (x0,y0,z0), p0

triangles=[(5.0,5.5,6.0),(4.0,5.0,6.0),(7.0,8.0,9.0),(3.0,3.0,4.0),(2.0,2.5,3.0)]
worst_exact=0.0; min_stab1=1e9; min_stab2=1e9
for a,b,c in triangles:
    A,B,C=angles_from_sides(a,b,c)
    if max(A,B,C)>=math.pi/2: continue
    for i in range(11):
        for j in range(11):
            for k in range(11):
                x=a*i/10; y=b*j/10; z=c*k/10
                e,s1,s2,_,_,_=check(a,b,c,x,y,z)
                worst_exact=max(worst_exact,e); min_stab1=min(min_stab1,s1); min_stab2=min(min_stab2,s2)
    x0=c*math.cos(B); y0=a*math.cos(C); z0=b*math.cos(A)
    e,s1,s2,d,_,_=check(a,b,c,x0,y0,z0)
    assert abs(d) < 1e-11*max(a,b,c)

random.seed(20261001)
for _ in range(5000):
    while True:
        a,b,c=[random.uniform(1,5) for _ in range(3)]
        if a+b>c and b+c>a and c+a>b:
            A,B,C=angles_from_sides(a,b,c)
            if max(A,B,C)<math.pi/2: break
    x=random.random()*a; y=random.random()*b; z=random.random()*c
    e,s1,s2,_,_,_=check(a,b,c,x,y,z)
    worst_exact=max(worst_exact,e); min_stab1=min(min_stab1,s1); min_stab2=min(min_stab2,s2)

assert worst_exact < 2e-11
assert min_stab1 > -2e-11
assert min_stab2 > -2e-11
print('PASS')
print('worst exact identity error =',format(worst_exact,'.3e'))
print('minimum stability margin Q/(2D) =',format(min_stab1,'.3e'))
print('minimum weighted-coordinate stability margin =',format(min_stab2,'.3e'))
