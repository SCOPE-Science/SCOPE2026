"""Independent finite-field Lie generation verifier; standard library only."""
from itertools import product

def ops(q):
    if q != 4:
        return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q,lambda a:(-a)%q
    def mul(a,b):
        p=0
        for i in (0,1):
            if (b>>i)&1:p^=a<<i
        for i in (2,):
            if p&(1<<i):p^=0b111<<(i-2)
        return p
    return lambda a,b:a^b,mul,lambda a:a

def rank(vectors,q,add,mul,neg):
    basis=[]
    for v in vectors:
        a=list(v)
        for pivot,b in basis:
            if a[pivot]:
                t=a[pivot]
                a=[add(x,neg(mul(t,y))) for x,y in zip(a,b)]
        j=next((i for i,t in enumerate(a) if t),None)
        if j is not None:
            inv=next(t for t in range(1,q) if mul(a[j],t)==1)
            a=[mul(inv,t) for t in a]
            basis.append((j,a));basis.sort(key=lambda t:t[0])
    return len(basis)

def bracket(x,y,add,mul,neg):
    a,b,c=x; d,e,f=y
    two=add(1,1)
    return (add(mul(b,f),neg(mul(e,c))),mul(two,add(mul(a,e),neg(mul(d,b)))),mul(two,add(mul(c,d),neg(mul(f,a)))))

def generated(xs,q,add,mul,neg):
    vec=list(xs)
    r=rank(vec,q,add,mul,neg)
    if r==3:return True
    for a in xs:
        for b in xs:
            vec.append(bracket(a,b,add,mul,neg))
    return rank(vec,q,add,mul,neg)==3

def test(q,k):
    add,mul,neg=ops(q); z=(0,0,0);elements=list(product(range(q),repeat=3))
    squares={mul(a,a) for a in range(1,q)}
    tally={}
    for x in elements:
        if x==z: kind='zero'
        elif q%2==0:kind='central' if x[1]==x[2]==0 else 'noncentral'
        else:
            D=add(mul(x[0],x[0]),mul(x[1],x[2]))
            kind='nilpotent' if D==0 else ('split' if D in squares else 'nonsplit')
        if kind in ('zero','central'):
            expected=q**k*(q**k-1)*(q**k-q)
        elif kind in ('noncentral','nilpotent'):
            expected=q**(3*k)-q**(2*k)
        elif kind=='split':
            expected=q**(3*k)-2*q**(2*k)+q**k
        else:
            expected=q**(3*k)-q**k
        success=sum(generated((x,)+ys,q,add,mul,neg) for ys in product(elements,repeat=k))
        assert success==expected,(q,k,x,kind,success,expected)
        tally.setdefault(kind,[]).append(success)
    print('field',q,'k',k,'types:',{k:(len(v),v[0]) for k,v in tally.items()})

if __name__=='__main__':
 for q,k in [(2,1),(3,1),(4,1),(5,1),(7,1),(2,2),(3,2)]:test(q,k)
 print('VERIFY_OK')
