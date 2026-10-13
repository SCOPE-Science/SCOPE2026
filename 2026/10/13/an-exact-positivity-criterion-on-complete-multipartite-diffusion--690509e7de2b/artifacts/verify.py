"""Exact rational checks of Padé positivity on complete multipartite graph Laplacians.

The infinite-family characterization is proved analytically in RESULT.md;
finite tests here are independent arithmetic stress tests, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product


def matrix_product(a,b):
    n=len(a); return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def matrix_inverse(a):
    n=len(a)
    m=[list(a[i])+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if m[i][j])
        m[j],m[pivot]=m[pivot],m[j]
        f=m[j][j]
        m[j]=[x/f for x in m[j]]
        for i in range(n):
            if i!=j:
                f=m[i][j]
                if f: m[i]=[x-f*y for x,y in zip(m[i],m[j])]
    return [line[n:] for line in m]

def r(s):
    return (s*s-6*s+12)/(s*s+6*s+12)

def phi(s):
    return 12/(s*s+6*s+12)

def part_data(parts):
    labels=[i for i,a in enumerate(parts) for _ in range(a)]
    n=len(labels)
    L=[[F(n-parts[labels[i]]) if i==j else (F(0) if labels[i]==labels[j] else F(-1)) for j in range(n)] for i in range(n)]
    return L,labels

def direct_pade(L,h):
    n=len(L)
    L2=matrix_product(L,L)
    I=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    P=[[12*I[i][j]-6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    D=[[12*I[i][j]+6*h*L[i][j]+h*h*L2[i][j] for j in range(n)] for i in range(n)]
    return matrix_product(P,matrix_inverse(D))

def projection_formula(parts,labels,h):
    n=len(labels); fN=r(n*h)
    return [[(F(1,n)+fN*((F(1,parts[labels[i]]) if labels[i]==labels[j] else F(0))-F(1,n)) +
             r((n-parts[labels[i]])*h)*((F(int(i==j))-F(1,parts[labels[i]])) if labels[i]==labels[j] else F(0)))
             for j in range(n)] for i in range(n)]

def compositions(n):
    for bits in product((False,True),repeat=n-1):
        p=[]; c=1
        for b in bits:
            if b: p.append(c);c=1
            else:c+=1
        p.append(c)
        if len(p)>=2:yield p


def verify():
    tested=0
    for n in range(2,9):
        for parts in compositions(n):
            L,labels=part_data(parts)
            for h in (F(1,19),F(1,2),F(2),F(17)):
                a=direct_pade(L,h)
                b=projection_formula(parts,labels,h)
                assert a==b,('spectral projection',parts,h)
                assert all(x>0 for row in a for x in row),('strict entrywise positivity',parts,h)
                assert all(sum(row)==1 for row in a),('row sums',parts,h)
                tested+=1
    for parts in ((1,16),(16,1),(8,8),(2,20,1),(3,4,5)):
        L,labels=part_data(parts)
        h=F(31)
        a=direct_pade(L,h)
        assert a==projection_formula(parts,labels,h)
        assert all(x>0 for row in a for x in row)
        tested+=1
    for s in [F(1,101),F(1),F(10),F(100),F(10000)]:
        assert 0<r(s)<1
    for s,t in [(F(1,17),F(17)),(F(1),F(3)),(F(13),F(57))]:
        assert s<t and phi(s)>phi(t)
    # Conditions 0 <= f <= 1 and decreasing phi are independent.
    bad=lambda s:F(1,1)/(1+s*s)
    testphi=lambda s:(1-bad(s))/s
    h=F(1,10)
    assert 0<bad(F(1,10))<1 and 0<bad(F(3,10))<1
    assert testphi(h)<testphi(3*h)
    within=h*(testphi(h)-testphi(3*h))/2
    assert within<0  # Same-part edge of K_{2,1}.
    cn=lambda s:(2-s)/(2+s)
    assert cn(F(10))<0
    assert (1+F(4)*cn(F(10)))/5<0 # Diagonal on K_5, h=2.
    assert r(F(1))!=r(F(100))
    print('VERIFY_OK',tested,'exact rational graph-step cases, spectral projections, row sums, strictly positive entries, sharp independent obstructions')

if __name__=='__main__': verify()
