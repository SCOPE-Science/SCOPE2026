# A five-zone edge-insertion law for endpoint cut–cycle projection norms of bicliques

## Finding

Let \(m,n\ge2\) be integers. Form the simple unweighted graph \(H_{m,n}\) by adding one edge between two vertices of the \(m\)-vertex part of \(K_{m,n}\). On the real edge-coordinate space, let \(Q_G\) be the Euclidean-orthogonal projection onto the graph's cut space, and \(P_G=I-Q_G\) its cycle projection. All norms below are induced \(\ell_1\)-operator norms (equivalently induced \(\ell_\infty\)-norms).

For the intact bipartite graph set
\[
q_0=\|Q_{K_{m,n}}\|=3-\frac2m-\frac2n+\frac2{mn},\qquad
p_0=\|P_{K_{m,n}}\|=\frac{4(m-1)(n-1)}{mn}.
\]
Define
\[
d(m,n)=\begin{cases}
\dfrac{2-n}{n(n+2)},&m\le n+2,\\[3pt]
\dfrac1{n+2}-\dfrac{2(n-1)}{mn},&m\ge n+2.
\end{cases}
\]
The two branches agree at \(m=n+2\). The **exact** cut-projection norm of the augmented graph is
\[
\boxed{\|Q_{H_{m,n}}\|=\begin{cases}
\dfrac{2(n+1)}{n+2},&m=2,\\[3pt]
q_0+\max\{0,d(m,n)\},&m\ge3.
\end{cases}}
\]
Put \(h(m,n)=d(m,n)+2/[n(n+2)]\). The **exact** cycle-projection norm is
\[
\boxed{\|P_{H_{m,n}}\|=\begin{cases}
\dfrac{3n}{n+2},&m=2,\\[3pt]
p_0+\dfrac{4-n}{n(n+2)},&m=3,\ n\in\{2,3\},\\[4pt]
\dfrac{3n}{n+2},&m=3,\ n\ge4,\\[3pt]
p_0+\max\{0,h(m,n)\},&m\ge4.
\end{cases}}
\]

For each fixed integer \(n\ge5\), the comparison with the intact biclique has **five complete and sharp parameter zones**, where signs refer to the respective norm changes \(\|Q_H\|-q_0\) and \(\|P_H\|-p_0\):

| Condition on \(m\) | Cut change | Cycle change |
| --- | --- | --- |
| \(m=2\) | strictly negative | strictly positive |
| \(m=3\) | zero | strictly positive |
| \(4\le m\le2n-2\) | zero | zero |
| \(2n-1\le m\le2n+1\) | zero | strictly positive |
| \(m\ge2n+2\) | strictly positive | strictly positive |

In particular, adding a graph edge can *lower*, preserve, or raise the endpoint cut-projection norm, while the cycle-projection norm never decreases in this family. The two large-part onset indices differ by exactly three.

## Assumptions and scope

All graphs are finite, simple, connected, unweighted, and equipped with the standard real edge-coordinate space \(\mathbb R^{E(G)}\). Choose any edge orientations and write \(B_G\) for the vertex–edge incidence matrix. Its Euclidean cut projection is
\[
Q_G=B_G^{\mathsf T}(B_GB_G^{\mathsf T})^+B_G,
\]
where the superscript \(+\) denotes the Moore–Penrose inverse. Its complementary cycle projection is \(P_G=I-Q_G\). These are canonical orthogonal projections, not minima over *all* possibly nonorthogonal projections. Their symmetric matrices have identical induced \(\ell_1\) and \(\ell_\infty\) norms. The edge orientations do not affect those norms.

## Proof

Label the \(m\)-part \(x_0,\ldots,x_{m-1}\), the other part \(y_0,\ldots,y_{n-1}\), orient intact edges \(x_i\to y_j\), and orient the new edge \(x_0\to x_1\). In the edge basis of the intact graph, the cut projector has the explicit kernel
\[
(Q_0)_{(i,j),(k,\ell)}
=\frac{\mathbf1_{i=k}}n+\frac{\mathbf1_{j=\ell}}m-\frac1{mn}.
\tag{1}
\]
Indeed, the orthogonal cycle projection on \(m\times n\) matrices is \(X\mapsto H_mXH_n\), where \(H_r=I_r-\mathbf1_r\mathbf1_r^{\mathsf T}/r\). Taking one absolute column sum of (1) and of its complement gives \(q_0,p_0\) above.

Let \(b=\mathbf e_{x_0}-\mathbf e_{x_1}\) be the new incidence vector, and let \(L_0\) be the old graph Laplacian. As \(L_0b=nb\), one has \(L_0^+b=b/n\) and \(b^{\mathsf T}L_0^+b=2/n\). The rank-one inverse identity on the zero-sum subspace gives
\[
(L_0+bb^{\mathsf T})^+=L_0^+-\frac{bb^{\mathsf T}}{n(n+2)}.
\tag{2}
\]
Set \(s_i=1\) for \(i=0\), \(s_i=-1\) for \(i=1\), and \(s_i=0\) otherwise. Equations (1)–(2) yield **every** matrix entry of the augmented cut projection:
\[
Q_{(i,j),(k,\ell)}=(Q_0)_{(i,j),(k,\ell)}-\frac{s_is_k}{n(n+2)},\quad
Q_{(i,j),\mathrm{new}}=\frac{s_i}{n+2},\quad
Q_{\mathrm{new},\mathrm{new}}=\frac2{n+2}.
\tag{3}
\]
All identities hold for the entire integer range, including \(m=n=2\).

