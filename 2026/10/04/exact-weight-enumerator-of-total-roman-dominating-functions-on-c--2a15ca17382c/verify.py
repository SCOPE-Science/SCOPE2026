#!/usr/bin/env python3
from itertools import product
from collections import Counter
from math import comb

MAX_N = 9

def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest

def build_parts(profile):
    parts=[]
    for i,n in enumerate(profile):
        parts += [i]*n
    return parts

def literal_trdf(labels, parts):
    N=len(labels)
    for v in range(N):
        if labels[v] == 0:
            if not any(parts[u] != parts[v] and labels[u] == 2 for u in range(N)):
                return False
    pos=[v for v in range(N) if labels[v] > 0]
    for v in pos:
        if not any(u != v and labels[u] > 0 and parts[u] != parts[v] for u in pos):
            return False
    return True

def criterion(labels, parts, r):
    z=[0]*r; p=[0]*r; t=[0]*r
    for a,i in zip(labels,parts):
        if a==0: z[i]+=1
        else: p[i]+=1
        if a==2: t[i]+=1
    if sum(x>0 for x in p) < 2:
        return False
    T=sum(t)
    return all(z[i]==0 or T-t[i]>0 for i in range(r))

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def add(a,b,scale=1):
    n=max(len(a),len(b)); c=[0]*n
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)+scale*(b[i] if i<len(b) else 0)
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def power(base,n):
    out=[1]
    for _ in range(n): out=conv(out,base)
    return out

def closed_coeffs(profile):
    N=sum(profile)
    out=add(power([1,1,1],N), power([1,1],N), -1)
    for ni in profile:
        Bi=add(power([1,1,1],ni), power([1,1],ni), -1)
        out=add(out, conv(Bi,power([1,1],N-ni)), -1)
    for ni in profile:
        Ci=add(power([0,1,1],ni), [0]*ni+[1], -1)
        outside=add(power([1,1],N-ni), [1], -1)
        out=add(out, conv(Ci,outside), 1)
    xn=[0]*N+[1]
    out=add(out,xn,1)
    return out + [0]*(2*N+1-len(out))

def main():
    profiles=labelings=coefficient_checks=minimum_checks=0
    for N in range(2,MAX_N+1):
        for profile in partitions(N):
            if len(profile)<2: continue
            profiles+=1
            parts=build_parts(profile); r=len(profile)
            counts=Counter(); best=None
            for labels in product(range(3), repeat=N):
                labelings+=1
                a=literal_trdf(labels,parts)
                b=criterion(labels,parts,r)
                if a != b:
                    raise AssertionError(('criterion',profile,labels,a,b))
                if a:
                    w=sum(labels); counts[w]+=1
                    best=w if best is None else min(best,w)
            coeff=closed_coeffs(profile)
            for w in range(2*N+1):
                coefficient_checks+=1
                if counts[w] != coeff[w]:
                    raise AssertionError(('coefficient',profile,w,counts[w],coeff[w]))
            expected=min(N,4,min(profile)+2)
            minimum_checks+=1
            if best != expected:
                raise AssertionError(('minimum',profile,best,expected))
    print(f'VERIFY_OK profiles={profiles} labelings={labelings} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order={MAX_N}')

if __name__=='__main__': main()
