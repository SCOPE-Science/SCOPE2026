# Sharp isosceles-triangle approximation at fixed triangle slack

## Finding

For a nondegenerate Euclidean triangle \(T\), list its side lengths as \(0<a\le b\le c<a+b\). Define its *normalized triangle slack* and *optimal embedded isosceles-area ratio* by
\[
\delta(T)=\frac{a+b-c}{b}\in(0,1],\qquad
J(T)=\max_{\substack{I\subseteq T\\I\text{ an isosceles triangle}}}\frac{\operatorname{area}(I)}{\operatorname{area}(T)}.
\]
The lower-order datum \(\delta\) measures the strictness of the triangle inequality for the longest side; \(\delta=1\) characterizes equilateral triangles, whereas \(\delta\downarrow0\) means approach to a collinear degeneration after normalizing the middle side.

The **complete sharp lower envelope at every fixed slack** is as follows. Let \(\rho>1\) be the unique real root of \(\rho^4-\rho-1=0\) and put
\[
\delta_*=1+\rho^{-1}-\rho\approx0.598428428790425.
\]
For \(0<d<1\), set
\[
Y_1(d)=\frac{1-d+\sqrt{(1-d)^2+4}}2,
\]
and let \(Y_2(d)\) be the unique root in \((1,2-d)\) of
\[
Y_2(d)^3-2(1-d)Y_2(d)-d(2-d)=0.
\]
Then
\[
\boxed{\inf_{\delta(T)=d} J(T)=\mathcal M(d)=
\begin{cases}
1/Y_2(d),&0<d\le\delta_*,\\
1/Y_1(d),&\delta_*\le d\le1.
\end{cases}}
\]
For \(d=1\), interpret \(Y_1(1)=1\), so \(\mathcal M(1)=1\). In every fixed-slack class \(0<d\le1\), the minimizing triangle is unique up to Euclidean similarity: its ordered side ratios satisfy
\[
\boxed{\frac ab=Y(d)-1+d,\qquad\frac cb=Y(d),\qquad Y(d)=\min\{Y_1(d),Y_2(d)\},}
\]
with the \(d=1\) case interpreted by continuity. For \(d\in(0,\delta_*)\), two particular embedded-isosceles constructions tie at the minimum; for \(d\in(\delta_*,1)\), a different pair tie; at \(d=\delta_*\), all three canonical constructions tie. The envelope is continuous and strictly increasing from \(1/\sqrt2\) to \(1\), and has a genuine derivative jump at \(\delta_*\):
\[
\mathcal M'(\delta_*-) =\frac{2}{5\rho^2+\rho-2},\qquad
\mathcal M'(\delta_*+)=\frac{1}{1+\rho^2},
\]
\[
\boxed{\mathcal M'(\delta_*+)-\mathcal M'(\delta_*-)=
\frac{3\rho^2+\rho-4}{(1+\rho^2)(5\rho^2+\rho-2)}>0.}
\]

In particular, every nondegenerate triangle obeys the **globally sharp linear stability inequality**
\[
\boxed{J(T)>\frac1{\sqrt2}+\frac{\sqrt2-1}{4}\,\delta(T).}
\]
The constant \((\sqrt2-1)/4\) cannot be raised with the intercept \(1/\sqrt2\) fixed. Indeed,
\[
\mathcal M(d)=\frac1{\sqrt2}+\frac{\sqrt2-1}{4}d+O(d^2)
\qquad(d\downarrow0),
\]
and the unique fixed-slack minimizers tend to the collinear side-ratio triple \((a:b:c)=(\sqrt2-1:1:\sqrt2)\).

## Assumptions and scope

The ambient space is the Euclidean plane. Triangle containment allows contact with the boundary; the inscribed triangle is nondegenerate and has two equal side lengths. Area is ordinary Euclidean area. Shapes are considered up to similarity, not arbitrary affine transformations. The optimization over all nondegenerate host triangles is at a fixed dimensionless \(d=(a+b-c)/b\), where \(a\le b\le c\) are the ordered side lengths. No arbitrary orientation restrictions are imposed on the inscribed isosceles triangle. The endpoint \(d=0\) is excluded because its host triangle would have zero area; all endpoint statements there are limits.

## Proof

