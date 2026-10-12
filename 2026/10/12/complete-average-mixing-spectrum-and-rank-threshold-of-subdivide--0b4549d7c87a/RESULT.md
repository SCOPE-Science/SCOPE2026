# Complete average-mixing spectrum and rank threshold of subdivided complete graphs

## Finding
For each integer \(n\ge3\), let \(S(K_n)\) be the *subdivision graph* of the complete graph: its vertices are the original \(n\) vertices and the \(m=\binom n2\) edges, with a vertex adjacent to an edge exactly when it is an endpoint. Let \(A_n\) be the ordinary zero-one adjacency matrix of this graph. Define its continuous-time quantum average mixing matrix by
\[
\widehat M_n=\lim_{T\to\infty}\frac1T\int_0^T e^{itA_n}\circ e^{-itA_n}\,dt,
\]
where \(\circ\) is the entrywise product. Put
\[
a_n=\frac{n-2}{2n},\quad b_n=\frac{(n-4)(2n^2-5n-4)}{2n(n-2)^2},\quad h_n=\frac{n-4}{2n(n-2)},
\]
\[
L_n=\begin{pmatrix}a_n&h_n\sqrt{n-2}\\h_n\sqrt{n-2}&b_n\end{pmatrix},\qquad
\eta_n=\frac{(n-3)^3+4}{(n-2)^2(n-1)}.
\]
**The complete real spectrum**, counting indexed multiplicities before combining coincident values, comprises
\[
1\quad(1),\qquad \frac{n-3}{2(n-1)}\quad(1),\qquad
\operatorname{Spec}(L_n)\quad(n-1\text{ copies of each}),\qquad
\eta_n\quad\left(\frac{n(n-3)}2\text{ copies}\right).
\]
In particular,
\[
\operatorname{rank}\widehat M_n=\begin{cases}3,&n=3,\\7,&n=4,\\n+\binom n2,&n\ge5.\end{cases}
\]
Hence \(\widehat M_n\) is strictly positive definite exactly when \(n\ge5\). The two eigenvalues of \(L_n\) are specified exactly by its trace and determinant, with
\[
\det L_n=\frac{(n-4)(n-3)}{2n(n-2)}.
\]

## Assumptions and scope
All graphs are finite, simple and unweighted. The base complete graph has \(n\ge3\) vertices; the subdivision retains original vertices and introduces one vertex for every edge, without edges among originals or among edge-vertices. The Hamiltonian is the adjacency matrix, with no potential, magnetic phases, or normalizing prefactors. The long-time average is a Cesàro limit; existence follows from the finite spectral resolution. Multiplicity annotations enumerate invariant sectors and must be merged if distinct displayed eigenvalue expressions coincide. No statement concerns instantaneous or arbitrarily sampled mixing.

## Proof
**1. Exact spectral projections.** Let \(B\) be the \(n\times m\) unsigned vertex-edge incidence matrix, so
\[
A_n=\begin{pmatrix}0&B\\B^\top&0\end{pmatrix},\qquad
BB^\top=(n-2)I_n+J_n.
\]
Set \(P=J_n/n\), \(R=I_n-P\), \(Q=B^\top RB/(n-2)\), and \(W=I_m-J_m/m-Q\). The matrices \(J_m/m,Q,W\) are pairwise orthogonal projections with respective ranks \(1,n-1,m-n\); when \(n=3\), the last rank is zero. The four nonzero adjacency eigenvalues are \(\pm\sqrt{2(n-1)}\) and \(\pm\sqrt{n-2}\), and zero has projector \(\operatorname{diag}(0,W)\). For \((F,\sigma^2)=(P,2(n-1))\) or \((R,n-2)\), the projector for eigenvalue \(\pm\sigma\) is
\[
E_{F,\pm}=\frac12\begin{pmatrix}F&\pm FB/\sigma\\ \pm B^\top F/\sigma&B^\top FB/\sigma^2\end{pmatrix}.
\]
Direct multiplication verifies idempotence, pairwise orthogonality and that all five projectors sum to identity. Integrating phases (not time sampling) gives the exact identity \(\widehat M_n=\sum_\theta E_\theta\circ E_\theta\), where \(\theta\) ranges over *distinct* adjacency eigenvalues.

**2. The orbit-block expression.** Let \(T=B^\top B-2I_m\), the adjacency matrix of the triangular graph on two-element subsets. For distinct edge-vertices, \(T_{ef}=1\) precisely when the corresponding base edges share one endpoint. Expanding the projector Schur squares yields
\[
\widehat M_n=\begin{pmatrix}
a_nI_n+J_n/n^2&h_nB+t_nJ_{n,m}\\
h_nB^\top+t_nJ_{m,n}&c_0I_m+c_1T+c_2(J_m-I_m-T)
\end{pmatrix},
\]
where \(J_{n,m}\) denotes the all-ones rectangular matrix, and
\[
t_n=\frac1{n^2(n-1)}+\frac2{n^2(n-2)},
\]
\[
c_0=\frac2{n^2(n-1)^2}+\frac2{n^2}+\frac{(n-3)^2}{(n-1)^2},
\]
\[
c_1=\frac2{n^2(n-1)^2}+\frac{(n-4)^2}{2n^2(n-2)^2}+\frac{(n-3)^2}{(n-2)^2(n-1)^2},
\]
\[
c_2=\frac2{n^2(n-1)^2}+\frac8{n^2(n-2)^2}+\frac4{(n-2)^2(n-1)^2}.
\]
These are actual entrywise formulas, including the diagonal and disjoint-edge classes. The independently constructible code in `verify.py` checks them by exact rational spectral projectors.

