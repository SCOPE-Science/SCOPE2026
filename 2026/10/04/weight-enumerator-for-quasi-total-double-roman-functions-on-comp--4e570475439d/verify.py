import itertools

def partitions(n,r,lo=1):
    if r==0:
        if n==0:
            yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1):
            break
        for tail in partitions(n-x,r-1,x):
            yield (x,)+tail

def part_labels(parts):
    out=[]
    for i,m in enumerate(parts):
        out.extend([i]*m)
    return out

def valid_qtdr(vals, parts):
    lab=part_labels(parts)
    n=len(vals)
    pos=[v for v,x in enumerate(vals) if x>0]
    for v,x in enumerate(vals):
        neigh=[u for u in range(n) if lab[u]!=lab[v]]
        if x==0:
            n3=sum(vals[u]==3 for u in neigh)
            n2=sum(vals[u]==2 for u in neigh)
            if not (n3>=1 or n2>=2):
                return False
        elif x==1:
            if not any(vals[u]>=2 for u in neigh):
                return False
    for v in pos:
        if not any(u!=v and vals[u]>0 and lab[u]!=lab[v] for u in range(n)):
            if vals[v]!=2:
                return False
    return True

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return trim(c)

def add(a,b,sign=1):
    n=max(len(a),len(b))
    c=[0]*n
    for i in range(n):
        c[i]=(a[i] if i<len(a) else 0)+sign*(b[i] if i<len(b) else 0)
    return trim(c)

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:
        a.pop()
    return a

def powp(a,n):
    out=[1]
    for _ in range(n):
        out=mul(out,a)
    return out

def monomial(k,coef=1):
    return [0]*k+[coef]

def formula(parts):
    N=sum(parts)
    C=lambda m: powp([1,1],m)
    A=lambda m: powp([1,1,1],m)
    B=lambda m: powp([1,1,1,1],m)
    X=lambda m: mul(monomial(2,m),C(m-1)) if m>=1 else [0]
    Y=lambda m: monomial(m+1,m) if m>=1 else [0]
    H=lambda m: add(add(A(m),C(m),-1),X(m),-1)
    R=lambda m: add(add(powp([0,1,1],m),monomial(m),-1),Y(m),-1)

    ans=[0]

    # At least two parts contain label 3.
    p=add(B(N),A(N),-1)
    for ni in parts:
        p=add(p,mul(add(B(ni),A(ni),-1),A(N-ni)),-1)
    ans=add(ans,p)

    # Exactly one part i contains label 3.
    for ni in parts:
        M=N-ni
        J0=mul(
            add(powp([0,0,1,1],ni),monomial(2*ni),-1),
            add(C(M),[1],-1)
        )
        J1=mul(
            add(powp([0,1,1,1],ni),powp([0,1,1],ni),-1),
            X(M)
        )
        J2=mul(
            add(B(ni),A(ni),-1),
            add(add(A(M),C(M),-1),X(M),-1)
        )
        ans=add(ans,J0)
        ans=add(ans,J1)
        ans=add(ans,J2)

    # No label 3, with label 2 in at least three parts.
    p=add(A(N),C(N),-1)
    for ni in parts:
        p=add(p,mul(add(A(ni),C(ni),-1),C(N-ni)),-1)
    for i,j in itertools.combinations(range(len(parts)),2):
        ni,nj=parts[i],parts[j]
        p=add(
            p,
            mul(
                mul(add(A(ni),C(ni),-1),add(A(nj),C(nj),-1)),
                C(N-ni-nj)
            ),
            -1
        )
    ans=add(ans,p)

    # No label 3, with label 2 in exactly two parts.
    for i,j in itertools.combinations(range(len(parts)),2):
        ni,nj=parts[i],parts[j]
        q=[0]
        for term in (
            mul(Y(ni),Y(nj)),
            mul(X(ni),R(nj)),
            mul(R(ni),X(nj)),
            mul(H(ni),H(nj)),
        ):
            q=add(q,term)
        ans=add(ans,mul(q,C(N-ni-nj)))

    # No label 3, with label 2 in exactly one part.
    for ni in parts:
        if ni>=2:
            U=mul(monomial(2*ni),C(N-ni))
        else:
            U=monomial(N+1)
        ans=add(ans,U)

    return trim(ans)

types=0
labelings=0
valid_total=0
for N in range(2,9):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            actual=[0]*(3*N+1)
            for vals in itertools.product(range(4),repeat=N):
                labelings+=1
                if valid_qtdr(vals,parts):
                    actual[sum(vals)]+=1
                    valid_total+=1
            pred=formula(parts)
            pred=pred+[0]*(len(actual)-len(pred))
            assert actual==pred[:len(actual)], (parts,actual,pred)
            gamma=min(i for i,c in enumerate(actual) if c)
            expected=3 if N==2 else (4 if min(parts)<=2 else 6)
            assert gamma==expected, (parts,gamma,expected)
            types+=1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("labelings_checked =",labelings)
print("valid_functions_counted =",valid_total)
print("orders = 2..8")
print("every weight-enumerator coefficient matched")
print("minimum-weight corollary matched")
