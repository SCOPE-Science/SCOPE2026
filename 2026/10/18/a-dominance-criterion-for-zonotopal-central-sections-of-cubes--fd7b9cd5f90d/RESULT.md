# A dominance criterion for zonotopal central sections of cubes

## Finding

For every integer \(n\ge 2\), let \(Q_n=[-1,1]^n\), let \(a=(a_1,\ldots,a_n)\in\mathbb R^n\setminus\{0\}\), and let
\[
K(a)=Q_n\cap\left\{x:\sum_{i=1}^n a_i x_i=0\right\}.
\]
Write \(m=|\{i:a_i\ne0\}|\) and let \(A=\max_i|a_i|\), \(T=\sum_i|a_i|\). Then the following conditions are equivalent:

1. \(K(a)\) is a zonoid in its affine span.
2. \(K(a)\) is a zonotope in its affine span.
3. Either \(m\le3\), or \(2A\ge T\).

When \(m\ge4\) and \(2A\ge T\), the slice is an affine \((n-1)\)-cube. If \(m\ge4\) and \(2A<T\), an explicitly identified coordinate face of the slice is not centrally symmetric, proving that the slice is not even a zonoid. Equality \(2A=T\) is included in the positive case.

## Assumptions and scope

The cube is centered; the section passes through its center; all coefficients are real, not necessarily rational, and zero coefficients are allowed. Zonoids are Hausdorff limits of finite Minkowski sums of segments; a zonotope is a finite such sum. Central symmetry and zonotopality refer to the section's intrinsic \((n-1)\)-dimensional affine geometry. Here \(n\ge2\), \(m\ge1\), and the zero vector \(a\) is excluded.

## Proof

**Lemma (off-center cube sections).** Suppose \(r\ge3\), \(u_1,\ldots,u_r>0\), and \(0<|t|<\sum_j u_j\). The full-dimensional \((r-1)\)-polytope
\[
S(u,t)=[-1,1]^r\cap\{y:\sum_j u_jy_j=t\}
\]
is centrally symmetric **if and only if** some \(k\) satisfies
\[
u_k\ge |t|+\sum_{j\ne k}u_j.
\]

Indeed, if this inequality holds, solve for \(y_k\): every assignment \((y_j)_{j\ne k}\in[-1,1]^{r-1}\) produces \(|y_k|\le1\). Thus \(S(u,t)\) is an affine cube, symmetric about \((t/u_k)e_k\).

Conversely, suppose \(S(u,t)\) is centrally symmetric about \(c\). The coordinate restrictions \(y_i|_{u\cdot y=t}\) have pairwise nonparallel gradients in that affine hyperplane: if two were proportional, \(\alpha e_i+\beta e_j\) would be proportional to \(u\), impossible because \(r\ge3\), all coordinates of \(u\) are nonzero, and some index differs from \(i,j\). Every facet of \(S(u,t)\) therefore comes from a unique bounding hyperplane \(y_i=1\) or \(y_i=-1\). By central symmetry, each facet in \(y_i=1\) has an opposite parallel facet, necessarily in \(y_i=-1\), and conversely. Consequently for every coordinate \(i\) that defines a facet, \(c_i=0\).

At least \(r-1\) distinct coordinates define facets. Otherwise, retaining only all facet-defining coordinate inequalities leaves at least two unconstrained coordinates, permitting a nonzero line direction tangent to \(u\cdot y=t\), contrary to the boundedness of the polytope, which equals the intersection of its facet halfspaces. If every coordinate defines facets, then \(c=0\), contradicting \(u\cdot c=t\ne0\). Hence exactly \(r-1\) coordinates define facets. Let \(k\) be the remaining coordinate. Since a polytope equals the intersection of its facet halfspaces, its inequalities \(|y_k|\le1\) are redundant: in free coordinates \((y_j)_{j\ne k}\), the entire cube \([-1,1]^{r-1}\) is feasible. Solving for \(y_k\) gives \(|t-\sum_{j\ne k}u_jy_j|\le u_k\) for every such assignment. Maximizing the absolute value gives \(u_k\ge|t|+\sum_{j\ne k}u_j\). This proves the lemma, including all equality cases under the stated strict full-dimensional hypothesis.

**Main theorem.** Changing coordinate signs and permuting coordinates preserves the question, so we can arrange all nonzero \(a_i\) to be positive and ordered \(a_1=A\ge a_2\ge\cdots\ge a_m>0\), while the other \(n-m\) coordinates have zero coefficients. The section decomposes as the product of the intrinsic \(m\)-coordinate slice and \([-1,1]^{n-m}\).

