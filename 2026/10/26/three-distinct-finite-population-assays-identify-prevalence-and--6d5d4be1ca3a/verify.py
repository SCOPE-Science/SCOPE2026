"""Exact checks for finite-population one-assay diagnostic identification.

All enumerations use fractions; execution needs only Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json


def falling(n,k):
    z=1
    for j in range(k): z*=n-j
    return z


def observed_law(N,M,a,b,draws):
    # Random ordered distinct members, independent conditional assay errors.
    law={y:F(0) for y in product((0,1),repeat=draws)}
    for x in product((0,1),repeat=draws):
        r=sum(x)
        if r>M or draws-r>N-M: continue
        px=F(falling(M,r)*falling(N-M,draws-r),falling(N,draws))
        for y in law:
            py=F(1)
            for xi,yi in zip(x,y):
                t=a if xi else b
                py*=t if yi else 1-t
            law[y]+=px*py
    assert sum(law.values())==1
    return law


def moments(law,draws):
    u=sum(pr*y[0] for y,pr in law.items())
    v=sum(pr*(y[0]-u)*(y[1]-u) for y,pr in law.items()) if draws>=2 else None
    w=sum(pr*(y[0]-u)*(y[1]-u)*(y[2]-u) for y,pr in law.items()) if draws>=3 else None
    return u,v,w


def verify():
    configs=0; equal_pairs=0; pair_examples=[]; example=None
    for N in range(3,12):
        for M in range(1,N):
            for a,b in ((F(4,5),F(1,10)),(F(7,8),F(1,5)),(F(3,4),F(1,4)),(F(9,10),F(1,8))):
                c=a-b;p=F(M,N)
                law=observed_law(N,M,a,b,3)
                u,v,w=moments(law,3)
                assert u==b+c*p
                assert v==-c*c*p*(1-p)/F(N-1)
                assert w==2*c**3*p*(1-p)*(1-2*p)/F((N-1)*(N-2))
                # The algebraic inverse: infer p from variance/third moment,
                # respecting the sign; confirm the exact rational polynomial.
                if w==0: assert p==F(1,2)
                else:
                    s=F(1)-2*p
                    assert (w>0)==(s>0)
                    assert (w*w*F((N-2)**2)*p*(1-p)
                            ==4*F(N-1)*(-v)**3*s*s)
                configs+=1
                if N==7 and M==2 and a==F(4,5):
                    example={
                        'N':N,'M':M,'sensitivity':str(a),'false_positive_rate':str(b),
                        'mean':str(u),'cross_covariance':str(v),'cross_third_central':str(w)}
        c=F(1,4);p=F(1,N);q=1-p;u=F(1,2)
        a1=u+c*(1-p);b1=u-c*p
        a2=u+c*(1-q);b2=u-c*q
        law1=observed_law(N,1,a1,b1,2)
        law2=observed_law(N,N-1,a2,b2,2)
        assert law1==law2
        mean1,cov1,_=moments(law1,2)
        assert mean1==u and cov1==-F(1,16*N*N)
        t1=moments(observed_law(N,1,a1,b1,3),3)[2]
        t2=moments(observed_law(N,N-1,a2,b2,3),3)[2]
        assert t1==F(1,32*N**3) and t2==-t1
        equal_pairs+=1
        pair_examples.append({'N':N,'paired_models':[[1,str(a1),str(b1)],[N-1,str(a2),str(b2)]],
                              'pair_covariance':str(cov1),'third_moments':[str(t1),str(t2)]})
    return {'model_configurations':configs,'two_draw_equivalence_checks':equal_pairs,
            'illustrative_case':example,'paired_examples':pair_examples}

if __name__=='__main__':
    print(json.dumps(verify(),indent=2,sort_keys=True))