**1. Reduction to three established constructions.** Theorem 3(ii) and Corollary 8 of Ambrus, Csikós, Kiss, Pach and Somlai (2022) prove that the largest-area isosceles triangle inside any triangle is among three particular special embedded triangles. For \(a\le b\le c\), direct similar-triangle area calculations give their respective area ratios
\[
\frac ab,\qquad \frac bc,\qquad\frac{c^2}{b^2+c^2-a^2}.
\]
The last construction takes the perpendicular bisector of the longest side and intersects it with the adjacent side of length \(b\). To see its exact ratio, put \(A=(0,0)\), \(B=(c,0)\), \(C=(b\cos\theta,b\sin\theta)\), with \(\cos\theta=(b^2+c^2-a^2)/(2bc)>0\). The intersection \(C_1\in AC\) of the perpendicular bisector of \(AB\) with \(AC\) is at fraction \(c/(2b\cos\theta)=c^2/(b^2+c^2-a^2)\) of \(AC\); the fact \(a\le b\) makes this fraction at most one. The triangle \(ABC_1\) is isosceles and has that fraction of the host's area. The other two constructions shorten an adjacent side to equal the opposite side. By the cited full classification, not merely by these examples,
\[
J(T)=\max\left\{\frac ab,\frac bc,\frac{c^2}{b^2+c^2-a^2}\right\}.
\]
The formula extends by continuity to host triangles with equal sides, where an isosceles host itself gives \(J=1\).

**2. One-variable constrained minimax.** Normalize \(b=1\), write \(y=c/b\), \(x=a/b\), and impose \(d=1+x-y\). Every triangle at a fixed \(0<d<1\) corresponds uniquely to
\[
1\le y\le2-d,\qquad x=y-1+d,
\]
and its ratio is
\[
J(y,d)=\max\left\{f_1(y,d),f_2(y),f_3(y,d)\right\},
\]
where
\[
f_1=y-1+d,\qquad f_2=y^{-1},\qquad
f_3=\frac{y^2}{2(1-d)y+d(2-d)}.
\]
For fixed \(d\), \(f_1\) and \(f_3\) are strictly increasing in \(y\), while \(f_2\) is strictly decreasing. In particular, with \(D=2(1-d)y+d(2-d)>0\),
\[
\partial_y f_3=\frac{2y((1-d)y+d(2-d))}{D^2}>0.
\]
At \(y=1\), the decreasing function dominates the others strictly, and at \(y=2-d\), the increasing functions both equal one and dominate. Therefore the minimum occurs at the *unique* crossing
\[
f_2(y)=\max\{f_1(y,d),f_3(y,d)\}.
\]
The separate crossings of \(f_2=f_1\) and \(f_2=f_3\) occur at \(y=Y_1(d)\) and \(y=Y_2(d)\), respectively. As the increasing envelope reaches the decreasing branch at the earlier crossing, the unique minimizer is \(Y(d)=\min\{Y_1(d),Y_2(d)\}\). This proves the expression for \(\mathcal M\) and the unique minimizing similarity class.

**3. Exact phase threshold.** At \(y=Y_1(d)\), the equality \(f_1=f_2\) gives \(d=1+y^{-1}-y\). On substituting this into the cubic equation for \(Y_2\), its left side factors as
\[
y^3-2(1-d)y-d(2-d)=\frac{(y-1)(y^4-y-1)}{y^2}.
\]
The polynomial \(y^4-y-1\) has precisely one zero \(\rho>1\), because its derivative is positive there. The function \(Y_1(d)\) decreases strictly from the golden ratio to one, crossing \(\rho\) at \(d=\delta_*\). For \(d<\delta_*\), the \(f_2=f_3\) crossing comes first; for \(d>\delta_*\), the \(f_2=f_1\) crossing comes first. The former gives \(1/Y_2\), the latter \(1/Y_1\). Both roots decrease with \(d\), proving strict increase of \(\mathcal M\). Implicit differentiation of their defining equations at the crossing, followed by \(\rho^4=\rho+1\), gives the displayed one-sided slopes. Their difference is positive because \(\rho>1\) implies \(3\rho^2+\rho-4>0\).

