# A sharp hub-revival cutoff for two hypercubes sharing one vertex

## Finding

Let \(G_n\) be obtained by identifying one corner in each of two disjoint unweighted hypercubes \(Q_n\), and let \(h\) denote their common vertex. For adjacency-matrix continuous-time evolution, there is a time \(t>0\) with

\[
e^{-itA(G_n)}|h\rangle=e^{i\theta}|h\rangle
\]

for some real phase \(\theta\) **if and only if** \(n\in\{1,2\}\). The least positive return times are respectively \(\pi/\sqrt2\) and \(2\pi/\sqrt6\). For all \(n\ge3\) the exact return probability is strictly less than one at every positive time.

## Assumptions and scope

Here \(n\) is any positive integer. Each hypercube has its standard unit-weight edges, and the two copies meet *only* at one identified vertex, with no additional edges, vertex potentials, or rescaling of the Hamiltonian. The graph has \(2^{n+1}-1\) vertices. The initial state is the common vertex \(h\), **not** either remote corner of the joined cubes. "Revival" means exact return of the entire state up to an overall phase, equivalently unit-modulus return amplitude. It does not mean a merely large revival peak or perfect transfer between remote corners.

## Proof

**1. Exact cyclic hub reduction.** For each shell distance \(r\ge1\), form the normalized uniform state on the \(2\binom nr\) vertices at distance \(r\) from \(h\), and let \(|0\rangle=|h\rangle\). These \(n+1\) vectors span an invariant adjacency subspace. In this orthonormal basis its matrix \(J_n\) is tridiagonal, with zero diagonal and positive off-diagonal entries

\[
b_0=\sqrt{2n},\qquad b_r=\sqrt{(r+1)(n-r)}\quad(1\le r<n).
\]

Every shell vector is reached from \(|0\rangle\) by the irreducible Jacobi recurrence. Consequently \(|0\rangle\) is cyclic for \(J_n\), so every eigenvalue of \(J_n\) lies in its spectral support. No eigenvalue from the orthogonal complementary subspace affects hub return.

**2. Positive squared spectral block.** Bipartiteness gives eigenvalue pairs \(\pm\lambda\). Reorder the tridiagonal basis by even/odd shell indices. The matrix has the form \(\begin{pmatrix}0&B\\B^{\!*}&0\end{pmatrix}\), and the eigenvalues of the positive definite odd-shell block \(M_n=B^{\!*}B\) are precisely the squares of the positive eigenvalues of \(J_n\). Its dimension is \(d=\lceil n/2\rceil\).

Let \(J_n^{(0)}\) be the standard radial hypercube Jacobi matrix, identical except that its first coupling is \(\sqrt n\). Its positive eigenvalues are the positive members of \(n,n-2,\ldots,-n\); in particular its least positive eigenvalue is \(\ell=1\) for odd \(n\) and \(\ell=2\) for even \(n\). Writing \(M_n^{(0)}\) for its odd-shell squared block gives exactly

\[
M_n=M_n^{(0)}+n|e_1\rangle\langle e_1|.
\]

The smallest eigenvalue of \(M_n^{(0)}\), namely \(\ell^2\), is simple. Its normalized eigenvector \(u\) obeys

\[
n|\langle e_1,u\rangle|^2=
\frac{2\ell^2}{2^n}\binom{n}{(n-\ell)/2}.
\tag{1}
\]

To see (1), diagonalize the hypercube by its coordinate Walsh characters. The original corner has squared overlap \(2^{-n}\binom{n}{(n-\ell)/2}\) with the energy \(\ell\) eigenspace; its normalized radial eigenvector has first odd-shell component \(\ell/\sqrt n\) times the corner component. Restricting an energy-\(\ell\) vector to the odd-shell sector and normalizing multiplies its squared amplitudes by two, yielding (1). The first component of \(u\) is nonzero.

By the positive rank-one perturbation and simplicity of the least eigenvalue, \(y_{\min}:=\min\sigma(M_n)>\ell^2\). The trial vector \(u\) and (1) give

\[
y_{\min}\le\ell^2+
\frac{2\ell^2}{2^n}\binom{n}{(n-\ell)/2}.
\tag{2}
\]

When \(n\ge3\) is odd, its central binomial coefficient is strictly below \(2^{n-1}\), and (2) yields \(1<y_{\min}<2\). When \(n=2m\ge4\), elementary binomial-ratio monotonicity yields

\[
\frac1{4^m}\binom{2m}{m-1}\le\frac14,
\]

