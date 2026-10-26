# Clique–star products: exact endpoint Hodge norms and switching edge directions

## Finding
For integers \(m\ge 2\) and \(k\ge 3\), form the simple, unweighted Cartesian-product graph \(G_{m,k}=K_m\square K_{1,k}\). The star has center indexed by \(0\) and leaves indexed by \(1,\ldots,k\). On real edge coordinates, let \(Q\) be the Euclidean-orthogonal projection onto the cut space and \(P=I-Q\) the complementary cycle projection. Both induced \(\ell_1\) and \(\ell_\infty\) norms are determined exactly below.

There are three edge types: clique-direction edges at the star center (hub), clique-direction edges at a star leaf (leaf), and star-direction edges (spoke). Their absolute column sums for \(Q\) and \(P\), respectively, are:

\[
\begin{array}{c|cc}
\text{edge type}&\sum_f|Q_{fe}|&\sum_f|P_{fe}|\\\hline
\text{hub}&\displaystyle\frac{2(2km-k+m^2-1)}{m(k+m+1)}&\displaystyle\frac{5km-2k+3m^2-3m-6}{m(k+m+1)}\\[5pt]
\text{leaf}&\displaystyle\frac{2(km^2+2km-k+m^3+2m^2-2m-1)}{m(m+1)(k+m+1)}&\displaystyle\frac{3km-2k+3m^2-m-6}{m(k+m+1)}\\[5pt]
\text{spoke}&\displaystyle\frac{5km-3k+3m^2-2m+3}{(m+1)(k+m+1)}&\displaystyle\frac{2(m-1)(3k+2m-1)}{(m+1)(k+m+1)}.
\end{array}
\]

In particular, **a leaf-layer clique edge never maximizes either norm**: the norm is the larger of the corresponding hub and spoke entries. More precisely:

* **Cut projection:** hub edges maximize for \(m=2,3\); at \(m=4\) spoke edges maximize for \(3\le k\le10\), both directions tie at \(k=11\), and hub edges maximize for \(k\ge12\); for \(m\ge5\) spoke edges maximize.
* **Cycle projection:** hub edges maximize for \(2\le m\le5\); at \(m=6\), spoke edges maximize for \(3\le k\le4\) and hub edges for \(k\ge5\); at \(m=7\), spoke edges maximize for \(3\le k\le10\), both tie at \(k=11\), and hub edges maximize for \(k\ge12\); at \(m=8\), spoke edges maximize for \(3\le k\le36\), both tie at \(k=37\), and hub edges maximize for \(k\ge38\); for \(m\ge9\), spoke edges maximize.

Thus the two complementary projections switch their maximizing *directions* along different sharp branching thresholds. For example, at \((m,k)=(4,3)\), \(\|Q\|=47/20\) occurs at spokes while \(\|P\|=21/8\) occurs at hub clique edges; at \((m,k)=(6,3)\), both maxima occur at spokes. Re-entrant hub maximization at sufficiently large branching occurs for the cycle norm when \(m=6,7,8\), but disappears for \(m\ge9\). The values are exact, not asymptotic estimates.

## Assumptions and scope
Each vertex is a pair \((i,t)\), where \(1\le i\le m\) is the clique coordinate and \(0\le t\le k\) is the star coordinate; each graph edge has unit weight. Choose any orientations and form the vertex–edge incidence matrix \(D\). Write \(L=DD^{\mathsf T}\), \(Q=D^{\mathsf T}L^+D\), and \(P=I-Q\). Because these two real matrices are symmetric, each induced \(\ell_\infty\) norm equals the corresponding induced \(\ell_1\) norm. The theorem does not assert optimality among all possibly nonorthogonal projections.

## Proof
**1. Decomposition.** The graph Laplacian is \(L=L_{K_m}\otimes I+I\otimes L_{K_{1,k}}\), where \(L_{K_m}=m(I-J/m)\) and \(J\) is the all-ones matrix. Put \(G=(mI+L_{K_{1,k}})^{-1}\). Direct inversion gives, for distinct star leaves \(r,s\),
\[
G_{00}=\frac{m+1}{m(m+k+1)},\quad G_{0r}=\frac1{m(m+k+1)},\quad G_{rr}=\frac{m(m+k+1)+1}{m(m+1)(m+k+1)},\quad G_{rs}=\frac1{m(m+1)(m+k+1)}.
\]
All these entries are positive and each row sum is \(1/m\).

**2. Horizontal (clique-direction) source.** For an oriented edge \(e\) from \((i,s)\) to \((j,s)\), an electrical potential is \((\mathbf e_i-\mathbf e_j)\otimes G\mathbf e_s\). In star layer \(t\), the sum of absolute voltage drops across clique edges is \(2(m-1)G_{ts}\). Across all star spokes it is \(2\sum_{r=1}^k|G_{0s}-G_{rs}|\). Thus
\[
\sum_f|Q_{fe}|=\frac{2(m-1)}m+2\sum_{r=1}^k|G_{0s}-G_{rs}|.
\]
For \(s=0\), the final sum is \(k/(m+k+1)\); for \(s\ne0\), it is \((m+2k-1)/((m+1)(m+k+1))\). Also \(Q_{ee}=2G_{ss}\). Substituting and using \(\sum_f|P_{fe}|=1+\sum_f|Q_{fe}|-2Q_{ee}\) yields all four horizontal entries in the displayed table.

