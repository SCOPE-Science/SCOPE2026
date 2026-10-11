"""Exact coefficient identities for the real 8-atom mean reflection.

Uses only Python's standard library.  The general all-dimension reduction
uses the published half-degree principle and is proved in RESULT.md; this
program checks exact finite polynomial identities, not infinite theorems.
"""
from fractions import Fraction
from decimal import Decimal, localcontext


def trim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q


def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])


def neg(a):
    return [-z for z in a]


def sub(a,b):
    return add(a,neg(b))


def mul(a,b):
    o=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):o[i+j]+=x*y
    return trim(o)


def scale(a,s):
    return trim([x*s for x in a])


def power(a,k):
    p=[1]
    for _ in range(k):p=mul(p,a)
    return p


def der(a):
    return trim([i*a[i] for i in range(1,len(a))]) if len(a)>1 else [0]


def evaluate(p,t):
    o=0
    for x in reversed(p):o=o*t+x
    return o


def raw(n,k):
    l=n-k
    u=add(scale(power([-2*l,n-2*k],4),k),scale(power([2*k-n,-2*k],4),l))
    v=[l,0,0,0,k]
    return u,v

# Verify the compact all-n derivative factorization at numerous dimension/count
# pairs as a diagnostic; its coefficient expansion is also given in RESULT.md.
for n in range(3,40):
    for k in range(1,(n-1)//2+1):
        u,v=raw(n,k)
        q=[(n-k)*(3*n-4*k),4*k*(n-k),0,4*k*(n-k),k*(4*k-n)]
        expected=scale(mul(power([-1,1],2),q),-8*k*n*(k-n)*(2*k-n))
        assert sub(mul(der(u),v),mul(u,der(v)))==expected,(n,k)

v1=[7,0,0,0,1]
n1=[371,-420,378,-84,11]
assert raw(8,1)[0]==scale(n1,128)
assert raw(8,1)[1]==v1
q=[-35,-7,0,-7,1]
assert sub(mul(der(n1),v1),mul(n1,der(v1)))==scale(mul(power([-1,1],2),q),84)

v2=[3,0,0,0,1]
n2=[21,-24,18,0,1]
assert raw(8,2)[0]==scale(n2,2048)
assert raw(4,1)[0]==scale(n2,64)
assert raw(4,1)[1]==v2
assert sub(scale(v2,16),n2)==scale(mul(power([1,1],2),[9,-10,5]),3)

v3=[5,0,0,0,3]
n3=[235,-180,90,60,51]
assert raw(8,3)[0]==scale(n3,128)
assert sub(scale(v3,128),n3)==[405,180,-90,-60,333]
assert raw(8,4)[0]==scale(raw(8,4)[1],8**4)

left=Fraction(-1435479,1000000)
right=Fraction(-1435477,1000000)
assert evaluate(q,left)>0 and evaluate(q,right)<0
# q(-u)=u**4+7*u**3+7*u-35 is strictly increasing for u>0;
# Descartes' rule gives one positive root, so this brackets the sole
# negative root and the unique global maximum of the k=1 rational branch.
with localcontext() as ctx:
    ctx.prec=45
    a,b=Decimal(str(float(left))),Decimal(str(float(right)))
    for i in range(170):
        mid=(a+b)/2
        if evaluate(q,mid)>0:a=mid
        else:b=mid
    root=(a+b)/2
    fourth=(evaluate(n1,root)/(Decimal(32)*evaluate(v1,root)))
    norm=fourth.sqrt().sqrt()
    assert Decimal('1.54452109')<norm<Decimal('1.54452110')
    print('NEGATIVE_ROOT',root)
    print('EIGHT_ATOM_FOURTH_POWER',fourth)
    print('EIGHT_ATOM_NORM',norm)
print('EXACT_IDENTITIES_OK')
