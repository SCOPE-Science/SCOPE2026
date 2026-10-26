"""Independent algebra and exact finite-circle checks for a two-periodic spline projection.

Requires Python 3 and SymPy >= 1.12. Run: python CHECKER.py
"""
from fractions import Fraction as Q
import sympy as s


def exact_abs_integral(u, v):
    if u*v >= 0:
        return (abs(u)+abs(v))/2
    return (u*u+v*v)/(2*(abs(u)+abs(v)))


def invert_rational(a):
    n=len(a)
    z=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(a)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if z[i][k])
        z[k],z[pivot]=z[pivot],z[k]
        t=z[k][k];z[k]=[v/t for v in z[k]]
        for i in range(n):
            if i==k:continue
            t=z[i][k]
            if t:z[i]=[v-t*w for v,w in zip(z[i],z[k])]
    return [row[n:] for row in z]


def circle_norm(m,a,b):
    n=2*m
    lengths=[a if j%2==0 else b for j in range(n)]
    g=[[Q(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        g[j][j]+=2*(lengths[j-1]+lengths[j])
        g[j][(j+1)%n]+=lengths[j]
        g[j][(j-1)%n]+=lengths[j-1]
    inv=invert_rational(g)
    rows=[6*sum((lengths[j]*exact_abs_integral(row[j],row[(j+1)%n]) for j in range(n)),Q(0)) for row in inv]
    assert len(set(rows))==1
    return rows[0]


def proposed(a,b):
    return (5*a*a+22*a*b+5*b*b)/((3*a+b)*(a+3*b))


def algebra_certificate():
    a,b,r=s.symbols('a b r')
    c=3*a*a+8*a*b+3*b*b
    d=2*a*b
    F=c-d*r
    D=2*(a+b)/F
    E=(a+b*r)/F
    H=(b+a*r)/F
    J=lambda x,y:(x*x+y*y)/(2*(x+y))
    expr=6/(1-r)*(a*J(D,E)+b*J(E,D*r)+b*J(D,H)+a*J(H,D*r))
    target=(5*a*a+22*a*b+5*b*b)/((3*a+b)*(a+3*b))
    num,den=s.fraction(s.factor(expr-target))
    assert s.Poly(den,r)!=s.Poly(0,r)
    assert s.rem(num,d*r*r-2*c*r+d,r)==0
    return 'exact polynomial divisibility proved'


def main():
    checks=0
    print(algebra_certificate());checks+=1
    for a,b in [(Q(1),Q(1)),(Q(1),Q(2)),(Q(1),Q(5)),(Q(2),Q(3)),(Q(3),Q(5))]:
        sharp=proposed(a,b)
        assert Q(5,3)<sharp<=2;checks+=1
        assert sharp==2-(a-b)**2/((3*a+b)*(a+3*b));checks+=1
        previous=Q(0)
        for m in [2,3,4,5,7,10,12]:
            val=circle_norm(m,a,b)
            assert 1<=val<sharp;checks+=1
            assert val>previous;checks+=1
            previous=val
        assert float(sharp-previous)<1e-3;checks+=1
        print(f'(a,b)=({a},{b}) sharp={sharp}, circle m=12: {previous}, deficit={float(sharp-previous):.7g}')
    print('PASS checks:',checks)

if __name__=='__main__': main()
