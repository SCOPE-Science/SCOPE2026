"""Independent finite-state and asymptotic diagnostics for directed tree parking.
Run: python _research32_checker.py
"""
import itertools, math, random
from collections import Counter

def root_flux_recursion(b, arrivals):
    # vertex 0: root; vertices 1..b: internal parents;
    # parent i has leaves b+1+(i-1)*b,...,b+i*b.
    root_input=arrivals[0]
    for i in range(1,b+1):
        x=arrivals[i]
        for j in range(b+1+(i-1)*b,b+1+i*b):
            x+=max(0,arrivals[j]-1)
        root_input+=max(0,x-1)
    return max(0,root_input-1)

def direct_flux(b, arrivals):
    occupied=set()
    escaped=0
    N=b*b+b+1
    for v in range(N):
        for _ in range(arrivals[v]):
            u=v
            while u is not None and u in occupied:
                if u==0: u=None
                elif u<=b: u=0
                else: u=1+(u-(b+1))//b
            if u is None:escaped+=1
            else:occupied.add(u)
    return escaped

def sequential_flux(b, sequence):
    occupied=set(); escaped=0
    for v in sequence:
        u=v
        while u is not None and u in occupied:
            if u==0:u=None
            elif u<=b:u=0
            else:u=1+(u-(b+1))//b
        if u is None:escaped+=1
        else:occupied.add(u)
    return escaped

def exhaustive():
    checks=0
    for b,mmax in [(2,5),(3,4)]:
        N=b*b+b+1
        for m in range(mmax+1):
            for seq in itertools.product(range(N), repeat=m):
                arrivals=[0]*N
                for x in seq:arrivals[x]+=1
                a=root_flux_recursion(b,arrivals)
                z=sequential_flux(b,seq)
                if a!=z:
                    raise AssertionError((b,m,seq,a,z))
                checks+=1
    return checks

def asymptotic():
    rng=random.Random(13067)
    comparisons=[]
    for b in (24,64,160,320):
        N=b*b+b+1
        t=1.5
        m=round(t*b**1.25)
        samples=5000 if b<=160 else 3000
        count=Counter()
        for _ in range(samples):
            draws=Counter(rng.randrange(N) for _ in range(m))
            parent_inputs=Counter()
            for v,a in draws.items():
                if 1 <= v <= b:
                    parent_inputs[v] += a
                elif v > b and a >= 2:
                    parent_inputs[1+(v-b-1)//b] += a-1
            x=draws.get(0,0)+sum(max(0,a-1) for a in parent_inputs.values())
            count[max(0,x-1)]+=1
        lam=t**4/8
        limit0=math.exp(-lam)*(1+lam)
        observed=count[0]/samples
        comparisons.append((b,m,samples,observed,limit0))
    return comparisons

if __name__=='__main__':
    n=exhaustive(); print('Exact complete small-tree sequence checks:',n)
    for x in asymptotic():print('b m samples P(no escapes) limit:',x)
