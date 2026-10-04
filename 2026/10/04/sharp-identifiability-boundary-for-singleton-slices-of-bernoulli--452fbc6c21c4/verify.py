import math

def phi(n,u):
    return u*(1-u)**(n-1)

def fingerprint_hom(n,u):
    return [phi(n,u)]*n

def bisect_companion(n,b,steps=120):
    target=phi(n,b)
    lo,hi=0.0,1.0/n
    for _ in range(steps):
        mid=(lo+hi)/2
        if phi(n,mid)<target:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def main():
    for n in range(2,9):
        ustar=1.0/n
        # derivative sign of the homogeneous profile around the unique fold
        left=ustar*0.8
        right=ustar+(1-ustar)*0.1
        dleft=(1-left)**(n-2)*(1-n*left)
        dright=(1-right)**(n-2)*(1-n*right)
        assert dleft>0 and dright<0
        b=ustar+(1-ustar)*0.08
        a=bisect_companion(n,b)
        assert 0<a<ustar<b<1
        assert abs(phi(n,a)-phi(n,b))<1e-12
        # distinct marginals imply positive product TV
        assert b-a>0
        # boundary ratio lower bound: TV >= eps, singleton discrepancy exact
        ratios=[]
        for k in range(6,12):
            eps=ustar*(2.0**(-k))
            delta=n*(phi(n,ustar)-phi(n,ustar-eps))
            ratios.append(eps/delta)
        assert all(ratios[i+1]>ratios[i] for i in range(len(ratios)-1))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
