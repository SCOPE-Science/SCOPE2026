from fractions import Fraction
from math import factorial
from decimal import Decimal, localcontext

def involutions(n):
    def rec(left,partial):
        if not left:
            yield tuple(partial); return
        i=left[0]
        partial[i]=i
        yield from rec(left[1:],partial)
        for j in left[1:]:
            partial[i]=j;partial[j]=i
            yield from rec([k for k in left[1:] if k!=j],partial)
            partial[j]=-1
        partial[i]=-1
    yield from rec(list(range(n)),[-1]*n)

def classify(a,b):
    n=len(a); seen=set(); types=[0]*5
    for x in range(n):
        if x in seen:continue
        orb={x,a[x],b[x],a[b[x]]}
        assert all({a[y],b[y]}<=orb for y in orb)
        seen.update(orb)
        if len(orb)==1: types[0]+=1
        elif len(orb)==4:types[4]+=1
        else:
            assert len(orb)==2
            if all(a[y]==y for y in orb):types[1]+=1
            elif all(b[y]==y for y in orb):types[2]+=1
            else:
                assert all(a[y]==b[y] for y in orb)
                types[3]+=1
    return tuple(types)

def recurrence(N):
    a=[Fraction(0)]*(N+1);b=[Fraction(0)]*(N+1)
    a[0]=b[0]=Fraction(1)
    for n in range(1,N+1):
        a[n]=((a[n-1] if n>=1 else 0)+(3*a[n-2] if n>=2 else 0)+(a[n-4] if n>=4 else 0))/n
        b[n]=((3*b[n-2] if n>=2 else 0)+(b[n-4] if n>=4 else 0))/n
    return a,b

a,b=recurrence(8)
for n in range(1,8):
    inv=list(involutions(n));count=0;no_common=0
    types_seen=set();one=[0]*5
    for x in inv:
        for y in inv:
            if all(x[y[i]]==y[x[i]] for i in range(n)):
                count+=1
                tp=classify(x,y)
                types_seen.add(tp)
                one=[m+int(t>0) for m,t in zip(one,tp)]
                if tp[0]==0:no_common+=1
    assert count==factorial(n)*a[n],(n,count,factorial(n)*a[n])
    assert no_common==factorial(n)*b[n]
    print('EXACT',n,len(inv),count,no_common,'types',len(types_seen),'active',one)

# All high-precision calculations below use Python's standard-library decimal.
with localcontext() as ctx:
    ctx.prec=65
    D=Decimal
    for n in [40,100,200,400,800,1600]:
        r=D(n).sqrt().sqrt()
        for _ in range(20):
            f=r+3*r*r+r**4-D(n)
            r-=f/(1+6*r+4*r**3)
        assert abs(r+3*r*r+r**4-D(n)) < D('1e-50')
        p=[D(0)]*(n+1);q=[D(0)]*(n+1)
        p[0]=(-r-D('1.5')*r*r-r**4/4).exp()
        q[0]=(-D('1.5')*r*r-r**4/4).exp()
        for k in range(1,n+1):
            p[k]=(r*p[k-1]+(3*r*r*p[k-2] if k>=2 else D(0))+(r**4*p[k-4] if k>=4 else D(0)))/k
            q[k]=((3*r*r*q[k-2] if k>=2 else D(0))+(r**4*q[k-4] if k>=4 else D(0)))/k
        nofixed=(-r).exp()*q[n]/p[n]
        rel=nofixed/(2*(-r).exp())
        assert D('0.90')<rel<1
        print('ASYM',n,'r',float(r),'ratio',float(rel),'nofixed',float(nofixed),'pcentral',float(p[n]))
print('COMMUTING_ACTION_CHECK_OK')