There are at most three column types. **Far** old-edge columns have \(i\ge2\), so their cut/cycle absolute sums equal \(q_0,p_0\). **New-edge** column sums are
\[
q_{\mathrm{new}}=\frac{2(n+1)}{n+2},\qquad
p_{\mathrm{new}}=\frac{3n}{n+2}.
\tag{4}
\]
For a **touched** old-edge column with \(i\in\{0,1\}\), only entries in its own row, the opposite touched row, and the new-edge coordinate differ from the old projector. The opposite-row off-diagonal entries \(-1/(mn)\) become \(1/[n(n+2)]-1/(mn)\). Taking absolute values and simplifying gives
\[
q_{\mathrm{touch}}=q_0+d(m,n).
\tag{5}
\]
The diagonal cut entry falls by \(1/[n(n+2)]\) while remaining strictly between zero and one, so the complementary cycle column satisfies
\[
p_{\mathrm{touch}}=p_0+d(m,n)+\frac{2}{n(n+2)}=p_0+h(m,n).
\tag{6}
\]
Thus (4)–(6) exhaust **all** columns and prove the exact maximum expressions.

It remains to identify the maximizers without hidden exceptional cases. When \(m=2\), no far column exists, and (4)–(6) give \(q_{\mathrm{touch}}=q_{\mathrm{new}}\) and \(p_{\mathrm{new}}>p_{\mathrm{touch}}\). When \(m\ge3\), \(q_0>q_{\mathrm{new}}\): \(q_0\) increases in \(m\), and at \(m=3\) their difference is \((n^2+4n-8)/[3n(n+2)]>0\). This proves the displayed cut formula.

When \(m=3\), direct subtraction gives
\[
p_{\mathrm{new}}-p_0=\frac{(n-4)^2}{3n(n+2)},\qquad
p_{\mathrm{touch}}-p_{\mathrm{new}}=\frac{(4-n)(n-1)}{3n(n+2)}.
\tag{7}
\]
For \(m\ge4\), \(p_0\ge p_{\mathrm{new}}\): its minimum at \(m=4\) exceeds the latter by \(3(n-2)/[n(n+2)]\ge0\). These comparisons prove the displayed cycle formula.

Finally fix \(n\ge5\). For \(m\ge4\), the sign of \(h(m,n)\) is positive precisely when \(m>2n-2\); otherwise its maximum with zero vanishes. The sign of \(d(m,n)\) is positive precisely when \(m>2(n-1)(n+2)/n=2n+2-4/n\). Since \(2n+1<2n+2-4/n<2n+2\), the corresponding *integer* onset is \(m=2n+2\). The cases \(m=2,3\) follow from (4) and (7). This proves the five-zone table without asymptotics or numerical extrapolation. \(\square\)

## Verification

`check_projection.py` is a standalone Python standard-library verifier. It builds the grounded graph Laplacian, computes its inverse with exact rational Gaussian elimination, reconstructs every cut and cycle projection entry, and compares all absolute column sums against (4)–(6), the unrestricted maximum formulas, and the five-zone signs. Running `python check_projection.py` checks 58 parameter pairs: all \(2\le m,n\le8\), plus nine pairs on the \(n=5,6\) phase boundaries, comprising 1,858 columns in total, and reports `GRAPH_PROJECTION_CERTIFICATE_OK`. This finite check is corroboration, not the proof of the universal integer statements; those follow from (1)–(7).

## Relationship to prior work

The graph-metric realization of Lipschitz-free spaces as quotients of edge \(\ell_1\) spaces by the cycle space, and the relevance of cycle projections, appear in Dilworth–Kutzarova–Ostrovskii (2018). Their detailed applications treat recursively generated diamond and Laakso graphs. Dilworth–Kutzarova–Ostrovskii (2020) analyze projections and their norms on Laakso/diamond graphs. Basso (2021) establishes general connections between finite Lipschitz extension constants and relative projection constants. Those frameworks do not state the two-parameter edge-insertion phase diagram proved here. The known intact-biclique values and the Laplacian rank-one identity are inputs, not claimed new results.

The new structural content is the *joint* five-zone classification for the two canonical projectors under an **intrapart** edge addition. It is not implied by a one-cross-edge deletion calculation on a biclique or by a numerical example of graph-edge insertion. Literature searches revealed no covering published exact classification, but unindexed electrical-network calculations remain a genuine bibliographic risk.

## Limitations

The theorem applies to the specific unweighted graph family and canonical **Euclidean-orthogonal** cut and cycle projections acting on real edge coordinates. It makes no claim about the smallest norms among arbitrary nonorthogonal projections, weighted edges, multi-edge perturbations, or other graph families. The result has not undergone independent mathematical validation.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, first public preprint 2018-07-10, arXiv:1807.03814, https://arxiv.org/abs/1807.03814.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Analysis on Laakso graphs with application to the structure of transportation cost spaces*, first public preprint 2020-07-15, arXiv:2007.07949, https://arxiv.org/abs/2007.07949.
3. G. Basso, *Absolute Lipschitz extendability and linear projection constants*, first public preprint 2021-04-29, arXiv:2104.14238, https://arxiv.org/abs/2104.14238.
