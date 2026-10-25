# Exact Minkowski asymmetry and the unique center of every convex quadrilateral

## Finding

For a nondegenerate convex quadrilateral \(Q\subset\mathbb R^2\), let its diagonals intersect at \(O\). For each diagonal, divide the length of its shorter segment from \(O\) by the length of its longer segment. Denote the resulting ratios by \(p,q\in(0,1]\); their order is immaterial. Define the Minkowski asymmetry by
\[
s(Q)=\inf\{s\ge1:\ \exists c\in\mathbb R^2,\;-(Q-c)\subseteq s(Q-c)\}.
\]
Then the **exact affine-invariant formula** is
\[
\boxed{s(Q)=1+\frac{1-pq}{1+\min\{p,q\}}.}
\]
Every nondegenerate convex quadrilateral has **exactly one Minkowski center** \(c\) attaining this infimum. In canonical affine coordinates where the diagonal intersection is the origin and, after interchange of diagonals if necessary, \(0<p\le q\le1\) and
\[
Q=\operatorname{conv}\{(1,0),(0,1),(-p,0),(0,-q)\},
\]
that center is precisely
\[
\boxed{c=\frac{(s(Q)-1,\,1-q)}{s(Q)+1}.}
\]
The exact attainable range over nondegenerate quadrilaterals is \([1,2)\); asymmetry \(1\) occurs exactly for parallelograms.

## Assumptions and scope

The quadrilateral is full-dimensional, compact, and convex with four extreme vertices; no angle, cyclicity, or symmetry restriction is imposed. The diagonal intersection belongs to the relative interior of both diagonals, so both ratios are strictly positive. The formula is invariant under nonsingular affine mappings. To define the canonical coordinates, translate the diagonal intersection to \(0\), send the longer segment endpoint of each diagonal to a positive coordinate basis vector by an invertible linear transformation, and interchange axes to arrange \(p\le q\). The term **center** refers to central inversion and dilation, not to axis-reflection chirality or a Euclidean circumcenter.

## Proof

Write \(Q=Q_{p,q}\) in the canonical coordinates, with \(0<p\le q\le1\). Its four facet inequalities have outer normals
\[
a_1=(1,1),\quad a_2=(-1/p,1),\quad a_3=(-1/p,-1/q),\quad a_4=(1,-1/q),
\]
all normalized so that \(a_i\cdot x\le1\). In these same directions the opposite support values are
\[
(h_Q(-a_1),h_Q(-a_2),h_Q(-a_3),h_Q(-a_4))=(q,1/p,1/p,1/q).
\]
Indeed, each value follows by maximizing the corresponding linear functional over the four listed vertices; \(p\le q\le1\) ensures \(\max(1/p,1/q)=1/p\) and \(\max(p,1/q)=1/q\).

Set \(z=(s+1)c\). The inclusion \(-(Q-c)\subseteq s(Q-c)\) holds if and only if its support function satisfies each of the four facet inequalities, equivalently
\[
a_i\cdot z\le s-h_Q(-a_i),\qquad 1\le i\le4.\tag{1}
\]
The necessity is obtained by testing all \(x\in Q\) after rewriting the inclusion as \(z-Q\subseteq sQ\); sufficiency follows because the four facets define \(sQ\).

Consider the nonnegative weights
\[
\omega_1=\frac{1-pq}{(1+p)(1+q)},\quad
\omega_2=\frac{p}{1+p},\quad
\omega_4=\frac{q}{1+q}.
\]
They satisfy \(\omega_1+\omega_2+\omega_4=1\) and \(\omega_1a_1+\omega_2a_2+\omega_4a_4=0\). Multiply inequalities (1) with indices \(1,2,4\) by these weights and add. The center variable cancels, giving the universal lower bound
\[
s\ge \omega_1q+\frac{\omega_2}{p}+\frac{\omega_4}{q}
=\frac{2+p-pq}{1+p}=:\,s_*.
\]
Conversely let \(z_*=(s_*-1,1-q)\). The three constraints \(i=1,2,4\) in (1) hold with equality. For the remaining constraint \(i=3\), its right-hand side minus left-hand side is exactly
\[
(s_*-1/p)-a_3\cdot z_*=\frac{1-q^2}{q}\ge0.
\]
Thus (1) is feasible at \(s=s_*\), and the lower bound is attained. Since \(p=\min\{p,q\}\) in our ordered coordinates, the advertised formula follows.

