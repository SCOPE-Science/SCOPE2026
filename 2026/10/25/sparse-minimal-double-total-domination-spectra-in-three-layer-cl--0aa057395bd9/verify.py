#!/usr/bin/env python3
"""Standalone direct verifier for double total domination of clique-path graphs.
No external dependencies. Adjacent-neighbor counts use the graph definition directly.
"""
import math, collections

def direct(a,b,c,n):
    chosen=(a,b,c)
    for layer in range(3):
        for i in range(n):
            neighbor_count=(chosen[layer].bit_count()-((chosen[layer]>>i)&1))
            if layer>0: neighbor_count+=((chosen[layer-1]>>i)&1)
            if layer<2: neighbor_count+=((chosen[layer+1]>>i)&1)
            if neighbor_count<2:return False
    return True

def predicted_min(a,b,c,n):
    na,nb,nc=map(int.bit_count,(a,b,c)); u=(1<<n)-1
    if nb==0:return a==c==u
    if nb==1:
        return na>=3 and nc>=3 and (a&c)==b and (a|c)==u
    if nb==2:
        cond=lambda x: (x==b) or (x.bit_count()==3 and (x&~b).bit_count()>=2)
        return cond(a) and cond(c) and (b&~(a|c))==0
    if nb==3:
        if na==nc==2:return (a|c)==b and (a&c).bit_count()==1
        if na==nc==3:return ((a&~b).bit_count()>=2 and (c&~b).bit_count()>=2 and ((a|c)&b).bit_count()<=1)
        return False
    if nb==4:
        return na==nc==2 and (a&c)==0 and (a|c)==b
    return False

def predicted_counter(n):
    a=math.comb(n-2,2)
    g=2*a+math.comb(n-2,3)
    h=math.comb(n-3,3);j=math.comb(n-3,2)
    c=collections.Counter()
    c[6]+=math.comb(n,2)
    c[7]+=2*math.comb(n,2)*g+n*(n-1)*(n-2)
    c[8]+=2*math.comb(n,2)*a*a+math.comb(n,2)*math.comb(n-2,2)
    c[9]+=math.comb(n,3)*(h*h+6*h*j+3*j*j)
    c[n+2]+=n*(2**(n-1)-2*n)
    c[2*n]+=1
    return c

def test(n):
    finite=1<<n
    all_by_size=collections.Counter()
    mini=collections.Counter()
    total=0
    for b in range(finite):
        for a in range(finite):
            for c in range(finite):
                valid=direct(a,b,c,n)
                if valid:
                    total+=1
                    all_by_size[a.bit_count()+b.bit_count()+c.bit_count()]+=1
                    minimal=all(not direct(a^(1<<i),b,c,n) for i in range(n) if a&(1<<i)) and all(not direct(a,b^(1<<i),c,n) for i in range(n) if b&(1<<i)) and all(not direct(a,b,c^(1<<i),n) for i in range(n) if c&(1<<i))
                    if minimal:mini[a.bit_count()+b.bit_count()+c.bit_count()]+=1
                else:minimal=False
                if n>=6 and minimal!=predicted_min(a,b,c,n):raise AssertionError(('classification',n,a,b,c,valid,minimal,predicted_min(a,b,c,n)))
    if n>=6 and mini!=predicted_counter(n):raise AssertionError((n,mini,predicted_counter(n)))
    print('n',n,'tested',finite**3,'valid',total,'inclusion_minimal',dict(sorted(mini.items())), 'PASS',flush=True)

if __name__=='__main__':
    for k in [3,4,5,6,7]:test(k)
