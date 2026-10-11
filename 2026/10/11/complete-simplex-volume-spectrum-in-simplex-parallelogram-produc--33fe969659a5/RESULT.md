# Complete simplex-volume spectrum in simplex–parallelogram products

## Finding

Let \(n\ge1\) be an integer, let \(\Delta\) be a nondegenerate \(n\)-simplex, let \(Q\) be a nondegenerate parallelogram, and set \(P=\Delta\times Q\). Write \(N=n+1\). For \(j\in\{0,1,2\}\), let \(H_j\) count the unordered sets of \(n+3\) distinct vertices of \(P\) whose convex hull has \((n+2)\)-dimensional volume
\[
\frac{j}{(n+1)(n+2)}\operatorname{vol}_{n+2}(P).
\]
All such vertex sets belong to precisely one of these three classes, with
\[
\boxed{H_2=N(N-1)4^{N-2},\qquad
H_1=N4^N+12N(N-1)4^{N-2},\qquad
H_0=\binom{4N}{N+2}-H_1-H_2.}
\]

The vertex-supported simplices in class \(2\) are exactly those obtained by choosing two distinct vertices of \(\Delta\), using opposite pairs of diagonals of \(Q\) at these two simplex-vertex layers, and using one arbitrary vertex of \(Q\) at every other simplex-vertex layer. There are \(N(N-1)4^{N-2}\) such geometric simplices.

The maximum over **all** full-dimensional simplices contained in \(P\), whether or not supported on vertices, is
\[
\boxed{\max_{T\subseteq P}\frac{\operatorname{vol}_{n+2}(T)}{\operatorname{vol}_{n+2}(P)}
=\frac{2}{(n+1)(n+2)}.}
\]
The term \(T\) denotes a simplex (not an arbitrary subset); degenerate simplices have zero volume.

## Assumptions and scope

The Cartesian product has dimension \(n+2\). The base simplex and parallelogram may have arbitrary positive volumes and shapes; the claims are invariant under independent invertible affine changes of coordinates in their respective factors. For counting, each unordered vertex subset is counted once, irrespective of ordering or orientation. The class \(0\) includes affinely dependent vertex selections. The classification of maximizers applies **only to vertex-supported maximizers**; other maximizing simplices can have nonvertex vertices, and no uniqueness assertion is made for those.

By affine reduction it suffices to consider the standard simplex \(\Delta_n=\operatorname{conv}\{0,e_1,\ldots,e_n\}\) and the unit square \(Q=[0,1]^2\). Its total \((n+2)\)-volume is \(1/n!\). Label its \(N=n+1\) simplex vertices by \(i\in\{0,\ldots,n\}\); its \(4N\) product vertices are the pairs \((i,q)\), with \(q\in\{(0,0),(0,1),(1,0),(1,1)\}\).

## Proof

**1. Determinant reduction.** Given a set \(S\) of \(N+2\) distinct product vertices, form the square \((N+2)\)-row homogeneous-coordinate matrix whose row for \((i,q)\) is \((e_i^{\mathsf T},q_1,q_2)\), where \(e_0,\ldots,e_n\) now denote the standard basis of \(\mathbb R^N\). The column transformation replacing the barycentric coordinate columns by \((1,x_1,\ldots,x_n)\) is unimodular. Thus the absolute determinant of this matrix is precisely \((n+2)!\) times the Euclidean volume of \(\operatorname{conv}(S)\) in the standard model.

If some simplex-vertex label \(i\) does not appear, its barycentric column vanishes and the determinant is zero. Otherwise choose one representative row for each of the \(N\) labels. Subtract it from every other row with the same label. After row permutation the matrix has an \(N\)-by-\(N\) identity block and a lower-right \(2\)-by-\(2\) block consisting of the square-coordinate differences \(u,v\) from the two extra rows. Consequently
\[
|\det(S)|=|\det(u,v)|.
\]
All row additions, permutations and the barycentric-to-affine column change preserve the determinant's absolute value.

**2. Classification of nonzero determinants.** There are exactly two ways to distribute the two rows exceeding one per simplex-vertex label.

In the first case, one label occurs three times and all other labels occur once. The three distinct square vertices form a triangle of area \(1/2\), so their two difference vectors have determinant of absolute value \(1\). The number of such sets is \(N\binom43 4^{N-1}=N4^N\).

