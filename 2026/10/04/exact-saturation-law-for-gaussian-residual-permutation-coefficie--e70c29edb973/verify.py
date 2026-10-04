#!/usr/bin/env python3
import itertools, math
from collections import Counter
from fractions import Fraction
def h(n): return Fraction(n,4*(n-1))
def counts(n):
    signs=[1]*(n//2)+[-1]*(n//2); c=Counter()
    for p in itertools.permutations(range(n)): c[signs[p[0]]-signs[p[1]]]+=1
    return c
def tail(m,p,k):
    if k>m: return 0.0
    return sum(math.comb(m,j)*(p**j)*((1-p)**(m-j)) for j in range(k,m+1))
def size(n,m,a):
    aa=math.sqrt(2/n); hh=n/(4*(n-1)); th=math.atan(aa)/math.pi
    k=math.ceil((1-a)*(m+1))
    if k>m: return 0.0
    return .5-th+th*(tail(m,1-hh,k)+tail(m,hh,k))
n=6; c=counts(n); tot=math.factorial(n)
assert c[2]==tot*h(n) and c[-2]==tot*h(n) and c[0]==tot*(1-2*h(n))
n=6; m=4; alpha=.30; hh=h(n); probs={-1:hh,0:1-2*hh,1:hh}; k=math.ceil((1-alpha)*(m+1))
def brute(mode):
    s=Fraction()
    for seq in itertools.product((-1,0,1), repeat=m):
        pr=Fraction(1); below=0
        for x in seq:
            pr*=probs[x]
            below += (x==-1) if mode=="neg" else (x in (-1,0))
        if below>=k: s+=pr
    return s
assert abs(float(brute("neg"))-tail(m,float(hh),k))<1e-15
assert abs(float(brute("pos"))-tail(m,float(1-hh),k))<1e-15
val=size(20,1000,.05)
assert abs(val-0.40250888547893166)<5e-16
lims=[.5-math.atan(math.sqrt(2/n))/math.pi for n in (20,100,500,2000)]
assert all(lims[i]<lims[i+1] for i in range(len(lims)-1)) and lims[-1]>.489
print("VERIFY_OK")
print("n20_m1000_alpha005",format(val,".17g"))
print("limit_n20",format(lims[0],".17g"))
print("limit_n2000",format(lims[-1],".17g"))
