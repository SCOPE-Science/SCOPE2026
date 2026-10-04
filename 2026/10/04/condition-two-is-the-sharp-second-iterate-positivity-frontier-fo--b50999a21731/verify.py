from fractions import Fraction as F

def moments(lam,b):
    return {j:sum((b[i]*b[i]*(lam[i]**j) for i in range(len(lam))),F(0))
            for j in range(1,5)}

def minres2_diag(lam,b):
    m=moments(lam,b)
    Delta=m[2]*m[4]-m[3]*m[3]
    c0=(m[1]*m[4]-m[2]*m[3])/Delta
    c1=(m[2]*m[2]-m[1]*m[3])/Delta
    beta=-c1
    theta=c0/beta
    x2=[b[i]*(c0+c1*lam[i]) for i in range(len(lam))]
    alpha1=m[1]/m[2]
    x1=[alpha1*z for z in b]
    return m,c0,c1,beta,theta,x1,x2

def pairwise(lam,b):
    D=F(0); N=F(0)
    for i in range(len(lam)):
        wi=b[i]*b[i]
        for j in range(i+1,len(lam)):
            wj=b[j]*b[j]
            x,y=lam[i],lam[j]
            w=wi*wj*x*y*(x-y)*(x-y)
            D+=w
            N+=w*(x+y)
    return D,N

tests=[
    ([F(1),F(2),F(4)],[F(1),F(1),F(1,10)]),
    ([F(2),F(5),F(7)],[F(3),F(1),F(2)]),
    ([F(1),F(3),F(8),F(10)],[F(1),F(2),F(1),F(3)])
]
for lam,b in tests:
    m,c0,c1,beta,theta,x1,x2=minres2_diag(lam,b)
    D,N=pairwise(lam,b)
    assert D==m[1]*m[3]-m[2]*m[2]
    assert N==m[1]*m[4]-m[2]*m[3]
    assert theta==N/D
    assert beta>0 and c1<0

# Explicit kappa=4 witness.
lam=[F(1),F(2),F(4)]
b=[F(1),F(1),F(1,10)]
m,c0,c1,beta,theta,x1,x2=minres2_diag(lam,b)
assert c0==F(243,200)
assert c1==F(-67,200)
assert beta==F(67,200)
assert theta==F(243,67)
assert x1==[F(76,129),F(76,129),F(38,645)]
assert x2==[F(22,25),F(109,200),F(-1,80)]
xstar=[F(1),F(1,2),F(1,40)]
assert all(z>0 for z in xstar)
assert x2[2]<0

# Sharpness family. Use t=eps^2 directly in spectral weights.
for K in [F(5,2),F(3),F(4),F(7),F(10)]:
    s=K/F(2)
    denom=K**4+16*(K-1)**2
    tcrit=(K-2)**3/denom
    for t,sign in [(tcrit/F(2),1),(tcrit*F(2),-1)]:
        # pairwise weights for squared b-components 1,1,t
        l=[F(1),s,K]
        w=[F(1),F(1),t]
        D=F(0); N=F(0)
        for i in range(3):
            for j in range(i+1,3):
                x,y=l[i],l[j]
                ww=w[i]*w[j]*x*y*(x-y)**2
                D+=ww
                N+=ww*(x+y)
        theta=N/D
        closed=((K-2)**3-t*denom)/(2*((K-2)**2+t*(K**3+8*K**2-16*K+8)))
        assert K-theta==closed
        if sign>0:
            assert theta<K
        else:
            assert theta>K

print("VERIFY_OK")
