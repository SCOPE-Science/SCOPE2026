#!/usr/bin/env python3
"""Exact check of the finite-state first-delay fixation identities.
Requires Python 3 standard library only. It does not replace the general proof.
"""
from fractions import Fraction as Q

class P:
    def __init__(self, terms=None):
        if isinstance(terms, P): terms=terms.t
        if isinstance(terms, int): terms={(0,0):terms}
        self.t={k:v for k,v in (terms or {}).items() if v}
    @staticmethod
    def make(a): return a if isinstance(a,P) else P(a)
    def __add__(self,b):
        b=P.make(b); z=dict(self.t)
        for k,v in b.t.items():z[k]=z.get(k,0)+v
        return P(z)
    __radd__=__add__
    def __neg__(self):return P({k:-v for k,v in self.t.items()})
    def __sub__(self,b):return self+-P.make(b)
    def __rsub__(self,b):return P.make(b)-self
    def __mul__(self,b):
        b=P.make(b); z={}
        for (i,j),a in self.t.items():
            for (k,l),c in b.t.items():z[(i+k,j+l)]=z.get((i+k,j+l),0)+a*c
        return P(z)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        z=P(1)
        for _ in range(n):z=z*self
        return z
    def __eq__(self,b):return self.t==P.make(b).t
    def __repr__(self):return repr(self.t)

X=P({(1,0):1});Y=P({(0,1):1});Z=P(0)
D=(X*Y+X+1)*(2*X*Y+3*X+2*Y+2)
A=X**2*(Y+2)*(2*Y+1)
B=X*(X+1)*(Y+2)*(2*Y+1)
C=X*(2*Y+1)*(X*Y+X+Y)
E=2*X**2*Y**2+5*X**2*Y+X**2+2*X*Y**2+6*X*Y+2*Y
assert (X+1)*A==X*B
assert (2*X+1)*B==C+X*E+X*D
assert (Y+2)*C==A+Y*B
assert (Y+1)*E==C+Y*D
assert A*(X*Y+Y+1)-X*Y*D==-X*(X-Y)*(X*Y-2*Y-2)
assert D.t and all(v>=0 for v in D.t.values())
print('Five global bivariate polynomial identities: PASS')

# Verify the strength-dependent witness at a=2,b=10,c=3,d=1.
W=X
assert (1+9*W)*(1+2*W)-(1+5*W)*(1+W)==W*(5+13*W)
assert ((1+9*W)*(1+5*W)-2*(1+5*W)*(1+W)
        -2*(1+W)*(1+2*W))==31*W**2-4*W-3
print('Two global selection-strength polynomial identities: PASS')

def independent_absorption(r1,r2):
    """Construct the entire transient Markov matrix afresh, then solve Gaussian equations."""
    states=((1,1),(1,2),(2,1),(2,2))
    mat=[[Q(int(i==j)) for j in range(4)] for i in range(4)]
    rhs=[Q(0) for _ in range(4)]
    for k,(history,current) in enumerate(states):
        rate=(r1,r2)[history-1]
        up=Q(current)*rate/(current*rate+3-current)*Q(3-current,2)
        down=Q(3-current)/(current*rate+3-current)*Q(current,2)
        transitions=((current+1,up),(current-1,down),
                     (current,Q(1)-up-down))
        assert sum((prob for _,prob in transitions),Q(0))==1
        assert all(prob>=0 for _,prob in transitions)
        for future,prob in transitions:
            if future==3: rhs[k]+=prob
            elif future!=0:mat[k][states.index((current,future))]-=prob
    for i in range(4):
        pivot=next(j for j in range(i,4) if mat[j][i])
        mat[i],mat[pivot]=mat[pivot],mat[i];rhs[i],rhs[pivot]=rhs[pivot],rhs[i]
        z=mat[i][i]
        for j in range(i,4):mat[i][j]/=z
        rhs[i]/=z
        for k in range(4):
            if k==i:continue
            z=mat[k][i]
            for j in range(i,4):mat[k][j]-=z*mat[i][j]
            rhs[k]-=z*rhs[i]
    return rhs[0]

def f0(x,y):return x*y/(x*y+y+1)
def f1(x,y):return x*x*(y+2)*(2*y+1)/((x*y+x+1)*(2*x*y+3*x+2*y+2))
def delta(x,y):return -x*(x-y)*(x*y-2*y-2)/((x*y+x+1)*(x*y+y+1)*(2*x*y+3*x+2*y+2))
choices=[Q(a,b) for a,b in [(1,9),(1,4),(1,2),(2,3),(1,1),(3,2),(2,1),(3,1),(4,1),(5,1),(7,1),(10,1)]]
n=0
for x in choices:
    for y in choices:
        assert f1(x,y)==independent_absorption(x,y)
        assert f1(x,y)-f0(x,y)==delta(x,y)
        assert 0<f0(x,y)<1 and 0<f1(x,y)<1
        n+=1
print(f'Exact-rational independent absorbing-chain checks: {n} ratio pairs PASS')

for w,expected in [(Q(1,10),Q(5871,917620)),
                   (Q(1,2),-Q(23,10640)),
                   (Q(1),-Q(15,2132))]:
    x=(1+9*w)/(1+w); y=(1+5*w)/(1+2*w)
    assert delta(x,y)==expected
print('Exact positive/negative example comparisons: PASS')
print('ALL TESTS PASSED')
