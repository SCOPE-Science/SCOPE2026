import itertools, math


def direct_sidf(m,n,vals):
    N=m+n
    def adj(u,v):
        if u==v:
            return False
        return u<m or v<m
    def italian(x):
        for v in range(N):
            if x[v]==0 and sum(x[u] for u in range(N) if adj(u,v))<2:
                return False
        return True
    if not italian(vals):
        return False
    for v in range(N):
        if vals[v]!=0:
            continue
        defended=False
        for u in range(N):
            if adj(u,v) and vals[u]>0:
                y=list(vals)
                y[v]=1
                y[u]-=1
                if italian(y):
                    defended=True
                    break
        if not defended:
            return False
    return True


def profile_criterion(m,n,vals):
    clique=vals[:m]
    independent=vals[m:]
    q=independent.count(0)
    c=sum(clique)
    if q==0:
        return c>0 or any(x==2 for x in independent)
    if q==1:
        return c>=2
    return c>=3


def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def ppow(base,e):
    out=[1]
    for _ in range(e):
        out=conv(out,base)
    return out


def add(a,b,scale=1):
    out=[0]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=scale*x
    return out


def shift(a,k,scale=1):
    return [0]*k+[scale*x for x in a]


def formula(m,n):
    C_m=ppow([1,1,1],m)
    C_n=ppow([1,1,1],n)
    P_n=shift(ppow([1,1],n),n)
    J_1=shift(ppow([1,1],n-1),n-1)
    J_1=[n*x for x in J_1]

    # q=0: all independent vertices are positive; exclude only
    # the labeling with all clique vertices 0 and all independent vertices 1.
    A=conv(P_n,C_m)
    A=add(A,shift([1],n),-1)

    # q=1: clique weight at least 2.
    C_ge2=C_m[:]
    C_ge2[0]-=1
    C_ge2[1]-=m
    B=conv(J_1,C_ge2)

    # q>=2: clique weight at least 3.
    J_ge2=C_n[:]
    J_ge2=add(J_ge2,P_n,-1)
    J_ge2=add(J_ge2,J_1,-1)
    C_ge3=C_m[:]
    C_ge3[0]-=1
    C_ge3[1]-=m
    C_ge3[2]-=math.comb(m+1,2)
    D=conv(J_ge2,C_ge3)

    out=add(add(A,B),D)
    target=2*(m+n)+1
    out += [0]*(target-len(out))
    return out[:target]


def minimum_formula(m,n):
    return n+1 if m==1 else 3


types=0
functions=0
for N in range(3,10):
    for m in range(1,N-1):
        n=N-m
        if n<2:
            continue
        actual=[0]*(2*N+1)
        for vals in itertools.product(range(3),repeat=N):
            functions+=1
            got=direct_sidf(m,n,vals)
            assert got==profile_criterion(m,n,vals),(m,n,vals,got)
            if got:
                actual[sum(vals)]+=1
        predicted=formula(m,n)
        assert actual==predicted,(m,n,actual,predicted)
        observed=min(i for i,x in enumerate(actual) if x)
        assert observed==minimum_formula(m,n),(m,n,observed,minimum_formula(m,n))
        types+=1

print('VERIFY_OK')
print('complete_split_types_checked =',types)
print('ternary_labelings_checked =',functions)
print('orders = 3..9')
print('all-set criterion matched')
print('all weight-enumerator coefficients matched')
print('minimum-weight corollary matched')
