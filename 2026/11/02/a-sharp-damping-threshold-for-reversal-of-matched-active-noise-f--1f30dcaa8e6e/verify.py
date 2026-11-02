"""Exact stationary moment recurrences for two matched active oscillator forcings."""
import sympy as s

def stationary_m4(a,b,d,kind):
    a,b,d=map(s.Rational,(a,b,d)); om=a*a+b*b
    M={(0,0,0):s.Integer(1)}
    if kind=='ABP':
        for n in range(1,5):M[(0,0,n)]=s.Integer(0)
    else:M[(0,0,1)]=s.Integer(0)
    for k in range(1,5):
        ns=range(5-k) if kind=='ABP' else range(2)
        pairs=[(p,k-p,n) for n in ns for p in range(k+1)]
        symbols={idx:s.Symbol('z%d_%d_%d'%idx) for idx in pairs}
        def get(p,q,n):
            if kind=='ABP':n=abs(n)
            return symbols[(p,q,n)] if p+q==k else M[(p,q,n)]
        equations=[]
        for p,q,n in pairs:
            cur=s.Integer(0)
            if p: cur+=p*get(p-1,q+1,n)
            cur-=(2*a*q+d*(n*n if kind=='ABP' else n))*get(p,q,n)
            if q:
                cur-=om*q*get(p+1,q-1,n)
                if kind=='ABP':
                    cur+=q/s.sqrt(2)*(get(p,q-1,n+1)+get(p,q-1,n-1))
                else:cur+=q*get(p,q-1,1-n)
            equations.append(cur)
        sol=s.solve(equations,list(symbols.values()),dict=True)[0]
        for idx,z in symbols.items(): M[idx]=s.simplify(sol[z])
    return s.factor(M[(4,0,0)]),s.factor(M[(2,0,0)])


def theoretical_gap(a,b,d):
    a,b,d=map(s.Rational,(a,b,d))
    z=b*b
    c0=(432*a**6+1846*a**5*d+2828*a**4*d*d+1887*a**3*d**3
        +588*a*a*d**4+93*a*d**5+6*d**6)
    c1=156*a**4+544*a**3*d+797*a*a*d*d+417*a*d**3+51*d**4
    c2=12*a*a-30*a*d-27*d*d
    den=(8*a*(a+2*d)*(a*a+b*b)*(4*a*a+b*b)
        *((a+d)**2+b*b)*((a+2*d)**2+b*b)
        *((3*a+d)**2+b*b)*((3*a+d)**2+9*b*b))
    return s.cancel(3*(c0+c1*z+c2*z*z)/den)


def run_checks():
    cases=[(1,1,1),(1,2,1),(1,10,1),(4,10,1),(1,3,2),(2,1,3)]
    for a,b,d in cases:
        Ma,Va=stationary_m4(a,b,d,'ABP')
        Mt,Vt=stationary_m4(a,b,d,'RTP')
        assert Va==Vt
        assert s.cancel(Ma-Mt-theoretical_gap(a,b,d))==0
        print('exact generator identity:',(a,b,d),'difference=',Ma-Mt)
    assert theoretical_gap(1,2,1)>0
    assert theoretical_gap(1,10,1)<0
    assert theoretical_gap(4,10,1)>0
    c0=s.Integer(7680);c1=s.Integer(1965);c2=s.Integer(-45)
    root=s.sqrt((s.Integer(131)+s.sqrt(23305))/6)
    assert s.simplify(c0+c1*root**2+c2*root**4)==0
    for a,b,d in cases:
        a,b,d=map(s.Rational,(a,b,d));v=(2*a+d)/(2*a*(a*a+b*b)*((a*a+b*b)+d*(2*a+d)))
        assert s.cancel(stationary_m4(a,b,d,'ABP')[1]-v)==0
    print('All exact-rational verification identities passed.')


if __name__ == '__main__':
    run_checks()
