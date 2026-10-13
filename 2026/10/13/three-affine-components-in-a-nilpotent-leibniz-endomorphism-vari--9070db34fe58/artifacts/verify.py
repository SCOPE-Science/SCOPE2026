"""Independent finite-field checks for the endomorphism variety of a rank-one Leibniz algebra.

Only Python standard library required. No finite experiment is used as a proof for all fields.
"""
from itertools import product


def mult(X,Y,p):
    return tuple(sum(X[3*i+k]*Y[3*k+j] for k in range(3)) % p for i in range(3) for j in range(3))

def actual_hom(X,p):
    # In the basis e1,e2,z: [e1,e1]=[e1,e2]=z, all other brackets 0.
    # Exact list of all bilinear homomorphism conditions.
    e1=(X[0],X[3],X[6]); e2=(X[1],X[4],X[7]); ez=(X[2],X[5],X[8]);
    def b(x,y): return (x[0]*(y[0]+y[1]))%p
    return (ez[0]==0 and ez[1]==0
            and b(e1,e1)==ez[2] and b(e1,e2)==ez[2]
            and b(e2,e1)==0 and b(e2,e2)==0
            and b(e1,ez)==0 and b(e2,ez)==0 and b(ez,e1)==0 and b(ez,e2)==0 and b(ez,ez)==0)

def component(X,p):
    a,b,h,c,d,j,u,v,t=X
    if h%p or j%p: return (False,False,False)
    C0 = b%p==0 and (d-a-c)%p==0 and (t-a*(a+c))%p==0
    C1 = a%p==0 and b%p==0 and t%p==0
    C2 = (a+c)%p==0 and (b+d)%p==0 and t%p==0
    return (C0,C1,C2)

def rank(X,p):
    if any(X[i]%p for i in range(9)) is False: return 0
    # Matrix rank by exhaustive minors (works in every characteristic).
    import itertools
    if X[0]*(X[4]*X[8]-X[5]*X[7])-X[1]*(X[3]*X[8]-X[5]*X[6])+X[2]*(X[3]*X[7]-X[4]*X[6]):
        if (X[0]*(X[4]*X[8]-X[5]*X[7])-X[1]*(X[3]*X[8]-X[5]*X[6])+X[2]*(X[3]*X[7]-X[4]*X[6]))%p:return 3
    for r1,r2 in itertools.combinations(range(3),2):
        for c1,c2 in itertools.combinations(range(3),2):
            if (X[3*r1+c1]*X[3*r2+c2]-X[3*r1+c2]*X[3*r2+c1])%p:return 2
    return 1

def is_nilpotent(X,p):
    y=mult(X,X,p)
    return all(v%p==0 for v in mult(y,X,p))

for q in (2,3,5):
    totals=[0,0,0,0]
    idem=nil=0
    n0=n1=n2=0
    if q==5:
        # Exact parametric census; q^9 brute comparison is done at q=2,3.
        matrices=set()
        for a,b,u,v in product(range(q),repeat=4):
            beta=b; alpha=a
            matrices.add(tuple(x%q for x in (alpha,0,0,beta-alpha,beta,0,u,v,alpha*beta)))
            matrices.add(tuple(x%q for x in (0,0,0,a,b,0,u,v,0)))
            matrices.add(tuple(x%q for x in (a,b,0,-a,-b,0,u,v,0)))
        iterator=matrices
    else:
        iterator=product(range(q),repeat=9)

    for X in iterator:
        C=component(X,q)
        rhs=any(C)
        if q in (2,3):
            lhs=actual_hom(X,q)
            assert lhs==rhs,(q,X,lhs,rhs)
        if not rhs: continue
        n0+=C[0];n1+=C[1];n2+=C[2]
        totals[rank(X,q)]+=1
        idem+=int(mult(X,X,q)==X)
        nil+=int(is_nilpotent(X,q))

    expected=(1,(q*q-1)*(2*q+1),2*(q*q-1)*(q*q-q),q*q*(q-1)**2)
    assert tuple(totals)==expected,(q,totals,expected)
    assert sum(totals)==3*q**4-2*q**3,(q,totals)
    assert idem==2*q*q+2,(q,idem)
    assert nil==q*q*(2*q-1),(q,nil)
    assert n0==n1==n2==q**4,(q,n0,n1,n2)
    print(f'q={q}: end={sum(totals)} ranks={totals} idempotents={idem} nilpotents={nil} components={[n0,n1,n2]}')

print('VERIFY_OK')
