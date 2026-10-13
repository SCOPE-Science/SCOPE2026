"""Exhaustive finite-field verification for bilinear short local algebras.

For each nonzero symmetric B, enumerate every similitude and compute
orbits on the radical J=V+S. The scalar summand is fixed, so its q
copies of these radical orbits give the full element-orbit count.
"""
from itertools import product


def field(q):
    if q == 4:
        def plus(a,b): return a^b
        def times(a,b):
            z=0
            for i in range(2):
                for j in range(2):
                    if ((a>>i)&1) and ((b>>j)&1): z ^= 1<<(i+j)
            if z & 8: z ^= (8|4|2)   # t^3=t^2+t=t+1+t=1
            if z & 4: z ^= (4|2|1)   # t^2=t+1
            return z
        char=2
    else:
        plus=lambda a,b:(a+b)%q
        times=lambda a,b:(a*b)%q
        char=q
    neg=lambda a:next(b for b in range(q) if plus(a,b)==0)
    inv=lambda a:next(b for b in range(1,q) if times(a,b)==1)
    return plus,times,neg,inv,char


def verify(q):
    add,mul,neg,inv,p=field(q)
    vec=list(product(range(q),repeat=2))
    mats=[]
    for a,b,c,d in product(range(q),repeat=4):
        if add(mul(a,d),neg(mul(b,c)))!=0: mats.append((a,b,c,d))
    zero=(0,0)
    reports={}
    for u,v,w in product(range(q),repeat=3):
        if (u,v,w)==(0,0,0): continue
        B=(u,v,v,w)
        mult=[]
        for a,b,c,d in mats:
            # columns g(e1)=(a,c), g(e2)=(b,d)
            def bil(x,y):
                return add(add(mul(u,mul(x[0],y[0])),mul(v,add(mul(x[0],y[1]),mul(x[1],y[0])))),mul(w,mul(x[1],y[1])))
            p11=bil((a,c),(a,c));p12=bil((a,c),(b,d));p22=bil((b,d),(b,d))
            base=next(t for t in (u,v,w) if t)
            formed=next(s for s,t in ((p11,u),(p12,v),(p22,w)) if t)
            k=mul(formed,inv(base))
            if k and (p11,p12,p22)==tuple(mul(k,t) for t in (u,v,w)):
                mult.append(((a,b,c,d),k))
        # union find all q^3 radical vectors, independently forming full group orbits
        n=q*q*q
        parent=list(range(n))
        def find(i):
            while parent[i]!=i:
                parent[i]=parent[parent[i]]
                i=parent[i]
            return i
        def merge(i,j):
            i=find(i);j=find(j)
            if i!=j:parent[j]=i
        def idx(x,y,s):return (x*q+y)*q+s
        for x,y in vec:
            if (x,y)!=zero:
                for s in range(q):merge(idx(x,y,0),idx(x,y,s))
        for (a,b,c,d),k in mult:
            for x,y in vec:
                xx=add(mul(a,x),mul(b,y));yy=add(mul(c,x),mul(d,y))
                merge(idx(x,y,0),idx(xx,yy,0))
            for s in range(q):merge(idx(0,0,s),idx(0,0,mul(k,s)))
        from collections import Counter
        sizes=sorted(Counter(find(i) for i in range(n)).values())
        result=len(sizes)
        determinant=add(mul(u,w),neg(mul(v,v)))
        if determinant==0:
            shape='rank1'; expected=5 if p!=2 else 4
        elif p==2:
            shape='alternating' if u==0 and w==0 else 'nonalternating'
            expected=3 if shape=='alternating' else 4
        else:
            isotropic=any((x,y)!=zero and add(add(mul(u,mul(x,x)),mul(2%q,mul(v,mul(x,y)))),mul(w,mul(y,y)))==0 for x,y in vec)
            shape='split' if isotropic else 'anisotropic'
            expected=4 if isotropic else 3
        if shape=='rank1':
            want=[1,q*(q-1),q*q*(q-1)]+([(q-1)//2]*2 if p!=2 else [q-1])
        elif shape=='split':
            want=[1,q-1,2*q*(q-1),q*(q-1)**2]
        elif shape in ('anisotropic','alternating'):
            want=[1,q-1,q*(q*q-1)]
        elif shape=='nonalternating':
            want=[1,q-1,q*(q-1),q*q*(q-1)]
        else: raise AssertionError(shape)
        assert sizes==sorted(want),(q,B,shape,sizes,sorted(want))
        assert result==expected,(q,B,shape,result,expected)
        reports[shape]=reports.get(shape,0)+1
    assert sum(reports.values())==q**3-1
    print(f'q={q}: checked {sum(reports.values())} symmetric products, all radical-orbit predictions verified; classes {reports}')


if __name__=='__main__':
    for q in (2,3,4,5):verify(q)
    print('VERIFY_OK')
