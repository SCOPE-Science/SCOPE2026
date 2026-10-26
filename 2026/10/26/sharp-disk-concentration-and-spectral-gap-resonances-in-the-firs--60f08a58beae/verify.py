"""Exact, dependency-free finite algebra checks for the disk-concentration theorem.
The infinite-dimensional maximum and the Gamma median comparison are proved
analytically in RESULT.md, not inferred from these finite checks.
"""
from fractions import Fraction as Q
from math import factorial

checks=0

def check(ok,msg):
    global checks
    checks+=1
    if not ok: raise AssertionError(msg)

def mul(a,b):
    o=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): o[i+j]+=x*y
    return o

def sub(a,b):
    return [(a[i] if i<len(a) else Q(0))-(b[i] if i<len(b) else Q(0)) for i in range(max(len(a),len(b)))]

def scale(a,s):return [s*v for v in a]

def eq(a,b):
    n=max(len(a),len(b));return all((a[i] if i<len(a) else 0)==(b[i] if i<len(b) else 0) for i in range(n))

def q(n):
    p=[Q(1,factorial(j)) for j in range(n)]
    p+=[Q(1-n,factorial(n)),Q(1,factorial(n))]
    return p

for n in range(0,501):
    # e^x(λ_{n+1}-λ_n) = q_n-q_{n+1}
    target=scale(mul([Q(-n),Q(1)],[Q(-n-1),Q(1)]),Q(-1,factorial(n+1)))
    target=[Q(0)]*n+target
    check(eq(sub(q(n),q(n+1)),target),f'adjacent identity n={n}')

# Polynomial q0-q2=x^2(1-x)/2; q1-q3=-x(x-2)(x^2-3)/6.
check(eq(sub(q(0),q(2)),[Q(0),Q(0),Q(1,2),Q(-1,2)]),'0/2 comparison')
check(eq(sub(q(1),q(3)),[Q(0),Q(-1),Q(1,2),Q(1,3),Q(-1,6)]),'1/3 comparison')
# correct explicit expansion of -x(x-2)(x^2-3)/6 is used below with symbolic multiplication
check(eq(sub(q(1),q(3)),scale(mul([Q(0),Q(1)],mul([Q(-2),Q(1)],[Q(-3),Q(0),Q(1)])),Q(-1,6))),'factored 1/3 comparison')
# At x=1, q0=q1=q2, and q3-q0=1/3, yielding e^-1/3 sharp gap.
def ev(p,x):return sum(v*x**i for i,v in enumerate(p))
check(ev(q(0),Q(1))==ev(q(1),Q(1))==ev(q(2),Q(1)),'triple resonance')
check(ev(sub(q(3),q(0)),Q(1))==Q(1,3),'triple rank gap')
# At x=2, q1=q2=q3 and q1-q0=2, yielding 2e^-2 gap.
check(ev(q(1),Q(2))==ev(q(2),Q(2))==ev(q(3),Q(2)),'runner-up triple resonance')
check(ev(sub(q(1),q(0)),Q(2))==Q(2),'second gap at x=2')
# Verify ordered candidate indices at rational abscissae by exact comparisons
for x in [Q(1,100),Q(1,10),Q(1,2),Q(9,10),Q(1),Q(11,10),Q(3,2),Q(19,10),Q(2),Q(21,10),Q(5,2),Q(29,10),Q(3),Q(4),Q(7),Q(10),Q(16)]:
    arr=[ev(q(n),x) for n in range(81)]
    # since λn=1-e^-x qn, smaller q means larger eigenvalue
    least=min(arr)
    top=[i for i,v in enumerate(arr) if v==least]
    expected=([1] if x<1 else ([0,1,2] if x==1 else [0]))
    check(top==expected,f'top indices x={x}: {top}')
    second=min(v for v in arr if v>least)
    second_ids=[i for i,v in enumerate(arr) if v==second]
    runner=[2] if x<1 or Q(1)<x<Q(2) else ([3] if x==1 else ([1,2,3] if x==2 else [1]))
    check(second_ids==runner,f'runner-up indices x={x}: {second_ids}')
print(f'PASS: {checks} exact rational assertions, all successful.')
