import sys
from functools import lru_cache
base=3
intern3={};intern2={};intern1={};intern0={}
def itab(tab, sig):
    if sig not in tab:tab[sig]=len(tab)
    return tab[sig]
def go(kind,n):
    N=2*n
    if kind=='P':
        def nbr(a,b):
            ia,ja=divmod(a,2);ib,jb=divmod(b,2)
            return int((ia==ib and ja!=jb) or (ja==jb and (ia-ib)%n in (1,n-1)))
        def canon2(b):
            i,j=divmod(b,2)
            return min(b, ((-i)%n)*2+j)
        def canon3(b,c):
            i,j=divmod(b,2);ii,jj=divmod(c,2)
            return min((b,c),(((-i)%n)*2+j,((-ii)%n)*2+jj))
    else:
        def nbr(a,b):
            d=(a-b)%N
            return int(d in (1,N-1,n))
        def canon2(b):return min(b,(-b)%N)
        def canon3(b,c):return min((b,c),((-b)%N,(-c)%N))
    E=[[nbr(a,b) for b in range(N)] for a in range(N)]
    def code4(v):
        a,b,c,d=v
        z=0;p=1
        for x,y in ((a,b),(a,c),(a,d),(b,c),(b,d),(c,d)):
            z+=(0 if x==y else 1 if E[x][y] else 2)*p;p*=3
        return z
    cache3={}
    def t3(b,c):
        bc=canon3(b,c)
        if bc in cache3:return cache3[bc]
        z=itab(intern3, tuple(sorted({code4((0,bc[0],bc[1],d)) for d in range(N)})))
        cache3[bc]=z
        return z
    cache2={}
    def t2(b):
        bc=canon2(b)
        if bc in cache2:return cache2[bc]
        z=itab(intern2,tuple(sorted({t3(bc,c) for c in range(N)})))
        cache2[bc]=z
        return z
    t1=itab(intern1,tuple(sorted({t2(b) for b in range(N)})))
    root=itab(intern0,(t1,))
    return root,len(cache3),len(intern3),len(intern2),len(intern1)

if __name__=='__main__':
 for n in range(3,int(sys.argv[1]) if len(sys.argv)>1 else 31):
    print(n,go('P',n),go('M',n),flush=True)
