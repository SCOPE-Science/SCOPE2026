"""Independent finite checks for the corner-signature Cheeger transition.
Only standard Python is required. Finite checks supplement, not replace, the proof.
"""
import math

PI = math.pi

def area(P):
    return abs(sum(P[i][0]*P[(i+1)%len(P)][1]-P[i][1]*P[(i+1)%len(P)][0] for i in range(len(P))))/2 if len(P)>=3 else 0.0

def geom(P):
    A=area(P); n=len(P)
    L=sum(math.dist(P[i],P[(i+1)%n]) for i in range(n))
    C=0.
    for i in range(n):
        a=P[(i-1)%n]; b=P[i]; c=P[(i+1)%n]
        u=(a[0]-b[0],a[1]-b[1]);v=(c[0]-b[0],c[1]-b[1])
        cross=abs(u[0]*v[1]-u[1]*v[0]);dot=u[0]*v[0]+u[1]*v[1]
        cot=(math.hypot(*u)*math.hypot(*v)+dot)/cross
        C+=cot
    return A,L,C

def inner_polygon(P,d):
    V=P[:]
    for i in range(len(P)):
        x,y=P[i]; X,Y=P[(i+1)%len(P)]
        dx=X-x;dy=Y-y; norm=math.hypot(dx,dy)
        def g(pt):return (dx*(pt[1]-y)-dy*(pt[0]-x))/norm-d
        W=[]
        for j in range(len(V)):
            a=V[j-1]; b=V[j]
            fa=g(a); fb=g(b)
            if (fa>=0)!=(fb>=0):
                v=fa/(fa-fb)
                W.append((a[0]+v*(b[0]-a[0]),a[1]+v*(b[1]-a[1])))
            if fb>=0: W.append(b)
        V=W
        if not V:return []
    return V

def cheeger_radius(P,t):
    A,L,C=geom(P)
    T=math.sqrt(A/PI)
    if t>=T:return (A+L*t+PI*t*t)/(L+2*PI*t)
    lo=0.;hi=1.
    while area(inner_polygon(P,hi))>PI*(t+hi)**2:hi*=2
    for _ in range(120):
        mid=(lo+hi)/2
        if area(inner_polygon(P,mid))>PI*(t+mid)**2:lo=mid
        else:hi=mid
    return t+(lo+hi)/2

def test(P):
    A,L,C=geom(P)
    T=math.sqrt(A/PI)
    D=L+2*PI*T
    assert C>PI, (A,L,C)
    b1=2*PI*T/D
    b2=PI*(4*PI*C*T*T-L*L)/D**3
    for d in [1e-4,1e-3,1e-2]:
        assert abs(area(inner_polygon(P,d))-(A-L*d+C*d*d))<1e-10
    assert abs(cheeger_radius(P,T)-T)<1e-12
    for eps in [0.02,0.005,0.001]:
        r=cheeger_radius(P,T-eps)
        model=T+(b1-1)*eps+b2*eps**2
        assert abs(r-model)<0.2*eps**3,(r,model,eps)
        t=T+eps
        rp=cheeger_radius(P,t)
        assert abs(rp-(A+L*t+PI*t*t)/(L+2*PI*t))<1e-12
    jp=-8*PI**2*(C-PI)/D**3
    assert jp<0
    return A,L,C,T,jp

def regular(n):return [(2*math.cos(2*PI*j/n),2*math.sin(2*PI*j/n)) for j in range(n)]

if __name__=='__main__':
    shapes=[[(0,0),(2,0),(2,2),(0,2)],[(0,0),(4,0),(2,2*math.sqrt(3))]]
    shapes += [regular(n) for n in range(3,16)]
    shapes += [[(-2,-0.5),(1,-1.1),(3,0),(1.4,2),(-1,2.2)]]
    for i,P in enumerate(shapes):
        vals=test(P)
        print('shape',i,'A,L,C,T,h_second_jump:',*(round(x,10) for x in vals))
    print('PASS: 16 convex polygons; 48 inner-offset area checks and 96 Cheeger radius checks; nonzero theoretical jumps')
