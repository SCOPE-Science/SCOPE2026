# Sharp side-distance Lipschitz constant for triangle strength

## Finding

Let \(T\) be a nondegenerate Euclidean triangle with side lengths \(a,b,c>0\), strict triangle inequalities, and semiperimeter \(p=(a+b+c)/2\). Its strength is

\[
\sigma(T)=\frac{\operatorname{Area}(T)^2}{p^3}
=\frac{(p-a)(p-b)(p-c)}{p^2}.
\]

On the open cone of nondegenerate triangle side triples, equipped with the metric
\[
 d_\infty((a,b,c),(a',b',c'))=\max\{|a-a'|,|b-b'|,|c-c'|\},
\]
the exact global Lipschitz constant of \(\sigma\) is \(3/8\). Thus every pair of nondegenerate triangles satisfies
\[
 |\sigma(T)-\sigma(T')|\le \frac{3}{8} d_\infty(T,T'),
\]
and no smaller constant works. The sharp value is a supremum approached by isosceles triangles whose side lengths are \((1-\varepsilon,(1+\varepsilon)/2,(1+\varepsilon)/2)\) as \(\varepsilon\downarrow0\); the limiting triangle is degenerate, so the supremum is not attained in the open domain.

This is a statement about perturbing the three side-length coordinates, not an assertion that \(3/8\) is the optimal constant for perturbing vertex coordinates in the Euclidean plane.

## Assumptions and scope

The domain is
\[
\mathcal T=\{(a,b,c)\in\mathbb R_{>0}^3:a<b+c,\ b<a+c,\ c<a+b\}.
\]
The metric is \(d_\infty\) on the ordered side-length triples. The strength is the standard squared-area divided by the cube of the semiperimeter, so it scales linearly under uniform scaling. The result is only for triangles; it does not assert an optimal perturbation constant for vertex-coordinate noise or for higher-dimensional simplices.

## Proof

Write
\[
 x=p-a,\qquad y=p-b,\qquad z=p-c.
\]
Then \(x,y,z>0\), \(p=x+y+z\), and \(a=y+z\), \(b=x+z\), \(c=x+y\). Heron's formula gives \(\sigma=xyz/(x+y+z)^2\). Since \(\sigma\) is homogeneous of degree one in the side lengths, its side-gradient is homogeneous of degree zero; for estimating that gradient we may normalize \(p=x+y+z=1\).

Define
\[
 X=yz(1-2x),\qquad Y=xz(1-2y),\qquad Z=xy(1-2z).
\]
These are the partial derivatives of \(xyz/(x+y+z)^2\) with respect to \(x,y,z\), evaluated at \(x+y+z=1\). The chain rule and \(a=y+z,b=x+z,c=x+y\) yield
\[
 \sigma_a=\frac{-X+Y+Z}{2},\quad
 \sigma_b=\frac{X-Y+Z}{2},\quad
 \sigma_c=\frac{X+Y-Z}{2}.
\]
For a differentiable function on the convex domain \(\mathcal T\), the global Lipschitz constant in \(d_\infty\) is bounded above by the supremum of \(|\sigma_a|+|\sigma_b|+|\sigma_c|\), by integrating the derivative along the line segment between two side triples. We show that this sum is at most \(3/8\).

First suppose \(x,y,z\le1/2\). Relabel the slacks so \(x\le y\le z\); then \(X\ge Y\ge Z\ge0\). Each is at most \(1/4\), since for example
\[
 X\le yz\le\frac{(y+z)^2}{4}=\frac{(1-x)^2}{4}\le\frac14,
\]
and the same argument applies to \(Y,Z\). If \(X\le Y+Z\), all three side derivatives are nonnegative and
\[
 |\sigma_a|+|\sigma_b|+|\sigma_c|=\frac{X+Y+Z}{2}\le\frac{3}{8}.
\]
If \(X>Y+Z\), only \(\sigma_a\) is negative, and
\[
 |\sigma_a|+|\sigma_b|+|\sigma_c|=\frac{3X-Y-Z}{2}\le\frac{3X}{2}\le\frac{3}{8}.
\]

Otherwise, after relabeling exactly one slack, say \(x\), exceeds \(1/2\). Then \(X<0\) and \(Y,Z>0\). Put \(u=-X,v=Y,w=Z\). The triangle inequality for real numbers gives
\[
 |\sigma_a|+|\sigma_b|+|\sigma_c|\le\frac32(u+v+w).
\]
Direct expansion using \(x+y+z=1\) gives
\[
 u+v+w=x(1-x)-yz-2xyz\le x(1-x)\le\frac14,
\]
so the same upper bound \(3/8\) follows. These cases exhaust the simplex of positive slacks.

To prove sharpness, take \(x=\varepsilon\) and \(y=z=(1-\varepsilon)/2\) for \(0<\varepsilon<1/2\). This corresponds to the nondegenerate side triple \((a,b,c)=((1-\varepsilon),(1+\varepsilon)/2,(1+\varepsilon)/2)\), with \(p=1\). As \(\varepsilon\downarrow0\), \(X\to1/4\) while \(Y,Z\to0\), so
\[
 (\sigma_a,\sigma_b,\sigma_c)\longrightarrow(-1/8,1/8,1/8)
\]
and the \(\ell_1\)-norm of the side-gradient tends to \(3/8\). For each positive \(\varepsilon\), the side triple lies in the open domain, so a sufficiently small perturbation in the side direction \((-1,1,1)\) remains admissible. Its directional derivative tends to the sum of the absolute side derivatives. Therefore every constant below \(3/8\) fails for some pair of nondegenerate triangles. This proves the claimed exact supremum.

## Verification

The accompanying `CHECK.py` uses exact rational arithmetic to check the derivative identities and the bound on a dense finite grid of positive slack triples, and checks that the isosceles boundary sequence approaches \(3/8\). These finite checks corroborate the algebra but are not the proof of the universal inequality; the case split above proves it for every positive slack triple. The proof uses only Heron's formula, the chain rule, convexity of the triangle side domain, and elementary inequalities.

## Relationship to prior work

Kurlin introduced the simplex strength \(\sigma=\operatorname{vol}^2/p^{2n-1}\) as a stable geometric descriptor and gave a Lipschitz bound for triangle strength under vertex perturbations (arXiv:2303.13486, Definition 4.1 and Theorem 4.2). Anosova and Kurlin's later account retains a dimension-two vertex-perturbation bound \(\lambda_2=\sqrt3\) (arXiv:2602.17630v2, Theorem 2.4 and its proof). Those statements use a different perturbation metric and do not state the exact \(d_\infty\) Lipschitz constant for the three side-length coordinates. The exact constant here is a sharp side-space stability modulus; it is not a claim about the optimal vertex-coordinate constant.

## Limitations

The theorem is specific to triangle strength and the \(\ell_\infty\) metric on side triples. It does not establish a sharp constant for the Euclidean perturbation of vertices, a higher-dimensional simplex, or a different normalization of strength. The extremal value is approached only at the boundary of the nondegenerate triangle domain. Literature searches and published-finding corpus comparisons do not prove exhaustive bibliographic uniqueness; an unindexed source may contain the same side-space calculation.

## References

1. V. Kurlin, *The strength of a simplex is the key to a continuous isometry classification of Euclidean clouds of unlabelled points*, arXiv:2303.13486 (first public version 2023-03-23), Definition 4.1 and Theorem 4.2.
2. O. Anosova and V. Kurlin, *The strength of a geometric simplex*, arXiv:2602.17630v2 (first public version 2026-02-19), Theorem 2.4 and the dimension-two proof.
