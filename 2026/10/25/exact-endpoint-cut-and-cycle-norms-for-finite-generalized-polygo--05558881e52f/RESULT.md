# Exact endpoint cut and cycle norms for finite generalized polygons

## Finding
Let \(G\) be the unweighted point–line incidence graph of any finite thick generalized \(m\)-gon of order \((s,t)\), where \(m\in\{3,4,6,8\}\), \(s,t\ge2\), each line has \(s+1\) points, and each point lies on \(t+1\) lines. Its girth is \(2m\) and its diameter is \(m\). Orient edges arbitrarily, let \(B\) be the vertex–edge incidence matrix, and put
\[
Q=B^{\mathsf T}(BB^{\mathsf T})^+B,\qquad P=I-Q.
\]
These are the standard Euclidean-orthogonal projections on the real edge coordinate space onto the cut and cycle spaces, respectively.

For \(1\le j\le m\), define the branching products
\[
 a_j=\prod_{i=1}^{j}\begin{cases}s,&i\text{ odd},\\t,&i\text{ even},\end{cases}\qquad
 b_j=\prod_{i=1}^{j}\begin{cases}t,&i\text{ odd},\\s,&i\text{ even}.\end{cases}
\]
The existence of the polygon entails \(a_m=b_m\) by double-counting edges at the middle layer. Define
\[
 R_m(s,t)=\sum_{j=1}^{m-1}\left(\frac1{a_j}+\frac1{b_j}\right)+\frac1{a_m}.
\]
Then, exactly, with no assumption of flag-transitivity,
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=1+\frac{2m-2}{1+R_m(s,t)}}
\]
and
\[
\boxed{\|P\|_{1\to1}=\|P\|_{\infty\to\infty}=\frac{2m}{1+R_m(s,t)}.}
\]
**Every edge column has the displayed absolute column sum.** The two norms therefore depend only on the polygon's girth parameter and order, even for non-flag-transitive realizations.

In the equal-order case \(s=t=q\), which is asserted only when such a polygon exists,
\[
R_m(q,q)=2\sum_{j=1}^{m-1}q^{-j}+q^{-m},\qquad
\|P\|-\|Q\|=\frac{1-R_m(q,q)}{1+R_m(q,q)}.
\]
For \(q=2\) the cut norm is strictly greater than the cycle norm, whereas for each integer \(q\ge3\) the cycle norm is strictly greater. Thus the order-two/order-three threshold is independent of polygon diameter. Along any existing equal-order family with \(q\to\infty\), the cut and cycle norms tend to \(2m-1\) and \(2m\), respectively.

## Assumptions and scope
The incidence graph is finite, connected, simple, bipartite, unweighted, of girth exactly \(2m\), diameter exactly \(m\), and biregular with point degree \(t+1\) and line degree \(s+1\). Thick means \(s,t\ge2\). The classification of possible thick finite polygon diameters is the standard Feit–Higman restriction. In fact the argument applies, without modification, to any finite connected biregular graph of girth \(2m\) and diameter \(m\), including thin cases; those are not needed for the claimed new thick-family classification. The operator norm uses real \(\ell_1(E)\) or \(\ell_\infty(E)\) coordinates and the **canonical orthogonal** projections, not minima over all projections.

## Proof
**1. The two-sided edge-distance partition.** Fix an arbitrary edge \(e=uv\), with \(u\) a point and \(v\) a line. For any vertex \(z\), bipartiteness and adjacency of \(u,v\) imply that \(d(z,u)\) and \(d(z,v)\) differ by exactly one. For \(0\le j<m\) put
\[
 X_j=\{z:d(z,v)=j,\ d(z,u)=j+1\},\qquad
 Y_j=\{z:d(z,u)=j,\ d(z,v)=j+1\}.
\]
The diameter condition makes these \(2m\) sets a partition, with singleton cells \(X_0=\{v\}\) and \(Y_0=\{u\}\).

Any two distinct shortest paths of length smaller than \(m\) between the same vertices would create a cycle of length strictly less than \(2m\), contrary to girth. Thus for \(1\le j<m\), every vertex in \(X_j\) has exactly one neighbor in \(X_{j-1}\), and symmetrically for \(Y_j\). For \(1\le j<m-1\), an edge joining \(X_j\) to \(Y_j\) would give two distinct paths of length \(j+1<m\) from \(v\) to its endpoint in \(Y_j\), again impossible. The remaining neighbors of a vertex in \(X_j\), for \(j<m-1\), therefore lie in \(X_{j+1}\); for \(j=m-1\), they all lie in \(Y_{m-1}\), because no distance can exceed \(m\). The symmetric assertion holds on the \(Y\) side. These neighbor counts depend only on vertex type and layer, so this partition is equitable for the adjacency matrix and for the combinatorial Laplacian.

**2. The weighted quotient cycle.** Contract each cell to one vertex, retaining every edge between cells as a parallel unit-conductance edge. The quotient is a cycle with \(2m\) successive edge bundles. The direct \(X_0Y_0\) bundle has one edge. Starting from \(X_0\) and moving along the other route, the bundles have multiplicities
\[
 a_1,a_2,\ldots,a_{m-1},a_m,b_{m-1},\ldots,b_2,b_1.
\]
Indeed, the first step leaves the line \(v\) in \(s\) ways without taking \(e\); subsequent steps have alternately \(t,s,t,s,\ldots\) choices. From the point \(u\), the reverse branch begins with \(t\) choices and alternates \(s,t,s,t,\ldots\). Counting the central bundle from both sides proves \(a_m=b_m\). A bundle of \(w\) unit parallel edges has effective resistance \(1/w\), so the total series resistance of the route avoiding \(e\) is exactly \(R=R_m(s,t)\).