If \(pq<1\), all three weights are strictly positive. Any minimizing \(z\) must make constraints \(1,2,4\) equalities, since their weighted sum equals the lower bound. Their normals span \(\mathbb R^2\), and the equalities determine uniquely \(z=z_*\), hence uniquely \(c=z_*/(1+s_*)\). If \(pq=1\), then \(p=q=1\), so \(Q\) is a parallelogram, \(s(Q)=1\), and the center of inversion of a bounded centrally symmetric body is unique. In the canonical form this center is the origin, again given by the formula.

The expression equals \(1\) exactly at \(p=q=1\), and is strictly less than \(2\) because \(1-pq<1+p\) for \(p>0\). Every \(\sigma\in[1,2)\) is realized by \(p=q=2-\sigma\) in the canonical family, giving \(s(Q)=\sigma\). This completes the proof.

## Verification

The included dependency-free exact-arithmetic program \(\texttt{checks/verify.py}\) enumerates every intersection of three of the four linear constraints in variables \((z_x,z_y,s)\), verifies feasibility of all candidate vertices, and compares the resulting minimum with the claimed formula for \(64\) ordered rational parameter pairs. It also tests the exhibited primal witness independently of the optimization. The script passed on all pairs, including \(p=q=1\), \(p=q<1\), and both parameter orderings. This finite exercise is a consistency test; the displayed dual certificate and primal witness prove the result for all real \(p,q\in(0,1]\).

## Relationship to prior work

The classical Minkowski measure of asymmetry is the point-inversion invariant denoted \(\alpha_0\) in Caragea, von Dichter, Gottwald, Grundbacher, Jahn and Runge (arXiv:2504.13013, publicly posted April 17, 2025). Their planar explicit analysis concerns axis-reflection chirality of triangles and parallelograms, not point-inversion asymmetry and its optimizing center for every quadrilateral. Xiong and Freund (arXiv:2608.30876, first posted August 31, 2026) use the reciprocal \(\operatorname{sym}(Q)=1/s(Q)\) in their general symmetry-dependent ellipsoidal rounding theorem; in the quadrilateral class the present formula makes this bound directly evaluable from diagonal intersection data. Brandenberg, von Dichter and González Merino (arXiv:2006.07259) give general Minkowski-center optimal-contact criteria and a planar golden-ratio theorem, rather than the quadrilateral calculation.

Related published geometric records concern the two-parameter Makai volume product and the centroid-chord asymmetry of quadrilaterals, and Minkowski asymmetry of certain hexagons. Those are different functionals or different classes, and do not state or establish the four-facet optimum and its unique center given here. General covering inequalities between vertex-convexification and Minkowski asymmetry supply only inequalities, not this equality classification.

## Limitations

This is a planar quadrilateral theorem, not a formula for polygons with more vertices. The canonical center coordinates are affine coordinates, not a Euclidean center-location formula invariant under similarities alone. The comparison with currently accessible literature supports originality on the investigated sources but cannot exclude equivalent statements in unindexed classical convex-geometry work. No independent external audit is claimed. The exact optimizer is characterized for the objective defined here; no claim of uniqueness of ellipsoidal rounding centers is made.

## References

1. A. Caragea, K. von Dichter, K. K. Gottwald, F. Grundbacher, T. Jahn, M. Runge, *Minkowski chirality: a measure of reflectional asymmetry of convex bodies*, arXiv:2504.13013 (first public version 2025-04-17), https://arxiv.org/abs/2504.13013 .
2. Z. Xiong and R. M. Freund, *Symmetry-dependence in Rounding of a Convex Body*, arXiv:2608.30876 (first public version 2026-08-31), https://arxiv.org/abs/2608.30876 .
3. R. Brandenberg, K. von Dichter, B. González Merino, *Relating Symmetrizations of Convex Bodies: Once More the Golden Ratio*, arXiv:2006.07259, https://arxiv.org/abs/2006.07259 .