If \(m\le3\), the intrinsic section has dimension at most two, is centrally symmetric (because the cube and hyperplane are centrally symmetric), and is therefore a zonotope; Cartesian products with segments preserve zonotopes.

If \(m\ge4\) and \(A\ge\sum_{j=2}^m a_j\), solving
\[
x_1=-\frac1A\sum_{j=2}^m a_jx_j
\]
shows \(|x_1|\le1\) for every other free cube coordinate. Thus \(K(a)\) is exactly the graph over an \((n-1)\)-cube and is an affine cube, including at equality.

Finally assume \(m\ge4\) and \(A<\sum_{j=2}^m a_j\). The intersection \(F=K(a)\cap\{x_1=-1\}\) is a proper exposed face. It is a product with the cube in the zero-coefficient coordinates of the off-center section
\[
[-1,1]^{m-1}\cap\left\{(x_2,\ldots,x_m):\sum_{j=2}^m a_jx_j=A\right\}.
\]
This is full-dimensional in its hyperplane because \(0<A<\sum_{j=2}^m a_j\). By the lemma it cannot be centrally symmetric: for each \(k\ge2\), one has \(a_k\le A<A+\sum_{j\ne1,k}a_j\). A Cartesian product with a cube cannot restore central symmetry, since projection of any central symmetry would give a central symmetry of the first factor. Thus \(F\) is not centrally symmetric. Every exposed face of a zonoid is centrally symmetric (indeed it is a translate of a lower-dimensional zonoid), so \(K(a)\) is not a zonoid. This proves all equivalences. \(\square\)

## Verification

The accompanying `check_cube_sections.py` uses exact rational arithmetic to enumerate vertices of coordinate faces cut from three- and four-dimensional cubes. It checks that none of the \(289\) non-dominant, sorted positive integer coefficient quadruples with entries \(1\) through \(8\) has a centrally symmetric largest-coordinate face; it also checks six five-coordinate examples, five dominant configurations, and 896 off-center three-cube sections including equality thresholds. These finite tests are sanity checks, not a substitute for the proof of the statements for all real parameters and dimensions. To reproduce, run `python check_cube_sections.py` with Python 3; no third-party packages are required.

## Relationship to prior work

Anantharaman's *Example of cube slices that are not zonoids* (2018, later publicly posted as arXiv:2305.18351) exhibited examples and proved a sufficient dominant-coefficient condition. It explicitly reported that necessity remained open in the general four-coordinate case, including a region with hexagonal coordinate faces. The theorem above gives necessity, handles equality and zero coefficients, and extends the classification to every dimension. The prior examples and the general fact that exposed faces of zonoids are themselves zonoids are credited.

Winter's 2021 classification paper lists the classical characterization of zonotopes by centrally symmetric faces, but addresses vertex-transitive zonotopes rather than classifying central cube sections. An available mathematical record on the face-vector distribution of Haar-random four-cube central sections identifies the same generic dominance transition in dimension four. It does not, in the information accessible for comparison, state this all-dimensional zonoid/zonotope characterization for arbitrary (including degenerate) coefficients.

## Limitations

The theorem concerns **central hyperplane sections of cubes**, not arbitrary affine sections, arbitrary codimension sections, or sections of general zonotopes. No new exact classification for noncentral sections is claimed. The finite checker cannot verify the universal statement independently of the proof. While targeted literature comparisons did not locate an equivalent all-dimensional theorem, a preexisting equivalent characterization under Banach-space terminology, or a stronger unpublished or unindexed treatment, remains a bibliographic risk. The complete text of the recent face-vector record was not accessible for direct comparison; only its public abstract-level description was available.

## References

- R. Anantharaman, *Example of cube slices that are not zonoids*, Scientiae Mathematicae Japonicae 81 (2018), 315–326; full-text preprint arXiv:2305.18351v2, https://arxiv.org/html/2305.18351v2 .
- M. Winter, *Classification of Vertex-Transitive Zonotopes*, Discrete & Computational Geometry 66 (2021), 1446–1462, https://doi.org/10.1007/s00454-021-00303-6 .
- E. D. Bolker, *A class of convex bodies*, Transactions of the American Mathematical Society 145 (1969), 323–345 (for classical zonoid facts referenced by Anantharaman).