In the second case, two different labels occur twice and all other labels occur once. At each doubled label, the two square corners determine one of six unoriented segments: two horizontal, two vertical, or two diagonals, one of each slope. Across two *ordered* labels there are \(6^2=36\) ordered pairs of segments. Exactly \(2\) pairs consist of the two distinct diagonal types and give \(|\det|=2\). Exactly \(24\) pairs give \(|\det|=1\): the \(8\) perpendicular edge–edge pairs and the \(16\) edge–diagonal pairs. The remaining \(10\) give zero. There are \(\binom N2\) choices of doubled labels and \(4^{N-2}\) ways to select singleton corners at the other labels. Therefore
\[
H_2=2\binom N2 4^{N-2}=N(N-1)4^{N-2}
\]
and
\[
H_1=N4^N+24\binom N2 4^{N-2}
=N4^N+12N(N-1)4^{N-2}.
\]
Every other vertex selection has zero determinant. Since \(\binom{4N}{N+2}\) subsets exist, the stated \(H_0\) follows. The two distinct diagonal types are precisely the choices of opposite corners \(\{(0,0),(1,1)\}\) and \(\{(0,1),(1,0)\}\); this proves the complete vertex-supported equality classification. Such choices exist for every \(N\ge2\), so the determinant bound \(2\) is sharp.

**3. From vertices to arbitrary contained simplices.** The signed homogeneous determinant of \(N+2\) points is affine in each point separately when the other points are fixed. The absolute value of an affine function on a compact polytope attains its maximum at a vertex. Starting with any choice of \(N+2\) points of \(P\), replace each point in succession with a vertex of \(P\) without decreasing the absolute determinant. Hence no contained simplex can have greater volume than the maximum vertex-supported simplex. Conversely the diagonal-pair construction is contained in \(P\) and attains the determinant \(2\). For the standard model this is volume \(2/(n+2)!\); dividing by \(\operatorname{vol}_{n+2}(P)=1/n!\) yields the asserted ratio.

**4. Affine invariance.** Every nondegenerate simplex is an affine image of \(\Delta_n\), and every nondegenerate parallelogram is an affine image of \([0,1]^2\). Applying the product affine map preserves vertex incidences, determinant classes relative to whole-body volume, and the list of maximizing vertex sets. This proves the theorem for general \(\Delta\) and \(Q\).

## Verification

The standalone standard-library checker `verify.py` enumerates **all** \(\binom{4(n+1)}{n+3}\) vertex sets for each \(n=1,2,3,4\), independently evaluates their homogeneous determinants by exact fraction-free integer elimination, and compares the entire determinant histogram with the closed formulas. It reports counts \((H_0,H_1,H_2)\) equal to \((12,56,2)\), \((288,480,24)\), \((4488,3328,192)\), and \((55760,20480,1280)\), respectively. Reproduce with `python3 verify.py` (Python standard library only). The universal theorem is proved by Steps 1–4, not by these finite diagnostics.

As an immediate volume-only consequence, any simplicial triangulation of \(P\), including one with additional interior vertices, contains at least \(\lceil(n+1)(n+2)/2\rceil\) top-dimensional simplices; this is a generally nonoptimal volume lower bound and is **not** asserted to improve established triangulation bounds.

## Relationship to prior work

Seacrest and Su, in *A lower bound technique for triangulations of simplotopes* (arXiv:0910.1134), study products of simplices and exact simplex classes in the product of a triangle and a square. Their Section 7 explicitly reports **24 class-two simplices in the four-dimensional case**, which coincides with \(H_2=24\) at \(n=2\) above; that special case is not new. The class-two simplices of the three-dimensional cube (\(n=1\)) are likewise classical. Their general treatment emphasizes covering and triangulation bounds, not the displayed all-\(n\) three-class vertex-volume census for one arbitrary-dimensional simplex crossed with two segments or the resulting all-\(n\) sharp unrestricted ratio.

Ardila and Billey's *Flag arrangements and triangulations of products of simplices* (arXiv:math/0605598) studies, among other constructions, triangulations of products of **two** simplices. That is not an exact determinant spectrum for the present three-factor product. These observations delimit what is claimed rather than establish comprehensive historical priority.

## Limitations

The theorem does not classify maximizing simplices with nonvertex points: moving one simplex vertex along a segment can preserve the determinant in some configurations. It does not determine minimal triangulation cardinalities, and the volume lower bound need not be sharp. Although the all-dimensional spectrum and equality formula were not found in the inspected sources, a structurally equivalent count in unsearched older literature remains a priority risk. Numerical checks stop at \(n=4\), while the exact combinatorial proof covers every integer \(n\ge1\).

## References

1. T. Seacrest and F. E. Su, *A lower bound technique for triangulations of simplotopes*, arXiv:0910.1134 (first public preprint October 6, 2009; later published in *SIAM Journal on Discrete Mathematics*, 2018), https://arxiv.org/html/0910.1134v2 .
2. F. Ardila and S. Billey, *Flag arrangements and triangulations of products of simplices*, arXiv:math/0605598 (2006), https://arxiv.org/abs/math/0605598 .
