from itertools import product
from fractions import Fraction

def trim(v):
    while v and v[-1]==0:v.pop()
    return v

def field(p,mod=None):
    if mod is None:
        d=1;q=p
        def dec(x):return [x]
    else:
        d=len(mod)-1;q=p**d
        def dec(x):
            o=[]
            for _ in range(d): o.append(x%p); x//=p
            return o
    def enc(v):
        v=list(v)+[0]*max(0,d-len(v));return sum((v[i]%p)*p**i for i in range(d))
    def add(a,b):return enc([(x+y)%p for x,y in zip(dec(a),dec(b))])
    def neg(a):return enc([(-x)%p for x in dec(a)])
    def mul(a,b):
        x=dec(a);y=dec(b);w=[0]*(2*d-1)
        for i in range(d):
            for j in range(d):w[i+j]=(w[i+j]+x[i]*y[j])%p
        if mod:
            for i in range(len(w)-1,d-1,-1):
                c=w[i]
                for j in range(d):w[i-d+j]=(w[i-d+j]-c*mod[j])%p
        return enc(w[:d])
    def inv(a):
        z=1
        for _ in range(q-2):z=mul(z,a)
        assert mul(z,a)==1
        return z
    return q,add,neg,mul,inv

def verify(p,mod,nmax):
    q,add,neg,mul,inv=field(p,mod)
    def polyrem(a,b):
        a=a[:];trim(a);b=b[:];trim(b)
        if not b:raise ZeroDivisionError()
        ib=inv(b[-1])
        while a and len(a)>=len(b):
            c=mul(a[-1],ib); shift=len(a)-len(b)
            for j,v in enumerate(b):a[j+shift]=add(a[j+shift],neg(mul(c,v)))
            trim(a)
        return a
    def is_squarefree(coeff):
        derivative=[mul(i%p,coeff[i]) for i in range(1,len(coeff))];trim(derivative)
        a=coeff[:];b=derivative
        while b:
            a,b=b,polyrem(a,b)
        return len(a)==1
    for n in range(2,nmax+1):
        cnt={(a,u):0 for a in range(1,q) for u in range(q)}
        for co in product(range(q),repeat=n):
            a=co[0]
            if a and is_squarefree(list(co)+[1]):
                u=mul(co[1],inv(a));cnt[a,u]+=1
        m=Fraction(sum(cnt.values()),len(cnt))
        SS=sum((v-m)**2 for v in cnt.values())
        expected=Fraction((q-3)*q**((n+1)//2)+q+1,q)
        print('p,mod,n,q',p,mod,n,q,'S=',SS,'expected=',expected,'mean=',m,'minmax=',(min(cnt.values()),max(cnt.values())))
        assert SS==expected
        if q==3:
            for (a,u),v in cnt.items():
                expect= ((3**n+3)//12 if (a==2 or u==0) else (3**n-9)//12) if n%2==0 else ((3**n+9)//12 if a==u else (3**n-3)//12)
                assert v==expect,(n,a,u,v,expect)

for args in [(3,None,7),(5,None,5),(7,None,4),(11,None,3),(3,[1,0,1],3)]:
    # GF9 irreducible x^2+1 over F3
    verify(*args)
print('VERIFY_OK cases=17')
