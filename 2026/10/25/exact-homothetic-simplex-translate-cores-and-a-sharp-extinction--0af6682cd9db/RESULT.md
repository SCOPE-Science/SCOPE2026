# Exact homothetic-simplex translate cores and a sharp extinction threshold

## Finding
Let \(d\ge2\), let \(S=\operatorname{conv}\{v_0,\ldots,v_d\}\subset\mathbb R^d\) be any nondegenerate simplex with barycentric coordinates \(\lambda_0,\ldots,\lambda_d\), and let \(s>0\). For \(0<\beta\le\min\{s,1\}^d\), define the high-mass translate core
\[
\mathcal F_{s,\beta}(S):=
\bigcap_{t:\,\operatorname{vol}_d(S\cap(sS+t))\ge\beta\operatorname{vol}_d(S)}(sS+t).
\]
The translating family is nonempty at every parameter in this range. The core has the exact, scale-independent description
\[
\boxed{\mathcal F_{s,\beta}(S)=\{y:\lambda_i(y)\ge1-\beta^{1/d}\text{ for every }0\le i\le d\}.}
\]
In particular, put \(\beta_\mathrm c=(d/(d+1))^d\) and let \(c\) be the centroid of \(S\). The core is empty for \(0<\beta<\beta_\mathrm c\), equals \(\{c\}\) for \(\beta=\beta_\mathrm c\), and is the positive homothetic simplex
\[
\mathcal F_{s,\beta}(S)=c+\big((d+1)\beta^{1/d}-d\big)(S-c)
\qquad(\beta_\mathrm c<\beta\le\min\{s,1\}^d).
\]
The exact relative volume in the nonempty range is
\[
\frac{\operatorname{vol}_d(\mathcal F_{s,\beta}(S))}{\operatorname{vol}_d(S)}
=\big((d+1)\beta^{1/d}-d\big)^d.
\]
Consequently there is a sharp **scale transition** at \(s=d/(d+1)\): for every \(s<d/(d+1)\), the intersection of *all* translates of \(sS\) capturing any fixed positive admissible fraction of \(S\) is empty; at equality the sole nonempty core is the singleton centroid at maximal overlap; for larger \(s\) the complete range of nonempty cores is the displayed centered homothetic family. All statements are affine-invariant and the scale threshold is attained.

## Assumptions and scope
Here \(sS\) denotes dilation around any chosen origin; varying the translation \(t\) removes dependence on that origin. The overlap fraction \(\beta\) must satisfy \(0<\beta\le\min(s,1)^d\); outside that range the family is empty and the usual intersection-of-empty-family convention would produce an unrelated entire-space artifact. The definition uses **nonstrict** overlap and includes maximal-overlap translates. A core may be empty, a point, or a full-dimensional simplex. The operation extends the translated-test-body floating intersection to scales for which \(S\) is not \(sS\)-ball-convex, and agrees with the latter construction where the requisite \(C\)-ball-convexity condition holds.

## Proof
Write \(\lambda_i\) for affine barycentric functionals, with \(\sum_i\lambda_i\equiv1\). Every translate \(T=sS+t\) is uniquely represented by thresholds \(a=(a_0,\dots,a_d)\) satisfying \(\sum_i a_i=1-s\), in the form
\[
T=\{z:\lambda_i(z)\ge a_i\text{ for all }i\}.
\]
Indeed, the coordinate inequalities of the dilated simplex read \(\lambda_i(z)\ge\lambda_i(t)-s\lambda_i(0)\), and summing their right sides gives \(1-s\). Conversely any threshold vector with this sum corresponds to some translation because barycentric coordinate differences encode arbitrary translations.

