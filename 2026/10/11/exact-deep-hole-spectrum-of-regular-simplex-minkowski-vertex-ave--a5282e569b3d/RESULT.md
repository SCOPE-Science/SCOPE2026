# Exact deep-hole spectrum of regular-simplex Minkowski vertex averages

## Finding

Let \(V=\{v_0,\dots,v_n\}\) be the vertex set of a nondegenerate regular Euclidean \(n\)-simplex, with \(n\ge1\) and side length \(\ell>0\). For every integer \(k\ge1\), take its \(k\)-fold Minkowski average
\[
V_{(k)}=\left\{\frac{v_{i_1}+\cdots+v_{i_k}}{k}: i_j\in\{0,\dots,n\}\right\}.
\]
Write
\[
d=n+1,\qquad r_* =\min\{k,\lfloor d/2\rfloor\}.
\]
Then the exact Euclidean Hausdorff distance to its convex hull is
\[
\boxed{D_{n,k}:=d_H(V_{(k)},\operatorname{conv}V)=\frac{\ell}{k}\sqrt{\frac{r_*(d-r_*)}{2d}}.}
\]

The complete set of farthest points can also be described. Let
\[
R_{d,k}=\operatorname*{arg\,max}_{1\le r\le\min(k,d-1)}r(d-r).
\]
Every farthest point, and no other point, has barycentric coordinates
\[
\boxed{p_i=\frac{b_i+r/d}{k}\quad(0\le i\le n),}
\]
where \(r\in R_{d,k}\), all \(b_i\) are nonnegative integers, and
\[
\sum_{i=0}^n b_i=k-r.
\]
The number of farthest points therefore equals
\[
\boxed{N_{n,k}=\sum_{r\in R_{d,k}}\binom{k-r+n}{n}.}
\]
In particular, for
\[
1\le k\le\lfloor d/2\rfloor
\]
the centroid is the **unique** farthest point, and
\[
\frac{D_{n,k}}{D_{n,1}}=\sqrt{\frac{d-k}{k(d-1)}}.
\]
When \(k>\lfloor d/2\rfloor\), further farthest points necessarily appear. At and beyond the threshold \(k=\lfloor d/2\rfloor\), the distance is the known infinite-lattice \(A_n\) covering radius, rescaled to the mesh of \(V_{(k)}\):
\[
D_{n,k}=\frac{\ell}{\sqrt2 k}\sqrt{\frac{\lfloor d/2\rfloor\lceil d/2\rceil}{d}}.
\]
The last lattice-covering formula is not independently new; the **finite simplex restriction**, the exact small-\(k\) transition, and the classification/count of every farthest point are the result asserted here.

## Assumptions and scope

Distances are Euclidean and \(V\) consists of **all and only** the vertices of a regular simplex. The integer \(k\) is arbitrary and may be smaller or larger than the dimension. Repeated indices are allowed in the Minkowski average, hence \(V_{(k)}\) is the uniform barycentric composition grid. The convex hull of \(V_{(k)}\) is exactly \(\operatorname{conv}V\), since all original vertices remain present.

Every farthest-point statement is about \(\operatorname{conv}V\), **not** all of the affine hyperplane or the full infinite root lattice. When \(d\) is odd and \(k\ge\lceil d/2\rceil\), both maximizing fractional-coordinate counts occur; the displayed sum includes both without double counting.

## Proof

An edge-length-\(\ell\) regular simplex is isometric, up to translation, to \(\{(\ell/\sqrt2)e_i:1\le i\le d\}\) in the affine hyperplane of coordinate sum \(\ell/\sqrt2\). Thus it suffices to analyze the standard simplex
\[
\Delta_{d-1}=\left\{p\in\mathbb R_{\ge0}^{d}:\sum_i p_i=1\right\}
\]
and the normalized grid
\[
G_{d,k}=\left\{m/k:m_i\in\mathbb Z_{\ge0},\ \sum_i m_i=k\right\}.
\]
For \(p\in\Delta_{d-1}\), put \(q=kp\), \(b_i=\lfloor q_i\rfloor\) and \(f_i=q_i-b_i\in[0,1)\). Since \(\sum_iq_i=k\) is an integer, the sum of fractional parts
\[
r:=\sum_i f_i=k-\sum_i b_i
\]
is an integer satisfying \(0\le r\le\min(k,d-1)\).

