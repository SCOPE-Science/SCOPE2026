# A Birkhoff-polytope family of incenters for partial assignment polytopes
## Finding
Let \(N\ge3\), let \(2\le k<N\), and let
\[
M_{N,k}=\operatorname{conv}\{X\in\{0,1\}^{N\times N}:\sum_{i,j}X_{ij}=k,\ \sum_jX_{ij}\le1,\ \sum_iX_{ij}\le1\}
\tag{1}
\]
be the polytope of size-\(k\) partial permutation matrices, also called the \(k\)-assignment polytope. It is equipped with the Frobenius norm in the affine hyperplane
\[
H_k=\left\{X\in\mathbb R^{N\times N}:\sum_{i,j}X_{ij}=k\right\}.
\tag{2}
\]
Write \(J\) for the all-ones matrix and \(\mathcal B_N\) for the ordinary Birkhoff polytope of doubly stochastic \(N\)-by-\(N\) matrices. Define
\[
q_N=\sqrt{1-\frac1{N^2}},\qquad
u_{N,k}=\frac{k}{N\sqrt{N^2-1}},\qquad
v_{N,k}=\frac{N-k}{N\sqrt{N-1}},
\tag{3}
\]
and the threshold
\[
\kappa_N=N+1-\sqrt{N+1}.
\tag{4}
\]

The exact intrinsic inradius is
\[
\boxed{\rho(M_{N,k})=\min\{u_{N,k},v_{N,k}\}.}
\tag{5}
\]
The uniform center
\[
C_0=\frac{k}{N^2}J
\tag{6}
\]
is always an incenter.

**Low-rank phase.** If \(k<\kappa_N\), then \(C_0\) is the **unique** incenter. Its maximal inscribed ball touches exactly the \(N^2\) nonnegativity facets \(X_{ij}=0\), and does not touch any row- or column-sum facet.

**Critical phase.** If \(k=\kappa_N\), then \(C_0\) remains the unique incenter, and all \(N^2+2N\) facets are tangent. This occurs at integer parameters precisely for
\[
N=h^2-1,\qquad k=h(h-1),\qquad h\ge2.
\tag{7}
\]

**High-rank phase.** If \(k>\kappa_N\), set
\[
s_{N,k}=\frac{(N-k)\sqrt{N+1}}{N^2},\qquad
\lambda_{N,k}=\frac{k-(N-k)\sqrt{N+1}}{N}>0.
\tag{8}
\]
Then the **complete set** of maximal-inball centers is
\[
\boxed{\mathcal I(M_{N,k})=s_{N,k}J+\lambda_{N,k}\mathcal B_N.}
\tag{9}
\]
The incenter locus consequently has affine dimension
\[
\boxed{(N-1)^2}
\tag{10}
\]
and exactly \(N!\) vertices, corresponding to permutation matrices. Every optimal ball in this regime touches all \(2N\) row/column facets. A coordinate facet \(X_{ij}=0\) is additionally tangent exactly when the corresponding entry of the underlying doubly stochastic matrix is zero. The uniform center (6), corresponding to the strictly positive doubly stochastic matrix \(J/N\), touches no coordinate facet.

The unique minimum enclosing Euclidean ball has center \(C_0\), squared radius
\[
\boxed{R_{\mathrm{out}}^2=k-\frac{k^2}{N^2},}
\tag{11}
\]
and all
\[
\binom Nk^2k!
\tag{12}
\]
vertices are contacts. In particular, there is a sharp transition in the geometry of the **inner** centers, from a point to a scaled Birkhoff polytope, even though the **outer** center is unique at every rank.

## Assumptions and scope
The parameter range is \(N\ge3\) and \(2\le k<N\), so the polytope is of dimension \(N^2-1\) with exactly \(N^2+2N\) facets. The full inequality description and this facet count are given in the same-object work of Gill and Linusson; the later paper of Torres recovers the same inequality description as a special case of a theorem for bipartite graphs.

In the standard coordinate realization, the inequalities are
\[
X_{ij}\ge0,\qquad
\sum_jX_{ij}\le1,\qquad
\sum_iX_{ij}\le1,\qquad
\sum_{ij}X_{ij}=k.
\tag{13}
\]
The affine-hull metric is induced by the ambient Frobenius norm
\[
\|X\|_F=\sqrt{\sum_{i,j}X_{ij}^2}.
\]
No metric under a nonorthogonal projection or arbitrary linear change of coordinates is claimed. The cases \(k=1\) and \(k=N\) have different facet/affine-hull structures and are intentionally outside the theorem.

