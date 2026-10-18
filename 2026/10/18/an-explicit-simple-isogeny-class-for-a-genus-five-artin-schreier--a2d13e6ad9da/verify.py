"""Exact finite-field verification of a genus-five Artin--Schreier zeta numerator.

Requires Python 3.9+ standard library only. No network, package, or external data.
"""

MODULI = {1:(1,), 2:(1,0), 3:(1,2,0), 4:(2,1,0,0), 5:(1,2,0,0,0)}


def trim(a):
    a=list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def divrem(a, b, p):
    a=trim([v % p for v in a]); b=trim([v % p for v in b])
    assert b
    q=[0]*max(1, len(a)-len(b)+1)
    while a and len(a)>=len(b):
        d=len(a)-len(b)
        c=a[-1]*pow(b[-1],-1,p)%p
        q[d]=c
        for j in range(len(b)):
            a[j+d]=(a[j+d]-c*b[j])%p
        a=trim(a)
    return trim(q),a


def is_irreducible(f, p):
    # Trial division by every monic polynomial of degree at most floor(deg/2).
    degree=len(f)-1
    for d in range(1,degree//2+1):
        for t in range(p**d):
            x=t; coeff=[]
            for _ in range(d):
                coeff.append(x%p); x//=p
            if not divrem(f,coeff+[1],p)[1]:
                return False
    return True


class GF:
    def __init__(self,n):
        self.n=n; self.q=3**n; self.poly=MODULI[n]
        assert is_irreducible(list(self.poly)+[1],3)
        self.digits=[self.to_tuple(i) for i in range(self.q)]
        self.addtable=[];self.multable=[]
        for a in range(self.q):
            self.addtable.append([self.to_int(tuple((u+v)%3 for u,v in zip(self.digits[a],self.digits[b]))) for b in range(self.q)])
            self.multable.append([self.mulslow(a,b) for b in range(self.q)])

    def to_tuple(self,i):
        v=[]
        for _ in range(self.n): v.append(i%3); i//=3
        return tuple(v)

    def to_int(self,a):
        return sum(v*3**i for i,v in enumerate(a))

    def mulslow(self,a,b):
        n=self.n; f=self.poly; v=[0]*(2*n-1)
        for i,u in enumerate(self.digits[a]):
            for j,w in enumerate(self.digits[b]): v[i+j]=(v[i+j]+u*w)%3
        for k in range(2*n-2,n-1,-1):
            c=v[k]
            for j in range(n): v[k-n+j]=(v[k-n+j]-c*f[j])%3
        return self.to_int(v[:n])

    def add(self,a,b): return self.addtable[a][b]
    def neg(self,a): return self.mul(a,2)
    def sub(self,a,b): return self.add(a,self.neg(b))
    def mul(self,a,b): return self.multable[a][b]
    def pow(self,a,n):
        r=1
        while n:
            if n&1: r=self.mul(r,a)
            a=self.mul(a,a); n//=2
        return r
    def inv(self,a):
        assert a
        return self.pow(a,self.q-2)
    def trace(self,a):
        v=a;tr=0
        for _ in range(self.n):
            tr=self.add(tr,v);v=self.pow(v,3)
        assert tr in (0,1,2)
        return tr


def count(n):
    F=GF(n); hist=[0,0,0]; direct=3; roots=[0]*F.q
    for y in range(F.q):
        roots[F.sub(F.pow(y,3),y)]+=1
    assert set(roots)=={0,3}
    for a in range(F.q):
        if a in (0,1): continue
        f=F.add(F.pow(a,2),a)
        f=F.add(f,F.inv(a))
        f=F.add(f,F.inv(F.sub(a,1)))
        t=F.trace(f); hist[t]+=1; direct+=roots[f]
        assert (roots[f]==3)==(t==0)
    assert sum(hist)==F.q-2
    return 3+3*hist[0], direct, hist


def polynomial_certificate(P):
    p=5
    monic=[int(a*pow(P[-1],-1,p))%p for a in P]
    assert monic[-1]==1
    def add(a,b,sign=1):
        return trim([( (a[i] if i<len(a) else 0)+sign*(b[i] if i<len(b) else 0))%p
                     for i in range(max(len(a),len(b)))])
    def mulmod(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,u in enumerate(a):
            for j,v in enumerate(b): c[i+j]=(c[i+j]+u*v)%p
        return divrem(c,monic,p)[1]
    def powmod(a,n):
        out=[1]
        while n:
            if n&1: out=mulmod(out,a)
            a=mulmod(a,a);n//=2
        return out
    def gcd(a,b):
        while b:
            a,b=b,divrem(a,b,p)[1]
        return [x*pow(a[-1],-1,p)%p for x in a]
    f=[0,1]
    for j in range(1,11):
        f=powmod(f,5)
        if j in (2,5):
            assert gcd(monic,add(f,[0,1],-1))==[1]
        if j==10:
            assert f==[0,1]
    return monic


def main():
    expected=[6,18,24,66,291]
    hist_expected=[[1,0,0],[5,2,0],[7,15,3],[21,28,30],[96,90,55]]
    for m in range(1,6):
        N,direct,hist=count(m)
        assert (N,direct,hist)==(expected[m-1],expected[m-1],hist_expected[m-1])
        print(f'm={m} N={N} trace_hist={hist} direct={direct}')
    S=[0]+[3**m+1-expected[m-1] for m in range(1,6)]
    a=[1]
    for k in range(1,6):
        s=sum(a[k-j]*S[j] for j in range(1,k+1))
        assert s%k==0
        a.append(-s//k)
    assert a==[1,2,6,8,10,15]
    # Functional equation for the reciprocal Frobenius polynomial of a genus-five curve.
    for k in range(6,11):
        a.append(3**(k-5)*a[10-k])
    assert a==[1,2,6,8,10,15,30,72,162,162,243]
    assert sum(a)==711==9*79
    monic=polynomial_certificate(a)
    assert monic==[2,4,2,1,0,0,0,4,4,4,1]
    print('VERIFY_OK points='+str(expected)+' numerator='+str(a)+' jacobian_order=711 irreducible_mod_5=True')

if __name__=='__main__':
    main()
