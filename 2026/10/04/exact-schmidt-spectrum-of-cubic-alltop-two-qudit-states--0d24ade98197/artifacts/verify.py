#!/usr/bin/env python3
import cmath, math


def nonsquare(p):
    sq={x*x%p for x in range(1,p)}
    for n in range(2,p):
        if n not in sq:
            return n
    raise AssertionError


def fphase(p,nu,x,y):
    return (2*pow(x,3,p)+6*nu*x*(y*y))%p


def check_prime(p):
    nu=nonsquare(p)
    w=cmath.exp(2j*math.pi/p)
    # Exact Schmidt eigenvalues from the circulant Fourier reduction.
    c=(6*nu)%p
    lamb=[]
    for k in range(p):
        count=sum(1 for y in range(p) if (c*y*y-k)%p==0)
        lamb.append(count/p)
    expected=sorted([2/p]*((p-1)//2)+[1/p]+[0.0]*((p-1)//2))
    assert all(abs(a-b)<1e-12 for a,b in zip(sorted(lamb),expected))
    assert abs(sum(lamb)-1)<1e-12

    # Direct Pauli check in the product computational basis.  Global phases
    # from Weyl ordering do not affect the tested magnitudes.
    mag_counts={"one":0,"zero":0,"flat":0}
    fourth=0.0
    tol=2e-10
    for a in range(p):
      for b in range(p):
       for r in range(p):
        for s in range(p):
            zsum=0j
            for x in range(p):
              for y in range(p):
                e=(fphase(p,nu,(x+a)%p,(y+b)%p)-fphase(p,nu,x,y)+r*x+s*y)%p
                zsum += w**e
            amp=zsum/(p*p)
            m=abs(amp)
            fourth += m**4
            if a==b==r==s==0:
                assert abs(m-1)<tol
                mag_counts["one"]+=1
            elif a==b==0:
                assert m<tol
                mag_counts["zero"]+=1
            else:
                assert abs(m-1/p)<tol, (p,a,b,r,s,m)
                mag_counts["flat"]+=1
    assert mag_counts == {"one":1,"zero":p*p-1,"flat":p*p*(p*p-1)}
    target_sum=(2*p*p-1)/(p*p)
    assert abs(fourth-target_sum)<2e-9
    purity=fourth/(p*p)
    target=(2*p*p-1)/(p**4)
    assert abs(purity-target)<2e-10
    return nu,lamb,purity

for p in (5,7):
    nu,lamb,purity=check_prime(p)
    print(f"p={p} nonsquare={nu} purity={purity:.15f} spectrum={sorted(lamb, reverse=True)}")
print("VERIFY_OK")
