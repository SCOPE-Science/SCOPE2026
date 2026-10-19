"""Independent rational edge/certificate checks for weighted two-clique bottleneck theorem.

Requires Python 3 and SymPy. General validity is proved in RESULT.md;
these finite checks test exact identities, the critical inequality and strict directions.
"""
import sympy as S

checks=0

def verify(condition, label):
    global checks
    assert condition, label
    checks += 1


def parameters(p,q,B=S.Rational(1)):
    p,q=S.Integer(p),S.Integer(q)
    B=S.Rational(B)
    alpha=(2*q-1)/(p-1)
    D=p+4*q-4
    ell=B/D
    return alpha,D,ell


def laplacian(p,q,a,b,z,c=0,d=0):
    n=p+q
    L=S.zeros(n)
    def add(i,j,w):
        L[i,i]+=w;L[j,j]+=w;L[i,j]-=w;L[j,i]-=w
    for i in range(1,p):add(0,i,a)
    for j in range(p+1,n):add(p,j,b)
    add(0,p,z)
    for i in range(1,p):
        for j in range(i+1,p):add(i,j,c)
    for i in range(p+1,n):
        for j in range(i+1,n):add(i,j,d)
    return L


for q in range(2,7):
    for p in range(2*q, min(4*q+4,24)):
        alpha,D,ell=parameters(p,q)
        a,b,z=ell,2*ell,(2*q-1)*ell
        v=S.Matrix([0]+[-alpha]*(p-1)+[1]+[2]*(q-1))
        verify(sum(v)==0,(p,q,'centering'))
        verify(v.dot(v)+(p-1)*(1-alpha**2)==D,(p,q,'certificate trace'))
        verify((2*q-1)**2==alpha*(p-1)*(2*q-1),(p,q,'consistency'))
        L=laplacian(p,q,a,b,z)
        verify(L*v==ell*v,(p,q,'four-level eigenvector'))
        verify((p-1)*a+(q-1)*b+z==1,(p,q,'budget'))
        verify(alpha<=1,(p,q,'dual coefficient'))
        critical=p*(p-1)<=2*(2*q-1)**2
        nu=(1-alpha**2)*(p-1)/(p-2)
        verify((2*nu<=1)==critical,(p,q,'dual threshold'))
        # Left-transverse and right-transverse leaf-space eigenvalues.
        if p>=3:
            u=S.zeros(p+q,1);u[1]=1;u[2]=-1
            verify(L*u==ell*u,(p,q,'left transverse eigenvalue'))
        if q>=3:
            u=S.zeros(p+q,1);u[p+1]=1;u[p+2]=-1
            verify(L*u==2*ell*u,(p,q,'right transverse eigenvalue'))
        if not critical:
            lo=(p-2)/(2*(1-alpha**2))
            hi=p-1
            verify(lo<hi,(p,q,'strict derivative interval'))
            k=(lo+hi)/2
            dc=S.Rational(1)
            da=-k
            dz=(p-1)*k-S.binomial(p-1,2)
            verify(da+(p-1)*dc>0,(p,q,'left-transverse derivative'))
            verify((p-1)*alpha**2*da+dz>0,(p,q,'quotient derivative'))
            verify((p-1)*da+S.binomial(p-1,2)*dc+dz==0,(p,q,'budget direction'))
        else:
            verify(2*nu<=1,(p,q,'support certificate'))

# Independent finite exact spectral sign checks of quotient at selected instances.
for p,q in [(6,3),(7,3),(8,3),(9,4),(10,4),(11,4),(13,5),(14,5)]:
    alpha,D,ell=parameters(p,q)
    L=laplacian(p,q,ell,2*ell,(2*q-1)*ell)
    ev=L.eigenvals()
    verify(sum(ev.values())==p+q,(p,q,'dimension'))
    verify(S.Integer(0) in ev and ell in ev,(p,q,'required eigenvalues'))
    verify(all(S.sign(S.simplify(e-ell))>=0 for e in ev if e!=0),(p,q,'Fiedler spectral order'))

print(f'VERIFY_OK {checks} exact rational certificate, edge, derivative and spectral checks')
