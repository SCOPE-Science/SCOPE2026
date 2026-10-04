from itertools import product
from collections import Counter

def partitions(n, max_part=None):
    if max_part is None or max_part > n: max_part=n
    if n==0:
        yield ()
        return
    for a in range(min(max_part,n),0,-1):
        for tail in partitions(n-a,a):
            yield (a,)+tail

def mul(p,q):
    r=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): r[i+j]+=a*b
    return r

def powpoly(base,n):
    p=[1]
    for _ in range(n): p=mul(p,base)
    return p

def add_into(dst, src, coeff=1):
    if len(dst)<len(src): dst.extend([0]*(len(src)-len(dst)))
    for i,a in enumerate(src): dst[i]+=coeff*a

def formula(parts):
    A=[powpoly([1,1,1],n) for n in parts]
    B=[powpoly([1,1],n) for n in parts]
    C=[([0]*n)+powpoly([1,1],n) for n in parts] # x^n(1+x)^n
    pa=[1]; pb=[1]
    for p in A: pa=mul(pa,p)
    for p in B: pb=mul(pb,p)
    R=pa[:]
    add_into(R,pb,-1)
    for i in range(len(parts)):
        amid=A[i][:]
        add_into(amid,B[i],-1)
        bout=[1]
        for j,p in enumerate(B):
            if j!=i: bout=mul(bout,p)
        add_into(R,mul(amid,bout),-1)
    N=sum(parts)
    one=[0]*(N+1); one[N]=1
    add_into(R,one,1)
    for i,n in enumerate(parts):
        ci=C[i][:]
        xn=[0]*(n+1); xn[n]=1
        add_into(ci,xn,-1)
        bout=[1]
        for j,p in enumerate(B):
            if j!=i: bout=mul(bout,p)
        add_into(R,mul(ci,bout),1)
    while R and R[-1]==0: R.pop()
    return R

def is_rdf(labels, part_of):
    twoparts={part_of[v] for v,x in enumerate(labels) if x==2}
    for v,x in enumerate(labels):
        if x==0 and not any(t!=part_of[v] for t in twoparts):
            return False
    return True

def class_ok(labels, part_of, r):
    T={part_of[v] for v,x in enumerate(labels) if x==2}
    if not T:
        return all(x==1 for x in labels)
    if len(T)>=2:
        return True
    i=next(iter(T))
    return all(labels[v]!=0 for v in range(len(labels)) if part_of[v]==i)

def expected_min(parts):
    N=sum(parts)
    s1=sum(n==1 for n in parts); s2=sum(n==2 for n in parts); s3=sum(n==3 for n in parts)
    if s1:
        return (2, 3 if N==2 else s1)
    if s2:
        return (3, 2*s2)
    return (4, sum(parts[i]*parts[j] for i in range(len(parts)) for j in range(i+1,len(parts))) + 3*s3)

gtypes=0; lab=0; coeffchecks=0
for N in range(2,11):
    for parts in partitions(N):
        if len(parts)<2: continue
        # complete multipartite connected
        part_of=[]
        for i,n in enumerate(parts): part_of += [i]*n
        brute=Counter()
        for labels in product(range(3), repeat=N):
            lab+=1
            a=is_rdf(labels,part_of); b=class_ok(labels,part_of,len(parts))
            assert a==b,(parts,labels,a,b)
            if a: brute[sum(labels)]+=1
        F=formula(parts)
        got=[brute[k] for k in range(2*N+1)]
        F=F+[0]*(2*N+1-len(F))
        assert F==got,(parts,F,got)
        gamma=next(k for k,v in enumerate(got) if v)
        cnt=got[gamma]
        assert (gamma,cnt)==expected_min(parts),(parts,(gamma,cnt),expected_min(parts))
        coeffchecks+=2*N+1; gtypes+=1
print(f'VERIFY_OK graph_types={gtypes} labelings={lab} coefficient_checks={coeffchecks} max_order=10')
