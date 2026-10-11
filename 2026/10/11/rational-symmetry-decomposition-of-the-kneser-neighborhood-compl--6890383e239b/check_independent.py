"""Independent exhaustive 32767-subset build, modular homology, and Young-rule character check."""
import itertools
from collections import Counter
from functools import lru_cache
from math import factorial
from sympy import Matrix
E=[(a,b) for a in range(6) for b in range(a+1,6)]
pointmask=[(1<<a)|(1<<b) for a,b in E]
# Distinct construction: a simplex iff its endpoint support omits at least two points.
F=[]
for mask in range(1,1<<15):
    support=0
    for i in range(15):
        if mask&(1<<i):support|=pointmask[i]
    if support.bit_count()<=4:F.append(mask)
C={n:[f for f in F if f.bit_count()==n+1] for n in range(6)}
assert tuple(map(len,C.values()))==(15,105,260,225,90,15)

def rank_boundary(dim,prime):
    if dim==0:return 1 # augmented boundary of all vertices
    idx={f:i for i,f in enumerate(C[dim-1])}
    piv={}
    for f in C[dim]:
        order=[i for i in range(15) if f&(1<<i)]
        vec={idx[f^(1<<v)]: (1 if j%2==0 else prime-1) for j,v in enumerate(order)}
        while vec:
            lead=max(vec)
            if lead not in piv:
                a=pow(vec[lead],-1,prime)
                piv[lead]={key:(val*a)%prime for key,val in vec.items()}
                break
            a=vec[lead]
            for i,b in piv[lead].items():
                z=(vec.get(i,0)-a*b)%prime
                if z:vec[i]=z
                elif i in vec:del vec[i]
    return len(piv)
for p in (2,3,5):
    ranks=[rank_boundary(d,p) for d in range(6)]
    # reduced Betti_j = C_j-rank d_j-rank d_{j+1}, use augmented d0=1
    betti=[len(C[j])-ranks[j]-(ranks[j+1] if j+1<6 else 0) for j in range(6)]
    print('prime',p,'ranks',ranks,'reduced Betti',betti)
    assert betti==[0,0,19,0,0,0]

def partitions(n,cap=None):
    if n==0:yield ()
    else:
        for v in range(min(cap or n,n),0,-1):
            for tail in partitions(n-v,v):yield (v,)+tail
PS=list(partitions(6))

def rep(c):
    out=list(range(6));t=0
    for n in c:
        for j in range(n):out[t+j]=t+(j+1)%n
        t+=n
    return out

ch=[]
for c in PS:
    g=rep(c)
    pos={(a,b):i for i,(a,b) in enumerate(E)}
    img=[pos[tuple(sorted((g[a],g[b])))] for a,b in E]
    L=0
    for k,face_list in C.items():
        trace=0
        for f in face_list:
            vs=[i for i in range(15) if (f>>i)&1]
            images=[img[v] for v in vs]
            if set(images)!=set(vs):continue
            trace+=(-1)**sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
        L+=(-1)**k*trace
    ch.append(L-1)
assert ch==[-1,-1,1,1,1,1,1,-1,-1,-5,19]

@lru_cache(None)
def kostka(shape,weight):
    cells=[(r,c) for r,lim in enumerate(shape) for c in range(lim)]
    count=0
    # Independent semistandard tableau count by recursive fillings.
    filled={};left=list(weight)
    def rec(t):
        nonlocal count
        if t==len(cells):count+=1;return
        r,c=cells[t]
        for i in range(len(left)):
            if not left[i]:continue
            x=i+1
            if c>0 and filled[(r,c-1)]>x:continue
            if r>0 and c<shape[r-1] and filled[(r-1,c)]>=x:continue
            filled[(r,c)]=x;left[i]-=1;rec(t+1);left[i]+=1;del filled[(r,c)]
    rec(0);return count

# Character of the ordered-tabloid permutation module M^mu at class c.
def young_permutation_char(mu,cycle_type):
    states={tuple(0 for _ in mu):1}
    for cycle in cycle_type:
        new={}
        for caps,num in states.items():
            for j in range(len(mu)):
                v=list(caps);v[j]+=cycle
                if v[j]>mu[j]:continue
                v=tuple(v);new[v]=new.get(v,0)+num
        states=new
    return states.get(mu,0)
K=Matrix([[kostka(lam,mu) for mu in PS] for lam in PS])
assert K.det() in (1,-1)
T=K.T.inv()*Matrix([[young_permutation_char(mu,c) for c in PS] for mu in PS])
assert all(int(x)==x for x in T)
sizes=[factorial(6)//__import__('math').prod(j**a*factorial(a) for j,a in Counter(c).items()) for c in PS]
assert all(sum(sizes[i]*T[j,i]*T[k,i] for i in range(len(PS)))==(720 if j==k else 0) for j in range(len(PS)) for k in range(len(PS)))
M=[sum(sizes[j]*ch[j]*T[i,j] for j in range(len(PS)))/720 for i in range(len(PS))]
print('Young-rule irreducible character multiplicities:', [(PS[i],int(z)) for i,z in enumerate(M) if z])
assert [int(z) for z in M]==[1 if p in ((3,1,1,1),(2,2,1,1)) else 0 for p in PS]
print('Independent check complete')
