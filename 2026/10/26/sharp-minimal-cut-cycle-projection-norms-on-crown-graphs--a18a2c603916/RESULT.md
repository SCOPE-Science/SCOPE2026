# Sharp minimal cut–cycle projection norms on crown graphs

## Finding
For each integer \(n\ge3\), let \(\mathrm{Cr}_n=K_{n,n}-M\) be the connected crown graph obtained by deleting a perfect matching from the complete bipartite graph. Its oriented edge set is \(E=\{(A_i,B_j):1\le i,j\le n,\ i\ne j\}\). Write \(Z_n=\ker D\) for its real cycle-flow space and \(B_n=\operatorname{im}D^{\mathsf T}=Z_n^\perp\) for its cut space, where \(D\) is the oriented vertex-by-edge incidence matrix. Define \(C_n\) and \(Q_n\) as the Euclidean-orthogonal projections onto \(Z_n\) and \(B_n\), respectively, so \(C_n+Q_n=I\).

**Theorem.** For every real norm on \(\mathbb R^E\) invariant under simultaneous relabeling \(A_i\mapsto A_{\sigma(i)}\), \(B_i\mapsto B_{\sigma(i)}\) for \(\sigma\in S_n\), \(C_n\) minimizes the operator norm among **all** real-linear projections onto \(Z_n\), and \(Q_n\) minimizes the operator norm among **all** real-linear projections onto \(B_n\). Each is the unique projection onto its space commuting with that relabeling group.

For the induced real edge-\(\ell_1\) operator norms, and likewise for the induced edge-\(\ell_\infty\) norms, the exact minimum relative projection constants are
\[
\lambda(Z_n)=\|C_n\|=\frac{2(2n^2-6n+3)}{n(n-1)}=4-\frac8n-\frac{2}{n(n-1)},\qquad
\lambda(B_n)=\|Q_n\|=\frac{3n-4}{n}=3-\frac4n.
\]
Here \(\lambda(W)\) means the infimum over projections from the **specified ambient edge space** onto \(W\), not an absolute projection constant over arbitrary superspaces. Consequently \(\|Q_n\|>\|C_n\|\) precisely for \(n=3,4\), and \(\|C_n\|>\|Q_n\|\) precisely for \(n\ge5\). Both increase strictly in \(n\), converging respectively to \(3\) and \(4\).

## Assumptions and scope
Everything is real, finite-dimensional, and unweighted; every original edge carries the same Euclidean inner product and the same unit edge-\(\ell_1\) or edge-\(\ell_\infty\) coordinate norm. All quantifiers range over integers \(n\ge3\) and all real-linear projections onto the stated fixed subspaces. The theorem about optimality under other norms assumes only simultaneous-index permutation invariance; it does not supply a formula for those other norm values.

## Proof
**1. Uniqueness of equivariant projections.** Let \(S_n\) act by the same permutation of the labels of both vertex classes, hence by isometries of any norm under consideration and by Euclidean orthogonal transformations on the edge-coordinate space. Both \(Z_n\) and \(B_n\) are invariant, so \(C_n,Q_n\) commute with this action.

A linear equivariant map \(T:\mathbb R^n\to Z_n\) has, at every off-diagonal coordinate, an expression of the form
\[
 (Tx)_{ij}=a x_i+b x_j+c\sum_{k=1}^n x_k\quad(i\ne j),
\]
with coefficients independent of \(i,j\). Indeed the stabilizer of an ordered pair \((i,j)\) permutes all remaining indices transitively, including the case \(n=3\). Because every row sum and every column sum of \(Tx\) vanish for every \(x\), we obtain
\[
 (n-1)a-b=0,\qquad (n-1)b-a=0,\qquad b+(n-1)c=0.
\]
For \(n\ge3\), this implies \(a=b=c=0\), so \(T=0\). Each of the row and column potential maps from \(\mathbb R^n\) into \(B_n\) is equivariant, and their images span \(B_n\); thus every equivariant map \(B_n\to Z_n\) is zero. By taking Euclidean adjoints, every equivariant map \(Z_n\to B_n\) is zero as well.

Every projection \(P\) onto \(Z_n\) has the form \(C_n+R Q_n\) with \(R:B_n\to Z_n\). If \(P\) is equivariant, then \(R=0\), hence \(P=C_n\); analogously \(Q_n\) is the unique equivariant projection onto \(B_n\). For an arbitrary projection \(P\) onto either invariant subspace, its group average \(\overline P=|S_n|^{-1}\sum_{\sigma\in S_n}\sigma P\sigma^{-1}\) is still a projection onto that subspace; convexity and isometry of the group action give \(\|\overline P\|\le\|P\|\). Uniqueness of the equivariant projection forces \(\overline P=C_n\) or \(Q_n\), proving optimality for every stated invariant norm.

