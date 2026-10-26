# A sharp edgewise stability law for matching-deleted complete bipartite graphs

## Finding

Let \(n\ge 3\) be an integer. Starting from the unweighted complete bipartite graph \(K_{n,n}\), delete \(t\) pairwise disjoint edges, where \(0\le t\le n\), and denote the resulting connected graph by \(G_{n,t}\). Orient all remaining edges from the left part to the right part. Let \(P_{n,t}\) be the Euclidean orthogonal projection of real edge data onto the space of gradient edge flows. Equip the edge-data space with the maximum-coordinate norm \(\|x\|_\infty=\max_e|x_e|\).

**Theorem.** For every such \(n,t\), the exact induced operator norm is
\[
\boxed{\|P_{n,t}\|_{\infty\to\infty}=
\begin{cases}
3-\dfrac4n+\dfrac{2(n-2)}{n\,[n(n-2)+t]},&0\le t<n,\\[6pt]
3-\dfrac4n,&t=n.
\end{cases}}
\]
All bounds are attained by edge-data vectors with coordinates in \(\{-1,1\}\). When \(t<n\), an edge whose two endpoints are untouched by the deleted matching is always a norming output coordinate. For \(1\le t<n\), its absolute row sum is strictly greater than those of the other two possible edge types. When \(t=n\), all surviving edges have the same absolute row sum.

As edges of a fixed matching are deleted successively, the sharp norm decreases *strictly* at every step. Put \(D_t=n(n-2)+t\). For \(0\le t\le n-2\),
\[
\|P_{n,t}\|_{\infty\to\infty}-\|P_{n,t+1}\|_{\infty\to\infty}
=\frac{2(n-2)}{nD_tD_{t+1}},
\]
whereas the final deletion produces the larger drop
\[
\|P_{n,n-1}\|_{\infty\to\infty}-\|P_{n,n}\|_{\infty\to\infty}
=\frac{2(n-2)}{nD_{n-1}}.
\]
The final drop is exactly \((n-2)(n+1)\) times the immediately preceding drop. Hence the last deletion creates a distinguished threshold: earlier matching deletions change the norm by order \(n^{-4}\), while the last changes it by order \(n^{-2}\).

## Assumptions and scope

The graph is finite, simple, unweighted and connected, with each part of cardinality \(n\ge3\). The deleted edges form a matching. The orthogonal projection uses the standard counting-measure Euclidean inner product on *surviving* oriented edges; the target norm is the induced \(\ell^\infty\)-operator norm on this edge set. Equivalently, if \(B\) is the edge-by-vertex signed incidence matrix, then \(P_{n,t}=B(B^{\mathsf T}B)^\dagger B^{\mathsf T}\). Reversing individual edge orientations conjugates this matrix by a diagonal sign matrix and does not change its induced norm.

The result is not about arbitrary deleted edge sets, nonlinear recovery, or relative error in reconstructed vertex potentials. It quantifies the coordinatewise amplification in the *fitted edge-gradient flow* under bounded disturbances in the observed edge data.

## Proof

Label the two parts by \(u_1,\dots,u_n\) and \(v_1,\dots,v_n\). By relabeling, delete the edges \((u_r,v_r)\), \(1\le r\le t\). The graph remains connected: any two distinct left vertices share at least one right neighbor when \(n\ge3\), even after the deletion of a matching, and the same argument applies on the other side.

**1. Orthogonal projection and removal of coordinates.** Identify the full edge-data space for \(K_{n,n}\) with real \(n\)-by-\(n\) arrays. A gradient array has form \(h_{ij}=a_i+b_j\); its Euclidean projector \(P^{(0)}\) is row averaging plus column averaging minus total averaging. Its kernel is
\[
P^{(0)}_{(i,j),(k,l)}=\frac{\mathbf1_{i=k}+\mathbf1_{j=l}}n-\frac1{n^2}.
\]
Partition the full edge coordinates as surviving \(R\) and deleted \(D\), and block-decompose the full orthogonal projection as
\[
P^{(0)}=\begin{pmatrix}A&C\\ C^{\mathsf T}&H\end{pmatrix}.
\]
The orthogonal projector onto the restrictions of the gradient arrays to \(R\) is
\[
P_{n,t}=A+C(I-H)^{-1}C^{\mathsf T}.
\tag{1}
\]
Indeed, the orthogonal complement of the restricted gradient space consists of surviving-coordinate vectors whose zero extension lies in the full cycle space. Taking the Schur complement of \(I-P^{(0)}\) along the deleted coordinates gives its orthogonal projector, and subtracting this from the identity yields (1). Invertibility holds because no nonzero gradient flow can be supported solely on the deleted matching; equivalently, restriction to the connected remaining graph is injective on the gradient-flow subspace. Directly,
\[
H=\frac2nI_t-\frac1{n^2}\mathbf1_t\mathbf1_t^{\mathsf T},\qquad
(I-H)^{-1}=\frac n{n-2}I_t-\frac{n}{(n-2)D_t}\mathbf1_t\mathbf1_t^{\mathsf T}.
\]
The formula also covers \(t=0\) by taking empty matrices and omitting the correction term.

