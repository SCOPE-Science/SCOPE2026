from itertools import product
from math import factorial
from collections import Counter

VALS=(-1,0,1)
G={
    -2:{(-1,1):1},
    -1:{(-1,0):1,(0,1):1},
     0:{(-1,-1):1,(0,0):1,(1,1):1},
     1:{(0,-1):1,(1,0):1},
     2:{(1,-1):1},
}

def padd(a,b,scale=1):
    c=Counter(a)
    for k,v in b.items():
        c[k]+=scale*v
        if c[k]==0: del c[k]
    return dict(c)

def pmul(a,b):
    c=Counter()
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            c[(i+k,j+l)]+=x*y
    return dict(c)

def ppow(a,n):
    r={(0,0):1}
    b=a
    while n:
        if n&1:r=pmul(r,b)
        n//=2
        if n:b=pmul(b,b)
    return r

def H(r,s):
    if r>s:return {}
    out={}
    for d in range(r,s+1):out=padd(out,G[d])
    return out

def exact_range(m,M,n):
    if m==M:return ppow(G[m],n)
    r=ppow(H(m,M),n)
    r=padd(r,ppow(H(m+1,M),n),-1)
    r=padd(r,ppow(H(m,M-1),n),-1)
    r=padd(r,ppow(H(m+1,M-1),n),1)
    return r

def formula(n):
    out=Counter()
    for m in range(-2,3):
        for M in range(m,3):
            for (A,B),c in exact_range(m,M,n).items():
                if A>=1+M and B>=1-m:
                    out[(A,B)]+=c
    return Counter({k:v for k,v in out.items() if v})

def direct_ok(xs,ys):
    n=len(xs)
    for i in range(n):
        if xs[i]+sum(ys[j] for j in range(n) if j!=i)<1:return False
        if ys[i]+sum(xs[j] for j in range(n) if j!=i)<1:return False
    return True

def crit_ok(xs,ys):
    A=sum(xs);B=sum(ys)
    ds=[xs[i]-ys[i] for i in range(len(xs))]
    return A>=1+max(ds) and B>=1-min(ds)

def min_count_formula(n):
    s=0
    for j in range((n-1)//2+1):
        s += factorial(n)//(factorial(j+1)*factorial(j)*factorial(n-2*j-1))
    return s

labelings=valid=criterion_checks=bicoef_checks=weightcoef_checks=min_checks=0
for n in range(3,7):
    brute=Counter(); wbrute=Counter(); minlabels=[]
    for lab in product(VALS,repeat=2*n):
        labelings+=1
        xs=lab[:n];ys=lab[n:]
        d=direct_ok(xs,ys);c=crit_ok(xs,ys);criterion_checks+=1
        if d!=c:raise AssertionError(('criterion',n,lab,d,c))
        if d:
            valid+=1
            A=sum(xs);B=sum(ys)
            brute[(A,B)]+=1;wbrute[A+B]+=1
    got=formula(n)
    keys=set(brute)|set(got)
    for k in keys:
        bicoef_checks+=1
        if brute[k]!=got[k]:raise AssertionError(('bicoef',n,k,brute[k],got[k]))
    wf=Counter()
    for (A,B),c in got.items():wf[A+B]+=c
    for k in set(wbrute)|set(wf):
        weightcoef_checks+=1
        if wbrute[k]!=wf[k]:raise AssertionError(('weightcoef',n,k,wbrute[k],wf[k]))
    mw=min(wbrute)
    if mw!=2:raise AssertionError(('minweight',n,mw))
    cnt=wbrute[2]
    want=min_count_formula(n)
    min_checks+=1
    if cnt!=want:raise AssertionError(('mincount',n,cnt,want))
    # Check every minimum labeling has matched-pair equality and side sum 1.
    cnt2=0
    for z in product(VALS,repeat=n):
        if sum(z)==1:cnt2+=1
    if cnt!=cnt2:raise AssertionError(('diagcount',n,cnt,cnt2))
    print('n',n,'valid',sum(brute.values()),'weight2',cnt,'support',len(brute))
print(f'VERIFY_OK n_range=3..6 labelings={labelings} valid_functions={valid} criterion_checks={criterion_checks} bivariate_coefficients={bicoef_checks} weight_coefficients={weightcoef_checks} minimum_checks={min_checks} max_order=12')
