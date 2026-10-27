"""Self-contained finite symbolic and numerical checks for a nonlinear opinion model.

No finite test is presented as a proof of all-k or all-initial-data results.
Run: python3 verify.py
"""
from fractions import Fraction as Q
from math import cos, pi


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out


def signed_polynomial(k):
    # (1+r) r Z'(r) - 2k r Z(r), ascending coefficients.
    z = [1] * (2*k+1)
    zd = [0] + [i for i in range(1, 2*k+1)]
    left = mul([1, 1], zd)
    right = [0] + [2*k]*len(z)
    M = max(len(left), len(right))
    left += [0]*(M-len(left));right += [0]*(M-len(right))
    return [a-b for a,b in zip(left,right)]


def factor(k):
    weights = [(j+1)*(2*k-1-j) for j in range(2*k-1)]
    return mul([0,-1,1],weights)


def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def neutral_eigen_and_barrier(k):
    n=2*k+1
    u=[i*(n-i) for i in range(1,n)]
    uext=[0]+u+[0]
    U=sum(u)
    c=Q(1,n)
    for j in range(1,n):
        Lv=Q(uext[j-1]+uext[j+1],2)-uext[j]
        assert Lv==-1
        Ju=Lv+c*Q(U,k)
        assert Ju==Q(2*k-1,3)>0
    phi=[cos(pi*(i+0.5)/n) for i in range(n)]
    assert abs(phi[k])<1e-12
    for i in range(k):
        assert phi[i]>0
    for j in range(n-1):
        assert sum(phi[:j+1])>1e-12



def cdf_exact_checks(k):
    n=2*k+1
    xs=list(range(-k,k+1))
    # Nonuniform strictly positive rational distribution.
    w=[i+1 for i in range(n)]
    z=sum(w)
    p=[Q(v,z) for v in w]
    m=sum(x*y for x,y in zip(xs,p))
    a=Q(k+m,2*k); b=1-a
    fd=[]
    for j in range(n-1):
        fd.append(b*p[j+1]-a*p[j])
    c=Q(1,n)
    D=[sum(p[:j+1])-Q(j+1,n) for j in range(n-1)]
    S=sum(D)
    assert m == -S
    DD=[Q(0)]+D+[Q(0)]
    for j in range(n-1):
        rhs=b*DD[j+2]+a*DD[j]-DD[j+1]+c*S/k
        assert fd[j] == rhs
        # The background coupling term in every off-diagonal derivative is nonnegative.
        assert (p[j]+p[j+1])/Q(2*k)>0
    # An explicit rational barrier is a physical distribution and a strict subsolution.
    u=[Q(i*(n-i)) for i in range(1,n)]
    eps=Q(1,100*n**5)
    U=sum(u)
    uw=[Q(0)]+u+[Q(0)]
    barp=[c+eps*(uw[i+1]-uw[i]) for i in range(n)]
    assert all(v>=0 for v in barp) and sum(barp)==1
    ma=-eps*U
    aa=Q(k+ma,2*k); bb=1-aa
    for j in range(n-1):
        val=eps*(bb*uw[j+2]+aa*uw[j]-uw[j+1]+c*U/k)
        assert val>0

def rhs(k,p):
    xs=list(range(-k,k+1))
    m=sum(float(x)*y for x,y in zip(xs,p))
    a=(k+m)/(2*k); b=1-a
    out=[0.0]*len(p)
    for i,prob in enumerate(p):
        if i<len(p)-1:
            out[i]-=a*prob; out[i+1]+=a*prob
        if i>0:
            out[i]-=b*prob; out[i-1]+=b*prob
    return out


def trajectory(k,p,T=130.0,h=0.025):
    steps=int(T/h)
    for _ in range(steps):
        a=rhs(k,p)
        b=rhs(k,[x+h*y/2 for x,y in zip(p,a)])
        c=rhs(k,[x+h*y/2 for x,y in zip(p,b)])
        d=rhs(k,[x+h*y for x,y in zip(p,c)])
        p=[x+(h/6)*(y+2*z+2*w+v) for x,y,z,w,v in zip(p,a,b,c,d)]
    return p


def run():
    n_polynomials=0
    for k in range(1,41):
        assert trim(signed_polynomial(k))==factor(k)
        neutral_eigen_and_barrier(k)
        cdf_exact_checks(k)
        for r in [Q(1,13),Q(2,5),Q(8,9)]:
            z=sum(r**i for i in range(2*k+1))
            f=-k+sum(i*r**i for i in range(2*k+1))/z
            m=k*(r-1)/(r+1)
            assert f<m
        n_polynomials+=1
    cases=0
    for k in range(1,7):
        for mass_negative in (0.01,0.1,0.65,1.0):
            p=[0.0]*(2*k+1)
            p[k]=1-mass_negative;p[k-1]=mass_negative
            end=trajectory(k,p)
            assert end[0]>0.9999, (k,mass_negative,end)
            assert abs(sum(end)-1)<1e-8
            cases+=1
        p=[0.0]*(2*k+1);p[k]=1
        end=trajectory(k,p)
        assert max(abs(x-1/(2*k+1)) for x in end)<1e-4
    print('PASS: 40 exact polynomial identities, 40 positive subsolution Jacobian checks,')
    print('120 exact stationary-mean comparisons, 40 exact CDF-flux/barrier checks,')
    print('and numerical signs of neutral reflected-walk eigenvectors.')
    print(f'PASS: {cases} independent numerical one-sided trajectories (k=1,...,6)')
    print('and six center-start convergence checks.')
    print('LIMIT: finite symbolic checks and numerical ODE integration are not all-k proofs.')

if __name__=='__main__':run()
