# Exact GF(2)[y] verifier for the special Collatz family in Conjecture 3.1.

def deg(p):
    return p.bit_length() - 1

def pmul(a,b):
    r=0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
    return r

def pdivmod(a,b):
    db=deg(b); q=0
    while a and deg(a) >= db:
        s=deg(a)-db
        q ^= 1 << s
        a ^= b << s
    return q,a

def vfac(p,fac):
    k=0
    while p:
        q,r=pdivmod(p,fac)
        if r:
            return k
        p=q; k+=1
    raise AssertionError('valuation of zero')

Z = 0b11  # y+1
Y = 0b10  # y

def B(n):
    q = n & -n
    p = (1 << n) ^ 1  # y^n+1 over F2
    for _ in range(q):
        p,r = pdivmod(p,Z)
        assert r == 0
    return p

def T(f):
    num = 1 ^ pmul(Y,f)
    v = vfac(num,Z)
    for _ in range(v):
        num,r = pdivmod(num,Z)
        assert r == 0
    return num,v

def block_t(n):
    q=n & -n
    u=n//q
    if u == 1:
        return 0
    k=(u-1) & -(u-1)
    return q*(k-1)

checked_starts=0
checked_steps=0
max_r=8
for r in range(1,max_r+1):
    top=1<<r
    lo=(1<<(r-1))+1
    for n in range(lo,top+1):
        f=B(n)
        expected_len=top-n+1
        got_len=1
        m=n
        while f != 1:
            t=block_t(m)
            assert t > 0
            f0=f
            vals=[]
            for s in range(t):
                f,v=T(f)
                vals.append(v)
                got_len += 1
                checked_steps += 1
            assert f == B(m+t), (r,n,m,t)
            if t > 1:
                assert vals[:-1] == [1]*(t-1), (r,n,m,t,vals)
            m += t
            assert m <= top
        assert m == top
        assert got_len == expected_len, (r,n,got_len,expected_len)
        checked_starts += 1
print(f'VERIFY_OK r=1..{max_r} starts={checked_starts} odd_steps={checked_steps} block_identity=exact length_formula=exact')