**2. Explicit electrical-current column.** Orient every edge from \(A\) to \(B\), and fix a source edge \(e=(A_i,B_j)\) with \(i\ne j\). For the Euclidean cut projection, the column \(Q_n\delta_e\) is the unit-conductance electrical current with injection at \(A_i\) and extraction at \(B_j\). If the vertex potentials in the two layers are \(u,v\in\mathbb R^n\), set \(s=u+v\) and \(d=u-v\). The Laplacian equations become
\[
 (nI-J)s=e_i-e_j,\qquad ((n-2)I+J)d=e_i+e_j,
\]
where \(J\) is the all-ones matrix. We may choose the harmless additive gauge of \(s\) so that
\[
 s=\frac{e_i-e_j}{n},\qquad
 d=\frac{e_i+e_j}{n-2}-\frac{\mathbf 1}{(n-2)(n-1)}.
\]
The current along any edge \((A_k,B_l)\) with \(k\ne l\) is
\[
 (Q_n\delta_e)_{kl}=\frac12(s_k-s_l+d_k+d_l).
\]
Writing \(o,o'\) for distinct indices outside \(\{i,j\}\), the complete disjoint current-type partition is:

| Edge type | Number of edges | Signed current |
| --- | ---: | ---: |
| \((i,j)\) | \(1\) | \((2n-1)/(n(n-1))\) |
| \((j,i)\) | \(1\) | \(1/(n(n-1))\) |
| \((i,o)\) or \((o,j)\) | \(2(n-2)\) | \((n^2-3n+1)/(n(n-2)(n-1))\) |
| \((j,o)\) or \((o,i)\) | \(2(n-2)\) | \(-1/(n(n-2)(n-1))\) |
| \((o,o')\) | \((n-2)(n-3)\) | \(-1/((n-2)(n-1))\) |

The sign in the third row is positive for all \(n\ge3\) because \(n^2-3n+1>0\) at every integer \(n\ge3\); the final row has count zero when \(n=3\). The counts sum to \(n(n-1)\). Taking absolute values, multiplying by the counts, and simplifying gives
\[
 \sum_{k\ne l}|(Q_n\delta_e)_{kl}|=\frac{3n-4}{n}.
\]
Simultaneous relabeling acts transitively on the edges, so this is the common absolute column sum and therefore \(\|Q_n\|_{1\to1}\).

**3. Complementary cycle projection.** The diagonal entry of the same current column is the effective resistance
\[
 (Q_n)_{ee}=\frac{2n-1}{n(n-1)}.
\]
Since \(C_n=I-Q_n\) and the diagonal lies strictly between zero and one, the absolute column sum of \(C_n\) is
\[
 \|Q_n\|_{1\to1}+1-2(Q_n)_{ee}
 =\frac{2(2n^2-6n+3)}{n(n-1)}.
\]
Both projections are real symmetric matrices, so their induced \(\ell_\infty\) norms equal the corresponding \(\ell_1\) norms. Finally, the difference between the cut and cycle norms is
\[
 \|Q_n\|-\|C_n\|=\frac{-n^2+5n-2}{n(n-1)},
\]
which is positive exactly for integer \(n=3,4\) and negative for every \(n\ge5\). The stated monotonicity and limits follow directly from the simplified formulas.

## Verification
The accompanying standard-library script `verify_crown.py` independently forms each graph's incidence matrix, grounds the vertex Laplacian, inverts it over exact rational numbers, reconstructs every cut-projection column, and checks the cycle complement. It passed all \(328\) columns for \(3\le n\le10\), including all projected column sums, diagonal resistances, symmetry, cycle-flow identities, and full cut-projector idempotence for \(n\le6\). Run `python3 verify_crown.py`. These finite computations corroborate but do not establish the universal proof above.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023) established the general invariant cycle-projection framework; averaging over graph automorphisms is **their prior methodology**, not a new general method here. Their explicit Hamming-cube case covers the special \(n=4\) crown graph (the three-dimensional cube). The new family-specific components are the vanishing intertwiner calculation for the simultaneous-label action, and the sharp all-parameter relative minimum norms and their crossing at \(n=5\). Ge and Dong (2019) treated effective resistances of nearly complete bipartite graphs, including graphs obtained by deleting matchings; effective resistance formulas are acknowledged prior information. Neither the scalar diagonal resistance nor the known three-cube value is claimed new.

## Limitations
Only relative projection minima inside the specified ambient edge-coordinate spaces are proved, not absolute projection constants. The all-invariant-norm optimality theorem does not furnish closed norms for arbitrary invariant norms, and uniqueness is only asserted among **equivariant** projections, not among all minimizers. The earlier Ye–Yan article on nearly complete bipartite effective resistances was identifiable bibliographically but its complete text was not available for inspection; a related operator-norm computation in less searchable literature remains possible. This work has undergone self-review, not independent mathematical audit.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (first public May 21, 2023), https://arxiv.org/abs/2305.12582.
2. J. Ge and F. Dong, *Spanning trees in complete bipartite graphs and resistance distance in nearly complete bipartite graphs*, arXiv:1904.07766v1 (April 16, 2019), https://arxiv.org/abs/1904.07766.
3. L. Ye and W. Yan, *Resistance between two vertices of almost complete bipartite graphs*, Discrete Applied Mathematics 257 (2019), 299–305, doi:10.1016/j.dam.2018.08.030.