Set \(a_i^+=\max(a_i,0)\) and \(P(a)=\sum_i a_i^+\). Intersection with \(S\) imposes \(\lambda_i(z)\ge a_i^+\). If \(P(a)<1\) it is a homothetic copy of \(S\) with scale \(1-P(a)\), and if \(P(a)\ge1\) it has zero \(d\)-dimensional volume. Thus
\[
\frac{\operatorname{vol}_d(S\cap T)}{\operatorname{vol}_d(S)}=(1-P(a))_+^d.
\]
Write \(h=1-\beta^{1/d}\). The overlap requirement is exactly \(P(a)\le h\). Since \(\sum_i a_i=1-s\), the minimum possible positive-part sum is \(\max(0,1-s)\). Therefore the overlap condition is feasible exactly when \(\beta^{1/d}\le\min(s,1)\), proving the stated admissible parameter range.

For each fixed facet index \(j\), \(P(a)\le h\) implies \(a_j\le h\). This bound is *attained*: take \(a_j=h\) and choose the remaining \(d\) entries nonpositive with total \(1-s-h\le0\). Then \(\sum_i a_i=1-s\) and \(P(a)=h\), so the chosen translate satisfies the overlap threshold. Consequently
\[
\sup_{T:\,\operatorname{vol}(S\cap T)\ge\beta\operatorname{vol}(S)}a_j(T)=h
\qquad(0\le j\le d).
\]
Intersecting the inequalities \(\lambda_j(y)\ge a_j(T)\) over all admissible translates gives \(\lambda_j(y)\ge h\) for each \(j\), proving the exact core identity. As the barycentric coordinates sum to one, feasibility of these \(d+1\) inequalities is equivalent to \((d+1)h\le1\), i.e. \(\beta\ge(d/(d+1))^d\). At equality all coordinates equal \(1/(d+1)\), yielding the centroid. Above it, substitute \(\lambda_i(y)=h+\rho\lambda_i(x)\) with \(\rho=1-(d+1)h=(d+1)\beta^{1/d}-d\); this gives the centered homothety and its \(d\)-dimensional volume. Finally, the greatest allowed \(\beta\) is \(\min(s,1)^d\); comparing this with \(\beta_\mathrm c\) establishes every scale-transition assertion. No smoothness, orientation, or Euclidean regularity is required.

## Verification
A standalone Python/SciPy linear-programming checker, `verify_simplex_floating.py`, solves independently for each maximum feasible facet threshold over the overlap superlevel set. It validates \(700\) test cases across dimensions \(2\) through \(6\), seven dilation scales and four overlap ratios per scale, including maximal-overlap boundaries. This numerical check is ancillary: the explicit feasible extremizer and inequalities in the proof certify all dimensions and all real admissible parameters. Run `python verify_simplex_floating.py` with NumPy/SciPy available. The critical threshold is also checked analytically by \(\sum_i\lambda_i=1\).

## Relationship to prior work
Schütt, Werner and Yalikun [1] introduced high-overlap translate intersections as \(C\)-ball floating bodies for \(C\)-ball-convex bodies, and expressed them using the cross covariogram (their Definition 1, equations (4)–(5)). Their main result concerns curvature and relative affine surface area, not this simplex-scale diagram. The present theorem computes the entire intersection, volume and sharp extinction boundary for a homothetic simplex test family. The small-scale range where the simplex is not ball-convex with respect to its testing body is treated directly, without asserting that it satisfies the hypotheses of [1]. A later paper by Molchanov and Nagy [2] develops translation-depth regions and their general relation to floating bodies; its structural framework does not itself give the explicit higher-dimensional, arbitrary-scale simplex formulas above. The statement is not a determination theorem for a general convex body.

## Limitations
The formula requires the **same orientation and shape** for \(S\) and \(sS\), with translation as the only motion. Arbitrary unequal simplex shapes, rotations or nonuniform densities are not covered. At the maximal-overlap level, nonstrict inclusion is essential; replacing it by a strict inequality changes endpoint conventions. The checker samples finitely many dimensions and parameters, while the proof handles the infinite range. No independent mathematical audit is asserted.

## References
[1] C. Schütt, E. M. Werner and D. Yalikun, *Floating bodies for ball-convex bodies*, arXiv:2504.15488v1 (first posted 2025-04-21), https://arxiv.org/html/2504.15488v1.

[2] I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108v1 (first posted 2026-10-19), https://arxiv.org/html/2610.26108v1.
