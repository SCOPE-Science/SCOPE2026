"""Independent finite checks of two-harmonic circle-map locking coefficients."""
import cmath
import math


def scalar_coefficients(p,q,m,A,B,phi,psi):
    n=q-m
    C=1/math.tan(math.pi*p*m/q)
    c0=-math.pi*q*(m*A*A-n*B*B)*C/2
    cq=(math.pi*q*A*B/4)*complex(-(n-m)*C,q)*cmath.exp(1j*(phi+psi))
    return c0,cq


def direct_s2(x,p,q,m,A,B,phi,psi):
    n=q-m
    h=lambda y:A*math.sin(2*math.pi*m*y+phi)+B*math.sin(2*math.pi*n*y+psi)
    hp=lambda y:2*math.pi*(m*A*math.cos(2*math.pi*m*y+phi)+n*B*math.cos(2*math.pi*n*y+psi))
    return sum(hp(x+j*p/q)*h(x+i*p/q) for j in range(q) for i in range(j))


def q_return(x,p,q,m,A,B,phi,psi,eps,delta):
    n=q-m
    w=p/q+delta
    y=x
    for j in range(q):
        y+=w+eps*(A*math.sin(2*math.pi*m*y+phi)+B*math.sin(2*math.pi*n*y+psi))
    return y-x-p


def critical_detuning(x,p,q,m,A,B,phi,psi,eps):
    c0,cq=scalar_coefficients(p,q,m,A,B,phi,psi)
    U=2*(abs(c0)+2*abs(cq)+1)*eps*eps/q
    left,right=-U,U
    assert q_return(x,p,q,m,A,B,phi,psi,eps,left)<0
    assert q_return(x,p,q,m,A,B,phi,psi,eps,right)>0
    for _ in range(65):
        mid=(left+right)/2
        if q_return(x,p,q,m,A,B,phi,psi,eps,mid)>0:
            right=mid
        else:
            left=mid
    return (left+right)/2


def execute():
    tests=[(3,1,1,1.2,.7,.15,-.3),(4,1,1,1.2,.7,.15,-.3),
        (5,2,2,1.1,-.8,.2,-.6),(6,5,1,.8,-.9,.8,1.7),
        (7,3,2,-1.3,.9,-1.5,.4),(8,3,3,.7,.9,1.2,-.2),
        (11,4,5,1.2,-.7,.4,1.7)]
    count=0
    for q,p,m,A,B,phi,psi in tests:
        c0,cq=scalar_coefficients(p,q,m,A,B,phi,psi)
        for ix in range(41):
            x=(ix+0.3)/41
            v=direct_s2(x,p,q,m,A,B,phi,psi)
            exp=c0+2*(cq*cmath.exp(2j*math.pi*q*x)).real
            assert abs(v-exp)<1e-8*(1+abs(v)), (q,p,m,x,v,exp)
            count+=1
        x=.271828
        error=[]
        for eps in (.012/q,.006/q,.003/q):
            value=q_return(x,p,q,m,A,B,phi,psi,eps,0)
            approx=eps*eps*(c0+2*(cq*cmath.exp(2j*math.pi*q*x)).real)
            error.append(abs(value-approx))
        assert error[0]>error[1]*5 and error[1]>error[2]*5, (q,error)
        count+=2
    # Directly locate periodic-point thresholds, without assuming the predicted extremizers.
    for q,p,m,A,B,phi,psi in tests[:5]:
        eps=.0006
        roots=[critical_detuning((j+0.37)/600,p,q,m,A,B,phi,psi,eps) for j in range(600)]
        observed=max(roots)-min(roots)
        n=q-m
        formula=math.pi*abs(A*B)*math.hypot(q,(n-m)/math.tan(math.pi*p*m/q))*eps*eps
        assert abs(observed-formula)/formula<.02,(q,observed,formula)
        count+=1
    print(f'PASS: {count} direct harmonic/return/threshold finite checks')

if __name__=='__main__':execute()
