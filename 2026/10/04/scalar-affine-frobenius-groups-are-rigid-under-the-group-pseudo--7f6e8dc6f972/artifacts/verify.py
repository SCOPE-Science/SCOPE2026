from math import gcd

class FiniteField:
    # Elements are integers encoding polynomial coefficients base p.
    def __init__(self,p,f,mod):
        self.p=p
        self.f=f
        self.q=p**f
        self.mod=mod[:]  # low-to-high, monic degree f
        assert len(mod)==f+1 and mod[-1]%p==1
    def coeffs(self,a):
        out=[]
        for _ in range(self.f):
            out.append(a%self.p)
            a//=self.p
        return out
    def encode(self,c):
        x=0
        for a in reversed(c):
            x=x*self.p+(a%self.p)
        return x
    def add(self,a,b):
        A=self.coeffs(a); B=self.coeffs(b)
        return self.encode([(x+y)%self.p for x,y in zip(A,B)])
    def neg(self,a):
        return self.encode([(-x)%self.p for x in self.coeffs(a)])
    def mul(self,a,b):
        A=self.coeffs(a); B=self.coeffs(b)
        t=[0]*(2*self.f-1)
        for i,x in enumerate(A):
            for j,y in enumerate(B):
                t[i+j]=(t[i+j]+x*y)%self.p
        for k in range(len(t)-1,self.f-1,-1):
            c=t[k]%self.p
            if c:
                for j in range(self.f):
                    t[k-self.f+j]=(t[k-self.f+j]-c*self.mod[j])%self.p
        return self.encode(t[:self.f])
    def pow(self,a,n):
        r=1
        while n:
            if n&1:
                r=self.mul(r,a)
            a=self.mul(a,a)
            n//=2
        return r
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)
    def trace(self,a):
        s=0
        x=a
        for _ in range(self.f):
            s=self.add(s,x)
            x=self.pow(x,self.p)
        c=self.coeffs(s)
        assert all(v==0 for v in c[1:])
        return c[0]%self.p
    def order(self,a):
        assert a
        x=1
        for n in range(1,self.q):
            x=self.mul(x,a)
            if x==1:
                return n
        raise AssertionError
    def primitive(self):
        for a in range(2,self.q):
            if self.order(a)==self.q-1:
                return a
        if self.q==2:
            return 1
        raise AssertionError

def ord_mod(p,m):
    x=1
    for e in range(1,m+1):
        x=x*p%m
        if x==1:
            return e
    raise AssertionError

def rank_mod_p(rows,p):
    A=[row[:] for row in rows]
    if not A:
        return 0
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]%p),None)
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(inv*x)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                z=A[i][c]%p
                A[i]=[(A[i][j]-z*A[r][j])%p for j in range(n)]
        r+=1
    return r

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

def phi(n):
    return sum(gcd(k,n)==1 for k in range(1,n+1))

def check(F,m):
    p,f,q=F.p,F.f,F.q
    assert (q-1)%m==0 and m>1
    g=F.primitive()
    hgen=F.pow(g,(q-1)//m)
    H=[]
    x=1
    for _ in range(m):
        H.append(x)
        x=F.mul(x,hgen)
    assert x==1 and len(set(H))==m
    assert F.order(hgen)==m

    e=ord_mod(p,m)
    assert f%e==0
    nonlinear_kernel_size=p**(f-e)

    # Verify every additive-character parameter.
    for a in range(1,q):
        span_rows=[F.coeffs(F.mul(a,h)) for h in H]
        assert rank_mod_p(span_rows,p)==e
        ker=[]
        for x in range(q):
            if all(F.trace(F.mul(F.mul(a,h),x))==0 for h in H):
                ker.append(x)
        assert len(ker)==nonlinear_kernel_size

    pseudo={d:phi(d) for d in divisors(m)}
    nonlinear=p**e
    assert nonlinear>m
    assert nonlinear not in pseudo
    pseudo[nonlinear]=(q-1)//m

    codes=sorted(pseudo)
    recovered_pe=codes[-1]
    recovered_m=codes[-2]
    recovered_q=1+recovered_m*pseudo[recovered_pe]
    assert recovered_pe==nonlinear
    assert recovered_m==m
    assert recovered_q==q

    print({
        "q":q,
        "m":m,
        "e":e,
        "nonlinear_codegree":nonlinear,
        "nonlinear_multiplicity":(q-1)//m,
        "pseudo":sorted(pseudo.items()),
    })

fields = {
    7: FiniteField(7,1,[0,1]),
    8: FiniteField(2,3,[1,1,0,1]),       # x^3+x+1
    9: FiniteField(3,2,[1,0,1]),         # x^2+1
    16: FiniteField(2,4,[1,1,0,0,1]),    # x^4+x+1
}
for q,m in [(7,3),(8,7),(9,4),(16,3),(16,5),(16,15)]:
    check(fields[q],m)

print("VERIFY_OK")
