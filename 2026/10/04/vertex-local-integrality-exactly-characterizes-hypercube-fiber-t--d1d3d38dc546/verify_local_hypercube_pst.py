#!/usr/bin/env python3
import itertools
import math
import cmath

def poly_add(a,b):
    n=max(len(a),len(b))
    out=[0]*n
    for i in range(n):
        out[i]=(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out

def poly_mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    while len(out)>1 and out[-1]==0:
        out.pop()
    return out

def charpoly_tI_minus_A(A):
    n=len(A)
    out=[0]
    for p in itertools.permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=[1]
        for i,j in enumerate(p):
            if i==j:
                term=poly_mul(term,[-A[i][i],1])
            else:
                term=poly_mul(term,[-A[i][j]])
        if inv%2:
            term=[-x for x in term]
        out=poly_add(out,term)
    return out

def jacobi_eigen(A,tol=1e-14,max_iter=10000):
    n=len(A)
    M=[[float(A[i][j]) for j in range(n)] for i in range(n)]
    V=[[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(max_iter):
        p=q=0
        mx=0.0
        for i in range(n):
            for j in range(i+1,n):
                if abs(M[i][j])>mx:
                    mx=abs(M[i][j]); p=i; q=j
        if mx<tol:
            return [M[i][i] for i in range(n)], V
        app,aqq,apq=M[p][p],M[q][q],M[p][q]
        phi=0.5*math.atan2(2*apq,aqq-app)
        c,s=math.cos(phi),math.sin(phi)
        for k in range(n):
            if k not in (p,q):
                mkp,mkq=M[k][p],M[k][q]
                M[k][p]=M[p][k]=c*mkp-s*mkq
                M[k][q]=M[q][k]=s*mkp+c*mkq
        M[p][p]=c*c*app-2*s*c*apq+s*s*aqq
        M[q][q]=s*s*app+2*s*c*apq+c*c*aqq
        M[p][q]=M[q][p]=0.0
        for k in range(n):
            vkp,vkq=V[k][p],V[k][q]
            V[k][p]=c*vkp-s*vkq
            V[k][q]=s*vkp+c*vkq
    raise RuntimeError("Jacobi iteration did not converge")

def evolve_basis(A,g,t):
    vals,V=jacobi_eigen(A)
    n=len(A)
    out=[0j]*n
    for j,lam in enumerate(vals):
        coeff=V[g][j]
        phase=cmath.exp(-1j*t*lam)
        for i in range(n):
            out[i]+=V[i][j]*coeff*phase
    return out

def main():
    # Vertex order: g,u,v,a1,a2,b1,b2.
    n=7
    edges=[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]
    A=[[0]*n for _ in range(n)]
    for u,v in edges:
        A[u][v]=A[v][u]=1

    phi=charpoly_tI_minus_A(A)
    # x^3(x^2-2)(x^2-4) = x^7 - 6 x^5 + 8 x^3.
    assert phi == [0,0,0,8,0,-6,0,1], phi

    inds=list(range(1,n))
    Ag=[[A[i][j] for j in inds] for i in inds]
    phig=charpoly_tI_minus_A(Ag)
    # x^2(x^2-2)^2 = x^6 - 4 x^4 + 4 x^2.
    assert phig == [0,0,4,0,-4,0,1], phig

    # Nonintegral global spectrum but integral local poles {-2,0,2}.
    vals,_=jacobi_eigen(A)
    vals=sorted(vals)
    expected=sorted([-2.0,-math.sqrt(2),0.0,0.0,0.0,math.sqrt(2),2.0])
    assert max(abs(a-b) for a,b in zip(vals,expected)) < 2e-10

    return_checks=0
    product_checks=0
    for d in (2,3,4,5):
        m=2**d
        t=math.pi/2
        outer_time=m*t
        vec=evolve_basis(A,0,outer_time)
        assert abs(vec[0]-1)<2e-10
        assert max(abs(z) for z in vec[1:])<2e-10
        return_checks+=1

        # Hypercube amplitudes at t=pi/2: only the antipode survives.
        amps=[]
        for r in range(d+1):
            amps.append(((-1j*math.sin(t))**r)*(math.cos(t)**(d-r)))
        assert max(abs(amps[r]) for r in range(d)) < 1e-12
        phase=amps[d]
        assert abs(abs(phase)-1)<1e-12

        # Uniform-sector phase equals hypercube transfer phase.
        uniform_phase=cmath.exp(-1j*d*t)
        assert abs(uniform_phase-phase)<1e-12
        product_checks+=1

    # Every odd half-period works for the local support {-2,0,2}.
    time_checks=0
    for d in (2,3,4,5):
        m=2**d
        for r in range(6):
            t=(2*r+1)*math.pi/2
            for theta in (-2,0,2):
                assert abs(cmath.exp(-1j*m*t*theta)-1)<2e-11
            time_checks+=1

    print("VERIFY_OK")
    print("exact_charpoly_checks = 2")
    print("outer_return_checks =",return_checks)
    print("product_phase_checks =",product_checks)
    print("odd_half_period_checks =",time_checks)
    print("local_support = -2,0,2")
    print("global_nonintegral_eigenvalues = +/-sqrt(2)")

if __name__=="__main__":
    main()
