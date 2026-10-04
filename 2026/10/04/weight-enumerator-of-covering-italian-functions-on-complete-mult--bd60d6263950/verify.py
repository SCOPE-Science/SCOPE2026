import itertools, math

def partitions(n,r,lo=1):
    if r==0:
        if n==0: yield ()
        return
    for x in range(lo,n+1):
        if n-x < x*(r-1): break
        for q in partitions(n-x,r-1,x):
            yield (x,)+q

def labels(parts):
    out=[]
    for i,a in enumerate(parts): out += [i]*a
    return out

def direct(vals,lab):
    n=len(lab)
    zeros=[v for v,x in enumerate(vals) if x==0]
    # Positive support is a vertex cover iff the zero set is independent.
    for a in range(len(zeros)):
        for b in range(a+1,len(zeros)):
            if lab[zeros[a]] != lab[zeros[b]]:
                return False
    # Italian condition.
    for v in zeros:
        if sum(vals[u] for u in range(n) if lab[u]!=lab[v]) < 2:
            return False
    return True

def formula(parts):
    N=sum(parts); c=[0]*(2*N+1)
    # Zero-free functions: labels 1 or 2 everywhere.
    for t in range(N+1):
        c[N+t] += math.comb(N,t)
    # Nonempty zero set lies in one unique part.
    for ni in parts:
        q=N-ni
        inside=[0]*(2*ni+1)
        for vals in itertools.product(range(3), repeat=ni):
            if 0 in vals:
                inside[sum(vals)] += 1
        if q>=2:
            outside=[0]*(2*q+1)
            for twos in range(q+1):
                outside[q+twos] = math.comb(q,twos)
        else:
            outside=[0,0,1]  # the unique outside vertex is forced to label 2
        for a,ca in enumerate(inside):
            if not ca: continue
            for b,cb in enumerate(outside):
                if cb: c[a+b] += ca*cb
    return c

def gamma_formula(parts):
    return max(2, sum(parts)-max(parts))

types=functions=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=labels(parts); actual=[0]*(2*N+1)
            for vals in itertools.product(range(3), repeat=N):
                functions += 1
                if direct(vals,lab): actual[sum(vals)] += 1
            predicted=formula(parts)
            assert actual==predicted, (parts,actual,predicted)
            g=min(i for i,x in enumerate(actual) if x)
            assert g==gamma_formula(parts), (parts,g,gamma_formula(parts))
            types += 1

# Published complete-bipartite minimum: for p>=q>=1, value 2 if q=1, else q.
for p in range(1,11):
    for q in range(1,p+1):
        expected=2 if q==1 else q
        assert gamma_formula((p,q))==expected

print('VERIFY_OK')
print('multipartite_types_checked =',types)
print('ternary_labelings_checked =',functions)
print('orders = 2..9')
print('all weight-enumerator coefficients matched')
print('minimum-weight formula matched')
print('published complete-bipartite minimum matched for 1 <= q <= p <= 10')
