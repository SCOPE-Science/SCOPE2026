#!/usr/bin/env python3
"""Exhaustive exact-arithmetic verification of the finite transfer identities and samples.

The proof for all ladder lengths uses polynomial annihilators of a completely
specified 256-state integer transfer operator, not extrapolation from samples.
"""
from collections import defaultdict

SYMS = [tuple((j >> k) & 1 for k in range(4)) for j in range(16)]
def majority(a, b, c):
    return int(a+b+c>=2)

def allowed_middle(a,b,c):
    la,lb,lc=SYMS[a],SYMS[b],SYMS[c]
    return (lb[2]==majority(la[0],lb[1],lc[0])
        and lb[3]==majority(la[1],lb[0],lc[1])
        and lb[0]==majority(la[2],lb[3],lc[2])
        and lb[1]==majority(la[3],lb[2],lc[3]))

def allowed_start(a,b):
    x,y=SYMS[a],SYMS[b]
    return (x[2]==majority(x[0],x[1],y[0])
        and x[3]==majority(x[1],x[0],y[1])
        and x[0]==majority(x[2],x[3],y[2])
        and x[1]==majority(x[3],x[2],y[3]))

def allowed_end(a,b):
    x,y=SYMS[a],SYMS[b]
    return (y[2]==majority(x[0],y[0],y[1])
        and y[3]==majority(x[1],y[1],y[0])
        and y[0]==majority(x[2],y[2],y[3])
        and y[1]==majority(x[3],y[3],y[2]))

S = [int(allowed_start(a,b)) for a in range(16) for b in range(16)]
E = [int(allowed_end(a,b)) for a in range(16) for b in range(16)]
EDGES = [(16*a+b,16*b+c) for a in range(16) for b in range(16) for c in range(16)
    if allowed_middle(a,b,c)]
FIXED = {i for i,s in enumerate(SYMS) if s[0:2] == s[2:4]}
SF = [int(allowed_start(a,b) and a in FIXED and b in FIXED)
     for a in range(16) for b in range(16)]
EF = [int(allowed_end(a,b) and a in FIXED and b in FIXED)
     for a in range(16) for b in range(16)]
EDGES_F = [(i,j) for i,j in EDGES if i//16 in FIXED and i%16 in FIXED and j%16 in FIXED]

def apply(vec, edges):
    out=[0]*256
    for i,j in edges:out[i]+=vec[j]
    return out

def vectors(e,edges,k):
    vals=[e]
    for _ in range(k):vals.append(apply(vals[-1],edges))
    return vals

def residual(arr,coeff):
    return [sum(coeff[j]*arr[j][i] for j in range(len(coeff))) for i in range(256)]

p=[-1,3,-1,1,-3,1] # (z^2-3z+1)(z^3-1)
q=[1,0,-2,1]       # (z-1)(z^2-z-1)
v=vectors(E,EDGES,6)
w=vectors(EF,EDGES_F,4)
assert len(EDGES)==400
assert sum(S)==36 and sum(E)==36
assert len(FIXED)==4
assert residual(v,p)==[0]*256
assert residual(w,q)==[0]*256

def dot(a,b):return sum(x*y for x,y in zip(a,b))
fixed2=[dot(S,v[i]) for i in range(5)]
fixed1=[dot(SF,w[i]) for i in range(3)]
assert fixed2==[8,22,48,124,326]
assert fixed1==[6,8,12]

def fibonacci(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def lucas(n):
    a,b=2,1
    for _ in range(n):a,b=b,a+b
    return a

def formula(n):
    f1=2*(fibonacci(n+1)+1)
    f2=lucas(2*n)+1+3*int(n%3==0)
    return f1,f2,(f2-f1)//2

def update(bits,n):
    new=0
    for j in range(n):
        for row in range(2):
            i=2*j+row
            selfval=(bits>>i)&1
            rung=(bits>>(i^1))&1
            if j==0:
                ngh=[selfval,rung,(bits>>(i+2))&1]
            elif j==n-1:
                ngh=[selfval,rung,(bits>>(i-2))&1]
            else:
                ngh=[rung,(bits>>(i-2))&1,(bits>>(i+2))&1]
            new|=(int(sum(ngh)>=2)<<i)
    return new

sample_total=0
for n in range(2,9):
    N=1<<(2*n)
    count1=count2=0
    for x in range(N):
        y=update(x,n)
        count1+=(x==y)
        count2+=(update(y,n)==x)
    a,b,c=formula(n)
    assert count1==a and count2==b and c==(b-a)//2,(n,count1,count2,a,b)
    sample_total+=N
    print(f'n={n} fixed={a} periodic={b} primitive_two_orbits={c} tested={N}')
print('transfer_edge_count=',len(EDGES),'boundary_pairs=',sum(S))
print('annihilator_residual_entries_all_zero=',len(residual(v,p))+len(residual(w,q)))
print('brute_force_configurations=',sample_total)
print('LADDER_MAJORITY_PERIODIC_CENSUS_OK')
