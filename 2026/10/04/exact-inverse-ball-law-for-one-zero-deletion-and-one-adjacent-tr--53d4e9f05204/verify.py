from itertools import product

def channel_outputs(x):
    out=set(); n=len(x)
    # deletion only
    for d,c in enumerate(x):
        if c=='0': out.add(x[:d]+x[d+1:])
    # swap first, then delete
    for s in range(n-1):
        if x[s]!=x[s+1]:
            z=x[:s]+x[s+1]+x[s]+x[s+2:]
            for d,c in enumerate(z):
                if c=='0': out.add(z[:d]+z[d+1:])
    # delete first, then swap
    for d,c in enumerate(x):
        if c!='0': continue
        z=x[:d]+x[d+1:]
        for s in range(len(z)-1):
            if z[s]!=z[s+1]: out.add(z[:s]+z[s+1]+z[s]+z[s+2:])
    return out

def zero_gaps(y):
    v=[]; c=0
    for b in y:
        if b=='0': c+=1
        else: v.append(c); c=0
    v.append(c)
    return v

def formula(y):
    v=zero_gaps(y); m=len(v)
    p=sum(a>0 for a in v)
    e=(1 if v[0]>0 else 0) if m==1 else int(v[0]>0)+int(v[-1]>0)
    return m+(2*m-3)*p-(m-2)*e

def expected_extremal(y):
    n=len(y)+1
    if n==2: return y=='1'
    if n==3: return y in {'01','10','11'}
    if n%2==0:
        return y == '10'*(n//2-1)+'1'
    return y[0]=='1' and y[-1]=='1' and '00' not in y and y.count('11')==1

def support_max(n):
    best=-1
    for m in range(1,n+1):
        z=n-m
        # enumerate possible number of positive gaps and positive endpoints;
        # feasibility is determined by support size because positive entries can absorb surplus zeros.
        for p in range(0,min(z,m)+1):
            if z>0 and p==0: continue
            if z==0 and p!=0: continue
            for e in range(0,min(2,p)+1):
                if m==1 and e>1: continue
                interior=m-(1 if m==1 else 2)
                if p-e<0 or p-e>interior: continue
                if m>1 and e>2: continue
                val=m+(2*m-3)*p-(m-2)*e
                best=max(best,val)
    return best

for n in range(2,11):
    parents={''.join(y):set() for y in product('01',repeat=n-1)}
    for xb in product('01',repeat=n):
        x=''.join(xb)
        for y in channel_outputs(x): parents[y].add(x)
    for y,P in parents.items():
        assert len(P)==formula(y),(n,y,len(P),formula(y))
    mx=max(len(P) for P in parents.values())
    target=n*n//2-n+2
    assert mx==target,(n,mx,target)
    actual={y for y,P in parents.items() if len(P)==mx}
    expected={y for y in parents if expected_extremal(y)}
    assert actual==expected,(n,actual,expected)

for n in range(2,201):
    assert support_max(n)==n*n//2-n+2,(n,support_max(n),n*n//2-n+2)

print('VERIFY_OK direct_n<=10 symbolic_n<=200 pointwise_formula_extremizers')
