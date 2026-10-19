from itertools import combinations
from collections import Counter
import math

N=4
edges=[(i, tuple(j for j in pair)) for i in range(N) for pair in combinations([j for j in range(N) if j!=i],2)]
assert len(edges)==12


def activate(mask, chosen):
    result=0
    for i,parents in chosen:
        if all((mask>>j)&1 for j in parents):
            result |= 1<<i
    return result


def core(chosen):
    s=(1<<N)-1
    for k in range(N+1):
        t=activate(s,chosen)
        assert (t|s)==s, (s,t)
        if t==s:
            return s,k
        s=t
    assert False

n_cases=n_fixed=n_empty=n_nonempty=0
examples=Counter()
for mask in range(1<<len(edges)):
    chosen=[edges[k] for k in range(len(edges)) if mask>>k&1]
    K,layer=core(chosen)
    fixed=[]
    for S in range(1<<N):
        if activate(S,chosen)==S:
            fixed.append(S)
            # at tau=4, delta=b=1, every supported index has input>=1/4,
            # response >=1/2. Outside have exactly zero input.
            for i in range(N):
                pin=sum(.25 for v,heads in chosen if v==i and all((S>>j)&1 for j in heads))
                response=4*pin/(1+4*pin)
                assert response >= ((S>>i)&1)/2-1e-10
                if not ((S>>i)&1): assert response==0
    U=0
    for S in fixed: U|=S
    assert U==K, (mask,K,U)
    assert 0 in fixed
    n_cases+=1
    n_fixed+=len(fixed)
    n_empty+= (K==0)
    n_nonempty+=(K>0)
    examples[len(fixed)]+=1

# Probe global-extinction induction with exact preconditions in a nontrivial graph
# n=5, triangular core absent: dependencies form a forward AND chain.
N2=5
E={0:[(1,2)],1:[(2,3)],2:[],3:[(4,0)],4:[(0,1)]}
# all nodes except 2 peel eventually (check)
s=(1<<N2)-1
peel=[]
while True:
 t=0
 for i, js in E.items():
  if any(all((s>>j)&1 for j in pair) for pair in js): t|=1<<i
 peel.append(t)
 if t==s:break
 s=t
 assert len(peel)<=N2
assert s==0,peel

delta=1.0;tau=5.0;h=0.04
rho=1-h*delta
x=[.9,.4,.7,.8,.1]
C=[1.0]
L=max(map(len,E.values()))
for k in range(1,len(peel)):
 C.append(1+(h*tau*L/rho)*C[-1])
for t in range(100):
 if t in [0,1,5,25,50,99]:
  assert max(x) <= C[-1]*(1+t)**(len(peel)-1)*rho**t+1e-9, (t,x)
 xnew=[]
 for i in range(N2):
  p=sum(math.prod(x[j] for j in pair) for pair in E[i])
  xnew.append(x[i]+h*(-delta*x[i]+tau*(1-x[i])*p))
 x=xnew
 assert all(0<=v<=1 for v in x)

print(f'PASS: {n_cases} directed four-node triadic hypergraphs, {n_fixed} fixed support tests')
print(f'PASS: maximal Boolean core equals union of all equilibrium supports in all cases; core-empty={n_empty}, core-nonempty={n_nonempty}')
print(f'PASS: exact q=1/2 subsolution under uniform tau=4; support-count distribution={dict(examples)}')
print(f'PASS: example layers={peel}, C_m={C[-1]:.8g}, nsteps=100 with explicit peeling decay envelope')
