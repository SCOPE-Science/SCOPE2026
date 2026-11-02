"""Independent finite numerical replay for two-dimensional dihedral tomography.

Usage: python3 verify.py
No external modules are required. The infinite-parameter theorem uses geometric
sums and trace identities, not this finite test.
"""
import cmath
import math


def matmul(A,B):
    return [[sum(A[i][t]*B[t][j] for t in range(2)) for j in range(2)] for i in range(2)]


def action(n,k,a,b,j,reflected):
    z=cmath.exp(2j*math.pi*k*j/n)
    u,v=z*a,b/z
    return (v,u) if reflected else (u,v)


def eigvals_symmetric(A):
    A=[r[:] for r in A]
    for _ in range(300):
        i,j=max(((i,j) for i in range(4) for j in range(i+1,4)),key=lambda t:abs(A[t[0]][t[1]]))
        if abs(A[i][j]) < 2e-12:break
        theta=0.5*math.atan2(2*A[i][j],A[j][j]-A[i][i])
        c,s=math.cos(theta),math.sin(theta)
        # Rotate columns then rows by the same orthogonal change of basis.
        # Standard Jacobi rotation uses columns [c,-s], [s,c] in the (i,j) plane.
        for row in range(4):
            u,v=A[row][i],A[row][j]
            A[row][i]=c*u-s*v
            A[row][j]=s*u+c*v
        for col in range(4):
            u,v=A[i][col],A[j][col]
            A[i][col]=c*u-s*v
            A[j][col]=s*u+c*v
    return sorted(A[i][i] for i in range(4))


def operator_eigenvalues(n,k,a,b):
    # Coefficients of the rank-one projector in normalized Pauli coordinates.
    M=[[0.0]*4 for _ in range(4)]
    root=math.sqrt(2)
    for j in range(n):
        for refl in (False,True):
            u,v=action(n,k,a,b,j,refl)
            off=u*v.conjugate()
            coords=[(abs(u)**2+abs(v)**2)/root,
                    2*off.real/root,-2*off.imag/root,
                    (abs(u)**2-abs(v)**2)/root]
            for i in range(4):
                for h in range(4):
                    M[i][h]+=coords[i]*coords[h]
    return eigvals_symmetric(M)


def formula_eigenvalues(n,k,a,b):
    ell=n//math.gcd(n,2*k)
    c=a*b.conjugate()
    d=abs(a)**2-abs(b)**2
    if ell == 2:
        return sorted([n,n*d*d,4*n*(c.real)**2,4*n*(c.imag)**2])
    assert ell>=3
    return sorted([n,n*d*d,2*n*abs(c)**2,2*n*abs(c)**2])


def run():
    count=0
    for n in range(3,30):
        for k in range(1,(n-1)//2+1):
            for p,ang in ((0.13,0.37),(0.44,1.15),
                          ((1+1/math.sqrt(3))/2,math.pi/4)):
                a=math.sqrt(p)
                b=math.sqrt(1-p)*cmath.exp(1j*ang)
                obs=operator_eigenvalues(n,k,a,b)
                target=formula_eigenvalues(n,k,a,b)
                assert max(abs(x-y) for x,y in zip(obs,target))<2e-8, (n,k,obs,target)
                count+=1
    # Sharp optimal fiducials tested in all ranks in the indicated range.
    count_opt=0
    p=(1+1/math.sqrt(3))/2
    for n in range(3,30):
        for k in range(1,(n-1)//2+1):
            ell=n//math.gcd(n,2*k)
            angle=(math.pi/4 if ell==2 else 0.0)
            a=math.sqrt(p)
            b=math.sqrt(1-p)*cmath.exp(1j*angle)
            lam=operator_eigenvalues(n,k,a,b)
            assert max(abs(x-y) for x,y in zip(lam,[n/3]*3+[n]))<2e-8
            count_opt+=1
    print(f'VERIFY_OK spectra={count} optimal_orbits={count_opt} n_range=3..29')


if __name__=='__main__':
    run()
