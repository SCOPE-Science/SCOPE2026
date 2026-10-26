# Sharp three-orbit Hodge projection transitions for three-layer clique strips

## Finding
For each integer \(n\ge 2\), form the connected graph \(G_n=K_n\square P_3\): three complete \(n\)-vertex layers indexed by \(s=0,1,2\), with corresponding vertices joined between layers \(0,1\) and \(1,2\). Orient its edges arbitrarily. On \(\ell_1(E(G_n);\mathbb R)\), let \(Q_n\) be the canonical Euclidean orthogonal projection onto the cut space and \(C_n=I-Q_n\) its complementary cycle projection.

The complete absolute-column-sum spectra consist of precisely three symmetry types. Write \(h_e,h_m,v\) for \(\ell_1\) column norms of \(Q_n\) on, respectively, an outer-layer clique edge, a middle-layer clique edge, and a vertical matching edge:
\[
h_e=\frac{2(n^2+n-1)}{n(n+1)},\qquad
h_m=\frac{2(n^2+4n-3)}{n(n+3)},\qquad
v=\frac{3n-1}{n+1}.
\]
The corresponding column norms of \(C_n\) are
\[
c_e=\frac{3n^2+5n-10}{n(n+3)},\qquad
c_m=\frac{(n-1)(3n+10)}{n(n+3)},\qquad
c_v=\frac{2(n-1)(2n+5)}{(n+1)(n+3)}.
\]
In particular, **the exact endpoint operator norms** are
\[
\|Q_n\|_{1\to1}=\|Q_n\|_{\infty\to\infty}
=\begin{cases}
\frac95,&n=2,\\[2pt]
\frac{3n-1}{n+1},&n\ge3,
\end{cases}
\]
and
\[
\|C_n\|_{1\to1}=\|C_n\|_{\infty\to\infty}
=\begin{cases}
\frac{(n-1)(3n+10)}{n(n+3)},&2\le n\le5,\\[2pt]
\frac{2(n-1)(2n+5)}{(n+1)(n+3)},&n\ge6.
\end{cases}
\]
The maximizing edge changes type at distinct sharp integer thresholds: the cut norm moves from middle horizontal to vertical at \(n=3\) (tie there), while the cycle norm moves at \(n=5\) (tie there). The cut norm exceeds the cycle norm at \(n=2\); the cycle norm strictly exceeds the cut norm at every \(n\ge3\).

## Assumptions and scope
All graphs are finite, simple, connected, unweighted and undirected before an arbitrary choice of orientation. \(P_3\) is the three-vertex path, **not** the three-cycle. Let \(D:\mathbb R^{E(G_n)}\to\mathbb R^{V(G_n)}\) denote signed vertex-edge incidence (\(-1\) at the tail, \(+1\) at the head). The cycle subspace is \(Z=\ker D\), and the cut subspace is \(B=\operatorname{ran}D^{\mathsf T}=Z^\perp\) for the standard Euclidean edge inner product. With \(L=DD^{\mathsf T}\) and its Moore–Penrose inverse \(L^+\), the canonical cut projection is \(Q_n=D^{\mathsf T}L^+D\). The theorem computes the \(\ell_1\)- and \(\ell_\infty\)-operator norms of these **particular** projections, not the minimum norm over all projections onto either subspace. Both endpoint norms agree because each projection matrix is real symmetric.

## Proof
**1. Complete-graph mode decomposition.** Regard vertex potentials as arrays indexed by a clique vertex \(i\in\{1,\dots,n\}\) and layer \(s\in\{0,1,2\}\). The graph Laplacian is the Kronecker sum
\[
L=(nI_n-J_n)\otimes I_3+I_n\otimes L_P,\qquad
L_P=\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix}.
\]
The clique-constant mode gives \(L_P\); every clique-mean-zero mode gives \(nI_3+L_P\). The latter has inverse
\[
R=\frac1{n(n+1)(n+3)}
\begin{pmatrix}
n^2+3n+1&n+1&1\\
n+1&(n+1)^2&n+1\\
1&n+1&n^2+3n+1
\end{pmatrix}.
\]
All its entries are positive, and every column sums to \(1/n\).

**2. Horizontal source edge.** Take a unit source edge between two distinct clique vertices \(a,b\) at layer \(\ell\), so that the divergence vector is \((e_b-e_a)\otimes e_\ell\). Its unique zero-mean potential is \((e_b-e_a)\otimes Re_\ell\). At layer \(s\), only horizontal edges meeting \(a\) or \(b\) carry current; the sum of their absolute magnitudes equals \(2(n-1)R_{s\ell}\). Across layer interface \(s,s+1\), the total absolute vertical current is \(2|R_{s+1,\ell}-R_{s\ell}|\). Hence the absolute cut-column sum is
\[
2(n-1)\sum_{s=0}^2R_{s\ell}+2\sum_{s=0}^1|R_{s+1,\ell}-R_{s\ell}|
=\frac{2(n-1)}n+2\,\operatorname{TV}(Re_\ell).
\]
Direct substitution yields \(\operatorname{TV}(Re_0)=\operatorname{TV}(Re_2)=1/(n+1)\) and \(\operatorname{TV}(Re_1)=2/(n+3)\), giving \(h_e,h_m\). The projection's diagonal entry for the source edge is \(2R_{\ell\ell}\). Because \(0<(Q_n)_{ee}<1\), the complementary projection has column sum
\(\|C_ne\|_1=1+\|Q_ne\|_1-2(Q_n)_{ee}\).
This gives \(c_e,c_m\).

