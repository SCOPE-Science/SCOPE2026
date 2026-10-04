# An exact half-spectrum zero mode on Hambly-Kumagai perfect-transfer diamonds

## Finding
For the Hambly-Kumagai diamond graphs \(HK_\ell\) and the perfect-state-transfer Hamiltonians \(H_\ell\) obtained in the cited work by lifting the zero-diagonal symmetric Krawtchouk Jacobi matrix, the zero-energy eigenspace occupies exactly half of the one-excitation Hilbert space at every nontrivial level:
\[
\dim\ker H_\ell=\frac{4^\ell+2}{3}=\frac12|V(HK_\ell)|,\qquad \ell\ge1.
\]
Equivalently,
\[
\operatorname{rank}H_\ell=\frac12|V(HK_\ell)|.
\]
The block-off-diagonal symmetry also pairs every nonzero eigenvalue with its negative. Hence the normalized integrated density of states defined in the source satisfies the exact finite-level identities
\[
N_\ell(0^-)=\frac14,\qquad N_\ell(0)=\frac34,
\]
so the zero-energy jump has mass exactly \(1/2\) for every \(\ell\ge1\).

The published tables show zero multiplicities \(6\), \(22\), and \(86\) at levels \(2\), \(3\), and \(4\), respectively. The formula above explains all three and gives the all-level law, including the integrated-density consequence.

## Assumptions and scope
The claim is restricted to the Hambly-Kumagai family and to the lifted Hamiltonians built from the symmetric Krawtchouk chain with vanishing diagonal entries, exactly as in arXiv:1909.08668 and arXiv:2003.11190. It does not assert the same nullity for arbitrary diamond-graph Hamiltonians, nonzero magnetic fields, other Jacobi data, or the Lang-Plaut family.

Multiplicity means spectral multiplicity of the self-adjoint finite-dimensional Hamiltonian. The statement starts at \(\ell=1\); the initial one-edge level \(HK_0\) has no zero eigenvalue for the corresponding two-site Krawtchouk Hamiltonian.

## Proof
Constructing \(HK_\ell\) from \(HK_{\ell-1}\) replaces every old edge by two branches of length two. Therefore the vertices of \(HK_\ell\) split into the old vertices
\[
U=V(HK_{\ell-1})
\]
and the new midpoint vertices \(W\), with two new midpoint vertices for every edge of \(HK_{\ell-1}\). Every edge of \(HK_\ell\) joins \(U\) to \(W\).

The Krawtchouk diagonal entries vanish, and the source's lifting formula therefore gives, after ordering vertices as \(U\cup W\),
\[
H_\ell=\begin{pmatrix}0&C_\ell\\D_\ell&0\end{pmatrix}.
\]
For one old edge \(e=\{u,v\}\), its two replacement midpoints have identical radial layers and identical neighborhoods. Consequently the corresponding two columns of \(C_\ell\) are equal. Keeping one column from each pair gives a weighted unsigned incidence matrix of \(HK_{\ell-1}\).

The two nonzero entries in the column belonging to an old edge between consecutive old radial layers \(k\) and \(k+1\) depend only on that layer pair: this follows directly from the source formula
\[
H(x,y)=\frac1{\deg_\pm(x)}\langle \Pi_A(x)|J|\Pi_A(x)\pm1\rangle
\]
and from constancy of the layer degrees. All Krawtchouk off-diagonal entries are positive. Hence invertible diagonal row scalings, chosen recursively by the radial layer, together with nonzero column scalings, convert this weighted incidence matrix into the ordinary unsigned vertex-edge incidence matrix \(B_{\ell-1}\). Thus
\[
\operatorname{rank}C_\ell=\operatorname{rank}B_{\ell-1}.
\]
The same reasoning, or self-adjointness with respect to the positive graph inner product, gives
\[
\operatorname{rank}D_\ell=\operatorname{rank}C_\ell.
\]

