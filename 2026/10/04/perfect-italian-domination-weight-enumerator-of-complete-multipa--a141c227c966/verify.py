import itertools, math

def partitions(n,r,lo=1):
    if r==0:
        if n==0:
            yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1):
            break
        for q in partitions(n-x,r-1,x):
            yield (x,)+q

def part_labels(parts):
    lab=[]
    for i,n in enumerate(parts):
        lab += [i]*n
    return lab

def pid_direct(vals,lab):
    n=len(vals)
    for v in range(n):
        if vals[v]==0:
            s=0
            for u in range(n):
                if lab[u]!=lab[v]:
                    s += vals[u]
            if s != 2:
                return False
    return True

def pid_profile(vals,parts):
    lab=part_labels(parts)
    r=len(parts)
    s=[0]*r
    has_zero=[False]*r
    W=sum(vals)
    for v,x in enumerate(vals):
        i=lab[v]
        s[i]+=x
        if x==0:
            has_zero[i]=True
    return all((not has_zero[i]) or W-s[i]==2 for i in range(r))

def conv(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def ppow(base,n):
    out=[1]
    for _ in range(n):
        out=conv(out,base)
    return out

def add_shift(dst,src,shift,mul=1):
    for i,x in enumerate(src):
        dst[i+shift]+=mul*x

def A(n):
    allp=ppow([1,1,1],n)
    pos=ppow([0,1,1],n)
    return [a-b for a,b in zip(allp,pos)]

def formula(parts):
    r=len(parts); N=sum(parts)
    c=[0]*(2*N+1)

    # no zero-labelled vertices: each vertex is 1 or 2
    for j in range(N+1):
        c[N+j]+=math.comb(N,j)

    # exactly one part contains a zero
    for ni in parts:
        outside=N-ni
        if 1 <= outside <= 2:
            add_shift(c,A(ni),2)

    s=sum(ni==1 for ni in parts)
    t=sum(ni==2 for ni in parts)
    c2=(s+t if r>=3 else 0) + (math.comb(s,2) if r>=4 else 0)
    c[2]+=c2

    if r==3:
        u=[ni if ni>=2 else 0 for ni in parts]
        c3=u[0]*u[1]*u[2]
        for k,ni in enumerate(parts):
            if ni==1:
                p=1
                for i in range(3):
                    if i!=k: p*=u[i]
                c3+=p
        c[3]+=c3

    if r==2:
        v=[]
        for ni in parts:
            if ni==1: v.append(0)
            elif ni==2: v.append(2)
            else: v.append(ni + math.comb(ni,2))
        c[4]+=v[0]*v[1]

    return c

types=subsets=published_min_checks=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=part_labels(parts)
            actual=[0]*(2*N+1)
            for vals in itertools.product(range(3), repeat=N):
                subsets+=1
                d=pid_direct(vals,lab)
                assert d==pid_profile(vals,parts), (parts,vals)
                if d:
                    actual[sum(vals)]+=1
            pred=formula(parts)
            assert actual==pred, (parts,actual,pred)
            if min(parts)>=3:
                observed=min(i for i,x in enumerate(actual) if x)
                expected=4 if r==2 else (3 if r==3 else N)
                assert observed==expected, (parts,observed,expected)
                published_min_checks+=1
            types+=1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("ternary_labelings_checked =",subsets)
print("orders = 2..9")
print("all-set profile criterion matched")
print("all weight-enumerator coefficients matched")
print("published all-parts-at-least-3 minimum specializations checked =",published_min_checks)
