from math import factorial, comb
from collections import Counter
import itertools

def partitions_of_n(n, max_part=None):
    if n==0:
        yield []
        return
    if max_part is None: max_part=n
    for f in range(min(max_part,n),0,-1):
        for rest in partitions_of_n(n-f, f):
            yield [f]+rest

def class_size(n, part):
    c=Counter(part)
    denom=1
    for l,m in c.items():
        denom*= (l**m)*factorial(m)
    return factorial(n)//denom

def stat(part,n):
    c=Counter(part)
    m1=c.get(1,0); m2=c.get(2,0); m3=c.get(3,0); m4=c.get(4,0)
    return m1,m2,m3,m4,c

def chi_W(part,n):
    f,m2,_,_,_=stat(part,n)
    a=f-1; b=(f+2*m2)-1
    return (a*a-b)//2

def chi_G(part,n):
    f,m2,_,_,_=stat(part,n)
    return f*(f-1)//2+m2

def chi_G_g2(part,n):
    # chi_G(g^2): C(f2,2)+m2' where f2=fix(g^2)=f+2m2, m2'= #2-cycles in g^2 = 2*m4
    f,m2,m3,m4,_=stat(part,n)
    f2=f+2*m2
    return f2*(f2-1)//2+2*m4

def chi_L2G_free(part,n):
    g=chi_G(part,n); g2=chi_G_g2(part,n)
    return (g*g-g2)//2

def chi_H2(part,n):
    f,_,_,_,_=stat(part,n)
    return 2*f

def chi_H4(part,n):
    f,m2,_,_,_=stat(part,n)
    return f + 2*(f*(f-1)//2+m2) + f*(f-1)

def chi_H6base(part,n):
    f,m2,m3,_,_=stat(part,n)
    return 2*f*(f-1) + 8*(f*(f-1)*(f-2)//6) + 4*m2*f + 2*m3

def inner(c1,c2,n):
    tot=0
    for part in partitions_of_n(n):
        tot+= class_size(n,part)*c1(part,n)*c2(part,n)
    return tot//factorial(n)

print("n invW invG_W invL2Gfree_W invH2_W invH4_W invH6base_W")
for n in range(2,11):
    print(f"{n} {inner(chi_W,chi_W,n)} {inner(chi_G,chi_W,n)} {inner(chi_L2G_free,chi_W,n)} {inner(chi_H2,chi_W,n)} {inner(chi_H4,chi_W,n)} {inner(chi_H6base,chi_W,n)}")
