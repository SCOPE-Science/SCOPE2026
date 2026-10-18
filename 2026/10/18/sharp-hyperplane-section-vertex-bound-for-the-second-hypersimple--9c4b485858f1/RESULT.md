# Sharp hyperplane-section vertex bound for the second hypersimplex

## Finding

For every integer \(n\ge3\), let the second hypersimplex be
\[
\Delta(n,2)=\operatorname{conv}\{e_i+e_j:1\le i<j\le n\}\subset\{x\in\mathbb R^n:\sum_i x_i=2\}.
\]
Its affine dimension is \(n-1\). Among **all nonempty affine hyperplane sections**, including those through polytope vertices, the largest possible number of vertices is exactly
\[
\boxed{\max_H f_0(\Delta(n,2)\cap H)=2\sum_{k=2}^{n-1}\left\lfloor\frac{k^2}{4}\right\rfloor
=\binom n3+\left\lfloor\frac{(n-1)^2}{4}\right\rfloor.}
\]
The bound is attained by generic hyperplanes through the centroid \((2/n)\mathbf1\), so restricting to central sections does not reduce the maximum. In particular the maxima for \(n=3,4,5,6,7,8\) are \(2,6,14,26,44,68\).

There is also a complete equality criterion for generic sections. A generic cutting hyperplane induces the *pair-sign graph* \(G\) on \([n]\), where \(ij\) is an edge if \(e_i+e_j\) lies in its chosen positive halfspace. This is a threshold graph. Write any threshold-graph construction as a first vertex followed by \(n-1\) isolated/dominating addition bits \(b_2,\ldots,b_n\in\{0,1\}\), where \(1\) means dominating. The section attains the displayed bound **if and only if** for each \(k=2,\ldots,n-1\), the final \(k\) bits contain numbers of zeros and ones differing by at most one. Every such construction word gives an extremal affine section. The statement about equality words applies to generic sections; the numerical bound applies to all sections.

## Assumptions and scope

A hyperplane means an affine codimension-one hyperplane in the affine hull of \(\Delta(n,2)\). Generic means that it avoids all \(\binom n2\) vertices. For a generic section, each section vertex is the transverse intersection of the cutting hyperplane with one edge of the hypersimplex. In the trivial case of a disjoint hyperplane the section has zero vertices. No probabilistic or asymptotic assumption is used. The statement holds at every finite \(n\ge3\).

A generic hyperplane may be written, without loss, as \(\sum_i a_ix_i=t\). We use the sign of \(a_i+a_j-t\) for its vertex \(e_i+e_j\). An overall reversal interchanges the two signs but does not affect the section's vertex count.

## Proof

**1. Reduction to sign-mixed triangles.** The one-skeleton of \(\Delta(n,2)\) is the Johnson graph \(J(n,2)\): \(e_i+e_j\) and \(e_i+e_k\) are adjacent when they share precisely one coordinate. This follows directly by intersecting the cube \([0,1]^n\) with \(\sum x_i=2\), or from the hypersimplex adjacency description of Kaibel and Walter. Each Johnson edge belongs to exactly one unordered triple of distinct indices. The three vertices \(e_i+e_j,e_i+e_k,e_j+e_k\) belonging to such a triple span a triangle in the one-skeleton.

Let \(G\) be the sign graph of the cutting hyperplane, so that \(ij\in E(G)\) precisely when \(a_i+a_j>t\). A triple of indices is **mixed** when its three pair-signs are not all equal. The cut across the corresponding Johnson triangle traverses exactly two of its three edges if the triple is mixed, and none otherwise. Different index triples supply disjoint Johnson edges. Thus the exact section-vertex count is
\[
f_0(\Delta(n,2)\cap H)=2M(G),\qquad
M(G)=\#\{\{i,j,k\}:\text{their three pair-signs are mixed}\}.
\]

**2. Threshold-word reduction.** By its additive pair-weight definition, \(G\) is a threshold graph. The standard equivalent construction adds each vertex as either isolated or dominating relative to all earlier vertices; this equivalence is explicitly recalled in Diaconis, Holmes and Janson (2009), Section 1, and the binary construction is discussed in their Section 2. Choose any construction ordering and denote its bits by \(b_2,\ldots,b_n\). For \(i<j<k\) in construction order, the pair signs are exactly \(b_j,b_k,b_k\). Hence the triple is mixed exactly when \(b_j\ne b_k\). Reorder the count according to the first index \(i\):
\[
M(G)=\sum_{i=1}^{n-2}Z_iO_i,
\]
where \(Z_i\) and \(O_i\) are the numbers of zero and one bits in the suffix \(b_{i+1},\ldots,b_n\). Their sum is \(n-i\). Therefore
\[
M(G)\le\sum_{i=1}^{n-2}\left\lfloor\frac{(n-i)^2}{4}\right\rfloor
=\sum_{k=2}^{n-1}\left\lfloor\frac{k^2}{4}\right\rfloor.
\]
Equality holds if and only if each of these suffixes is balanced to within one bit, as claimed. This argument is an exact bound for **every** threshold graph, with no restriction on the magnitudes of its representing weights. Conversely, each isolated/dominating word represents some threshold graph by strictly separating pair sums from a real threshold; its corresponding affine section therefore realizes the count specified by that word. All balanced-suffix words realize the maximum.

