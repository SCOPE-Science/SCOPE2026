"""Exact arithmetic verification of cut-cycle norms on antipodally augmented cubes.

Scientific verification for the finite folded-cube projection formula. All arithmetic
uses Python's Fraction; the matrix solve uses a distinct graph-Laplacian method.
"""
from fractions import Fraction as F
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def spectral_potential(n, j):
    # Character sum on F_2^(n+1)/<all-one vector>.
    return sum(
        (F(sum((-1)**a * binom(j, a) * binom(n-j, s-a)
               for a in range(s+1)), s+1) for s in range(1, n+1, 2)),
        F(0)
    ) / (1 << n)


def expected_cut(n):
    k=(n+1)//2
    return F(n,2) + 1 - F(comb(2*k,k), 1 << (2*k))


def expected_cycle(n):
    return expected_cut(n) + 1 - 4*F((1<<n)-1, (1<<n)*(n+1))


def spectral_graph_check(n):
    values=[spectral_potential(n,j) for j in range(n+1)]
    assert all(values[j] > values[j+1] for j in range(n))
    assert all(values[j]==-values[n-j] for j in range(n+1))
    N=1<<n
    source=0; target=N-1  # source is the antipodal matching edge
    U=lambda vertex: values[vertex.bit_count()]
    generators=[1<<j for j in range(n)] + [N-1]
    edges=sorted({(min(v,v^g),max(v,v^g)) for v in range(N) for g in generators})
    # Direct vertex current conservation is independent of the closed norm formula.
    for v in range(N):
        lap=sum(U(v)-U(v^g) for g in generators)
        assert lap==(1 if v==source else (-1 if v==target else 0)),(n,v,lap)
    cut_norm=sum(abs(U(v)-U(w)) for v,w in edges)
    diagonal=U(source)-U(target)
    cycle_norm=cut_norm + 1 - 2*diagonal
    assert cut_norm==expected_cut(n),(n,cut_norm,expected_cut(n))
    assert cycle_norm==expected_cycle(n),(n,cycle_norm,expected_cycle(n))
    assert diagonal==2*F(N-1,N*(n+1))
    return len(edges)


def solve_fraction_matrix(A,b):
    size=len(b)
    M=[list(map(F,row))+[F(b[i])] for i,row in enumerate(A)]
    for i in range(size):
        pivot=next((j for j in range(i,size) if M[j][i]),None)
        assert pivot is not None
        M[i],M[pivot]=M[pivot],M[i]
        div=M[i][i]
        for j in range(i,size+1): M[i][j]/=div
        for row in range(i+1,size):
            mul=M[row][i]
            if not mul: continue
            for col in range(i+1,size+1):M[row][col]-=mul*M[i][col]
            M[row][i]=F(0)
    x=[F(0)]*size
    for row in range(size-1,-1,-1):
        x[row]=M[row][size]-sum((M[row][j]*x[j] for j in range(row+1,size)),F(0))
    return x


def full_graph_check(n):
    N=1<<n
    gs=[1<<j for j in range(n)]+[N-1]
    E=sorted({(min(v,v^g),max(v,v^g)) for v in range(N) for g in gs})
    M=N-1 # ground last vertex
    L=[[0]*M for _ in range(M)]
    for a,b in E:
        if a<M:L[a][a]+=1
        if b<M:L[b][b]+=1
        if a<M and b<M:
            L[a][b]-=1;L[b][a]-=1
    for source,target in [(0,N-1),(0,1)]:
        demand=[int(v==source)-int(v==target) for v in range(M)]
        potentials=solve_fraction_matrix(L,demand)+[F(0)]
        currents=[abs(potentials[a]-potentials[b]) for a,b in E]
        assert sum(currents)==expected_cut(n),(n,source,target)
        diag=potentials[source]-potentials[target]
        assert sum(currents)+1-2*diag==expected_cycle(n)
        assert diag==2*F(N-1,N*(n+1))
    return len(E)*2


def main():
    graph_edges=0
    for n in range(3,12):
        graph_edges+=spectral_graph_check(n)
    full_cols=0
    for n in range(3,6):
        full_cols+=full_graph_check(n)
    print(f"FOLDED_CUBE_EXACT_OK dimensions=9 spectral_edge_currents={graph_edges} full_grounded_columns=6 full_grounded_currents={full_cols}")

if __name__=='__main__':
    main()
