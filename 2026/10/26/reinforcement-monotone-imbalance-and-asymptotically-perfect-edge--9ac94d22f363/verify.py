"""Independent finite-state checks for two competing edge counts on a three-vertex path.

Run with Python >=3.10; standard library only. The checks are finite diagnostics;
the analytical coupling and variance recursion prove the infinite statements.
"""
from fractions import Fraction
from math import atanh, tanh, exp, factorial, sqrt

def distribution(n, alpha, center=4.0, leaf=1.0, initial=1.0):
    c=center/(center+2*leaf)
    d={0:1.0}
    for j in range(n):
        new={}
        s=2*initial+j
        for diff,prob in d.items():
            z=diff/s
            if alpha==0:
                m=0.0
            else:
                # Direct positive-weight probability (numerically stable here).
                x=(initial+(j+diff)/2)**alpha
                y=(initial+(j-diff)/2)**alpha
                m=c*(x-y)/(x+y)
            p=(1+m)/2
            new[diff+1]=new.get(diff+1,0)+prob*p
            new[diff-1]=new.get(diff-1,0)+prob*(1-p)
        d=new
    return d

def exact_distribution(n, exponent=Fraction(1), center=Fraction(4), leaf=Fraction(1), initial=Fraction(1)):
    assert exponent in (0,1,2)
    c=center/(center+2*leaf)
    d={0:Fraction(1)}
    for j in range(n):
        new={}
        for diff,prob in d.items():
            a=(initial+Fraction(j+diff,2))**exponent
            b=(initial+Fraction(j-diff,2))**exponent
            m=c*(a-b)/(a+b)
            p=(1+m)/2
            new[diff+1]=new.get(diff+1,0)+prob*p
            new[diff-1]=new.get(diff-1,0)+prob*(1-p)
        d=new
    return d

def second(d): return sum(prob*diff*diff for diff,prob in d.items())
def tails(d):
    return {k:sum(p for j,p in d.items() if abs(j)>=k) for k in range(1,max(map(abs,d))+1)}

checks=0
for exponent in (0,1,2):
    for n in range(1,14):
        d=exact_distribution(n,exponent)
        assert sum(d.values())==1
        assert all(d.get(k,0)==d.get(-k,0) for k in d)
        assert sum(k*p for k,p in d.items())==0
        if exponent==0: assert second(d)==n
        elif n>=2: assert second(d)>n
        checks+=4
for n in range(2,31):
    ds=[distribution(n,a) for a in (0,.3,.7,.95,1.,2.)]
    ts=[tails(d) for d in ds]
    for i in range(len(ts)-1):
        assert all(ts[i][k]<=ts[i+1][k]+1e-12 for k in ts[i])
        assert second(ds[i]) < second(ds[i+1]) + 1e-12
        checks+=2
    checks+=1

# One-step second-moment inequality, using both exact and numerical distributions.
for alpha in (0.2,0.5,0.75,0.9,1.0):
    b=4/(4+2)*alpha
    for n in range(1,28):
        v=second(distribution(n,alpha))
        v_next=second(distribution(n+1,alpha))
        assert v_next + 1e-10 >= (1+2*b/(2+n))*v+1
        checks+=1

# Exact covariance relation after Poissonization; more reinforcement -> less covariance.
rate=6.0
for t in (0.1,0.5,1.0,2.0,3.0):
    L=rate*t
    vals=[]
    for alpha in (0,.4,.8,1.0):
        pmf=exp(-L)
        ev=0.0
        for n in range(120):
            ev+=pmf*second(distribution(n,alpha))
            pmf*=L/(n+1)
        cov=(L-ev)/4
        corr=(L-ev)/(L+ev)
        vals.append(cov)
        assert abs(corr)<=1+1e-12
        checks+=1
    assert abs(vals[0])<1e-9
    assert all(vals[i] > vals[i+1] for i in range(3))
    checks+=4

print(f"PASS: {checks} exact and floating finite-state checks")
print("Exact n=6 second moments for alpha=0,1,2:", [str(second(exact_distribution(6,a))) for a in (0,1,2)])
print("At t=2, leaf=1, center=4, covariance for alpha=0,.4,.8,1:", [round((12-sum(exp(-12)*12**n/factorial(n)*second(distribution(n,a)) for n in range(75)))/4,7) for a in (0,.4,.8,1.)])