**3. Passing back to the full graph.** Let \(L=BB^{\mathsf T}\). The real vector subspace of potentials constant on every \(X_j\) and \(Y_j\) is \(L\)-invariant by equitability. The dipole source \(\delta_u-\delta_v\) belongs to it, since its two nonzero coordinates are singleton cells. As \(G\) is connected, the unique solution of \(L\phi=\delta_u-\delta_v\) modulo constants is therefore cell-constant and agrees with the parallel-bundle circuit solution. This proves that **each** edge current within a given bundle has the same magnitude; no automorphism group action is required.

**4. Exact column sums.** The direct unit edge is in parallel with a path of total resistance \(R\). Under unit injected current, the direct-edge current is \(R/(1+R)\), while the full current through every one of the other \(2m-1\) bundles is \(1/(1+R)\), with a consistent sign along the alternative path. Since the cut-projection column \(Q\mathbf e\) is precisely this electrical-current vector, summing absolute currents over all edges gives
\[
 \|Q\mathbf e\|_1=\frac{R+2m-1}{1+R}=1+\frac{2m-2}{1+R}.
\]
The diagonal entry is \(Q_{e,e}=R/(1+R)\). Hence
\[
 \|P\mathbf e\|_1=|1-Q_{e,e}|+\sum_{f\ne e}|Q_{f,e}|
 =1+\|Q\mathbf e\|_1-2Q_{e,e}=\frac{2m}{1+R}.
\]
The same argument applies to **every** choice of \(e\), and the formulas are independent of its location. Symmetry of the matrices \(Q,P\) makes the maximum absolute row sum equal to the maximum absolute column sum, proving both \(\ell_1\) and \(\ell_\infty\) claims.

**5. The equal-order crossover.** If \(s=t=q\), then \(a_j=b_j=q^j\), giving the asserted geometric sum. That sum decreases strictly with \(q\). For \(m\ge3\),
\[
R_m(2,2)=2-3\,2^{-m}>1,\qquad
R_m(3,3)=1-2\,3^{-m}<1.
\]
Consequently \(\|P\|-\|Q\|=(1-R)/(1+R)\) changes sign between orders two and three. Taking \(q\to\infty\) in the formula proves the conditional asymptotics.

## Verification
An exact-rational standalone checker, `gp_exact_verifier.py`, reconstructs the grounded graph Laplacian directly, solves its dipole equations, and recomputes every column of \(Q\) and \(P\) for eight independently constructed incidence graphs. It checks 312 columns without floating-point approximations. The cases include the Fano and ternary projective planes, the generalized quadrangle of order \((2,2)\), rectangular-grid thin quadrangles, an asymmetric complete bipartite graph, and doubled incidence graphs of diameters six and eight. It also checks 70 symbolic equal-order specializations. The thin cases test the general lemma but are not claimed as new. For the Fano incidence graph the norms are \(53/21\) and \(16/7\); for the order-\((2,2)\) quadrangle they are \(47/15\) and \(128/45\). The universal mathematical assertion is established by the preceding proof, not by the finite checks.

Run with standard Python 3: `python3 gp_exact_verifier.py`.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023) develop cycle/cut projection methods in transportation-cost spaces, with specific endpoint calculations for Hamming cubes and an emphasis on tori and Hamming graphs. Their 2018 work establishes general finite-metric and graph-cycle-space frameworks. Neither inspected paper states the present endpoint formulas for generalized-polygon incidence graphs. De Wispelaere and Van Maldeghem (2006) study regular partitions of generalized polygons, providing related combinatorial machinery without these operator norm evaluations. Colangelo, Monzillo and Siciliano (2024) compute a flag association scheme for generalized quadrangles, again a different invariant. These results motivate the equitable reduction but do not directly give the complete two-projection classification or the equal-order crossover as a stated conclusion.

## Limitations
These are canonical Euclidean-orthogonal edge projections, not minimal projection constants among arbitrary real-linear maps. The result does not cover arbitrary non-generalized incidence structures, weighted edges, intermediate \(\ell_p\) norms, or existence of generalized polygons with arbitrary nominal parameters. The equal-order crossover and limit apply only for orders for which the specified finite generalized polygon exists; no existence claim for nonexistent parameter families is intended. Full independent mathematical audit is not asserted.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (2023), arXiv:2305.12582v1, first posted 2023-05-21, https://arxiv.org/abs/2305.12582.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces* (2018), arXiv:1807.03814v1, https://arxiv.org/abs/1807.03814.
3. A. De Wispelaere, H. Van Maldeghem, *Regular partitions of (weak) finite generalized polygons* (2006), https://cage.ugent.be/~hvm/artikels/170.pdf.
4. F. Colangelo, G. Monzillo, A. Siciliano, *The association scheme on the set of flags of a finite generalized quadrangle* (2024), arXiv:2406.03942v1, https://arxiv.org/abs/2406.03942.
