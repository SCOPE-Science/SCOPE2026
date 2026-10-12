#!/usr/bin/env python3
"""Independent finite checks of generator-homogeneous rainbow paths in cyclic graphs."""
from itertools import combinations

def lengths(k, ell):
    return tuple(range(1, k+1))+(ell,)

def cyclic_step(u,v,n):
    d=(v-u)%n
    return min(d,n-d)

def expected(k,ell,n):
    return ell<=2*k+1 or (ell<=3*k-1 and n<=2*(ell+k)-1)

def modular_test(k,ell,n):
    steps=lengths(k,ell)
    demands=[]
    for d in range(1,n//2+1):
        if d in steps: continue
        usable=[]
        for i,a in enumerate(steps):
            for j,b in enumerate(steps[:i]):
                sums=((a+b)%n,(a-b)%n,(b-a)%n,(-a-b)%n)
                if d in sums or n-d in sums:
                    usable.append((i,j))
        demands.append(tuple(usable))
    for mask in range(1 << (k+1)):
        if all(any(((mask>>i)^(mask>>j))&1 for i,j in opt) for opt in demands):
            return True
    return False

def explicit_color(k,ell):
    if ell<=2*k+1:
        return {x:(1 if x==ell else 0) for x in lengths(k,ell)}
    return {x:(1 if x==ell or x==k else 0) for x in lengths(k,ell)}

def graph_test(k,ell,n,col):
    step_set=set(lengths(k,ell))
    for u in range(n):
        for v in range(u+1,n):
            d=cyclic_step(u,v,n)
            if d in step_set:continue
            found=False
            for w in range(n):
                a,b=cyclic_step(u,w,n),cyclic_step(w,v,n)
                if a in step_set and b in step_set and col[a]!=col[b]:
                    found=True;break
            if not found: return False,(u,v)
    return True,None

def diameter_two(k,ell,n):
    step_set=set(lengths(k,ell))
    for d in range(1,n//2+1):
        if d in step_set:continue
        if not any(cyclic_step(0,w,n) in step_set and cyclic_step(w,d,n) in step_set for w in range(n)):
            return False,d
    return True,None

cases=0; positive=0; negative=0; witnessed=0
for k in range(3,9):
    for ell in range(k+2,3*k+2):
        for n in range(2*ell+1,2*(ell+k)+2):
            truth=expected(k,ell,n)
            found=modular_test(k,ell,n)
            assert truth==found,(k,ell,n,truth,found)
            two,d=diameter_two(k,ell,n)
            assert two,(k,ell,n,d)
            if truth:
                ok,bad=graph_test(k,ell,n,explicit_color(k,ell))
                assert ok,(k,ell,n,bad)
                positive+=1; witnessed+=1
            else:negative+=1
            cases+=1
print(f'VERIFY_OK; k=3..8; ell=k+2..3k+1; 2ell+1<=n<=2(ell+k)+1; cases={cases}; generator_yes={positive}; generator_no={negative}; explicit_graph_checks={witnessed}; diameter_two={cases}')
