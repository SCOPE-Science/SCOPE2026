#!/usr/bin/env python3
from itertools import combinations, product


def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def add(a,b,scale=1):
    c=a[:] + [0]*max(0,len(b)-len(a))
    for i,v in enumerate(b): c[i]+=scale*v
    while len(c)>1 and c[-1]==0: c.pop()
    return c


def label_poly(n, allowed):
    base=[0]*(max(allowed)+1)
    for a in allowed: base[a]+=1
    p=[1]
    for _ in range(n): p=mul(p,base)
    return p


def closed_formula(parts):
    r=len(parts); N=sum(parts)
    out=label_poly(N,(1,2))
    A={}; C={}; P={}
    for i,n in enumerate(parts):
        P[i]=label_poly(n,(1,2))
        A[i]=add(label_poly(n,(0,1,2)),P[i],-1)
        C[i]=add(label_poly(n,(0,1)),[0]*n+[1],-1)
    for q in range(2,r+1):
        for qt in combinations(range(r),q):
            Q=set(qt)
            term=[1]
            for i in range(r): term=mul(term,A[i] if i in Q else P[i])
            for i in Q:
                bad=[1]
                for j,n in enumerate(parts):
                    if j==i: fac=A[j]
                    elif j in Q: fac=C[j]
                    else: fac=[0]*n+[1]
                    bad=mul(bad,fac)
                term=add(term,bad,-1)
            none=[1]
            for j,n in enumerate(parts):
                none=mul(none,C[j] if j in Q else [0]*n+[1])
            term=add(term,none,q-1)
            out=add(out,term)
    return out+[0]*(2*N+1-len(out))


def partitions(n,lo=1):
    if n==0:
        yield ()
        return
    for a in range(lo,n+1):
        for rest in partitions(n-a,a): yield (a,)+rest


def test_profile(parts):
    N=sum(parts)
    part=[]
    for i,n in enumerate(parts): part += [i]*n
    hist=[0]*(2*N+1); count=0
    for lab in product((0,1,2), repeat=N):
        literal=True
        for v in range(N):
            if lab[v]!=0: continue
            i=part[v]
            if not any(part[u]!=i and lab[u]==0 for u in range(N)):
                literal=False; break
            if not any(part[u]!=i and lab[u]==2 for u in range(N)):
                literal=False; break
        z=[0]*len(parts); t=[0]*len(parts)
        for v,a in enumerate(lab):
            if a==0: z[part[v]]+=1
            elif a==2: t[part[v]]+=1
        Z=sum(z); T=sum(t)
        criterion=all(z[i]==0 or (Z-z[i]>0 and T-t[i]>0) for i in range(len(parts)))
        assert literal==criterion, (parts,lab,literal,criterion)
        if literal:
            hist[sum(lab)]+=1; count+=1
    f=closed_formula(parts)
    assert hist==f, (parts,hist,f)
    m=min(parts); r=len(parts)
    predicted=(N if r==2 and m==1 else 4 if r==2 else min(4,m+1))
    actual=next(i for i,c in enumerate(hist) if c)
    assert actual==predicted,(parts,actual,predicted)
    return 3**N,count,len(hist)


def main():
    profiles=labelings=valid=coeffs=0
    for N in range(2,10):
        for p in partitions(N):
            if len(p)<2: continue
            a,b,c=test_profile(p)
            profiles+=1; labelings+=a; valid+=b; coeffs+=c
    print(f'VERIFY_OK profiles={profiles} labelings={labelings} valid_functions={valid} coefficient_checks={coeffs} max_order=9')

if __name__=='__main__': main()