**2. Explicit transfer-current kernel.** For a surviving oriented edge \(e=(i,j)\), let \(s_e=\mathbf1_{i\le t}+\mathbf1_{j\le t}\), where indices refer to their respective bipartition sides. For another surviving edge \(f=(k,l)\), put
\[
L(e,f)=\mathbf1_{i=k}+\mathbf1_{j=l},\qquad
O(e,f)=\sum_{r=1}^t(\mathbf1_{i=r}+\mathbf1_{j=r})(\mathbf1_{k=r}+\mathbf1_{l=r}).
\]
Substituting the block of deleted coordinates into (1), and simplifying, gives
\[
\boxed{(P_{n,t})_{ef}=
\frac{L(e,f)}n+\frac{O(e,f)}{n(n-2)}
-\frac{(n-2+s_e)(n-2+s_f)}{n(n-2)D_t}.}
\tag{2}
\]
This is a complete entrywise formula; it includes the diagonal and every surviving edge. The constant edge vector is a gradient (left potential one, right potential zero), so every row of \(P_{n,t}\) sums to one.

**3. Entry signs and row classes.** There are three row types, according to \(s_e=0,1,2\). Formula (2) yields the following sign accounting (zeros may be grouped with the nonnegative entries).

For \(s_e=0\), an entry is positive precisely when its column edge shares the left endpoint or the right endpoint of \(e\); all nonsharing entries are negative. For \(s_e=1\), the positive entries are the sharing entries, together with nonsharing edges that encounter the same deleted-matching index on the opposite side and have just one endpoint incident to the deleted matching. These additional entries equal \((t-1)/[n(n-2)D_t]\); they are zero when \(t=1\). For \(s_e=2\), the positive entries are the sharing entries and the edge obtained by reversing the two matched *indices* of \(e\) between the bipartition classes. In that last case the reverse-pair entry is \([n(n-4)+2t]/[n(n-2)D_t]>0\) for the permitted \(n\ge3,t\ge2\). All other nonsharing entries are nonpositive.

To verify this classification algebraically, substitute \(L=0,1,2\), \(O=0,1,2\), \(s_e,s_f\in\{0,1,2\}\) in (2), retaining only realizable incidence patterns. The potentially exceptional nonsharing expressions reduce to \((t-1)/[n(n-2)D_t]\), \((t-n)/[n(n-2)D_t]\), \((t-2n)/[n(n-2)D_t]\), and \([n(n-4)+2t]/[n(n-2)D_t]\); their signs are as asserted. The sharing cases are strictly positive by the same formula. This checks boundaries \(n=3\), \(t=1\), \(t=n-1\), and \(t=n\).

Because a row sums to one, its absolute row sum equals twice its sum over positive entries minus one. For clarity, the direct counts of nonnegative entries are as follows. Let \(N_+\) denote the number of chosen nonnegative columns and use \(\sum_+\) for sums over those columns:

| Row type | \(N_+\) | \(\sum_+ L(e,f)\) | \(\sum_+ O(e,f)\) | \(\sum_+ s_f\) |
| --- | ---: | ---: | ---: | ---: |
| \(s_e=0\) | \(2n-1\) | \(2n\) | \(0\) | \(2t\) |
| \(s_e=1\) | \(3n-t-2\) | \(2n-1\) | \(2n-t-1\) | \(2n+t-3\) |
| \(s_e=2\) | \(2n-2\) | \(2n-2\) | \(2n\) | \(2n+2t-4\) |

