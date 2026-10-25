"""Exact independent checks for the wheel two-leader coherence theorem."""
import sympy as s
from math import isclose
q=(3-s.sqrt(5))/2
rt=s.sqrt(5)
def phi(t): return t*q**t/(1-q**t)
def rim_formula(n,d):
    g0=(1+q**n)/(rt*(1-q**n))
    total=(2*n+1)*g0-2
    S=(1-q**d)*(1-q**(n-d))/(rt*(1-q**n))
    return s.simplify(s.radsimp(total-s.Rational(n+1,2)*S-s.Rational(3,5)+(phi(d)+phi(n-d)-phi(n))/rt))
def hub_formula(n):
    return s.simplify(s.radsimp(n*(1+q**(2*n))/(rt*(1-q**(2*n)))-s.Rational(3,5)))
def wheel_laplacian(n):
    M=s.zeros(n+1)
    for i in range(n):
        for u,v in [(0,i+1),(i+1,(i+1)%n+1)]:
            M[u,u]+=1;M[v,v]+=1;M[u,v]-=1;M[v,u]-=1
    return M
def cost(M,leaders):
    ff=[i for i in range(M.rows) if i not in leaders]
    return s.trace(M.extract(ff,ff).inv())
cnt=0
for n in range(3,12):
    M=wheel_laplacian(n)
    hub=hub_formula(n)
    assert cost(M,{0,1})==hub,(n,'hub')
    cnt+=1
    values=[]
    for d in range(1,n//2+1):
        observed=cost(M,{1,1+d})
        expected=rim_formula(n,d)
        assert observed==expected,(n,d,observed,expected)
        values.append(observed);cnt+=1
    assert all(values[i]>values[i+1] for i in range(len(values)-1)),(n,'monotonic')
    diff=values[-1]-hub
    if n==3: assert diff==0
    elif n<=6: assert diff<0
    else:assert diff>0
small={3:(s.Rational(3,4),s.Rational(3,4)),4:(s.Rational(31,30),s.Rational(25,21)),5:(s.Rational(67,44),s.Rational(18,11)),6:(s.Integer(2),s.Rational(25,12)),7:(s.Rational(31,12),s.Rational(954,377)),8:(s.Rational(221,70),s.Rational(2939,987))}
for n,(v,h) in small.items():
    assert rim_formula(n,n//2)==v
    assert hub_formula(n)==h
lower=s.simplify(s.radsimp(s.Rational(9,2)/rt-2-phi(8)/rt-16*q**16/(rt*(1-q**16))))
assert lower==-s.Rational(36362,4935)+s.Rational(33,10)*rt and lower>0
print(f'VERIFY_OK {cnt} exact independent grounded-Laplacian trace comparisons; small-n values and positive n=8 uniform bound')
