#!/usr/bin/env python3
import itertools
import math

def q_matrix(n, edges):
    A = [[0.0]*n for _ in range(n)]
    deg = [0]*n
    for u,v in edges:
        A[u][v] = A[v][u] = 1.0
        deg[u] += 1
        deg[v] += 1
    return [[(deg[i] if i==j else 0.0) + A[i][j] for j in range(n)] for i in range(n)]

def jacobi_eigs(M, tol=1e-13, max_iter=5000):
    A = [row[:] for row in M]
    n = len(A)
    for _ in range(max_iter):
        p=q=0
        m=0.0
        for i in range(n):
            for j in range(i+1,n):
                if abs(A[i][j]) > m:
                    m=abs(A[i][j]); p=i; q=j
        if m < tol:
            return sorted(A[i][i] for i in range(n))
        app,aqq,apq=A[p][p],A[q][q],A[p][q]
        phi=0.5*math.atan2(2*apq, aqq-app)
        c,s=math.cos(phi),math.sin(phi)
        for k in range(n):
            if k not in (p,q):
                aik,akq=A[k][p],A[k][q]
                A[k][p]=A[p][k]=c*aik-s*akq
                A[k][q]=A[q][k]=s*aik+c*akq
        A[p][p]=c*c*app-2*s*c*apq+s*s*aqq
        A[q][q]=s*s*app+2*s*c*apq+c*c*aqq
        A[p][q]=A[q][p]=0.0
    raise RuntimeError("Jacobi iteration did not converge")

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def det_poly_tI_minus_int(M):
    n=len(M)
    out=[0]
    for perm in itertools.permutations(range(n)):
        inv=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=[1]
        for i,j in enumerate(perm):
            if i==j:
                term=poly_mul(term,[-M[i][i],1])
            else:
                term=poly_mul(term,[-M[i][j]])
        if len(out)<len(term): out += [0]*(len(term)-len(out))
        sg=-1 if inv%2 else 1
        for k,x in enumerate(term): out[k]+=sg*x
    while len(out)>1 and out[-1]==0: out.pop()
    return out

def dtN_matrix(n, edges, ell, k):
    A=[[0.0]*n for _ in range(n)]
    deg=[0]*n
    for u,v in edges:
        A[u][v]=A[v][u]=1.0
        deg[u]+=1; deg[v]+=1
    s=math.sin(k*ell); c=math.cos(k*ell)
    fac=k/s
    return [[fac*(A[i][j]-(c*deg[i] if i==j else 0.0)) for j in range(n)] for i in range(n)]

def min_singular_symmetric(M):
    return min(abs(x) for x in jacobi_eigs(M))

def all_edges(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def main():
    graph_checks=0
    for n in range(3,6):
        E=all_edges(n)
        target=n-2
        maxima=[]
        best=-1.0
        for mask in range(1<<len(E)):
            edges=[E[i] for i in range(len(E)) if (mask>>i)&1]
            qmin=jacobi_eigs(q_matrix(n,edges))[0]
            if qmin > best+1e-9:
                best=qmin; maxima=[mask]
            elif abs(qmin-best)<1e-9:
                maxima.append(mask)
            assert qmin <= target+2e-9
            graph_checks+=1
        complete=(1<<len(E))-1
        assert abs(best-target)<2e-9
        assert maxima==[complete], (n,best,maxima)

    # Exact characteristic polynomial, coefficients in ascending powers.
    tri_pendant=[[3,1,1,1],[1,2,1,0],[1,1,2,0],[1,0,0,1]]
    coeff=det_poly_tI_minus_int(tri_pendant)
    # (t-2)(t-1)(t^2-5t+2) = 4 -16t +19t^2 -8t^3 + t^4.
    assert coeff == [4,-16,19,-8,1], coeff
    qmin=(5-math.sqrt(17))/2
    assert abs(jacobi_eigs([[float(x) for x in row] for row in tri_pendant])[0]-qmin)<1e-10
    factor=4/(5-math.sqrt(17))
    assert abs(factor-(5+math.sqrt(17))/2)<1e-12

    for m in (3,5,7,9,11):
        cyc=[(i,(i+1)%m) for i in range(m)]
        got=jacobi_eigs(q_matrix(m,cyc))[0]
        want=2-2*math.cos(math.pi/m)
        assert abs(got-want)<2e-10, (m,got,want)

    # Near-resonance checks for K4 and C4, ell=1, first resonance.
    ell=1.0; k0=math.pi; lam0=k0*k0
    K4=all_edges(4)
    C4=[(0,1),(1,2),(2,3),(3,0)]
    predicted_K4=2*lam0*2
    for h in (1e-3,3e-4,1e-4):
        k=k0+h; lam=k*k
        scaled=abs(lam-lam0)*min_singular_symmetric(dtN_matrix(4,K4,ell,k))
        assert abs(scaled-predicted_K4)/predicted_K4 < 5e-3
        scaled_bip=abs(lam-lam0)*min_singular_symmetric(dtN_matrix(4,C4,ell,k))
        assert scaled_bip < 1e-3

    # Even resonance for K4 has vanishing scaled minimum singular value.
    k0=2*math.pi; lam0=k0*k0
    for h in (1e-3,3e-4,1e-4):
        k=k0+h; lam=k*k
        scaled=abs(lam-lam0)*min_singular_symmetric(dtN_matrix(4,K4,ell,k))
        assert scaled < 2e-3

    print("VERIFY_OK")
    print("simple_graphs_checked =", graph_checks)
    print("exact_triangle_pendant_charpoly = 4 - 16 t + 19 t^2 - 8 t^3 + t^4")
    print("odd_cycles_checked = 3,5,7,9,11")
    print("resonance_limit_checks = OK")

if __name__ == "__main__":
    main()
