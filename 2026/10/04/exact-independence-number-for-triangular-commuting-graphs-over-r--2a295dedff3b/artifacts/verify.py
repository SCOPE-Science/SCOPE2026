from math import gcd

def primes(n):
    out=[]; x=n; d=2
    while d*d<=x:
        if x%d==0:
            out.append(d)
            while x%d==0: x//=d
        d+=1
    if x>1: out.append(x)
    return out

def phi(n):
    z=n
    for p in primes(n): z=z//p*(p-1)
    return z

def psi(n):
    z=n
    for p in primes(n): z=z//p*(p+1)
    return z

def primitive(v,n):
    return gcd(gcd(v[0],v[1]),n)==1

def det(v,w,n):
    return (v[0]*w[1]-v[1]*w[0])%n

def line_from(v,n):
    return frozenset(((a*v[0])%n,(a*v[1])%n) for a in range(n))

def projective_lines(n):
    lines={}
    for x in range(n):
        for y in range(n):
            v=(x,y)
            if primitive(v,n):
                lines.setdefault(line_from(v,n),v)
    return lines

def expected_unimodular(n):
    z=n*n
    for p in primes(n):
        z=z//(p*p)*(p*p-1)
    return z

def matrix_mul(A,B,n):
    a,b,c=A; d,e,f=B
    return ((a*d)%n,(a*e+b*f)%n,(c*f)%n)

def max_pairwise_nonzero_det(n):
    V=[(x,y) for x in range(n) for y in range(n) if (x,y)!=(0,0)]
    N=len(V)
    adj=[0]*N
    for i,v in enumerate(V):
        mask=0
        for j,w in enumerate(V):
            if i!=j and det(v,w,n)!=0:
                mask|=1<<j
        adj[i]=mask
    best=0
    def expand(size,P):
        nonlocal best
        if size+P.bit_count()<=best: return
        if not P:
            if size>best: best=size
            return
        while P:
            if size+P.bit_count()<=best: return
            bit=P & -P
            i=bit.bit_length()-1
            P^=bit
            expand(size+1,P & adj[i])
    expand(0,(1<<N)-1)
    return best

def check_projective(n):
    lines=projective_lines(n)
    assert len(lines)==psi(n),(n,len(lines),psi(n))
    assert all(len(L)==n for L in lines)
    for L in lines:
        assert sum(primitive(v,n) for v in L)==phi(n)

    nonzero=[(x,y) for x in range(n) for y in range(n) if (x,y)!=(0,0)]
    covered={v:False for v in nonzero}
    for L in lines:
        pts=list(L)
        for v in pts:
            if v!=(0,0): covered[v]=True
        for i,v in enumerate(pts):
            for w in pts[i+1:]:
                assert det(v,w,n)==0
    assert all(covered.values())

    reps=list(lines.values())
    for i,v in enumerate(reps):
        assert primitive(v,n)
        for w in reps[i+1:]:
            assert det(v,w,n)!=0,(n,v,w)

    uv=sum(primitive((x,y),n) for x in range(n) for y in range(n))
    assert uv==expected_unimodular(n)
    assert uv//phi(n)==psi(n)

def check_matrix_formula(n):
    nonzero=[(x,y) for x in range(n) for y in range(n) if (x,y)!=(0,0)]
    lifts=(0,1%n)
    for v in nonzero:
        for w in nonzero:
            expected=(det(v,w,n)==0)
            for c in lifts:
                for f in lifts:
                    A=((c+v[0])%n,v[1],c)
                    B=((f+w[0])%n,w[1],f)
                    assert (matrix_mul(A,B,n)==matrix_mul(B,A,n))==expected

for n in range(2,41):
    check_projective(n)

for n in range(2,11):
    check_matrix_formula(n)

for n in range(2,7):
    exact=max_pairwise_nonzero_det(n)
    assert exact==psi(n),(n,exact,psi(n))
    print("exact",n,exact)

assert psi(4)==6
assert 4*phi(4)*(8-phi(4))==48
print("VERIFY_OK")
