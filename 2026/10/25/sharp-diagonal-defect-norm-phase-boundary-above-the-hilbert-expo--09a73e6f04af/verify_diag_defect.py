#!/usr/bin/env python3
"""Numerical consistency checks for diagonal defect curvature.
Proof for the full parameter continuum is in RESULT.md; samples are not proof.
"""
from math import sqrt
from random import Random


def norm_p(x, p):
    return sum(v**p for v in x)**(1.0/p)


def hessian_half(x, d, p):
    q = [v*t for v, t in zip(x, d)]
    s = sum(t**p for t in q)
    h = []
    for i in range(len(x)):
        row=[]
        for j in range(len(x)):
            off=(2-p)*s**(2/p-2)*q[i]**(p-1)*q[j]**(p-1)*d[i]*d[j]
            diag=(p-1)*s**(2/p-1)*q[i]**(p-2)*d[i]**2 if i==j else 0.0
            row.append(off+diag)
        h.append(row)
    return h


def inv_half_hessian_formula(x,d,p):
    q=[v*t for v,t in zip(x,d)]
    qnorm=norm_p(q,p)
    return [[(qnorm**(p-2)*x[i]**(2-p)/d[i]**p if i==j else 0.0)
             /(p-1)+(p-2)*x[i]*x[j]/((p-1)*qnorm**2)
             for j in range(len(x))] for i in range(len(x))]


def dot(a,b):
    return sum(s*t for s,t in zip(a,b))


def mv(m,v):
    return [dot(row,v) for row in m]


def defect(x,d,p):
    n2=norm_p([abs(t) for t in x],p)**2
    q2=norm_p([abs(t*u) for t,u in zip(x,d)],p)**2
    return sqrt(max(0.0,n2-q2))


def main():
    rng=Random(221054)
    tests=0
    for p in (2.15,3.0,4.0,6.5,10.0):
        for d in ((0.8,0.7),(0.97,0.96,0.94),(0.8,0.5,0.4),(0.48,0.48,0.48)):
            n=len(d)
            k=max(d)**p/min(d)**(p-2)
            for _ in range(180):
                x=[rng.uniform(.12,2.0) for i in range(n)]
                v=[rng.uniform(-2,2) for i in range(n)]
                h=hessian_half(x,(1,)*n,p)
                hd=hessian_half(x,d,p)
                ihd=inv_half_hessian_formula(x,d,p)
                for i in range(n):
                    for j in range(n):
                        z=sum(hd[i][a]*ihd[a][j] for a in range(n))
                        assert abs(z-float(i==j))<2e-8,('inverse',p,d,x,i,j,z)
                hratio=dot(v,mv(hd,v))/dot(v,mv(h,v))
                assert hratio <= k+1e-9,('hessian-bound',p,d,x,hratio,k)
                tests+=1
            if k<=1:
                for _ in range(150):
                    x=[rng.uniform(-2,2) for i in range(n)]
                    y=[rng.uniform(-2,2) for i in range(n)]
                    assert defect([a+b for a,b in zip(x,y)],d,p)<=defect(x,d,p)+defect(y,d,p)+1e-9
                    tests+=1
    p=4
    a,b=.9,.8
    k=a**p/b**(p-2)
    assert k>1
    witness=None
    for eps in (0.1,0.03,0.01,0.003):
        # Two points at fixed first-positive coordinate around a j-axis.
        x=[eps,1.0];d=[a,b]
        h=hessian_half(x,[1,1],p);hd=hessian_half(x,d,p)
        if hd[0][0]>h[0][0]:
            delta=eps*0.01
            mid=defect(x,d,p)
            avg=(defect([eps-delta,1.0],d,p)+defect([eps+delta,1.0],d,p))/2
            # Because defect^2 has negative curvature, defect itself may have
            # negative curvature; verify independently by midpoint.
            if mid>avg:
                witness=(eps,delta,mid-avg)
                break
    assert witness,witness
    print('PASS', tests, 'Hessian inverses/Loewner bounds/positive triangles;',
          'nonconvex defect witness', witness)


if __name__=='__main__':
    main()
