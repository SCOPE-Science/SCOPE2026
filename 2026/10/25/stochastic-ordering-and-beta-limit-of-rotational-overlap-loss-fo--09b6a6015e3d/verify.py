"""Standalone numerical checks of the random-rotation overlap theorem.
Only computational corroboration; the universal result uses an analytic proof.
"""
import math
import random


def regular_polygon(n, phi):
    return [(math.cos(phi+2*math.pi*j/n), math.sin(phi+2*math.pi*j/n)) for j in range(n)]


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


def sub(a,b):
    return (a[0]-b[0],a[1]-b[1])


def segment_line_intersection(a,b,c,d):
    v=sub(b,a);w=sub(d,c)
    den=cross(v,w)
    if abs(den)<1e-14:
        return a
    t=cross(sub(c,a),w)/den
    return (a[0]+t*v[0],a[1]+t*v[1])


def intersection_area(n,phi):
    p=regular_polygon(n,0.)
    q=regular_polygon(n,phi)
    for j in range(n):
        v=q[j];w=q[(j+1)%n]
        new=[]
        if not p:
            return 0.
        for i,a in enumerate(p):
            b=p[(i+1)%len(p)]
            fa=cross(sub(w,v),sub(a,v))
            fb=cross(sub(w,v),sub(b,v))
            if fa>=-1e-12:
                new.append(a)
            if (fa < -1e-12 and fb > 1e-12) or (fa > 1e-12 and fb < -1e-12):
                new.append(segment_line_intersection(a,b,v,w))
        p=new
    return abs(sum(cross(p[i],p[(i+1)%len(p)]) for i in range(len(p))))/2


def formulas(n,u):
    k=math.pi/n
    c=math.cos(k)
    a_n=n*math.sin(k)*c
    dmax=a_n*math.tan(k/2)**2
    q=(math.tan((1+u)*k/2)*math.tan((1-u)*k/2)/math.tan(k/2)**2)
    return a_n,dmax,q


def run():
    rng=random.Random(191026)
    trials=0
    for n in range(3,31):
        for j in range(31):
            u=(j+.37)/31
            phi=math.pi/n*(1-u)
            a,d,q=formulas(n,u)
            measured=intersection_area(n,phi)
            theoretical=a-d*q
            assert abs(measured-theoretical)<1e-9, (n,u,measured,theoretical)
            trials+=1
    print('DIRECT_HALFPLANE_POLYGON_CLIPPING_IDENTITY_OK',trials)

    for j in range(1,200):
        u=j/200
        a=1-u*u
        prev=2.
        for n in range(3,150):
            q=formulas(n,u)[2]
            assert q<=prev+1e-12,(n,u,prev,q)
            assert q>a-1e-12,(n,u,a,q)
            prev=q
    print('STRICT_ORDER_BY_POLYGON_SIDES_AND_BETA_BOUND_OK')

    for n in [3,4,5,9,13,28]:
        k=math.pi/n
        c=math.cos(k)
        N=15000
        samples=[rng.random() for _ in range(N)]
        qvalues=[formulas(n,u)[2] for u in samples]
        expect_q=(math.tan(k)-(2/k)*math.log(1/c))/(math.tan(k)*math.tan(k/2)**2)
        assert abs(sum(qvalues)/N-expect_q)<.015,(n,expect_q,sum(qvalues)/N)
        for x in [.11,.27,.5,.71,.9]:
            h=x*(1-c)/(1+c)
            z=c*(1+h)/(1-h)
            F=1-math.acos(max(-1,min(1,z)))/k
            empirical=sum(q<=x for q in qvalues)/N
            assert abs(empirical-F)<.026,(n,x,F,empirical)
    print('EXACT_CDF_AND_EXACT_MEAN_MONTE_CARLO_OK')

    for n in [30,60,120,240]:
        k=math.pi/n
        differences=[]
        for j in range(1,100):
            u=j/100
            exact=formulas(n,u)[2]
            two=1-u*u + k*k*u*u*(1-u*u)/6
            differences.append(abs(exact-two))
        assert max(differences)< .03*k**4,(n,max(differences),k**4)
    print('UNIFORM_SECOND_ORDER_EXPANSION_NUMERICS_OK')

    print('ALL_ROTATED_POLYGON_OVERLAP_CHECKS_OK')

if __name__=='__main__':
    run()
