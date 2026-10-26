"""Exact finite-field check for harmonic four-subsets of five marked points."""
from itertools import product

def field(n):
    pol={1:[0,1],2:[1,0,1],3:[1,2,0,1]}[n]
    q=3**n
    def v(a):
        return [(a//3**i)%3 for i in range(n)]
    def enc(cs):
        return sum((z%3)*3**i for i,z in enumerate(cs))
    def add(a,b):
        return enc([(x+y)%3 for x,y in zip(v(a),v(b))])
    def mul(a,b):
        a,b=v(a),v(b)
        if n==1:return (a[0]*b[0])%3
        c=[0]*(2*n-1)
        for i,ai in enumerate(a):
            for j,bj in enumerate(b): c[i+j]=(c[i+j]+ai*bj)%3
        for deg in range(2*n-2,n-1,-1):
            z=c[deg]
            for j in range(n):c[deg-n+j]=(c[deg-n+j]-z*pol[j])%3
        return enc(c[:n])
    return q,add,mul

for n in (1,2,3):
    q,plus,times=field(n)
    zero=0; one=1; two=2
    count=[0,0,0,0,0,0]
    for a,b in product(range(q),repeat=2):
        if a in (zero,one) or b in (zero,one) or a==b:continue
        predicates=[a==two,b==two,plus(a,b)==zero,
            plus(plus(one,a),b)==zero,
            plus(plus(a,b),times(a,b))==zero]
        count[sum(predicates)]+=1
    assert count[0]==(q-3)*(q-7),(q,count)
    assert count[1]==5*(q-3),(q,count)
    assert all(c==0 for c in count[2:]),(q,count)
    print('q',q,'ordinary',count[0],'rank4',count[1],'rank<=3',sum(count[2:]))