**Nearest-composition lemma.** Among all nonnegative integer vectors \(m\) with \(\sum_i m_i=k\), a nearest one to \(q\) is obtained by setting
\[
m_i=b_i+\mathbf 1_{\{i\in S\}},\quad |S|=r,
\]
where \(S\) consists of indices of \(r\) largest fractional parts. To prove this, suppose \(m_i\le b_i-1\). The total-sum condition forces some \(j\) with \(m_j\ge b_j+1\), and replacing \((m_i,m_j)\) with \((m_i+1,m_j-1)\) strictly decreases the sum of squared coordinate errors: the old error relative to the floor is at least one below \(f_i\), whereas the other is at least one above \(f_j\). Likewise, if some \(m_i\ge b_i+2\), the sum condition forces some \(m_j\le b_j\); transferring one from \(i\) to \(j\) strictly decreases squared error (including if \(j\) is still below its floor). Iterating produces floor-or-ceiling entries, and among such entries choosing the largest fractions minimizes the total squared error. All intermediate entries remain nonnegative. Thus
\[
E(f):=\min_{\substack{m_i\ge0\text{ integer}\\ \sum m_i=k}}\|q-m\|_2^2
=\min_{|S|=r}\sum_i(f_i-\mathbf 1_{\{i\in S\}})^2.
\]

The hypersimplex
\[
H_{d,r}=\{f\in[0,1]^d:\sum_i f_i=r\}
\]
is the convex hull of the indicator vectors of the \(r\)-subsets of \(\{1,\dots,d\}\). This follows directly because every extreme point of \(H_{d,r}\) is integral: if two coordinates are strictly between zero and one, varying them by opposite small amounts contradicts extremality, while exactly one fractional coordinate is incompatible with integer sum. Consequently there is a probability distribution on \(r\)-subsets \(S\) with \(\mathbb P(i\in S)=f_i\). Taking its average gives
\[
\begin{aligned}
E(f)&\le \mathbb E\sum_i(f_i-\mathbf1_{\{i\in S\}})^2\\
&=\sum_i f_i(1-f_i)
=r-\sum_i f_i^2\\
&\le r-\frac{r^2}{d}=\frac{r(d-r)}d.
\end{aligned}
\]
The last inequality is Cauchy--Schwarz, and equality in it requires precisely
\[
f_1=\cdots=f_d=r/d.
\]
For this uniform fractional vector, the squared distance to **every** indicator vertex of \(H_{d,r}\) equals \(r(d-r)/d\), so the upper bound is attained. Hence the *only* maximizing fractional vectors for a fixed nonzero \(r\) are uniform, with
\[
\max E(f)=r(d-r)/d.
\]

Every \(r\in\{1,\dots,\min(k,d-1)\}\) is feasible: choose any nonnegative integer composition \(b\) of \(k-r\) and set \(q=b+(r/d)\mathbf1\). This has nonnegative coordinates, coordinate sum \(k\), and floor vector \(b\). Therefore
\[
\sup_{q_i\ge0,\ \sum q_i=k}\min_{\substack{m_i\in\mathbb Z_{\ge0}\\\sum m_i=k}}\|q-m\|_2^2
=\frac1d\max_{1\le r\le\min(k,d-1)}r(d-r).
\]
Because \(r(d-r)\) increases through the midpoint and then decreases, the maximum value is \(r_*(d-r_*)\) with \(r_*=\min\{k,\lfloor d/2\rfloor\}\); for odd \(d\) and sufficiently large \(k\), two adjacent \(r\)-values tie. Undoing the grid normalization and simplex isometry multiplies squared distances by \(\ell^2/(2k^2)\), proving the claimed Hausdorff distance.

