# No simultaneous-extension penalty for cyclic triples over an equilateral source

## Finding
Let \(A=\{a_0,a_1,a_2\}\) and \(B=\{b_0,b_1,b_2\}\) be disjoint layers of a six-point metric space. Suppose the three distances within \(A\) equal \(L>0\), those within \(B\) equal \(s>0\), and for \(i,j\in\mathbb Z/3\mathbb Z\) the cross distance is
\[
d(b_i,a_{i+j})=r_j>0.
\]
Then **for every nonzero real Banach target \(E\)**, the least operator norm of a real-linear, constant-preserving right inverse of restriction \(\operatorname{Lip}(A\cup B;E)\to\operatorname{Lip}(A;E)\), with Lipschitz seminorms, is
\[
\boxed{\Lambda=\max\!\left\{1,\frac{2L}{r_0+r_1+r_2}\right\}.}
\]
An optimal operator is a cyclically equivariant positive averaging operator. In particular, its sharp norm does **not** depend on \(s\), once the six distances define a metric.

For distinct radii, this is a genuinely three-parameter circulant cross-distance family, rather than the two-orbit matched/unmatched special case. The explicit optimizer changes support at the **triangle-defect threshold** \(r_{\max}=r_{\min}+r_{\mathrm{mid}}\), even though the norm is already one beyond that threshold.

As a geometric corollary, fix an equilateral Euclidean triangle with side \(L\), center \(o\), and rotation \(R\) through \(120^\circ\) about \(o\). For any planar point \(x\), extend from the three vertices to the union with \(\{x,Rx,R^2x\}\). Its optimal universal real-linear norm is
\[
\boxed{\Lambda(x)=\max\!\left\{1,\frac{2L}{|x-a_0|+|x-a_1|+|x-a_2|}\right\}.}
\]
The norm-one region is exactly the exterior, including the boundary, of the three-focus sublevel set \(\sum_j|x-a_j|<2L\). No claim is made about extending simultaneously to *every* planar point with this same norm.

## Assumptions and scope
Indices are taken modulo three. The distance assignment defines a metric **if and only if**, for every distinct \(i,j\),
\[
|r_i-r_j|\le\min\{L,s\},\qquad r_i+r_j\ge\max\{L,s\}.
\]
The theorem assumes these inequalities and all five parameters strictly positive, so the six points are distinct. For a Banach target, consider all bounded real-linear right inverses of restriction on the finite-dimensional spaces of Lipschitz maps modulo constant maps (equivalently, constant-preserving extensions acting on raw function spaces). The exact infimum is independent of the nonzero real Banach target. Norms are Lipschitz seminorm operator norms, not the ambient Euclidean norm or a nonlinear extension constant.

## Proof
**1. Equilateral transport identity.** On a three-point equilateral set of side \(L\), any coefficients \(c_i\in\mathbb R\) of sum zero satisfy
\[
\sup_{\operatorname{Lip}(f)\le1}\left|\sum_i c_i f(a_i)\right|=\frac L2\sum_i|c_i|.
\]
Indeed the sum of positive coefficients equals minus the sum of negative coefficients and moving this mass between opposite supports costs exactly \(L\) per unit. This proves the identity directly by a two-level test function and its matching upper bound. It also holds for vector-valued input by scalarization against norm-one functionals.

**2. Lower bound with no positivity assumption.** Average an arbitrary scalar extension over the three simultaneous cyclic permutations of \(A\) and \(B\); the averaging cannot increase its norm. At \(b_0\), write the resulting linear functional as \(\sum_i\alpha_i f(a_i)\). Constants must be preserved, so \(\sum_i\alpha_i=1\). By the identity in step 1, the column for the pair \((b_0,a_i)\) has norm at least \(L|1-\alpha_i|\). Therefore, for extension norm \(K\),
\[
K r_i\ge L|1-\alpha_i|,\qquad
K\sum_i r_i\ge L\sum_i|1-\alpha_i|\ge2L.
\]
As the operator is a right inverse, \(K\ge1\). For any arbitrary real Banach-space-valued linear extension, embed scalar data as multiples of a fixed unit vector and compose the output with a norm-one supporting functional. This produces a scalar linear extension with no larger norm, so the same lower bound holds for every target.

**3. Construct an optimal positive kernel when the radii form a triangle.** Put \(S=r_0+r_1+r_2\). If \(2r_{\max}\le S\), take
\[
\alpha_j=1-\frac{2r_j}{S}\quad(j=0,1,2),\qquad
(Tf)(b_i)=\sum_{j=0}^2\alpha_j f(a_{i+j}),
\]
while retaining \(Tf=f\) on \(A\). The coefficients are nonnegative and sum to one. For each source-target pair, the transport identity yields the exact operator-column norm
\[
\left\|\sum_j\alpha_j\delta_{a_{i+j}}-\delta_{a_{i+k}}\right\|_{\mathcal F(A)}
=L(1-\alpha_k)=\frac{2Lr_k}{S}.
\]
For a pair of distinct new points, the signed coefficient vector is a cyclic difference of a triple and therefore has transport norm
\[
L\big(\max_j\alpha_j-\min_j\alpha_j\big)
=\frac{2L}{S}(r_{\max}-r_{\min}).
\]
The metric inequality \(r_{\max}-r_{\min}\le s\) bounds the new-to-new operator ratio by \(2L/S\). The resulting norm is at most \(\max\{1,2L/S\}\).