**4. Sharp linear stability.** Put \(r_0=1/\sqrt2\), \(k=(\sqrt2-1)/4\), and \(h=r_0+kd\). For every \(0<d\le1\), the exact identity
\[
\begin{aligned}
1-2(1-d)h^2-d(2-d)h^3
=d^2\biggl(&\frac{11-6\sqrt2}{8}
+\frac{12-7\sqrt2}{16}d\\
&+\frac{4\sqrt2-5}{32}d^2
+\frac{5\sqrt2-7}{64}d^3\biggr)>0
\end{aligned}
\]
holds: each displayed coefficient is strictly positive. For fixed \(d\), the function \(f_3(y,d)\) increases with \(y\). If \(J(y,d)\le h\), then \(f_2=1/y\le h\), so \(y\ge1/h\). Consequently,
\[
f_3(y,d)\ge f_3(1/h,d)>h,
\]
where the strict last inequality is precisely the positive polynomial identity after multiplying through by its positive denominators. This contradicts \(J(y,d)\le h\), establishing the stated strict inequality.

Finally, on the first branch \(Y_2(d)\) satisfies \(F(y,d)=y^3-2(1-d)y-d(2-d)=0\). At \((y,d)=(\sqrt2,0)\) its partial derivatives are \(F_y=4\) and \(F_d=2(\sqrt2-1)\). Thus \(Y_2'(0+)=-(\sqrt2-1)/2\), and
\[
\mathcal M'(0+)=\frac{\sqrt2-1}{4}=k.
\]
The actual fixed-slack minimizing triangles, which exist for every \(d>0\), therefore force the global linear coefficient to be no larger than \(k\). Their side ratios tend to \((\sqrt2-1):1:\sqrt2\), as claimed. This completes the proof.

## Verification

The companion standalone checker `checker.py` uses symbolic polynomial identities and independent Euclidean-coordinate area constructions. Running `python checker.py` with the dependency listed in `requirements.txt` verifies the positive-coefficient certificate, the quartic transition factor, the derivative relations, representative exact phase branches, and 12,000 seeded numerical side triples. Its expected terminal line is `ALL_CHECKS_PASSED`. The symbolic identities and the proof above establish the universal theorem; numerical sampling alone cannot certify it.

## Relationship to prior work

Ambrus, Csikós, Kiss, Pach and Somlai (2022), Theorem 3(ii) and Corollary 8, provide the powerful underlying theorem that the **pointwise** maximum embedded isosceles area comes from three specific constructions. This is explicitly used, not rediscovered here. They do not state the sharp **minimum over host triangles constrained by normalized triangle slack**, its unique extremizing host shape at every slack, the quartic switch, or the optimal global linear stability coefficient. The present result solves that additional constrained minimax problem rather than claiming the earlier per-triangle formula as new.

Kiss, Pach and Somlai (2020) prove a sharp \(\sqrt2\) *enclosing* isosceles-area guarantee; it is not an inscribed triangle fixed-slack optimization and does not assert the phase transition above. The numerical coincidence between the limiting reciprocal constant here and their enclosing bound does not establish a duality theorem. Priority remains subject to further specialist literature review, especially because the earlier pointwise classification makes this refined optimization approachable.

## Limitations

The result is Euclidean and planar, applies only to isosceles triangles embedded in a triangle, and uses a specifically normalized side-slack parameter. It does not extend without proof to arbitrary convex domains, other norms, or fixed-perimeter classes. No noisy-data or numerical optimization error guarantees are claimed. The limiting sharp family is collinear at \(d=0\) and is **not** an equality case among nondegenerate triangles. The derivation invokes the cited established pointwise classification; the new step is the constrained minimax/stability analysis. Literature comparisons do not constitute an independent historical priority certificate.

## References

1. Á. Ambrus, M. Csikós, G. Kiss, J. Pach and G. Somlai, *Optimal Embedded and Enclosing Isosceles Triangles*, arXiv:2205.11637 (initial public posting 23 May 2022); published in *International Journal of Foundations of Computer Science* 34 (2023), 737–760. https://arxiv.org/abs/2205.11637 .
2. G. Kiss, J. Pach and G. Somlai, *Minimum Area Isosceles Containers*, arXiv:2001.09525 (initial public posting 26 January 2020); *Journal of Information Processing* 28 (2020), 759–765. https://arxiv.org/abs/2001.09525 .
