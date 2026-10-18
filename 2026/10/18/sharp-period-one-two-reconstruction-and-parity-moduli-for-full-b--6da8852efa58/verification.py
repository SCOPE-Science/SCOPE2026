"""Exact diagnostic checks for a finite periodic-data rigidity theorem.
Public implementation: rational computations, no private source data.
"""
from fractions import Fraction as Q
from random import Random


def fixed_points(b):
    m=len(b)-1
    p=[]
    for i in range(1,m+1):
        l,r=b[i-1],b[i]
        if i%2:
            p.append(l/(1-r+l))
        else:
            p.append(r/(1+r-l))
    return p


def periodic_two(b):
    m=len(b)-1
    ab=[]
    for i in range(1,m+1):
        delta=b[i]-b[i-1]
        ab.append((b[i-1] if i%2 else b[i], delta if i%2 else -delta))
    out=[]
    for i,(a,c) in enumerate(ab,1):
        for j,(d,e) in enumerate(ab,1):
            if i==j:continue
            q=(a+c*d)/(1-c*e)
            assert b[i-1]<q<b[i],(i,j,b,q)
            out.append((q,i,j))
    return sorted(out)


def reconstruct(p,knob=None):
    m=len(p)
    if m%2:
        assert knob is not None
        t=knob*(1-p[1])/(p[1]-knob)
    else:
        last=2-1/p[-1]
        # Affine forward propagation b_{m-1}=A+B*t
        A=B=Q(0)
        for i in range(1,m):
            if i==1:
                A,B=Q(0),Q(1)
            elif i%2==0:
                K=p[i-1]/(1-p[i-1]); A,B=K*(1-A),-K*B
            else:
                K=(1-p[i-1])/p[i-1]; A,B=1-K*A,-K*B
        t=(last-A)/B
    b=[Q(0),t]
    for i in range(2,m):
        if i%2==0:b.append(p[i-1]*(1-b[-1])/(1-p[i-1]))
        else:b.append(1-(1-p[i-1])*b[-1]/p[i-1])
    b.append(Q(1))
    assert all(u<v for u,v in zip(b,b[1:])),b
    return b


def check():
    rng=Random(6202610)
    checks=0
    for m in range(2,15):
        for trial in range(20):
            weights=[rng.randrange(1,21) for _ in range(m)]
            tot=sum(weights)
            b=[Q(0)]
            for w in weights:b.append(b[-1]+Q(w,tot))
            p=fixed_points(b)
            prime=periodic_two(b)
            assert len(prime)==m*(m-1)
            first=prime[0]
            assert (first[1],first[2])==(1,2),(m,first)
            q=first[0]
            assert q==p[1]*b[1]/(1-p[1]+b[1]),(m,trial,q)
            r=reconstruct(p, q if m%2 else None)
            assert r==b,(m,trial,r,b)
            checks+=1
            if m%2 and trial==0:
                step=Q(1,1000)
                for _ in range(100):
                    t2=b[1]+step
                    q2=p[1]*t2/(1-p[1]+t2)
                    try:
                        b2=reconstruct(p,q2)
                    except AssertionError:
                        step/=2
                        continue
                    assert fixed_points(b2)==p
                    assert b2!=b and periodic_two(b2)[0][0]!=q
                    checks+=1
                    break
                else:
                    raise AssertionError('No rational perturbation found')
    # A whole rational one-parameter family with three laps and identical fixed points.
    for t in [Q(1,20),Q(1,10),Q(1,4),Q(1,3),Q(2,5)]:
        b=[Q(0),t,1-t,Q(1)]
        assert fixed_points(b)==[Q(0),Q(1,2),Q(1)]
        p2=periodic_two(b)
        assert p2[0][0]==t/(1+2*t)
        checks+=1
    return checks

if __name__=='__main__':
    print('Exact deterministic rational samples passed:',check())