Here zero entries may be included in \(N_+\) without changing the sum (the \(s_e=1,t=1\) row contains such zeros). The \(s_e=1\) counts consist of the union of \(n-1\) edges in its matched left row, \(n\) edges in its unmatched right column, and \(n-t\) reverse-index cross edges; the first two sets overlap in just the row edge itself. The \(s_e=2\) counts similarly add one reverse-index edge to two overlapping sharing families, each of size \(n-1\). Inserting these counts into (2) gives, with \(D_t=n(n-2)+t\),
\[
\begin{aligned}
R_0(n,t)&=3-\frac4n+\frac{2(n-2)}{nD_t},&&s_e=0,\\
R_1(n,t)&=3-\frac4n+\frac{2(t-1)(n-t-1)}{n(n-2)D_t},&&s_e=1,\\
R_2(n,t)&=3-\frac4n,&&s_e=2.
\end{aligned}
\tag{3}
\]
The first expression applies when \(t<n\), the second when \(1\le t<n\), and the third when \(t\ge2\). For example, in the \(s_e=0\) case the negative entries are the nonsharing columns. Their total *absolute* mass is \((n-2)[n(n-2)+t+1]/(nD_t)\); adding twice this mass to one gives \(R_0\). In the \(s_e=2\) case the two families of sharing edges and the single reverse-index edge sum to \((2n-2)/n+2n/[n(n-2)]-[(n-2)(2n-2)+2n+2t-4]/[(n-2)D_t]\), which simplifies to \((R_2+1)/2\). The intermediate type is counted similarly from its sharing edges and \(n-t\) cross-index edges.

**4. Selecting the maximizing edge.** For \(1\le t<n\),
\[
R_0-R_2=\frac{2(n-2)}{nD_t}>0,
\]
\[
R_0-R_1=\frac{2\big[(n-2)^2-(t-1)(n-t-1)\big]}{n(n-2)D_t}>0,
\]
since \((t-1)(n-t-1)\le(n-2)^2/4\). Thus every row of type zero is maximizing, with strict superiority over the other types. For \(t=0\) every edge is of type zero. For \(t=n\) all surviving edges are of type two, giving the last formula. The induced \(\ell^\infty\)-norm of a finite real matrix equals its largest absolute row sum, attained by selecting the input coordinates to agree with the signs of a maximizing row. This proves the sharp norm and attainment.

**5. Monotonicity and the final-edge jump.** Subtracting adjacent rational expressions in the theorem gives the first formula for each \(t\le n-2\). The last-step expression follows by comparing \(R_0(n,n-1)\) with \(R_2(n,n)\). Dividing that drop by the immediately preceding drop gives \(D_{n-2}=(n-2)(n+1)\), proving the asserted exact threshold and its orders in \(n\).

## Verification

The standalone `checker.py` uses Python's standard-library `fractions.Fraction` and builds the graph incidence matrix directly, grounds one vertex, inverts the resulting exact integer Gram matrix, and recomputes the projection without using the closed formula. For every \(3\le n\le9\) and \(0\le t\le n\), it checks the explicit kernel (2) entry by entry, each row sum, each of the three row-type norms (3), the global norm, a sign-valued sharpness witness, all deletion monotonicities, and the final/preceding-drop ratio. Its execution on the included code reports **123,977 exact-rational assertions passed**. These finite checks are independent corroboration, not the proof for unbounded \(n\).

Run from the directory containing both files with `python3 checker.py`.

## Relationship to prior work

Jiang, Lim, Yao and Ye [1] establish least-squares graph-gradient projection for incomplete comparison networks. Kassel and Wu [2] discuss the transfer-current kernel as a graph-theoretic object and its applications. Neither work's inspected text gives the induced edgewise maximum norm for complete bipartite graphs with an arbitrary deleted matching or the exceptional final-deletion law. Standard complete-bipartite row-column projection yields the undeleted endpoint \(3-4/n+2/n^2\), but does not cover even one deleted edge without changing the observation subspace. Existing formulas for electrical effective resistance or the Kirchhoff index concern diagonal entries or trace-type combinations rather than full signed row sums; those invariants do not alone imply the present norm. The full projection update, sign classification and row maximization are supplied here.

## Limitations

The conclusion requires the deleted edges to be disjoint, and the two original bipartition sizes to be equal. Nothing is asserted for arbitrary failures, unequal observation weights, or any nonlinear estimator. The originality assessment is relative to the inspected literature and available mathematical records; an unlocated equivalent formula under electrical-network terminology remains possible. The result has been checked internally and has not undergone independent mathematical or historical-priority review.

## References

[1] X. Jiang, L.-H. Lim, Y. Yao and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067, initially public 2008-11-07; *Mathematical Programming* 127 (2011), 203–244, DOI:10.1007/s10107-010-0419-x.

[2] A. Kassel and W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946, initially public 2013-12-10; *Probability Theory and Related Fields* 163 (2015), 89–121.

[3] E. W. Weisstein, *Crown Graph*, MathWorld, https://mathworld.wolfram.com/CrownGraph.html (terminology for the perfect-matching deletion case only).
