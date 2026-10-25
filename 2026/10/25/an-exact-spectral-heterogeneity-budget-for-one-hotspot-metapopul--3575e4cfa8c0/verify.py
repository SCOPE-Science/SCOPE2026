"""Reproduce exact spectral threshold identities for a one-hotspot SIR mobility model.
Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as s

M,p,r,z=s.symbols('M p r z', positive=True, real=True)
m=M-1
T=s.Matrix([[1-p,s.sqrt(m)*p],[s.sqrt(m)*p,1-m*p]])
Q=T*s.diag(1,z)*T
L=(1-p)**2 + m*p**2 + z*(m*p**2+(1-m*p)**2)
assert s.simplify(s.trace(Q)-L)==0
assert s.simplify(Q.det()-z*(1-M*p)**2)==0
identity=(M-r*(m+z))/M-r*M*(1+z*(m-M*r))*(p-1/M)**2
assert s.simplify((s.eye(2)-r*Q).det()-identity)==0

R=s.Rational(4,5); Z=s.Rational(11,5); size=5
zcrit=1+size*(1-R)/R
assert zcrit==s.Rational(9,4)
threshold=(zcrit-Z)/(size*(Z-1)*(1-R))
assert threshold==s.Rational(1,24)

hub=[s.Rational(17,50),s.Rational(3,50),s.Rational(1,5),s.Rational(1,5)]
def movement(background_edge):
    result=s.zeros(5)
    for i in range(4):
        for j in range(4):
            result[i,j]=1-hub[i]-3*background_edge if i==j else background_edge
        result[i,4]=result[4,i]=hub[i]
    result[4,4]=1-sum(hub)
    assert result==result.T
    assert all(x>=0 for x in result)
    assert all(sum(result[i,j] for j in range(5))==1 for i in range(5))
    return result

exact=[]
for d in [s.Rational(1,10),s.Rational(1,5)]:
    F=movement(d)
    v=F[:,4]
    # Independent calculation using a rational matrix inverse, not eigenvectors.
    H=s.factor((v.T*(s.eye(5)-R*F**2).inv()*v)[0]
               -1/(5*(1-R)))
    K=R*F*s.diag(1,1,1,1,Z)*F
    char_at_one=s.factor((s.eye(5)-K).det())
    variance=s.factor(((v-s.ones(5,1)/5).T*(v-s.ones(5,1)/5))[0])
    assert variance==s.Rational(49,1250)
    assert variance <= H <= variance/(1-R)
    assert (H<threshold)==(char_at_one>0)
    exact.append((H,char_at_one))
assert exact==[(s.Rational(529543,11008272),-s.Rational(111229704,152587890625)),
               (s.Rational(245,5956),s.Rational(113164,1220703125))]
assert exact[0][0]>threshold>exact[1][0]

# Every admissible row-stochastic symmetric flux with the *same uniform* hub
# column has the identical dominant quotient eigenvalue. Exact five-by-five
# checks exercise four different background mobilities at two hub strengths.
for p0 in [s.Rational(1,5),s.Rational(1,4)]:
    row=1-p0
    Bcases={"isolated":s.zeros(4),"cycle":s.zeros(4),
            "matching":s.zeros(4),"irregular":s.zeros(4)}
    for i in range(4): Bcases['isolated'][i,i]=row
    for i in range(4):
        for j in range(i+1,4):
            if (j-i)%4 in (1,3):
                Bcases['cycle'][i,j]=Bcases['cycle'][j,i]=s.Rational(1,20)
    Bcases['matching'][0,1]=Bcases['matching'][1,0]=s.Rational(1,10)
    Bcases['matching'][2,3]=Bcases['matching'][3,2]=s.Rational(3,20)
    for i in range(4):
        for j in range(i+1,4):
            Bcases['irregular'][i,j]=Bcases['irregular'][j,i]=s.Rational(i+j+1,100)
    expected_q=(R*Q).subs({M:5,r:R,z:Z,p:p0})
    expected_max=max(expected_q.eigenvals(),key=lambda x:float(s.N(x)))
    for name,B in Bcases.items():
        if name!='isolated':
            for i in range(4):
                B[i,i]=row-sum(B[i,j] for j in range(4) if i!=j)
        assert all(x>=0 for x in B)
        F=s.zeros(5)
        for i in range(4):
            for j in range(4): F[i,j]=B[i,j]
            F[i,4]=F[4,i]=p0
        F[4,4]=1-4*p0
        assert F==F.T
        assert all(sum(F[i,j] for j in range(5))==1 for i in range(5))
        K=R*F*s.diag(1,1,1,1,Z)*F
        eigen=K.eigenvals()
        largest=max(eigen,key=lambda x:float(s.N(x)))
        assert s.simplify(largest-expected_max)==0,(name,p0)

print('PASS: symbolic characteristic identities, spectral-energy thresholds,')
print('two exact opposite classifications with identical hub column,')
print('and eight full-matrix quotient comparisons.')