Each \(HK_{\ell-1}\) is connected and bipartite. For a connected bipartite graph, the ordinary unsigned incidence matrix has rank \(|V|-1\) over \(\mathbb R\): a vector \(a\) lies in the left kernel exactly when \(a_u+a_v=0\) on every edge, and connected bipartiteness leaves precisely the one-dimensional alternating-sign solution. Therefore
\[
\operatorname{rank}C_\ell=|V(HK_{\ell-1})|-1
\]
and the block matrix has
\[
\operatorname{rank}H_\ell=2\bigl(|V(HK_{\ell-1})|-1\bigr).
\]

The graph recursion has \(|E(HK_j)|=4^j\) and
\[
|V(HK_j)|=\frac{2\cdot4^j+4}{3}.
\]
Substitution yields
\[
\dim\ker H_\ell
=|V(HK_\ell)|-2\bigl(|V(HK_{\ell-1})|-1\bigr)
=\frac{4^\ell+2}{3}
=\frac12|V(HK_\ell)|.
\]

Finally, the involution that is \(+1\) on \(U\) and \(-1\) on \(W\) anticommutes with \(H_\ell\), so all nonzero eigenvalues occur in \(\pm\)-pairs. Self-adjointness makes the zero eigenvalue semisimple. The remaining half of the spectrum therefore splits equally between positive and negative eigenvalues, proving the two integrated-density values.

## Verification
The standalone verifier reconstructs the Hambly-Kumagai graphs through level \(6\), forms the ordinary unsigned incidence matrix of \(HK_{\ell-1}\), computes its rank by exact rational Gaussian elimination, and checks
\[
\operatorname{rank}B_{\ell-1}=|V(HK_{\ell-1})|-1,
\qquad
|V(HK_\ell)|-2\operatorname{rank}B_{\ell-1}=\frac{4^\ell+2}{3}.
\]
It also checks the published zero multiplicities \(6\), \(22\), and \(86\) for levels \(2\), \(3\), and \(4\). These finite checks support the bookkeeping but do not replace the all-level incidence-rank proof.

## Relationship to prior work
The 2019 construction paper establishes perfect state transfer on diamond fractal graphs and gives the radial coupling rule used here. The 2020 spectral paper develops the lifting-and-gluing spectral decomposition, gives the exact level-
\(2\) zero multiplicity \(6\), tabulates multiplicities \(22\) and \(86\) at levels \(3\) and \(4\), gives the total number of localized eigenvectors, and plots the integrated density of states at higher levels. It does not state the all-level identity \(\dim\ker H_\ell=|V(HK_\ell)|/2\), the resulting exact quarter-half-quarter spectral mass split, or the incidence-rank proof above.

Semantic searches for zero-mode multiplicity, nullity, half-spectrum atoms, the sequence \(6,22,86\), and equivalent integrated-density formulations found no covering result. General facts about ranks of bipartite incidence matrices are classical, but by themselves do not identify the source Hamiltonian with the recursively scaled incidence block or yield the physical half-spectrum law.

## Limitations
The proof relies on the zero diagonal, nonzero radial Krawtchouk couplings, and the two-parallel-length-two replacement rule of the Hambly-Kumagai family. A diagonal field destroys the chiral block form, and a different lifting may change the nullity. No assertion is made for the Lang-Plaut graphs or for arbitrary self-similar networks. The searches cannot exclude an equivalent statement under substantially different terminology.

## References
1. M. Derevyagin, G. V. Dunne, G. Mograby, and A. Teplyaev, *Perfect quantum state transfer on diamond fractal graphs*, arXiv:1909.08668v1 (2019), DOI:10.1007/s11128-020-02828-w.
2. G. Mograby, M. Derevyagin, G. V. Dunne, and A. Teplyaev, *Spectra of Perfect State Transfer Hamiltonians on Fractal-Like Graphs*, arXiv:2003.11190v2 (2020), DOI:10.1088/1751-8121/abc4b9.
