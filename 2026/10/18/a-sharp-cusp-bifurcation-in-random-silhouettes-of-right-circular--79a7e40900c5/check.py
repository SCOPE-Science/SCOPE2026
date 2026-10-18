"""Independent numerical checks for the right circular cone brightness bifurcation.
Run: python3 check.py (Python standard library only).
"""
import math

PI=math.pi

def area(k,t):
    t=float(t)
    threshold=k/math.hypot(k,1.0)
    if t>=threshold: return PI*t
    s=math.sqrt(max(0.,k*k-(1+k*k)*t*t))
    q=t/(k*math.sqrt(1-t*t))
    return PI*t+s-t*math.acos(max(-1.,min(1.,q)))

def derivative(k,t):
    th=k/math.hypot(k,1.)
    if t>=th:return PI
    b=math.acos(t/(k*math.sqrt(1-t*t)))
    return PI-b-k*k*math.sin(b)*math.cos(b)

def cross(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])

def hull_area(points):
    p=sorted(set(points))
    lo=[]
    for q in p:
        while len(lo)>=2 and cross(lo[-2],lo[-1],q)<=0:lo.pop()
        lo.append(q)
    hi=[]
    for q in reversed(p):
        while len(hi)>=2 and cross(hi[-2],hi[-1],q)<=0:hi.pop()
        hi.append(q)
    h=lo[:-1]+hi[:-1]
    return abs(sum(h[i][0]*h[(i+1)%len(h)][1]-h[(i+1)%len(h)][0]*h[i][1] for i in range(len(h)))/2)

def approximate_cone_shadow(k,t,n=1536):
    # Project an independently discretized base disk and the cone apex.
    # Horizontal projected semiaxis 1 and axial projected semiaxis t.
    pts=[(math.cos(2*PI*j/n),t*math.sin(2*PI*j/n)) for j in range(n)]
    pts.append((0.,k*math.sqrt(1-t*t)))
    return hull_area(pts)

def bisect(fun,lo,hi):
    fl=fun(lo);fh=fun(hi)
    assert fl*fh<0
    for _ in range(100):
        mid=(lo+hi)/2
        fm=fun(mid)
        if fm==0:return mid
        if fm*fl<0:hi=mid;fh=fm
        else:lo=mid;fl=fm
    return (lo+hi)/2

b=bisect(lambda beta: math.tan(2*beta)+2*(PI-beta),PI/4+1e-4, PI/2-1e-4)
kstar=math.sqrt(2*(PI-b)/math.sin(2*b))
assert 2.1455<kstar<2.1456
num_hull=0
for k in (.5,1.,1.9,2.1,2.2,2.5,3.,5.):
    for t in (.03,.1,.23,.42,.61,.74,.89,.97):
        actual=approximate_cone_shadow(k,t)
        exact=area(k,t)
        assert abs(actual-exact)<1.2e-5,(k,t,actual,exact)
        num_hull+=1
        if t<k/math.hypot(k,1.)-.015:
            h=2e-5
            numeric=(area(k,t+h)-area(k,t-h))/(2*h)
            assert abs(numeric-derivative(k,t))<1e-6,(k,t,numeric,derivative(k,t))

def simpson(f,n=5000):
    h=1/n
    return (f(0)+f(1)+4*sum(f(i*h) for i in range(1,n,2))+2*sum(f(i*h) for i in range(2,n,2)))*h/3
for k in (.6,1.5,2.2,3.,5.):
    mu=simpson(lambda t:area(k,t))
    expected=PI/4*(1+math.hypot(k,1))
    assert abs(mu-expected)<1e-7,(k,mu,expected)
for k in (kstar*.85,kstar, kstar*1.01, 2.5,3.5):
    # derivative sign count by a grid not taken as proof.
    tmax=k/math.hypot(k,1.)
    d=[derivative(k,(i+.3)/1001*tmax) for i in range(1000)]
    changes=sum(a*b<0 for a,b in zip(d,d[1:]))
    assert changes==(2 if k>kstar else 0),(k,changes)
for k in (kstar*1.01,2.5,3.5):
    tmax=k/math.hypot(k,1.)
    roots=[]
    for i in range(1000):
        lo=i*tmax/1000;hi=(i+1)*tmax/1000
        if derivative(k,lo)*derivative(k,hi)<0:
            roots.append(bisect(lambda x:derivative(k,x),lo,hi))
    assert len(roots)==2
    assert derivative(k,roots[0]-.0001)>0
    assert derivative(k,(roots[0]+roots[1])/2)<0
    assert derivative(k,roots[1]+.0001)>0
print('CONE_BRIGHTNESS_BIFURCATION_OK hull_samples=%d expectations=5 cusp_threshold=%.12f'%(num_hull,kstar))
