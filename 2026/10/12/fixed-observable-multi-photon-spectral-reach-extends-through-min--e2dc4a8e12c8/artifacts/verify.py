from fractions import Fraction

def basis(N):
    # coordinates: c0,c1..cN,s1..sN
    out=[]
    for k in range(N+1):
        v=[Fraction(0)]*(2*N+1); v[k]=1; out.append(v)
    for k in range(1,N+1):
        v=[Fraction(0)]*(2*N+1); v[N+k]=1; out.append(v)
    return out

def mul_cos(vec, r, N):
    out=[Fraction(0)]*(2*N+1)
    # constant
    c0=vec[0]
    if r<=N: out[r]+=c0
    for k in range(1,N+1):
        c=vec[k]
        if c:
            a=abs(r-k); b=r+k
            out[a]+=c*Fraction(1,2)
            if b<=N: out[b]+=c*Fraction(1,2)
        s=vec[N+k]
        if s:
            # sin(kx) cos(rx) = [sin((k+r)x)+sin((k-r)x)]/2
            b=k+r
            if b<=N: out[N+b]+=s*Fraction(1,2)
            q=k-r
            if q>0: out[N+q]+=s*Fraction(1,2)
            elif q<0: out[N+(-q)]-=s*Fraction(1,2)
    return out

def mul_sin(vec, r, N):
    out=[Fraction(0)]*(2*N+1)
    c0=vec[0]
    if r<=N: out[N+r]+=c0
    for k in range(1,N+1):
        c=vec[k]
        if c:
            # cos(k) sin(r) = [sin(r+k)+sin(r-k)]/2
            b=r+k
            if b<=N: out[N+b]+=c*Fraction(1,2)
            q=r-k
            if q>0: out[N+q]+=c*Fraction(1,2)
            elif q<0: out[N+(-q)]-=c*Fraction(1,2)
        s=vec[N+k]
        if s:
            # sin(k) sin(r) = [cos(k-r)-cos(k+r)]/2
            out[abs(k-r)]+=s*Fraction(1,2)
            b=k+r
            if b<=N: out[b]-=s*Fraction(1,2)
    return out

def rank(rows):
    if not rows: return 0
    A=[r[:] for r in rows]; m=len(A); n=len(A[0]); i=j=0
    while i<m and j<n:
        p=next((q for q in range(i,m) if A[q][j]),None)
        if p is None: j+=1; continue
        A[i],A[p]=A[p],A[i]
        z=A[i][j]; A[i]=[x/z for x in A[i]]
        for q in range(m):
            if q!=i and A[q][j]:
                z=A[q][j]; A[q]=[A[q][k]-z*A[i][k] for k in range(n)]
        i+=1; j+=1
    return i

def check(d,L):
    N=d*L
    PL=basis(L)
    rows=[]
    if d==1:
        # derivative multiplier 1
        for v in PL:
            w=[Fraction(0)]*(2*N+1)
            w[:L+1]=v[:L+1]
            for k in range(1,L+1): w[N+k]=v[L+k]
            rows.append(w)
    else:
        # embed P_L in P_N, then multiply by derivative multipliers
        emb=[]
        for v in PL:
            w=[Fraction(0)]*(2*N+1)
            w[:L+1]=v[:L+1]
            for k in range(1,L+1): w[N+k]=v[L+k]
            emb.append(w)
        rows += [mul_cos(v,L,N) for v in emb]
        rows += [mul_sin(v,L,N) for v in emb]
        for r in range(2,d): rows += [mul_cos(v,r*L,N) for v in emb]
    got=rank(rows); want=2*N+1
    assert got==want,(d,L,got,want)

for d in range(1,8):
    for L in range(1,6): check(d,L)
print('VERIFY_OK')