## Proof
Let
\[
L_0=\left\{Y\in\mathbb R^{N\times N}:\sum_{i,j}Y_{ij}=0\right\}
\]
be the tangent space of (2). If \(E_{ij}\) is the standard matrix unit, its orthogonal projection onto \(L_0\) is
\[
E_{ij}-\frac1{N^2}J,
\]
which has squared Frobenius norm
\[
1-\frac1{N^2}=q_N^2.
\tag{14}
\]
If \(R_i=\sum_jE_{ij}\) is the indicator of row \(i\), then its projection is \(R_i-J/N\) and has squared norm
\[
\|R_i-J/N\|_F^2=N-1.
\tag{15}
\]
The same formula holds for a column indicator.

For a center \(C\in H_k\), the intrinsic distances to the coordinate, row, and column facet hyperplanes are therefore
\[
\frac{C_{ij}}{q_N},\qquad
\frac{1-\sum_jC_{ij}}{\sqrt{N-1}},\qquad
\frac{1-\sum_iC_{ij}}{\sqrt{N-1}},
\tag{16}
\]
respectively. A Frobenius ball of radius \(\rho\), centered at \(C\), is contained in (13) **if and only if** every expression in (16) is at least \(\rho\). This follows directly by maximizing each linear functional over the ball within the affine hyperplane, and does not assume that the nearest point of the facet hyperplane is a facet-interior point.

Suppose such a ball exists. The coordinate inequalities give
\[
C_{ij}\ge\rho q_N
\]
for all \(i,j\). Summing and using \(\sum_{ij}C_{ij}=k\) yields
\[
\rho\le\frac{k}{N^2q_N}=u_{N,k}.
\tag{17}
\]
On the other hand, every row inequality yields
\[
\sum_jC_{ij}\le1-\rho\sqrt{N-1}.
\]
Summing over the \(N\) rows gives
\[
\rho\le\frac{N-k}{N\sqrt{N-1}}=v_{N,k}.
\tag{18}
\]
The columns give the same bound. Hence no inscribed ball can exceed the right-hand side of (5).

At the uniform matrix \(C_0=(k/N^2)J\), every coordinate clearance is exactly \(u_{N,k}\), and every row or column clearance is exactly \(v_{N,k}\). Thus \(C_0\) attains the upper bound, proving (5).

The equality
\[
u_{N,k}=v_{N,k}
\]
is equivalent, after cancellation of \(\sqrt{N-1}\), to
\[
\frac{k}{\sqrt{N+1}}=N-k,
\]
which is equivalent to \(k=\kappa_N\). This proves the claimed threshold. Integer equality holds exactly when \(\sqrt{N+1}=h\) is an integer, yielding (7).

If \(k\le\kappa_N\), then the optimal radius equals \(u_{N,k}\). At *any* optimal center, each coordinate must satisfy
\[
C_{ij}\ge u_{N,k}q_N=\frac{k}{N^2}.
\]
The sum of these \(N^2\) lower bounds is exactly \(k\). Thus every coordinate equals \(k/N^2\), proving that \(C_0\) is the unique incenter in both the low and critical phases. Comparing the three quantities in (16) proves the tangency descriptions.

Now let \(k>\kappa_N\), so the optimal radius equals \(v_{N,k}\). For any optimal center, every row sum is at most
\[
1-v_{N,k}\sqrt{N-1}=\frac{k}{N}.
\]
Since the \(N\) row sums add to \(k\), every row sum is **exactly** \(k/N\). The identical column argument forces every column sum to be \(k/N\). The coordinate inequalities require
\[
C_{ij}\ge v_{N,k}q_N=s_{N,k}.
\tag{19}
\]
These conditions are sufficient, by (16), for optimality.

Set
\[
Y=\frac{C-s_{N,k}J}{\lambda_{N,k}},
\]
where \(\lambda_{N,k}=k/N-Ns_{N,k}>0\) agrees with (8). Condition (19) becomes \(Y_{ij}\ge0\), and the row and column sums become exactly \(1\). Thus \(Y\in\mathcal B_N\), and conversely each such \(Y\) produces an optimal center. This proves (9). Since \(\mathcal B_N\) has nonempty relative interior in its row/column affine subspace, and that subspace has dimension \((N-1)^2\), (10) follows. Its vertices are the \(N!\) permutation matrices. The tangency characterization follows from (16) and \(C_{ij}=s_{N,k}+\lambda_{N,k}Y_{ij}\).

