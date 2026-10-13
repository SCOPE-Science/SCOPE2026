"""Standalone checks for Hermitian-relative point-count formulas.

Requires only Python 3. Exhaustive base- and quadratic-extension counts for
s=2 and s=3; they are checks, not the proof for arbitrary prime powers.
"""

def field(p, coefficients):
    k = len(coefficients)-1
    q = p**k
    coeffs = tuple(coefficients)
    def digits(a):
        return [(a//(p**i))%p for i in range(k)]
    def encode(a):
        return sum(int(v%p)*p**i for i,v in enumerate(a))
    def add(a,b):
        x,y=digits(a),digits(b)
        return encode([(v+w)%p for v,w in zip(x,y)])
    def neg(a): return encode([(-v)%p for v in digits(a)])
    def mul(a,b):
        x,y=digits(a),digits(b)
        t=[0]*(2*k-1)
        for i in range(k):
            for j in range(k): t[i+j]=(t[i+j]+x[i]*y[j])%p
        for m in range(2*k-2,k-1,-1):
            lead=t[m]
            for j in range(k): t[m-k+j]=(t[m-k+j]-lead*coeffs[j])%p
        return encode(t[:k])
    def powf(a,n):
        out=1
        while n:
            if n&1:out=mul(out,a)
            a=mul(a,a)
            n//=2
        return out
    return q,add,neg,mul,powf

cases=[(2,1,[1,1,1]),(2,2,[1,1,0,0,1]),(3,1,[1,0,1]),(3,2,[2,1,0,0,1])]
for s,n,poly in cases:
    p=2 if s==2 else 3
    Q,add,neg,mul,powf=field(p,poly)
    q=s*s
    assert Q==q**n
    eta=next(v for v in range(Q) if powf(v,q)==v and powf(v,s)!=v)
    trace_counts={}
    for z in range(Q):
        tr=add(powf(z,s),z)
        trace_counts[tr]=trace_counts.get(tr,0)+1
    N=1
    for x in range(Q):
        target=neg(add(powf(x,s+1),eta))
        N+=trace_counts.get(target,0)
    predicted=q**n+1 + (s*(-s)**n if n%p else -s*(s-1)*(-s)**n)
    assert N==predicted, (s,n,N,predicted)
    print('s=%d n=%d N=%d: OK'%(s,n,N))
for s,p in [(2,2),(3,3),(4,2),(5,5),(8,2),(9,3)]:
    a=s*s//p
    b=a-s
    assert b>=0 and (p-1)*a+b==s*(s-1)
    for n in range(1,2*p+1):
        full_trace=(-s)**n*(b+(a*(p-1) if n%p==0 else -a))
        target=(-s)**n*(s*(s-1) if n%p==0 else -s)
        assert full_trace==target
print('HERMITIAN_RELATIVE_ZETA_CHECK_OK')