**3. Complete invariant-sector decomposition.** As \(B\mathbf1_m=(n-1)\mathbf1_n\), the normalized constant vectors on original and edge vertices span a two-dimensional invariant subspace. Its matrix is
\[
\begin{pmatrix}1/2&1/\sqrt{2(n-1)}\\1/\sqrt{2(n-1)}&(n-2)/(n-1)\end{pmatrix},
\]
whose eigenvalues are \(1\) and \((n-3)/(2(n-1))\). On each of the \(n-1\) independent mean-zero original-vertex modes \(v\), the normalized edge partner \(B^\top v/\sqrt{n-2}\) is orthonormal. These pairs have common matrix \(L_n\), since the triangular graph has eigenvalue \(n-4\) on \(\operatorname{im}(B^\top R)\) and the edge block takes the value
\[
c_0+(n-4)c_1-(n-3)c_2=b_n.
\]
The remaining edge space \(\ker B\), dimension \(m-n=n(n-3)/2\), has triangular-graph eigenvalue \(-2\) and eigenvalue
\[
c_0-2c_1+c_2=\eta_n.
\]
These spaces account for all \(n+m\) dimensions. Algebraic simplification gives the displayed determinant of \(L_n\).

**4. Sharp positivity and exceptional ranks.** For \(n\ge5\), \(a_n>0\) and \(\det L_n>0\), so \(L_n\) is positive definite. Both the other nonconstant scalar \((n-3)/(2(n-1))\) and \(\eta_n\) are then positive, and the constant eigenvalue equals one. When \(n=3\), the constant sector eigenvalues are \(1,0\), \(L_3\) has eigenvalues \(1/3,0\) each repeated twice, and \(\ker B\) is empty. Hence rank is three. When \(n=4\), the constant eigenvalues are \(1,1/6\), \(L_4\) has eigenvalues \(1/4,0\) each repeated three times, and \(\eta_4=5/12\) occurs twice. Hence rank is seven. This exhausts all integers \(n\ge3\).

## Verification
Run `python3 verify.py` with Python 3, SymPy and NumPy. The script proves four parameterized algebraic identities symbolically; for every \(n\in\{3,4,5,6,7,8\}\), it constructs the incidence matrix, checks exact rational entries of the full average mixing matrix by two formulas, independently diagonalizes the actual subdivided adjacency matrix and evaluates its spectral projector Schur sum, compares every eigenvalue with the stated indexed spectrum, and tests the exceptional ranks. Successful local replay printed `SYMBOLIC_OK sector_identities=4` and `VERIFY_OK exact_graph_orders=3..8 exact_entries=2882 independent_adjacency_spectra=6`. These finite tests corroborate, but do not replace, the algebraic argument valid for every integer \(n\ge3\).

## Relationship to prior work
Godsil's average-mixing projector formula is used as an established identity, not claimed as new. Coutinho, Godsil, Guo and Zhan develop a general commutant and Gram-matrix account of rank; this does not give the above closed indexed spectrum for the incidence subdivision family. Coutinho, Baptista, Godsil, Spier and Werner give exact algorithms for quantum averages of integral Hamiltonians; the family-specific rank transition is not among the results inspected. Silva, Posner and Portugal define quantum walks between vertices and edges; their detailed complete-graph analysis concerns the *total graph* rather than the bipartite subdivision, and their subdivision discussion motivates further study. A survey of searched sources did not locate a published statement of this complete spectrum or the \(n=5\) rank threshold. This is a literature-search finding, not a proof of priority; general association-scheme results might imply the formula implicitly.

## Limitations
The theorem concerns only single subdivisions of complete graphs and the unweighted adjacency walk. It says nothing about subdivision depth greater than one, irregular base graphs, or instantaneous uniform mixing. The proof is complete subject to the usual finite spectral theorem, but the literature comparison may miss an equivalent theorem stated in the language of design-incidence graphs or association schemes. No independent external audit has been performed.

## References
1. C. Godsil, *Average mixing of continuous quantum walks*, arXiv:1103.2578 (2011), especially the spectral-projector expression.
2. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A new perspective on the average mixing matrix*, arXiv:1709.03591 (first posted 2017), commutant and rank theory.
3. C. F. T. Silva, D. Posner, R. Portugal, *Walking on vertices and edges by continuous-time quantum walk*, arXiv:2206.03375v1 (June 7, 2022), subdivision/total-graph distinction and vertex-edge quantum dynamics.
4. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (August 18, 2022), exact averages of quantum mixing and integral Hamiltonians (MSC 81P68).
