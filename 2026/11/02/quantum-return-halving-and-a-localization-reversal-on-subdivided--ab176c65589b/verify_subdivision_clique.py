"""Finite-dimensional numerical checks for quantum return on subdivided cliques.

Requires numpy. This verifies sample sizes numerically; the proof in RESULT.md
establishes the all-size statement without numerical extrapolation.
"""
import numpy as np


def formulas(n):
    core = (n*n - 2*n + 2)/(2*n*n)
    bridge = (n**4 - 6*n**3 + 11*n*n - 4*n + 4)/(n*n*(n-1)**2)
    return core, bridge


def run():
    cases=0
    for n in range(3,17):
        edges=[(i,j) for i in range(n) for j in range(i+1,n)]
        m=len(edges)
        adjacency=np.zeros((n+m,n+m))
        for k,(u,v) in enumerate(edges):
            adjacency[u,n+k]=adjacency[n+k,u]=1
            adjacency[v,n+k]=adjacency[n+k,v]=1
        eigenvalues,eigenvectors=np.linalg.eigh(adjacency)
        groups=[]
        for k,eigenvalue in enumerate(eigenvalues):
            if not groups or abs(eigenvalue-eigenvalues[groups[-1][0]])>1e-7:
                groups.append([k])
            else: groups[-1].append(k)
        spectrum=[(float(eigenvalues[grp[0]]),len(grp)) for grp in groups]
        expected=sorted([(0.,m-n),(-np.sqrt(2*(n-1)),1),(-np.sqrt(n-2),n-1),
                         (np.sqrt(n-2),n-1),(np.sqrt(2*(n-1)),1)])
        expected=[(val,mult) for val,mult in expected if mult>0]
        assert len(spectrum)==len(expected), (n,spectrum,expected)
        for (a,m1),(b,m2) in zip(spectrum,expected):
            assert abs(a-b)<1e-8 and m1==m2, (n,spectrum,expected)
        return_prob=np.zeros(n+m)
        for group in groups:
            projector_diag=np.sum(eigenvectors[:,group]**2,axis=1)
            return_prob += projector_diag**2
        core,bridge=formulas(n)
        assert np.max(abs(return_prob[:n]-core)) < 5e-10, (n,core,return_prob[:n])
        assert np.max(abs(return_prob[n:]-bridge)) < 5e-10, (n,bridge,return_prob[n:])
        cases+=1
    print(f'PASS: {cases} independent adjacency-matrix diagonalizations; exact spectra and all vertex return values match.')

if __name__=='__main__':run()


def projector_return(matrix):
    eig, vec=np.linalg.eigh(matrix)
    ans=np.zeros(matrix.shape[0])
    zero_diag=np.zeros(matrix.shape[0])
    k=0
    while k<len(eig):
        j=k+1
        while j<len(eig) and abs(eig[j]-eig[k])<1e-7:j+=1
        diag=np.sum(vec[:,k:j]**2,axis=1)
        ans+=diag**2
        if abs(eig[k])<1e-7:zero_diag=diag
        k=j
    return ans,zero_diag


def check_general_graphs():
    from itertools import combinations
    count=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for bits in range(1,1<<len(pairs)):
            edges=[e for k,e in enumerate(pairs) if bits>>k&1]
            visited={0}
            for _ in range(n):
                visited|={v for u,v in edges if u in visited}
                visited|={u for u,v in edges if v in visited}
            if len(visited)!=n:continue
            m=len(edges)
            B=np.zeros((n,m))
            for j,(u,v) in enumerate(edges):B[u,j]=B[v,j]=1
            H=np.block([[np.zeros((n,n)),B],[B.T,np.zeros((m,m))]])
            Q=B@B.T
            orig_return, _=projector_return(H)
            signless_return, zero_proj=projector_return(Q)
            predicted=signless_return/2 +zero_proj**2/2
            assert np.max(abs(orig_return[:n]-predicted))<1e-8,(n,edges,orig_return[:n],predicted)
            count+=1
    print(f'PASS: general subdivision identity for all {count} connected simple graphs on 2–5 vertices.')

if __name__=='__main__':check_general_graphs()
