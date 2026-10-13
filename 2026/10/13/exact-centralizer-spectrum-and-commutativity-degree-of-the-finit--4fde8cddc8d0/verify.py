from itertools import product


def poly_mul(a,b,p):
    n=p
    c=[0]*n
    for i,x in enumerate(a):
        if x%p==0: continue
        for j,y in enumerate(b):
            if i+j>=n: break
            c[i+j]=(c[i+j]+x*y)%p
    return c

def deriv(a,p):
    return [((i+1)*a[i+1])%p for i in range(p-1)] + [0]

def bracket(f,g,p):
    fp=deriv(f,p); gp=deriv(g,p)
    a=poly_mul(f,gp,p); b=poly_mul(g,fp,p)
    return [(x-y)%p for x,y in zip(a,b)]

def rank_mod(A,p):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(v*inv)%p for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                t=A[i][c]%p
                A[i]=[(x-t*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def centralizer_dim(f,p):
    cols=[]
    for j in range(p):
        g=[0]*p; g[j]=1
        cols.append(bracket(f,g,p))
    M=[[cols[j][i] for j in range(p)] for i in range(p)]
    return p-rank_mod(M,p)

def valuation(f):
    for i,a in enumerate(f):
        if a: return i
    return None

def predicted_dim(s,p):
    if s is None: return p
    if s==0: return 1
    return s if 2*s<=p else s-1

def unit_identity_check(p):
    checks=0
    # deterministic unit and h families, all valuations
    units=[]
    for seed in range(1, min(p,5)):
        u=[1]+[((seed*(i+1)+i*i)%p) for i in range(1,p)]
        units.append(u)
    hs=[]
    for seed in range(min(p,5)):
        hs.append([((seed+2*i+i*i)%p) for i in range(p)])
    for s in range(p):
        xs=[0]*p; xs[s]=1
        for u in units:
            f=poly_mul(xs,u,p)
            for h in hs:
                g=poly_mul(u,h,p)
                lhs=bracket(f,g,p)
                rhs=poly_mul(poly_mul(u,u,p), bracket(xs,h,p), p)
                if lhs!=rhs:
                    raise AssertionError((p,s,u,h,lhs,rhs))
                checks+=1
    return checks

def exhaustive_p5():
    p=5
    hist={}
    pair_count=0
    for tup in product(range(p), repeat=p):
        f=list(tup)
        d=centralizer_dim(f,p)
        s=valuation(f)
        if d!=predicted_dim(s,p):
            raise AssertionError((f,s,d,predicted_dim(s,p)))
        hist[d]=hist.get(d,0)+1
        pair_count += p**d
    expect={1:(p*p-1)*p**(p-2),2:(p*p-1)*p,3:p-1,5:1}
    if hist!=expect:
        raise AssertionError((hist,expect))
    m=(p-1)//2
    closed=p**(p-2)*(p**3+m*(p*p-1))
    if pair_count!=closed:
        raise AssertionError((pair_count,closed))
    return hist,pair_count

def representative_checks(p):
    checked=0
    for s in range(p):
        for seed in range(1,min(p,6)):
            # u has constant 1, hence is a unit
            u=[1]+[((seed*i+i*i+2)%p) for i in range(1,p)]
            xs=[0]*p; xs[s]=1
            f=poly_mul(xs,u,p)
            d=centralizer_dim(f,p)
            if d!=predicted_dim(s,p):
                raise AssertionError((p,s,seed,d,predicted_dim(s,p)))
            checked+=1
    return checked

def distribution_identity(p,q):
    assert q%p==0 or q==p  # only used at q=p here
    m=(p-1)//2
    hist={1:(q*q-1)*q**(p-2), p:1}
    for d in range(2,m): hist[d]=(q-1)*q**(p-d-1)
    hist[m]=(q*q-1)*q**(m-1)
    for d in range(m+1,p-1): hist[d]=(q-1)*q**(p-d-2)
    if sum(hist.values())!=q**p:
        raise AssertionError((p,q,hist,sum(hist.values()),q**p))
    pairs=sum(n*q**d for d,n in hist.items())
    closed=q**(p-2)*(q**3+m*(q*q-1))
    if pairs!=closed:
        raise AssertionError((p,q,pairs,closed))
    return hist,pairs

if __name__=='__main__':
    h5,c5=exhaustive_p5()
    reps=sum(representative_checks(p) for p in (7,11))
    uchecks=sum(unit_identity_check(p) for p in (5,7,11))
    for p in (5,7,11): distribution_identity(p,p)
    print(f'VERIFY_OK exhaustive_F5={5**5} representative_checks={reps} unit_identity_checks={uchecks} pair_count_F5={c5}')