**3. Vertical (star-direction) source.** Fix a spoke joining \((i,0)\) to \((i,\ell)\). Put \(d=\mathbf e_0-\mathbf e_\ell\) and \(z=Gd\). A potential is
\[
 u=\frac1m\mathbf 1_m\otimes h+(\mathbf e_i-\mathbf 1_m/m)\otimes z,
\]
where \(L_{K_{1,k}}h=d\). The star is a tree, so \(h_0-h_r\) equals \(1\) for \(r=\ell\) and \(0\) otherwise. Explicitly,
\[
 z_0=\frac1{m+k+1},\quad z_\ell=-\frac{m+k}{(m+1)(m+k+1)},\quad z_r=\frac1{(m+1)(m+k+1)}\quad(r\ne\ell).
\]
Write \(a=z_0-z_\ell=(2m+k+1)/((m+1)(m+k+1))\) and \(b=z_0-z_r=m/((m+1)(m+k+1))\) for \(r\ne\ell\). We have \(0<a<1\), \(b>0\), so all relevant absolute-value signs are determined. The sum of absolute drops over horizontal edges is \(2(m-1)(m+k)/((m+1)(m+k+1))\). The sum over vertical edges is \(1+2(m-1)(k-1)/((m+1)(m+k+1))\). Thus the spoke entry for \(Q\) is \(1+2(m-1)(m+2k-1)/((m+1)(m+k+1))\). Its diagonal entry is \(Q_{ee}=(1+(m-1)a)/m\); the same complementary-column identity yields the spoke entry for \(P\).

**4. Location and sharp transitions.** Let \(q_h,q_l,q_s\) denote the three cut entries, and \(p_h,p_l,p_s\) the cycle entries. Exact subtraction gives
\[
q_h-q_l=\frac{2(k-1)(m-1)}{(m+1)(m+k+1)}>0,\qquad
p_h-p_l=\frac{2(k-1)}{m+k+1}>0.
\]
Define the two integer polynomials
\[
A_Q=k(m^2-5m+2)+m^3-4m^2+5m+2,\quad
A_P=k(m^2-9m+2)+m^3-6m^2+11m+6.
\]
The remaining differences are
\[
q_h-q_s=-\frac{A_Q}{m(m+1)(m+k+1)},\qquad
p_h-p_s=-\frac{A_P}{m(m+1)(m+k+1)}.
\]
For \(m=2,3,4\), \(A_Q\) is respectively \(4-4k\), \(8-4k\), \(22-2k\). For \(m\ge5\), both its coefficient of \(k\) and its constant term are positive, the latter being \(m((m-2)^2+1)+2\). For \(m=2,\ldots,8\), \(A_P\) is respectively \(12-12k\), \(12-16k\), \(18-18k\), \(36-18k\), \(72-16k\), \(132-12k\), \(222-6k\). For \(m\ge9\), both its coefficient of \(k\) and its constant term are positive, the latter being \(m((m-3)^2+2)+6\). These complete sign checks prove every transition and tie stated above. \(\square\)

## Verification
An accompanying standalone Python/SymPy script (`checker.py`) proves the four symbolic column-difference identities by exact simplification and independently reconstructs \(Q=D^{\mathsf T}(DD^{\mathsf T})^+D\) using a grounded Laplacian for nine finite graph configurations. The script checks all 406 edge columns exactly, both projections, edge-orbit constancy, and projector idempotence. It also checks the winning-orbit formulas on an integer parameter grid. Run `python checker.py` from a directory with SymPy installed; the expected final message is `CLIQUE_STAR_CERTIFICATE_OK configurations=9 exact_columns=406`. The all-parameter theorem follows from the analytical argument, not from the finite grid.

## Relationship to prior work
The connection between cut/cycle projections and finite transportation or Lipschitz-free spaces, and explicit projection calculations for Hamming graphs and discrete tori, are developed by Dilworth, Kutzarova and Ostrovskii in *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582, public since 2023-05-21). Their Theorem 45 treats hypercube cut projections, while Sections 2.4–2.6 concern discrete tori and Hamming graphs. The clique–star product here has unequal vertex degrees across its star coordinate and is not one of those homogeneous Hamming or toroidal families. Their general framework does not give the above formulas or sharp phase boundaries as a stated consequence.

Their earlier *Lipschitz free spaces on finite metric spaces* (arXiv:1807.03814, public since 2018-07-10) studies general finite metrics and recursive diamond/Laakso graph projections rather than this product-family endpoint calculation. The general transfer-current representation of electrical projection matrices supplies a method, but not the present absolute-column-sum optimization. A previously calculated three-layer special case \(K_m\square P_3=K_m\square K_{1,2}\) falls outside the stated \(k\ge3\) domain and neither determines the new branching thresholds nor implies this theorem for larger stars. A broader unpublished or less-indexed transfer-current norm computation remains a literature risk.

## Limitations
Only the canonical Euclidean-orthogonal projectors on real, unweighted clique–star product graphs are studied. No assertion concerns their minimum norms among arbitrary projections, weighted products, other Banach operator norms, or independent validation. The source results give motivation and terminology; the exact formulas above are derived here rather than attributed to those sources.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public 2023-05-21), https://arxiv.org/abs/2305.12582.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first public 2018-07-10), https://arxiv.org/abs/1807.03814.
3. T. Alberts, *The Burton–Pemantle Theorem*, online lecture notes, section “The Transfer Current Matrix”, https://www.math.utah.edu/~alberts/notes/burton-pemantle/.
