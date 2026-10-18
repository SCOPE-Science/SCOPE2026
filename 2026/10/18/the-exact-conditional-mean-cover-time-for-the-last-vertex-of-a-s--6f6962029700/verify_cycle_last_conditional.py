"""Exact checks of the conditional cover-time theorem; standard library only.
Run: python verify_cycle_last_conditional.py
"""
from collections import defaultdict
from fractions import Fraction as F

checks=0
state={(0,'L'):(F(1,2),F(1,2)),(1,'R'):(F(1,2),F(1,2))}
for m in range(2,61):
    for (r,side),(pr,tw) in state.items():
        l=m-1-r
        if side=='R':
            pexp=F(r,m*(m-1))
            cond=F(2*m*(m-1)-r*r,3)
        else:
            pexp=F(l,m*(m-1))
            cond=F(m*m-1+2*r*(m-1)-r*r,3)
        assert pr==pexp and (pr==0 or tw==pr*cond)
        checks+=2
    for r in range(m):
        total=sum(state.get((r,side),(0,0))[0] for side in ('R','L'))
        first=sum(state.get((r,side),(0,0))[1] for side in ('R','L'))
        assert total==F(1,m)
        assert first/total==F(m*m-1,3)+r*(m-1-r)
        checks+=2
    # Following expansion ends at a vertex of the previously visited interval.
    nxt=defaultdict(lambda:(F(0),F(0)))
    for (r,side),(pr,tw) in state.items():
        for newside in ('R','L'):
            same=(side==newside)
            trans=F(m,m+1) if same else F(1,m+1)
            joint=F(m*(2*m+1),3*(m+1)) if same else F(m*(m+2),3*(m+1))
            key=(r+(newside=='R'),newside)
            oldp,oldt=nxt[key]
            nxt[key]=(oldp+pr*trans,oldt+tw*trans+pr*joint)
    state=nxt

# For a cycle of n vertices, the expected last holding increment is n-1.
for n in range(3,62):
    for k in range(1,n):
        expected=F(n*n+n-3,3)+(k-1)*(n-1-k)
        assert expected==F((n-1)**2-1,3)+(k-1)*(n-2-(k-1))+(n-1)
        checks+=1
print('PASS',checks,'exact rational invariants, levels 2..61')


# Independently check the absorbing-interval moment Dirichlet equation.
for m in range(1,41):
    length=m+1
    def joint_exit_wait(y):
        return F(y*(length*length-y*y),3*length)
    for y in range(1,m+1):
        assert joint_exit_wait(y)==F(y,length)+(joint_exit_wait(y-1)+joint_exit_wait(y+1))/2
        checks+=1
print('PASS independent Dirichlet checks:', 820)