**3. Vertical source edge.** Take the unit edge joining clique vertex \(a\) from layer \(0\) to \(1\); layer reflection treats the other vertical orbit. Put \(d=(-1,1,0)^{\mathsf T}\) and \(w=Rd\). A convenient potential (defined modulo an additive constant) for the point injection is
\[
p_{i,s}=\frac{\phi_s}{n}+(\delta_{ia}-\frac1n)w_s,
\qquad L_P\phi=d.
\]
Here
\[
w_0=-\frac{n+2}{(n+1)(n+3)},\qquad
w_1=\frac1{n+3},\qquad
w_2=\frac1{(n+1)(n+3)}.
\]
The horizontal absolute current sum is \((n-1)(|w_0|+|w_1|+|w_2|)\). Since \(\phi_1-\phi_0=1\) and \(0<w_1-w_0<1\), all currents across the first vertical interface have the same sign and their total is \(1\); those across the second have total absolute magnitude \(2(n-1)|w_2-w_1|/n\). Consequently,
\[
\|Q_ne\|_1=1+(n-1)\sum_{s=0}^2|w_s|+\frac{2(n-1)}n|w_2-w_1|=\frac{3n-1}{n+1}=v.
\]
The diagonal transfer current is
\[
(Q_n)_{ee}=\frac1n+\frac{n-1}{n}(w_1-w_0)
=\frac1n+\frac{(n-1)(2n+3)}{n(n+1)(n+3)}.
\]
The complementary-column identity above produces \(c_v\).

**4. Exhaustion and sharp transitions.** Permuting clique vertices and reflecting the path makes exactly the three source-edge types exhaustive. Direct simplification gives
\[
h_m-h_e=\frac{2(n-1)}{(n+1)(n+3)}>0,
\quad v-h_m=\frac{(n-3)(n-1)(n+2)}{n(n+1)(n+3)},
\]
\[
c_m-c_e=\frac2{n+3}>0,
\quad c_v-c_m=\frac{(n-5)(n-1)(n+2)}{n(n+1)(n+3)}.
\]
Thus the claimed maxima and ties follow for every integer \(n\ge2\). At \(n=2\), \(\|Q_2\|=9/5>8/5=\|C_2\|\). For \(3\le n\le5\), the difference \(\|C_n\|-\|Q_n\|=2(n^2-5)/[n(n+1)(n+3)]>0\); for \(n\ge6\) it equals \((n^2-2n-7)/[(n+1)(n+3)]>0\). This concludes the proof.

## Verification
The supplied standalone `CHECKER.py` constructs the complete signed incidence matrix, computes the reduced graph Laplacian inverse in exact rational arithmetic, reconstructs every cut and complementary cycle column, and compares its absolute sum with the independently stated three-orbit formulas. For each integer \(2\le n\le8\), all \(322\) columns across seven graph instances passed. This is a **finite regression check**; the all-integer theorem follows from the analytical proof above.

## Relationship to prior work
Dilworth, Kutzarova, and Ostrovskii [1] develop the cut/cycle projection framework and explicitly analyze discrete tori and Hamming graphs, including canonical projections of the Hamming cube. Their Hamming factors are complete graph factors; the path factor \(P_3\) in the present graph is not complete. Their stated computations do not determine the three edge-orbit spectra above. Ostrovska and Ostrovskii [2] provide the transportation-cost quotient representation and underlying graph-cycle framework but do not evaluate the present endpoint projection norms. Previously determined two-layer clique-prism and rectangular rook-graph constants concern distinct Cartesian factors. General clique-factor comparison bounds and limiting values do not imply the finite three-layer rational formulas or the two distinct maximizing-edge thresholds.

## Limitations
No global minimality over arbitrary, potentially nonorthogonal projections is claimed. Only real endpoint operator norms are determined, not intermediate \(\ell_p\) operator norms. The asymptotic limits \(\|Q_n\|\to3\) and \(\|C_n\|\to4\) are compatible with general clique-factor limits and are not presented as an independent asymptotic advance. An equivalent expression in less-indexed electrical-network literature remains possible. The proof and checker have not undergone independent mathematical audit.

## References
[1] S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, 2023 preprint arXiv:2305.12582; Proceedings of Symposia in Pure Mathematics 106 (2024), 97–131. https://arxiv.org/abs/2305.12582

[2] S. Ostrovska and M. I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689 (2021). https://arxiv.org/abs/2112.02689