Finally, each vertex \(V\) of (1) has exactly \(k\) unit entries, so
\[
\|V-C_0\|_F^2=k-\frac{k^2}{N^2}.
\tag{20}
\]
The average of all \(\binom Nk^2k!\) vertices is \(C_0\), because row/column permutations act transitively and the total number of ones is always \(k\). Consequently, for any competing enclosing-ball center \(Z\),
\[
\frac1{|\mathcal V|}\sum_{V\in\mathcal V}\|V-Z\|_F^2
=k-\frac{k^2}{N^2}+\|Z-C_0\|_F^2.
\tag{21}
\]
At least one vertex has squared distance at least the average, so no ball of smaller radius exists, and equality forces \(Z=C_0\). Equations (11)--(12) and uniqueness follow.

## Verification
The proof works for every integer \(N\ge3\) and \(2\le k<N\), without extrapolating from finite examples. The source-dependent representation (13), the complete facet count, and the affine dimension were checked in Gill--Linusson, Theorem 3 and the facet table immediately following it, and in Torres, Theorem 3.1 and its complete-bipartite specialization.

The standalone `verify.py` computes exact projected facet-normal norms and uses independent full-dimensional linear programs to maximize intrinsic ball radius for every \(3\le N\le15\), \(2\le k<N\). It checks the formulas for the high-rank Birkhoff family and the endpoint equality cases, and exhaustively generates all \(k\)-assignment vertices in selected smaller instances to verify the outer sphere and barycenter identity. These finite computations are corroborative and are **not** proofs of the all-parameter formulas or of originality.

## Relationship to prior work
Torres proves the normality of the fixed-cardinality matching polytope of any bipartite graph and, as a preliminary result, its linear inequality representation. Gill and Linusson established the same inequality representation for complete bipartite graphs in 2009, together with facet counts, dimension, graph diameter, a face-poset model, and an ear decomposition.

These works establish the exact objects and facets used in this proof. Neither inspected full text states the Euclidean inradius, the square-root threshold, or the description of all maximum-ball centers as a scaled Birkhoff polytope. Their diameter results are for **graph distance** in the one-skeleton, not the Euclidean enclosing-ball radius.

The 2009 paper also represents a \(k\)-assignment polytope as a facet of a larger transportation polytope followed by a coordinate projection. Such a projection is not an isometry and the inradius of the ambient transportation polytope does not determine the intrinsic inradius of the projected facet. Likewise, formulas for the ordinary Birkhoff polytope correspond to the excluded endpoint \(k=N\), where the affine hull and facet system are different.

The new geometric feature is a rank-triggered **nonuniqueness transition**. At small \(k\), every coordinate facet forces the unique uniform incenter. At large \(k\), row and column facets determine only the margins, leaving precisely a translated, scaled Birkhoff polytope of admissible incenter locations. This yields a complete face-lattice and tangency-pattern description of the incenter locus.

## Limitations
The theorem treats square \(N\)-by-\(N\) partial assignment polytopes of cardinality strictly between \(1\) and \(N\). General rectangular dimensions have three potentially distinct facet-distance scales; the endpoints \(k=1\) and \(k=N\) change the facet structure. No rectangular or endpoint formula is claimed.

The geometry is intrinsic Euclidean geometry in the fixed-total affine hyperplane with Frobenius metric. General affine images need not preserve any of these radii or centers.

No volume, John ellipsoid, or general bipartite-graph extension is claimed. The proof is elementary after the exact facet system is known, so rediscovery under older “partial permutation matrix” or “doubly substochastic slice” terminology remains a residual originality risk.

## References
1. Juan Camilo Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1, publicly submitted 2023-06-20; *Revista Colombiana de Matemáticas* 57(2) (2023), 193--206, DOI 10.15446/recolma.v57n2.115853. Primary MSC 52B11.
2. Jonna Gill and Svante Linusson, *The k-assignment polytope*, *Discrete Optimization* 6(2) (2009), 148--161, DOI 10.1016/j.disopt.2008.10.003. Author-posted full text: https://liu.diva-portal.org/smash/get/diva2:210918/FULLTEXT01.pdf.
