# Exact endpoint Hodge norms and an edge-orbit reversal for complete multipartite graphs

## Finding

Let \(r\ge 2\), let \(n_1,\ldots,n_r\) be positive integers, and put \(N=\sum_{i=1}^r n_i\). On the unweighted complete multipartite graph \(G=K_{n_1,\ldots,n_r}\), let \(Q\) be the Euclidean orthogonal projection of the real edge-coordinate space onto the cut space, and let \(C=I-Q\) project onto the cycle-flow space. Define, for \(1\le s<N\),
\[
F_N(s)=1+\frac{s}{N}-\frac{2(N-1)}{N(N-s)},\qquad
H_N(s)=1+\frac{s}{N}-\frac{4(N-1)}{N(N-s)}.
\]
Then the exact endpoint operator norms are
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}
=\max_{1\le i<j\le r}(F_N(n_i)+F_N(n_j)),}
\]
\[
\boxed{\|C\|_{1\to1}=\|C\|_{\infty\to\infty}
=1+\max_{1\le i<j\le r}(H_N(n_i)+H_N(n_j)).}
\]
An edge attaining the cut-projection norm always exists between two largest parts. In contrast, for every integer \(N\ge6\), the graph \(K_{N-3,2,1}\) has cut-norm-maximizing edges between the largest and middle parts, but cycle-norm-maximizing edges between the two smaller parts. In this family the norms are, respectively,
\[
\boxed{\frac{7N^2-21N+8}{3N(N-2)}},\qquad
\boxed{\frac{(N-3)(3N-2)}{N(N-2)}},
\]
and the cycle norm exceeds the cut norm by \(2(N-5)(N-1)/(3N(N-2))>0\).

## Assumptions and scope

The graph has one undirected unit-conductance edge between every pair of vertices belonging to different parts and no other edges. It is connected because \(r\ge2\) and every part is nonempty. Choose any orientation of its edges. If \(D\) is the vertex-by-edge incidence matrix and \(L=DD^{\mathsf T}\), then \(Q=D^{\mathsf T}L^+D\), where \(L^+\) is the Moore--Penrose pseudoinverse. The operators act on the real coordinate spaces \(\ell_1(E)\) and \(\ell_\infty(E)\) with no edge weights. The assertion concerns these **canonical orthogonal projections** and does not determine minimum norms over all projections with the same range. Parts of size one, bipartite graphs, and the tree/star boundary are included. On a tree the cycle projection is zero.

## Proof

**Step 1: Exact potential for one edge.** Choose an edge with endpoints \(a\in V_i\), \(b\in V_j\), where \(i\ne j\), and write \(s=n_i\), \(t=n_j\), \(d_s=N-s\), \(d_t=N-t\),
\[
\alpha=\frac1{Nd_s},\qquad \beta=\frac1{Nd_t}.
\]
Consider the vertex potential \(u\) whose values are
\[
\begin{array}{c|ccccc}
\text{vertex type}&a&V_i\setminus\{a\}&b&V_j\setminus\{b\}&V\setminus(V_i\cup V_j)\\\hline
u&(N-1)\alpha&-\alpha&-(N-1)\beta&\beta&0.
\end{array}
\]
The entries sum to zero. For any vertex \(x\in V_h\), the complete multipartite Laplacian satisfies
\[
(Lu)_x=(N-n_h)u_x-\sum_{y\notin V_h}u_y.
\]
The total potential on \(V_i\) is \((N-s)\alpha=1/N\), and that on \(V_j\) is \(-(N-t)\beta=-1/N\); all other part sums vanish. Substitution shows \(Lu=e_a-e_b\) at every vertex. Hence \(u=L^+(e_a-e_b)\) and the \(a b\) column of \(Q\) is the signed edge-gradient of \(u\), independent of the arbitrary orientations up to entry signs.

**Step 2: Absolute column sum.** There are eight possibly nonzero types of edge current. With \(w=N-s-t\) other vertices, their absolute magnitudes and multiplicities are
\[
\begin{array}{c|c|c}
\text{endpoints}&\text{count}&\text{magnitude}\\\hline
(a,b)&1&(N-1)(\alpha+\beta)\\
(a,V_j\setminus\{b\})&t-1&(N-1)\alpha-\beta\\
(V_i\setminus\{a\},b)&s-1&(N-1)\beta-\alpha\\
(V_i\setminus\{a\},V_j\setminus\{b\})&(s-1)(t-1)&\alpha+\beta\\
(a,\text{other parts})&w&(N-1)\alpha\\
(V_i\setminus\{a\},\text{other parts})&(s-1)w&\alpha\\
(b,\text{other parts})&w&(N-1)\beta\\
(V_j\setminus\{b\},\text{other parts})&(t-1)w&\beta.
\end{array}
\]
The two displayed differences are nonnegative: for instance \((N-1)\alpha\ge\beta\) is equivalent to \((N-1)(N-t)\ge N-s\), immediate from \(N-t\ge1\) and \(N-s\le N-1\). All edges between two untouched parts carry zero current. Thus the complete absolute column sum simplifies exactly to
\[
S_{s,t}=
\frac{N^2-2N+2-s^2}{N(N-s)}
+\frac{N^2-2N+2-t^2}{N(N-t)}
=F_N(s)+F_N(t).
\]
Since the induced \(\ell_1\) norm of a matrix is its maximum absolute column sum, this establishes the formula for \(Q\).