All equality conditions were forced above: \(r\) must maximize \(r(d-r)\), and each fractional coordinate must equal \(r/d\). Thus the farthest points are exactly the stated barycentric compositions. For each \(r\), the number of \(d\)-tuples of nonnegative integers with sum \(k-r\) is \(\binom{k-r+d-1}{d-1}\). For distinct \(r\), the points cannot coincide because their common fractional parts are distinct. This proves the count. When \(k\le\lfloor d/2\rfloor\), only \(r=k\) maximizes and \(b=0\), so the centroid is unique; the other cases follow immediately.

## Verification

The accompanying standalone checker reproduces the exact squared-distance maximum and equality-point counts for all integer parameters \(2\le d\le8\), \(1\le k\le6\). It enumerates the integer composition grid, constructs every claimed maximizer, verifies their squared nearest distances, and checks many interior random points do not exceed the analytic bound. The finite checks are reproducibility tests, **not** the infinite-dimensional/all-parameter proof; that is the nearest-composition plus hypersimplex argument above.

For \(d=3\), the farthest-site counts for \(k=1,2,3\) are \(1,4,9\), matching the triangular grid subdivision. For \(d=4\), they are \(1,1,4\): the tetrahedral centroid persists as the unique worst point through two-fold averaging, then additional worst points appear.

## Relationship to prior work

Meyer studies the Hausdorff distance from a compact set to its convex hull and obtains sharp \(\ell_p\) Minkowski-sum inequalities in the plane; the paper defines precisely the geometric distance used here but does not calculate this all-dimensional finite simplex-grid invariant. Van Hintum treats the \(k\)-fold Minkowski average, proves that some high-dimensional compact sets do not improve through multiple averages, and establishes a general contraction threshold; its construction uses a lifted simplex with additional points, not the pure vertex set of a regular simplex.

Classical \(A_n\) root-lattice theory **already knows** the full-space Euclidean covering radius
\[
\rho(A_n)=\sqrt{\frac{\lfloor d/2\rfloor\lceil d/2\rceil}{d}}.
\]
This literature indeed covers the large-\(k\) numerical branch of the present formula after scaling. What is **not implied by that unrestricted covering theorem** is the exact low-\(k\) restricted simplex-grid radius, the sharp transition as the barycentric grid matures, or the complete enumeration of farthest points within the simplex. Those are proven directly above, without claiming the unrestricted lattice theorem as new.

The geometric covering radius of an unbounded lattice of simplex translates is a different invariant from the distance between a finite barycentric point grid and its convex hull; the two formulations must not be conflated.

## Limitations

This is an exact profile for one canonical input family, not a new upper bound for all finite subsets of \(\mathbb R^n\). It does not settle the optimal general Hausdorff convexification contraction factor or classify extremizers of van Hintum's dimension-dependent inequality. The proof uses Euclidean distance and regularity of the simplex; arbitrary norms, distorted simplices, and sampled subsets are outside its scope.

The large-\(k\) radius coincides with an established \(A_n\) covering radius; novelty is restricted to the finite-domain profile, its transition, and the equality classification in the bounded simplex.

## References

1. Mark Meyer, *A sharp p-subadditive bound for the l_p Hausdorff distance from convex hull*, arXiv:2604.20387v1, first publicly submitted 22 April 2026; inspected lawful full-text revision v2 of 29 July 2026.
2. Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1, first publicly submitted 9 June 2026.
3. J. H. Conway and N. J. A. Sloane, *Sphere Packings, Lattices and Groups*, Springer, 3rd edition, 1999, standard root-lattice \(A_n\) covering radius.
4. The Error Correction Zoo, *A_n lattice*, public mathematical reference citing Conway--Sloane for the same full-space covering radius.
