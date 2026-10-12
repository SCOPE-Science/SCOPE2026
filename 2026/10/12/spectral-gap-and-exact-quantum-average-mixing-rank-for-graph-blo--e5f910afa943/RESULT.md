# Spectral gap and exact quantum average-mixing rank for graph blow-ups

## Finding
Let \(G\) be **any finite simple undirected graph** on \(n\geq1\) vertices. For each integer \(m\geq2\), let its independent-fibre blow-up be \(B_m(G)=G[\overline{K_m}]\), so its adjacency matrix in base-first vertex order is \(A(G)\otimes J_m\). For a graph \(H\), let
\[
\widehat M(H)=\lim_{T\to\infty}\frac1T\int_0^T e^{\mathrm{i}tA(H)}\circ e^{-\mathrm{i}tA(H)}\,dt.
\]
Let \(E_0\) be the orthogonal projector onto \(\ker A(G)\) (zero if \(A(G)\) is invertible), and set \(d_u=(E_0)_{uu}\). The complete spectrum of \(\widehat M(B_m(G))\), **with multiplicities**, is the union of
\[
\left\{\frac{m-1+\lambda}{m}:\lambda\in\operatorname{Spec}(\widehat M(G))\right\}
\]
and, for each vertex \(u\in V(G)\), the eigenvalue
\[
\frac{m-2+2d_u}{m}\quad\text{of multiplicity }m-1.
\]
Here repeated values are counted with their combined multiplicities. In particular,
\[
\boxed{\operatorname{rank}\widehat M(B_m(G))=
\begin{cases}
n+|\{u:d_u>0\}|,&m=2,\\
nm,&m\geq3.
\end{cases}}
\]
For every \(m\geq3\), the **universal sharp spectral bound** is
\[
\widehat M(B_m(G))\succeq\frac{m-2}{m}I_{nm}.
\]
Equality in this lower eigenvalue bound occurs for every base graph with invertible adjacency matrix (for example \(K_2\)). At \(m=2\), the kernel is exactly the span of the antisymmetric clone-pair vectors \(e_u\otimes(1,-1)\) for vertices satisfying \(d_u=0\). Equivalently, the nullity counts the pairs of strongly cospectral clones, using the characterization in Bhattacharjya–Monterde–Pal.

## Assumptions and scope
Every graph is finite, undirected, unweighted and loopless; disconnected graphs and isolated vertices are allowed. Only equal-size independent fibres are considered. The standard adjacency-Hamiltonian, one-excitation continuous-time walk and uniform long-time Cesàro average are used. The limit exists for all such graphs, because their adjacency matrices have finitely many real eigenvalues. No assumption of distinct eigenvalues, regularity, connectedness or invertibility is imposed. \(\operatorname{Spec}\) denotes eigenvalue multisets of real symmetric matrices, and \(\succeq\) the positive-semidefinite order.

## Proof
Write \(A=A(G)\), and let \(\{E_\lambda\}\) be the orthogonal spectral projectors for its distinct real eigenvalues. Put \(P_m=J_m/m\) and \(Q_m=I_m-P_m\). As
\[
A(B_m(G))=A\otimes J_m=mA\otimes P_m,
\]
its nonzero-eigenvalue spectral projectors are \(E_\lambda\otimes P_m\), one for each nonzero \(\lambda\) of \(A\). The projector at eigenvalue zero is
\[
F_0=E_0\otimes P_m+I_n\otimes Q_m.
\]
Indeed \(E_0\otimes P_m\) and \(I_n\otimes Q_m\) are orthogonal projectors with orthogonal ranges; their sum complements the nonzero spectral projectors. This also covers \(E_0=0\) and \(A=0\).

For every real-symmetric adjacency matrix \(H\), spectral expansion of the matrix exponential and Cesàro cancellation of unequal frequencies give
\[
\widehat M(H)=\sum_\theta F_\theta\circ F_\theta.
\]
Using this identity for the blow-up, set \(R=\widehat M(G)\) and \(D_0=\operatorname{diag}(d_u:u\in V(G))\). Expanding \(F_0\circ F_0\) and adding the nonzero contributions yields
\[
\widehat M(B_m(G))=
R\otimes(P_m\circ P_m)+2D_0\otimes(P_m\circ Q_m)+I_n\otimes(Q_m\circ Q_m).
\]
The three elementary identities
\[
P_m\circ P_m=\frac{J_m}{m^2},\qquad
P_m\circ Q_m=\frac{Q_m}{m},\qquad
Q_m\circ Q_m=\frac{m-2}{m}I_m+\frac{J_m}{m^2}
\]
therefore give the exact matrix formula
\[
\boxed{\widehat M(B_m(G))=
\frac1{m^2}R\otimes J_m+\frac2m D_0\otimes Q_m+
I_n\otimes\left(\frac{m-2}{m}I_m+\frac{J_m}{m^2}\right).}
\]
To diagonalize it, split the real vertex space orthogonally as
\[
\mathbb R^n\otimes\operatorname{span}\{\mathbf1_m\}\ \oplus\
\bigoplus_{u\in V(G)}\left(\operatorname{span}\{e_u\}\otimes\mathbf1_m^\perp\right).
\]
On the first summand, \(J_m\) acts by \(m\), \(Q_m\) vanishes, and the operator is exactly \((R+(m-1)I_n)/m\). On each second summand, \(J_m\) vanishes and \(Q_m\) acts as the identity, leaving the scalar \((m-2+2d_u)/m\). These mutually orthogonal invariant subspaces exhaust all \(nm\) dimensions, proving the claimed multiset including multiplicities.

