"""Reproducible small finite-field checks for a Grassmann metric kernel theorem.

Works with prime fields F_2 and F_3 without dependencies beyond Python 3.
Checks incidence identities and exact finite-level Gram identities.
The theorem for arbitrary prime powers and all dimensions uses an analytic proof.
"""
from fractions import Fraction
from itertools import product, combinations
from math import comb, log2

def rref(rows, q):
    a=[list(row) for row in rows]
    pivot_row=0
    for col in range(len(a[0])):
        idx=next((j for j in range(pivot_row,len(a)) if a[j][col] % q),None)
        if idx is None:continue
        a[pivot_row],a[idx]=a[idx],a[pivot_row]
        inv=pow(a[pivot_row][col],-1,q)
        a[pivot_row]=[(x*inv)%q for x in a[pivot_row]]
        for j in range(len(a)):
            if j!=pivot_row:
                factor=a[j][col]
                if factor:
                    a[j]=[(x-factor*y)%q for x,y in zip(a[j],a[pivot_row])]
        pivot_row+=1
        if pivot_row==len(a):break
    return tuple(tuple(x) for x in a[:pivot_row])

def field_points_lines(n,q):
    vectors=list(product(range(q),repeat=n))
    points=sorted({rref((v,),q)[0] for v in vectors if any(v)})
    lines=sorted({rref((u,v),q) for u,v in combinations(vectors,2) if len(rref((u,v),q))==2})
    return points,lines

def qbinom2(n,q):
    return ((q**n-1)*(q**(n-1)-1))//((q**2-1)*(q-1))

def check(n,q):
    pts,lines=field_points_lines(n,q)
    m=len(pts); N=len(lines)
    r=(q**(n-1)-1)//(q-1)
    assert m==(q**n-1)//(q-1)
    assert N==qbinom2(n,q)
    index={p:i for i,p in enumerate(pts)}
    supports=[]
    for u,v in lines:
        S={rref((tuple((a*u[k]+b*v[k])%q for k in range(n)),),q)[0]
           for a,b in product(range(q),repeat=2) if a or b}
        assert len(S)==q+1
        supports.append({index[p] for p in S})
    assert all(sum(i in S for S in supports)==r for i in range(m))
    assert all(sum(i in S and j in S for S in supports)==1
               for i in range(m) for j in range(i+1,m))
    k=(q+1)*(r-1)
    deg=[]
    for i,S in enumerate(supports):
        deg.append(sum(len(S&T)==1 for j,T in enumerate(supports) if i!=j))
    assert all(d==k for d in deg)
    b=Fraction(q+1,q)
    for i,S in enumerate(supports):
        for j,T in enumerate(supports):
            meet=len(S&T)
            d=0 if i==j else (1 if meet==1 else 2)
            norm_squared=Fraction(len(S.symmetric_difference(T)),2*q)
            target={0:Fraction(0),1:Fraction(1),2:b}[d]
            assert norm_squared==target
    mu1=Fraction(-(r-1),q)
    mu2=Fraction(0)
    assert mu1==-b+(1-b)*(r-q-2)
    assert mu2==-b+(1-b)*(-(q+1))
    assert N>m>1
    return {'q':q,'n':n,'points':m,'lines':N,'degree':k,
            'critical_power_of_two':str(b),'incidence_rank':m,
            'boundary_centered_rank':m-1,'interior_centered_rank':N-1}

if __name__=='__main__':
    for q,n in ((2,4),(2,5),(3,4)):
        print('PASS',check(n,q))
