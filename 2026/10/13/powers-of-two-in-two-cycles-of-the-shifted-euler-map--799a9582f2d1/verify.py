#!/usr/bin/env python3
def totients(n):
    phi=list(range(n+1))
    for p in range(2,n+1):
        if phi[p]==p:
            for j in range(p,n+1,p):
                phi[j]-=phi[j]//p
    if n>=1:
        phi[1]=1
    return phi

A_MAX=18
limit=3*(1<<(A_MAX-1))
phi=totients(limit)
equation_values=0
cycle_cases=0
for a in range(1,A_MAX+1):
    rhs=3*(1<<(a-1))
    got=[]
    for y in range(1,rhs+1):
        equation_values+=1
        if y+phi[y]==rhs:
            got.append(y)
    expected=[1<<a]
    if a>=4:
        expected.append(9*(1<<(a-3)))
    expected=sorted(expected)
    assert got==expected, (a,got,expected)
    if a>=4:
        k=5*(1<<(a-3))
        x=1<<a
        y=9*(1<<(a-3))
        assert phi[x]+k==y
        assert phi[y]+k==x
        assert x!=y
        cycle_cases+=1

print(f"VERIFY_OK a_cases={A_MAX} equation_values={equation_values} cycle_cases={cycle_cases}")