**Step 3: Complementary projection.** The diagonal of that column is the effective resistance
\[
R_{s,t}=u_a-u_b=\frac{N-1}{N}\left(\frac1{N-s}+\frac1{N-t}\right).
\]
It lies in \([0,1]\), as an edge of unit resistance exists directly between the terminals (or by the projection identity \(0\le Q_{ee}\le1\)). All off-diagonal entries of \(C=I-Q\) are negatives of those of \(Q\), while its diagonal has absolute value \(1-R_{s,t}\). Consequently the absolute column sum of \(C\) is
\[
1+S_{s,t}-2R_{s,t}=1+H_N(s)+H_N(t),
\]
which proves the second norm formula. Both matrices are real symmetric, so their \(\ell_\infty\) norms equal their \(\ell_1\) norms.

**Step 4: Maximizing edge types.** For \(s>t\), direct subtraction gives
\[
F_N(s)-F_N(t)=\frac{s-t}{N}\left(1-\frac{2(N-1)}{(N-s)(N-t)}\right),
\]
\[
H_N(s)-H_N(t)=\frac{s-t}{N}\left(1-\frac{4(N-1)}{(N-s)(N-t)}\right).
\]
For any two distinct classes of a graph with at least three parts, put \(w=N-s-t\ge1\). Then
\[
(N-s)(N-t)-2(N-1)
=(s-1)(t-1)+(w-1)(s+t+w-1)\ge0.
\]
Thus among the part sizes actually present, \(F_N\) is nondecreasing, and an edge between two largest parts maximizes the cut norm. For a two-part graph there is only one edge orbit to consider.

For \(K_{N-3,2,1}\) with \(N\ge6\), evaluation yields
\[
\begin{array}{c|ccc}
\text{part size}&N-3&2&1\\\hline
F_N&(4N-7)/(3N)&(N^2-2N-2)/(N(N-2))&(N-1)/N\\
H_N&(2N-5)/(3N)&(N-4)/(N-2)&(N-3)/N.
\end{array}
\]
The ordering is strictly \(F_N(N-3)>F_N(2)>F_N(1)\), whereas \(H_N(2)\ge H_N(1)>H_N(N-3)\) (equality only in the first inequality at \(N=6\)). Hence the two norms are attained on the claimed different edge types. Adding the two corresponding entries gives the stated rational formulas and their positive difference, completing the proof.

## Verification

Run `python3 verification/check.py` from the package directory; the checker uses only Python's standard library and exact rational Gaussian elimination. It constructs the full Laplacian independently of the theorem's current formulas, solves \((L+\mathbf1\mathbf1^{\mathsf T}/N)u=e_a-e_b\), checks Kirchhoff's equations, verifies both predicted absolute column sums for **every edge**, and then verifies the global maxima. It exhausts all 128 unordered multipartitions with \(2\le N\le10\), adds three larger/independent profiles, and checks the extremizer reversal algebra for each \(6\le N\le100\). In total this is **131 multipartitions, 3,029 exact edge columns, and 95 reversal instances**. These finite tests detect arithmetic and indexing errors; the proof, not the enumeration, establishes the infinite-family statement.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582, first posted 21 May 2023), develop the Banach-space framework for canonical and minimal graph projections. Their detailed graph-family calculations concern tori and Hamming graphs, not general unequal-part complete multipartite graphs. Bapat, Karimi and Liu, *Kirchhoff index and degree Kirchhoff index of complete multipartite graph* (arXiv:1611.09457, posted 29 November 2016), reproduce known formulas for **pairwise effective resistance** on complete multipartite graphs, citing Gervacio's earlier treatment. Such resistance information is strong input: transfer currents can in principle be recovered by polarization of pairwise resistances. The present contribution does **not** claim the resistance formula, the electrical-potential method, or the equal-part and split-graph special cases as new. It evaluates the induced Banach norms for arbitrary unequal parts, solves the edge-orbit maximization for both complementary projections, and identifies an explicit family in which the maximizers differ. These extra maximization statements are not given by the inspected sources.

## Limitations

The projections are fixed Euclidean-orthogonal operators; global minimality over arbitrary nonorthogonal projections is not asserted. Existing resistance-distance formulas can recover the matrix entries through standard identities, so the novelty is limited to the complete absolute-column evaluation and extremizing-edge comparison. An equivalent norm formula under electrical-network terminology could exist beyond the inspected sources. The 2012 journal version of Gervacio's resistance-distance paper was located, but its linked full-text PDF did not resolve in the available reading interface; Bapat, Karimi and Liu provide the same resistance formula in an accessible full text. No independently performed mathematical audit is claimed.

## References

1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (2023), https://arxiv.org/abs/2305.12582.
2. R. B. Bapat, M. Karimi and J.-B. Liu, *Kirchhoff index and degree Kirchhoff index of complete multipartite graph*, arXiv:1611.09457 (2016), https://arxiv.org/abs/1611.09457.
3. S. V. Gervacio, *Resistance distance in complete n-partite graphs*, The Mindanawan Journal of Mathematics **3** (2012), 1–19, https://journals.msuiit.edu.ph/tmjm/article/view/26; and Discrete Applied Mathematics **203** (2016), 53–61, DOI:10.1016/j.dam.2015.09.017.