with equality only at \(m=1,2\). Thus (2) gives \(4<y_{\min}\le6\). For \(n=4\), equality in the trial-vector bound is impossible: the lowest eigenvector \(u\) of \(M_n^{(0)}\) has a nonzero component outside \(e_1\), hence is not an eigenvector of \(M_n^{(0)}+n|e_1\rangle\langle e_1|\). All larger even \(n\) have strict binomial inequality. Therefore

\[
4<y_{\min}<6\qquad(n\ge4\text{ even}).
\tag{3}
\]

**3. Exact return forces integral squared eigenvalues.** Suppose exact hub return occurs at a positive time. All eigenvalues of \(J_n\) are in its hub spectral support and both signs of each nonzero \(\lambda_j\) occur. Equality of their phases implies \(t\lambda_j\in\pi\mathbb Z\) for every positive \(\lambda_j\). Consequently every squared-eigenvalue ratio \(\lambda_j^2/\lambda_k^2\) is rational. Their sum \(S=\operatorname{tr}(M_n)\) is a positive integer, because every squared Jacobi coupling \(b_r^2\) is an integer. It follows that all positive squared eigenvalues are rational. But each is a root of the monic integer polynomial \(F_n(y)=\det(yI-M_n)\). The rational-root theorem forces *every* positive squared eigenvalue to be an integer.

For odd \(n\ge3\), \(1<y_{\min}<2\) immediately contradicts integrality. For even \(n\ge4\), all squared Jacobi couplings \(b_r^2\) are even, so the tridiagonal determinant recurrence gives

\[
F_n(y)\equiv y^{n/2}\pmod2.
\]

Thus no positive odd integer can be a root. Yet (3) leaves \(5\) as the only possible integer for \(y_{\min}\), again a contradiction.

**4. Low-dimensional exceptions.** For \(n=1\), the cyclic radial spectrum is \(\{-\sqrt2,\sqrt2\}\), giving a smallest positive return time \(\pi/\sqrt2\). For \(n=2\), it is \(\{-\sqrt6,0,\sqrt6\}\), all supported at the hub, giving a smallest positive return time \(2\pi/\sqrt6\). This proves the classification.

## Verification

The included standalone `verify.py` independently constructs the full joined-hypercube adjacency matrices and normalized shell states through dimension six and checks their invariant Jacobi reductions. Its exact symbolic determinant recurrence and parity checks cover dimensions one through fifteen, with numerical checks of the predicted strict smallest-squared-eigenvalue intervals; direct return-amplitude checks cover dimensions one and two. All 23 labeled checks pass. Finite calculations corroborate the arguments and are **not** offered as a proof for unbounded dimension.

Reproduce with `python verify.py`; the script requires Python with NumPy and SymPy.

## Relationship to prior work

Desaules, Bull, Daniel, and Papić introduced the same two-hypercube single-vertex junction as a tractable parent of many-body scarred quantum walks, reducing **remote-corner/Néel-state** dynamics to a tridiagonal chain and exhibiting imperfect revival peaks. Their treatment does not establish a dimension-uniform necessary-and-sufficient criterion for **exact return at the common vertex**. The reduction here starts at that common vertex instead, producing a different first Jacobi coupling and an arithmetic obstruction from squared eigenvalues. Work on continuous-time walks on graph joins supplies general periodicity context, but graph *join* adds edges between all vertices and is not the single-vertex identification considered here. The unit-weight hypercube spectrum and the rational-algebraic-integer argument use standard ingredients; originality is asserted for their sharp junction-specific combination and classification, not those ingredients separately.

## Limitations

The result concerns unweighted adjacency evolution, a precisely identified shared hub, and *exact* positive-time recurrence. It neither estimates best approximate recurrence times nor classifies return from remote corners, perturbed edge weights, or the Laplacian walk. Compact almost-periodicity in finite-dimensional quantum mechanics is compatible with the absence of exact return. No independent mathematical or priority audit has been performed.

## References

1. J.-Y. Desaules, K. Bull, A. Daniel, and Z. Papić, "Hypergrid subgraphs and the origin of scarred quantum walks in the many-body Hilbert space," arXiv:2112.06885 (first public 13 December 2021), *Physical Review B* **105**, 245137 (2022), especially Section II and Figure 2. https://arxiv.org/abs/2112.06885
2. S. Kirkland and H. Monterde, "Quantum walks on join graphs," arXiv:2312.06906 (12 December 2023). The operation there is a graph join, not vertex identification. https://arxiv.org/abs/2312.06906
