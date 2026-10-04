from itertools import product
from collections import defaultdict

# Polynomial lists: p[k] is coefficient of x^k.
def add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def sub(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]-=v
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def pow_poly(a,n):
    r=[1]
    for _ in range(n): r=mul(r,a)
    return r

def F(n,z,t):
    if not z and not t: return [0]*n+[1]           # x^n
    if z and not t: return pow_poly([1,1],n)       # (1+x)^n
    if not z and t: return pow_poly([0,1,1],n)     # (x+x^2)^n
    return pow_poly([1,1,1],n)                     # (1+x+x^2)^n

def formula(alpha,beta):
    p=len(alpha); N=sum(alpha)+sum(beta)
    ans=[0]*N+[1]
    # A-side only: s is latest A class containing a 2
    for s in range(p):
        term=sub(F(alpha[s],0,1),F(alpha[s],0,0))
        for i in range(p):
            if i==s: continue
            term=mul(term,F(alpha[i],0,1 if i<s else 0))
        for j in range(p):
            term=mul(term,F(beta[j],1 if j<=s else 0,0))
        ans=add(ans,term)
    # B-side only: r is earliest B class containing a 2
    for r in range(p):
        term=sub(F(beta[r],0,1),F(beta[r],0,0))
        for j in range(p):
            if j==r: continue
            term=mul(term,F(beta[j],0,1 if j>r else 0))
        for i in range(p):
            term=mul(term,F(alpha[i],1 if i>=r else 0,0))
        ans=add(ans,term)
    # Both sides have a 2: r earliest B-two class, s latest A-two class.
    for r in range(p):
        for s in range(p):
            za = (s>=r)
            zb = (r<=s)
            term=sub(F(alpha[s],za,1),F(alpha[s],za,0))
            term=mul(term,sub(F(beta[r],zb,1),F(beta[r],zb,0)))
            for i in range(p):
                if i==s: continue
                term=mul(term,F(alpha[i],i>=r,i<=s))
            for j in range(p):
                if j==r: continue
                term=mul(term,F(beta[j],j<=s,j>=r))
            ans=add(ans,term)
    return ans

def build(alpha,beta):
    A=[]; B=[]; vertices=[]
    for i,a in enumerate(alpha):
        cls=[]
        for k in range(a):
            v=('A',i,k); cls.append(v); vertices.append(v)
        A.append(cls)
    for j,b in enumerate(beta):
        cls=[]
        for k in range(b):
            v=('B',j,k); cls.append(v); vertices.append(v)
        B.append(cls)
    idx={v:k for k,v in enumerate(vertices)}
    nbr=[set() for _ in vertices]
    for i,cls in enumerate(A):
        for v in cls:
            for j in range(i+1):
                for w in B[j]:
                    nbr[idx[v]].add(idx[w]); nbr[idx[w]].add(idx[v])
    return nbr

def brute(alpha,beta):
    nbr=build(alpha,beta); n=len(nbr); c=[0]*(2*n+1); checked=0
    for lab in product((0,1,2), repeat=n):
        checked+=1
        ok=True
        for v,x in enumerate(lab):
            if x==0 and not any(lab[u]==2 for u in nbr[v]):
                ok=False; break
        if ok: c[sum(lab)]+=1
    while len(c)>1 and c[-1]==0: c.pop()
    return c,checked

def comps(total,p):
    if p==1:
        yield (total,); return
    for first in range(1,total-p+2):
        for rest in comps(total-first,p-1):
            yield (first,)+rest

profiles=0; labelings=0; coefficient_checks=0; max_order=9
for N in range(2,max_order+1):
    for p in range(1,N//2+1):
        for na in range(p,N-p+1):
            nb=N-na
            if nb<p: continue
            for alpha in comps(na,p):
                for beta in comps(nb,p):
                    f=formula(alpha,beta)
                    b,count=brute(alpha,beta)
                    profiles+=1; labelings+=count
                    L=max(len(f),len(b)); coefficient_checks+=L
                    f=f+[0]*(L-len(f)); b=b+[0]*(L-len(b))
                    if f!=b:
                        raise SystemExit(f'MISMATCH alpha={alpha} beta={beta} formula={f} brute={b}')
print(f'VERIFY_OK profiles={profiles} labelings={labelings} coefficient_checks={coefficient_checks} max_order={max_order}')
