#!/usr/bin/env python3
"""Reproducible direct labelled-state and count-representative checks."""
from math import comb

def step_direct(a,b,x):
    n=a+b; full=(1<<n)-1; cmask=(1<<a)-1
    y=0
    for i in range(n):
        neigh = (full ^ (1<<i)) if i<a else cmask
        ones=(x&neigh).bit_count(); deg=neigh.bit_count()
        if 2*ones>deg or (2*ones==deg and (x>>i)&1):
            y |= (1<<i)
    return y

def step_formula(a,b,x):
    cmask=(1<<a)-1; imask=((1<<b)-1)<<a
    c=(x&cmask).bit_count(); l=(x&imask).bit_count(); t=c+l
    if 2*t<a+b: newc=0
    elif 2*t>a+b: newc=cmask
    else: newc=(~x)&cmask
    if 2*c<a: newi=0
    elif 2*c>a: newi=imask
    else: newi=x&imask
    return newc|newi

def predicted(a,b):
    p=2+2*int(b>=a)
    if a%2==0 and b%2==0: p+=comb(a,a//2)*comb(b,b//2)
    if a>b and (a-b)%2==0: p+=2*comb(a,(a-b)//2)
    return p,(a>b and (a-b)%2==0 and b>=3)

def exhaustive(a,b):
    period=fixed=depth_max=0
    for x in range(1<<(a+b)):
        path=[x]
        for t in range(5): path.append(step_direct(a,b,path[-1]))
        assert path[3]==path[5],(a,b,x)
        if path[2]==x:
            period+=1
            fixed+=(path[1]==x)
        depth=next(t for t in range(4) if path[t]==path[t+2])
        depth_max=max(depth_max,depth)
    return period,fixed,depth_max

if __name__=='__main__':
    cases=states=0
    for a in range(1,11):
        for b in range(1,11):
            if a+b>14: continue
            p,q,depth=exhaustive(a,b)
            pe,sharp=predicted(a,b)
            assert (p,q,depth==3)==(pe,2,sharp),(a,b,p,q,depth,pe,sharp)
            cases+=1; states+=2**(a+b)
    representative_cases=0
    for a in range(1,31):
        for b in range(1,31):
            depth_max=0
            for c in range(a+1):
                for d in range(b+1):
                    x=((1<<c)-1)|(((1<<d)-1)<<a)
                    path=[x]
                    for _ in range(5): path.append(step_formula(a,b,path[-1]))
                    assert path[3]==path[5]
                    depth=next(t for t in range(4) if path[t]==path[t+2])
                    depth_max=max(depth,depth_max)
            assert (depth_max==3)==predicted(a,b)[1]
            representative_cases+=1
    print(f'VERIFY_OK exhaustive_parameter_pairs={cases} exhaustive_labelled_states={states} representative_parameter_pairs={representative_cases}')