**3. Central attainment.** Label indices in their natural increasing order and begin with the centered normal coordinates
\[
a_i^{(0)}=i-\frac{n+1}{2},\qquad\sum_i a_i^{(0)}=0.
\]
Choose an arbitrarily small centered perturbation \(\eta_i\), with \(\sum_i\eta_i=0\) and \(|\eta_i|<1/10\), outside the finitely many hyperplanes on which \(a_i^{(0)}+\eta_i+a_j^{(0)}+\eta_j=0\) for some \(i<j\). Such perturbations exist because these proper hyperplanes cannot cover the \((n-1)\)-dimensional centered normal space. The resulting plane \(\sum_i(a_i^{(0)}+\eta_i)x_i=0\) passes through the centroid, avoids all hypersimplex vertices and leaves the sign of every originally nonzero pair sum unchanged.

For each index triple \(i<j<k\), the smallest and largest unperturbed pair sums are \(i+j-(n+1)\) and \(j+k-(n+1)\). Strict mixed triples therefore obey \(i+j<n+1<j+k\). For fixed middle index \(j\), each inequality has exactly \(s_j=\min(j-1,n-j)\) possible choices, giving \(\sum_{j=2}^{n-1}s_j^2\) strict mixed triples.

The only ties are complementary pairs \(i<j\) with \(i+j=n+1\). A tied pair appearing as the *middle* pair of a triple has one smaller negative and one larger positive pair sum; that triple is already counted and stays mixed. For a tied pair \((i,n+1-i)\), there are exactly \(i-1\) additional triples with a third index smaller than \(i\), and exactly \(i-1\) with a third index larger than \(n+1-i\). Resolving the tie positively makes precisely the first group mixed; resolving it negatively makes precisely the second group mixed. Hence the total new contribution is \(i-1\), independent of the perturbation. No triple has both its smallest and largest pair sums tied.

Writing \(m=\lfloor n/2\rfloor\), every sufficiently small generic centered perturbation consequently has
\[
M(G)=\sum_{j=2}^{n-1}\min(j-1,n-j)^2
+\sum_{i=1}^{m}(i-1).
\]
Splitting these elementary sums by the parity of \(n\) gives exactly
\[
M(G)=\sum_{k=2}^{n-1}\left\lfloor\frac{k^2}{4}\right\rfloor.
\]
Thus centered generic hyperplanes attain the universal upper bound. Using \(\lfloor k^2/4\rfloor=(k^2-\mathbf1_{k\,\mathrm{odd}})/4\) and the sum of squares gives the equivalent closed form in the theorem.

**4. Nongeneric sections.** If a hyperplane passes through hypersimplex vertices, a sufficiently small parallel displacement into a side of the polytope that it meets eliminates all vertex incidences and has at least as many section vertices: each old section vertex lying at a hypersimplex vertex supplies an edge intersection after the displacement, while already transverse edge intersections persist. A further arbitrarily small perturbation of direction avoids residual degeneracies without decreasing this count. This is also the perturbation lemma stated and proved by De Loera, Lopez-Campos and Torres (2024, Lemma 2.1) for general polytopes. Hence the generic upper bound applies to all affine hyperplane sections. This completes the proof.

## Verification

The accompanying `checker.py` is standalone Python using only the standard library. Run `python3 checker.py`. It exhaustively enumerates all threshold construction words through \(n=15\), independently counts mixed triples directly, and verifies the sharp formula and exact suffix-balance criterion. It also constructs generic sum-zero integer normals near centered arithmetic progressions and arbitrary generic sum-zero integer normals; for each it independently counts crossings across Johnson edges indexed by triples. All calculations of signs and combinatorial counts use integers, not floating-point tolerances. The checked cases are finite corroboration; the proof above establishes all \(n\).

## Relationship to prior work

The foundational ingredients are established: the hypersimplex vertex/adjacency structure is described by Kaibel and Walter (2013 preprint, Section 4); additive-weight and isolated/dominating descriptions of threshold graphs are classical and explicitly developed by Diaconis, Holmes and Janson (2009, Sections 1–2); De Loera, Lopez-Campos and Torres (2024, Theorem 1.1 and Lemma 2.1) give general bounds on section vertices and a perturbation principle. No novelty is claimed for any of these ingredients.

The result here is the **family-specific sharp maximum** for the second hypersimplex, the balanced-suffix equality classification, and attainment by central sections for every dimension. The 2024 general bound for polytopes of dimension at least four having \(N\) vertices is \(\lfloor N^2/4\rfloor\), attained by other polytope families; substituting \(N=\binom n2\) does not imply the much smaller sharp hypersimplex number. The examined threshold-graph source treats graph limits and constructions, not the maximum mixed-triple statistic. The inspected hypersimplex source treats extension complexity, not hyperplane sections. Overlap checks include the associated graph reformulation and the all-dimensional central-section case. Historical priority, especially under a threshold-graph extremal reformulation, remains open to independent checking.

## Limitations

The equality-word characterization applies only to generic sections; degenerate sections are covered by the numerical bound, not individually classified. The statement is specific to the second hypersimplex and does not assert analogous formulas for higher hypersimplex levels. It counts vertices, not higher-dimensional faces or section volume. The calculations establish a theorem by the displayed finite combinatorial proof, not by a computational search. Independent review and definitive bibliographic priority verification have not been performed.

## References

1. P. Diaconis, S. Holmes and S. Janson, *Threshold graph limits and random threshold graphs*, arXiv:0908.2448, first public 17 August 2009, Sections 1–2. https://arxiv.org/abs/0908.2448
2. V. Kaibel and M. Walter, *Simple Extensions of Polytopes*, arXiv:1311.3470, first public 14 November 2013, Section 4. https://arxiv.org/abs/1311.3470
3. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in a Hyperplane Section of a Polytope*, arXiv:2412.12419, first public 17 December 2024, Theorem 1.1 and Lemma 2.1. https://arxiv.org/abs/2412.12419
