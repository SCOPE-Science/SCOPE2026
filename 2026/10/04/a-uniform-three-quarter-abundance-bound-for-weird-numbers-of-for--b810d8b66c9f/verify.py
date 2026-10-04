from math import isqrt

def isprime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def weird_exact(k,p,q):
    M=(1<<(k+1))-1
    a=M+M*p+M*q-p*q
    if not (a>M and M<p<2*M and p<q): return False
    # Iannucci's criterion pq != r+s p+t q, 1<=r,s,t<=M.
    # With u=M-s,v=M-t this is equivalent to absence of
    # a-M+1 <= u p+v q <= a, 0<=u,v<=M-1.
    for v in range(min(M-1,a//q)+1):
        b=a-v*q
        u=b//p
        if u <= M-1 and b-u*p <= M-1:
            return False
    return True

expected=[1,1,5,3,10,23,29,53]
counts=[]
checked=0
worst=(0,None)
for k in range(1,9):
    M=(1<<(k+1))-1
    c=0
    for p in range(M+2,2*M,2):
        if not isprime(p): continue
        x=p-M
        # abundance a>M gives xy < M^2, so y < M^2/x; q=M+y.
        maxy=(M*M-1)//x
        for y in range(x+2,maxy+1,2):
            q=M+y
            if not isprime(q): continue
            checked += 1
            if weird_exact(k,p,q):
                c+=1
                a=M*(M+1)-x*y
                assert 4*a < 3*M*M+4*M, (k,p,q,a,M)
                ratio=a/(M*M)
                if ratio>worst[0]: worst=(ratio,(k,p,q,a,M))
    counts.append(c)
assert counts==expected,(counts,expected)
print('VERIFY_OK counts='+repr(counts)+' prime_pairs_checked='+str(checked)+' max_a_over_M2='+str(worst))
