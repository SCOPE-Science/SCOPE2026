"""Standalone numerical consistency checks for the axial cap-body illumination theorem.

The analytic proof does not depend on finite computation.
"""
import math
import random


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def build(q):
    assert all(0<t<1 for t in q)
    assert all(q[i]+q[j]>=1-1e-14 for i in range(3) for j in range(i+1,3))
    pairs=[(i,j) for i in range(3) for j in range(i+1,3) if q[i]+q[j]>1+1e-13]
    if not pairs:
        assert all(abs(t-0.5)<1e-13 for t in q)
        return None
    i,j=pairs[0]
    k=3-i-j
    c=[math.sqrt(1-t) for t in q]
    lo=math.asin(c[j]); hi=math.acos(c[i]); theta=(lo+hi)/2
    delta=min((hi-lo)/4,math.sqrt(q[k])/2)
    assert delta>0
    def unit_angle(phi):
        return (math.cos(phi),math.sin(phi))
    u=unit_angle(theta); up=unit_angle(theta+delta)
    w=((up[0]-u[0])/2,(up[1]-u[1])/2)
    z=math.sqrt(1-w[0]**2-w[1]**2)
    assert z>c[k]
    def xyz(a,b,c3):
        arr=[0.,0.,0.]
        arr[i]=a; arr[j]=b; arr[k]=c3
        return arr
    v=[xyz(u[0],u[1],0),xyz(-up[0],-up[1],0),xyz(w[0],w[1],z),xyz(w[0],w[1],-z)]
    assert all(abs(dot(t,t)-1)<1e-13 for t in v)
    assert all(abs(sum(v[a][b] for a in range(4)))<1e-13 for b in range(3))
    det=dot(v[0],cross(v[1],v[2]))
    assert abs(det)>1e-14, (q,det)
    assert all(any(sign*t[axis]<-c[axis] for t in v) for axis in range(3) for sign in (-1,+1))
    return v


samples=[(.8,.8,.2),(.50001,.49999,.50001),(.7,.3,.8),(.5625,.5625,.5625),(.9,.9,.1),(.5,.5,.5)]
for q in samples:
    build(q)
random.seed(1707)
count=0
for _ in range(300):
    q=tuple(random.uniform(.5,.99) for i in range(3))
    build(q)
    count+=1
print(f'VERIFY_OK: {len(samples)} structured and {count} random consistency cases; non-exhaustive numerical checks only')