Each \(E_\lambda\) is positive semidefinite; the Schur product theorem makes \(R=\sum E_\lambda\circ E_\lambda\) positive semidefinite. Also \(d_u=e_u^TE_0e_u=\|E_0e_u\|^2\geq0\). Thus the first spectral family is bounded below by \((m-1)/m>0\). The second family is at least \((m-2)/m\), which is positive for \(m\geq3\). For \(m=2\) the second-family eigenvalue equals \(d_u\), so its nullity is exactly the number of vertices with \(d_u=0\). The orthogonal decomposition identifies its nullvectors explicitly. Since all components have been considered, there are no additional zeros. If \(A\) is invertible, \(E_0=0\), and the bound is attained on every nonconstant fibre direction. This proves the full rank classification and sharp gap.

Finally, for a projection, \(d_u=0\iff E_0e_u=0\), so the exact zero criterion is that eigenvalue zero is absent from the adjacency eigenvalue support of \(u\). Theorem 2(2) of Bhattacharjya–Monterde–Pal identifies precisely this condition with strong cospectrality of the two cloned vertices in the two-fold blow-up. This establishes the stated transport interpretation.

## Verification
The self-contained checker `artifacts/verify.py` uses SymPy and NumPy (tested in Python 3). Run `python3 artifacts/verify.py` in the directory containing `artifacts/`. It recomputes all spectral projectors algebraically, rather than importing the claimed formula to obtain the direct average, for 14 exact graph/fibre-size cases. It also constructs 54 numerical blow-up projectors independently for randomly generated base graphs and compares the resulting matrix to the formula. Expected output begins `VERIFY_OK exact_matrices=14 numerical_matrices=54` and includes the two-fold blow-up ranks \(5/6\) for \(P_3\) and \(7/8\) for \(K_{1,3}\). Algebraic and numerical examples corroborate the calculation; the proof above establishes the unrestricted theorem.

## Relationship to prior work
Coutinho–Baptista–Godsil–Spier–Werner, *Irrational quantum walks*, develops exact average-mixing methods and states the general Schur-square spectral-projector identity. Bhattacharjya–Monterde–Pal, *Quantum walks on blow-up graphs*, gives the adjacency and spectral projectors for independent-set blow-ups, and separately characterizes strong cospectral clone pairs. Neither inspected paper states the present **full average-mixing spectrum, universal positive-definite gap, or exact rank dichotomy**. The formula arises by combining these known starting points with a separate Schur-square expansion and a two-sector diagonalization. The earlier literature on average mixing, including Coutinho–Godsil–Guo–Zhan, develops general rank theory without this equal-fibre classification. Baptista–Coutinho–Marques studies alternative sampling distributions; the present result concerns only the ordinary long-time average.

## Limitations
The spectral theorem is for equal-size independent-fibre blow-ups and the adjacency Hamiltonian, not arbitrary lexicographic factors, irregular fibre sizes, graph Laplacians or time-sampling laws. It does not characterize individual state-transfer amplitudes. The lower bound is sharp for invertible bases but need not be attained for singular bases. The results are not a claim of novelty for the pre-existing spectral projectors or Schur-square formula; possible previously unnoticed equivalent rank consequences of these results remain a literature risk. The explicit eigenvalues on the clone-constant sector still depend on \(\widehat M(G)\). Independent audit has not been performed.

## References
1. G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1, first posted 2022-08-18, especially Section 2. https://arxiv.org/abs/2208.08971
2. B. Bhattacharjya, H. Monterde, H. Pal, *Quantum walks on blow-up graphs*, arXiv:2308.13887v2 (first publicly posted 2023-08-26), especially Sections 3–4 and Theorem 2(2). https://arxiv.org/abs/2308.13887
3. G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (2017), especially Sections 1 and 5. https://arxiv.org/abs/1709.03591
4. P. Baptista, G. Coutinho, V. Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378v1 (2023), especially Section 2. https://arxiv.org/abs/2308.16378
