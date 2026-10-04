#!/usr/bin/env python3
import math, cmath

def zeros(n): return [[0j for _ in range(n)] for _ in range(n)]
def eye(n):
    A=zeros(n)
    for i in range(n): A[i][i]=1
    return A

def dagger(A): return [[A[j][i].conjugate() for j in range(len(A))] for i in range(len(A[0]))]
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def madd(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A,B): return [[A[i][j]-B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def scale(a,A): return [[a*z for z in row] for row in A]
def hs2(A): return sum(abs(z)**2 for row in A for z in row)
def kron(A,B):
    return [[A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])] for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
def proj(v): return [[v[i]*v[j].conjugate() for j in range(len(v))] for i in range(len(v))]
def basis_identity(m):
    return [[1+0j if i==j else 0j for i in range(m)] for j in range(m)]
def basis_fourier(m):
    w=cmath.exp(2j*math.pi/m)
    return [[w**(i*j)/math.sqrt(m) for i in range(m)] for j in range(m)]
def basis_rotation(m,theta):
    B=basis_identity(m)
    c,s=math.cos(theta),math.sin(theta)
    B[0]=[c,s]+[0j]*(m-2)
    B[1]=[-s,c]+[0j]*(m-2)
    return B

def flip(m):
    d=m*m; F=zeros(d)
    for i in range(m):
        for j in range(m):
            F[j*m+i][i*m+j]=1
    return F

def dephase(A,BA,BB):
    d=len(A); out=zeros(d)
    for a in BA:
        Pa=proj(a)
        for b in BB:
            P=kron(Pa,proj(b))
            PAP=mm(mm(P,A),P)
            out=madd(out,PAP)
    return out

def overlap_s(BA,BB):
    s=0.0
    for a in BA:
        for b in BB:
            z=sum(a[i].conjugate()*b[i] for i in range(len(a)))
            s+=abs(z)**4
    return s

def density_from_basis(B,weights):
    A=zeros(len(B))
    for v,w in zip(B,weights): A=madd(A,scale(w,proj(v)))
    return A

def maxerr(A,B): return max(abs(A[i][j]-B[i][j]) for i in range(len(A)) for j in range(len(A[0])))

def main():
    disturbance_checks=0; endpoint_checks=0; perturbation_checks=0; intermediate_checks=0
    for m in range(2,7):
        BA=basis_identity(m); BF=basis_fourier(m); BR=basis_rotation(m,0.37)
        F=flip(m)
        for BB in (BA,BF,BR):
            S=overlap_s(BA,BB)
            D=dephase(F,BA,BB)
            lhs=hs2(msub(F,D)); rhs=m*m-S
            assert abs(lhs-rhs)<2e-10, (m,lhs,rhs)
            disturbance_checks+=1
            assert 1-1e-11 <= S <= m+1e-11
        assert abs(overlap_s(BA,BA)-m)<2e-11
        assert abs(overlap_s(BA,BF)-1)<2e-11
        endpoint_checks+=2
        sr=overlap_s(BA,BR)
        assert 1 < sr < m
        intermediate_checks+=1

        # Explicit perturbation with distinct marginal spectra in BA and BR.
        wa=[2*(i+1)/(m*(m+1)) for i in range(m)]
        raw=[m-i for i in range(m)]; sm=sum(raw); wb=[x/sm for x in raw]
        sigA=density_from_basis(BA,wa); sigB=density_from_basis(BR,wb); sigma=kron(sigA,sigB)
        x=0.37
        b=(m*x-1)/(m**3-m)
        I=eye(m*m); rho=madd(scale((m-x)/(m**3-m),I),scale(b,F))
        S=overlap_s(BA,BR)
        for eps in (0.2,0.03,0.004):
            tau=scale(1/(1+eps),madd(rho,scale(eps,sigma)))
            Dt=dephase(tau,BA,BR)
            lhs=hs2(msub(tau,Dt))
            rhs=(b*b*(m*m-S))/(1+eps)**2
            assert abs(lhs-rhs)<3e-10, (m,eps,lhs,rhs)
            perturbation_checks+=1

    print('VERIFY_OK')
    print('disturbance_identity_checks =',disturbance_checks)
    print('endpoint_checks =',endpoint_checks)
    print('intermediate_overlap_checks =',intermediate_checks)
    print('finite_epsilon_perturbation_checks =',perturbation_checks)

if __name__=='__main__': main()