**4. Construct an optimal positive kernel when one radius dominates.** If \(r_{\max}>r_{\min}+r_{\mathrm{mid}}\), let the two smaller radii be \(u\le v\), with indices \(p,q\), and let the largest have index \(h\). Define
\[
\alpha_p=\frac{v}{u+v},\qquad \alpha_q=\frac{u}{u+v},\qquad\alpha_h=0.
\]
Every source-target operator ratio is at most \(L/(u+v)\): the first two have equality and the third is \(L/r_h<L/(u+v)\). Every target-target operator ratio is at most \(Lv/((u+v)s)\). But metric feasibility implies \(u+v\ge L\) and \(s\ge r_h-u>v\). Consequently all new pair ratios are at most one. Also \(S>2(u+v)\ge2L\); hence the asserted \(\Lambda\) equals one. The two kernel formulas agree at \(r_h=u+v\), completing the classification, including boundaries and all real Banach targets.

**5. Geometric specialization.** For any planar \(x\), the lengths \(r_j=|x-a_j|\) satisfy \(2r_{\max}\le S\): the classical Pompeiu triangle inequality. For completeness, rotate \(x\) by \(60^\circ\) around one triangle vertex so that a second original vertex is mapped to the third; the triangle inequality in the resulting three-point diagram proves the relevant inequality, and cyclic relabeling gives all three. The three rotated target sites and three source vertices form the specified cyclic metric, provided they do not coincide; overlap at the original vertices follows directly or by continuity. This gives the formula in the finding. The function \(S(x)=\sum_j|x-a_j|\) is continuous, coercive, and strictly convex because the three foci are not collinear. Symmetry forces its unique minimum at \(o\), with \(S(o)=\sqrt3 L<2L\), whereas \(S(a_j)=2L\). Thus its \(2L\)-level is the exact boundary of the nonexpansive-extension region.

## Verification
The standalone file `cyclic_extension_checker.py` enumerates every source-function extreme point of the three-site Lipschitz unit ball, tests all fifteen pairs of the six-point extension metric for 384 rational instances, and checks the exact proposed norm. It reports `CYCLIC_TRIANGLE_EXACT_OK metrics=384 full_pairs=5760 extreme_pair_checks=34560 phases={'three': 382, 'two': 2}`. The optional `independent_lp_spotcheck.py` uses unrestricted numerical linear programming in nine coefficients, without assuming cyclic symmetry or positivity, on five test metrics; all five optima agree with the theorem. Finite checks support the analytic proof; they do not prove its infinite parameter range.

## Relationship to prior work
Bruè, Di Marino, and Stra (2018, arXiv:1801.07533v1) develop positive random-projection methods and general linear Lipschitz extension bounds but do not state an exact cyclic six-point constant. Basso (first public preprint 2017, arXiv:1707.06593v1, inspected in v3 HTML) studies extensions to finitely many points, including sharp one-point examples, but not a complete metric-circulant **simultaneous** three-point interpolation theorem. O'Hara (2020, arXiv:2002.07084v1) analyzes the geometry of the Pompeiu triple, supplying a geometric ingredient without an operator-norm statement. An existing exact one-point equilateral-source classification determines the separate extension problems; it does not by itself establish that three coupled orbit values impose no extra norm. Existing matched/nonmatched two-orbit results address the special case \(r_1=r_2\), not arbitrary distinct cyclic cross radii. A previously indexed three-focus radial-envelope computation describes extrema of the geometric sum but does not supply the linear extension theorem.

## Limitations
The exact classification is for **three equilateral source points and a single isometric cyclic orbit of three equilateral new points**. It does not assert norm independence for higher-order orbits, arbitrary six-point metrics, noncyclic cross matrices, general targets outside the real Banach category, nonlinear maps, or a uniform simultaneous extension to a continuum of Euclidean points. The geometric three-focus component relies on Pompeiu's theorem, which is classical; no novelty is claimed for that lemma, the one-point lower bound alone, or the known three-focus radial envelope. Literature comparison is not a proof of global uniqueness of the result.

## References
1. G. Basso, *Lipschitz extensions to finitely many points*, first posted 20 July 2017, arXiv:1707.06593v1; examined version v3, https://arxiv.org/html/1707.06593v3.
2. E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and C1 extension operators through random projection*, first posted 23 January 2018, arXiv:1801.07533v1, https://arxiv.org/abs/1801.07533.
3. J. O'Hara, *Pompeiu's theorem and the moduli space of triangles*, first posted 14 February 2020, arXiv:2002.07084v1, https://arxiv.org/abs/2002.07084.
4. D. Pompeiu, classical triangle-of-distances theorem (1936), used solely as a geometric ingredient and reproved in the text.
