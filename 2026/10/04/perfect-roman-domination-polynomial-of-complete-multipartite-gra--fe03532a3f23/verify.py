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
    for v in range(n):
        if vals[v]==0:
            if sum(vals[u]==2 and lab[u]!=lab[v] for u in range(n)) != 1:
                return False
    return True

def formula(parts):
    N=sum(parts)
    c=[0]*(2*N+1)

    # No zeros: every vertex independently has label 1 or 2.
    for t in range(N+1):
        c[N+t] += math.comb(N,t)

    # Exactly one vertex labeled 2; its part has no zeros.
    for nh in parts:
        out=N-nh
        for q in range(out+1):
            if q==out: continue
            c[nh+1+q] += nh*math.comb(out,q)

    # Exactly two 2-labels in distinct parts; zeros occur only in those parts.
    r=len(parts)
    for i in range(r):
        for j in range(i+1,r):
            ni,nj=parts[i],parts[j]
            m=ni+nj-2
            base=N-ni-nj+4
            for q in range(m+1):
                if q==m: continue
                c[base+q] += ni*nj*math.comb(m,q)

    # At least three 2-labels and some zero: one zero-containing part has
    # t>=2 of the 2-labels and exactly one 2-label lies outside it.
    for ni in parts:
        outside=N-ni
        for t in range(2,ni):
            rem=ni-t
            for q in range(rem+1):
                if q==rem: continue
                weight=N-ni+2*t+1+q
                c[weight] += outside*math.comb(ni,t)*math.comb(rem,q)
    return c

def min_formula(parts):
    N=sum(parts)
    a=sorted(parts)
    return min(N, a[0]+1, N-a[-1]-a[-2]+4)

types=functions=0
for N in range(2,10):
    for r in range(2,N+1):
        for parts in partitions(N,r):
            lab=labels(parts)
            actual=[0]*(2*N+1)
            for vals in itertools.product(range(3), repeat=N):
                functions += 1
                if direct(vals,lab):
                    actual[sum(vals)] += 1
            predicted=formula(parts)
            assert actual==predicted, (parts,actual,predicted)
            observed_min=min(i for i,x in enumerate(actual) if x)
            assert observed_min==min_formula(parts), (parts,observed_min,min_formula(parts))
            types += 1

print("VERIFY_OK")
print("multipartite_types_checked =",types)
print("ternary_labelings_checked =",functions)
print("orders = 2..9")
print("all polynomial coefficients matched")
print("minimum-weight formula matched")
