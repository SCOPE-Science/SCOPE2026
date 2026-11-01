# Sharp Gaussian-perimeter symmetry breaking for one-axis translations of orthotopes

## Finding

A fixed Euclidean orthotope can have **two distinct, noncentral translations that maximize its Gaussian boundary measure**, even though the orthotope itself is centrally symmetric. The exact threshold and all maximizers are determined here in every dimension.

Write \(\varphi(s)=(2\pi)^{-1/2}\exp(-s^2/2)\) and \(\Phi(s)=\int_{-\infty}^s\varphi(u)\,du\). Let \(d\ge2\), \(a>0\), and \(b_2,\ldots,b_d>0\). For \(t\in\mathbb R\), put

\[
Q_t=[t-a,t+a]\times\prod_{j=2}^d[-b_j,b_j],\qquad
G(t)=\int_{\partial Q_t}(2\pi)^{-d/2}e^{-\|x\|^2/2}\,d\mathcal H^{d-1}(x).
\]

Define the positive constants

\[
q_j=2\Phi(b_j)-1,\qquad C=\prod_{j=2}^d q_j,\qquad
\Lambda=\sum_{j=2}^d\frac{2\varphi(b_j)}{q_j},\qquad
\delta=a(a-\Lambda)-1.
\]

**Complete one-axis classification.** If \(\delta\le0\), then \(G\) is strictly decreasing on \((0,\infty)\); its unique global maximizer is \(t=0\). If \(\delta>0\), then \(t=0\) is a strict local minimum, and \(G\) has precisely two global maximizers, \(t=\pm t_*\), where \(t_*\in(0,a-\Lambda)\) is the unique positive solution of

\[
\boxed{\;t_*=(a-\Lambda)\tanh(a t_*)\;.}
\]

In the second regime \(G\) strictly increases on \((0,t_*)\) and strictly decreases on \((t_*,\infty)\). For fixed transverse halfwidths \(b_2,\ldots,b_d\), the exact transition is

\[
\boxed{\;a_c=\frac{\Lambda+\sqrt{\Lambda^2+4}}2\;},
\]

with a unique centered maximizer for \(a\le a_c\) and a pair of noncentral maximizers for \(a>a_c\).

**Critical behavior.** As \(a\downarrow a_c\) from above, while the transverse halfwidths remain fixed,

\[
t_*=\frac{\sqrt{3\delta}}{a_c}+O(\delta^{3/2}),\qquad
G(t_*)-G(0)=\frac{3C\varphi(a_c)}{2a_c^2}\delta^2+O(\delta^3).
\]

At the critical value \(a=a_c\), the centered maximum is quartically flat:

\[
G(t)-G(0)=-\frac{C\varphi(a_c)a_c^2}{6}t^4+O(t^6)\qquad(t\to0).
\]

For a concrete planar example, the rectangle \(Q_t=[t-2,t+2]\times[-1,1]\) has \(\Lambda\approx0.708875\), hence \(a_c\approx1.415393<2\). Its maximizing offsets are approximately \(t=\pm1.275509\); its Gaussian boundary measure increases from \(G(0)\approx0.535640\) to \(G(t_*)\approx0.581020\). These decimal values are illustrative, not inputs to the proof.

## Assumptions and scope

The Gaussian is standard, centered and isotropic. Every halfwidth is strictly positive, \(d\) is any finite integer at least two, and only translation along the first coordinate is optimized; the orientation and all side lengths remain fixed. The Gaussian perimeter normalization is the surface integral of the standard \(d\)-dimensional Gaussian density, rather than a version multiplied by \(\sqrt{2\pi}\). All statements about strict monotonicity refer to positive translation distances. Euclidean facets have disjoint relative interiors; their overlaps are null sets for the boundary measure.

## Proof

**1. Exact facet decomposition.** Put \(q(t)=\Phi(t+a)-\Phi(t-a)\). The two facets normal to the first coordinate contribute \(C[\varphi(t-a)+\varphi(t+a)]\). The two facets normal to coordinate \(j\ge2\) contribute \(2\varphi(b_j)q(t)C/q_j\). Adding yields the exact identity

\[
\boxed{\quad G(t)=C\big[\varphi(t-a)+\varphi(t+a)+\Lambda q(t)\big].\quad}
\]

In particular \(G(-t)=G(t)>0\) and \(G(t)\to0\) as \(|t|\to\infty\).

**2. Derivative and global sign.** Since \(\varphi'(s)=-s\varphi(s)\) and \(q'(t)=\varphi(t+a)-\varphi(t-a)\), differentiation and the identities \(\varphi(t\mp a)=\varphi(a)e^{-t^2/2}e^{\pm at}\) give

\[
G'(t)=2C\varphi(a)e^{-t^2/2}\cosh(at)
\big[(a-\Lambda)\tanh(at)-t\big].
\]

For \(t>0\), set \(f(t)=(a-\Lambda)\tanh(at)-t\). If \(a-\Lambda\le0\), then \(f(t)<0\). Otherwise \(f(0)=0\), \(f'(0)=\delta\), and

\[
f''(t)=-2a^2(a-\Lambda)\operatorname{sech}^2(at)\tanh(at)<0
\qquad(t>0).
\]

Thus if \(\delta\le0\), strict concavity forces \(f(t)<0\) for every \(t>0\). If \(\delta>0\), \(f\) initially rises, is strictly concave, and tends to minus infinity, so it has exactly one positive zero \(t_*\). Since \(t_*=(a-\Lambda)\tanh(a t_*)\), necessarily \(0<t_*<a-\Lambda\). The derivative's sign, evenness and decay at infinity give all the asserted global extremizers. Solving \(a(a-\Lambda)=1\) for its unique positive root proves the threshold \(a_c\).

**3. Sharp critical expansion.** For fixed transverse widths, \(C\) and \(\Lambda\) are constants and \(a=a_c+O(\delta)\). Uniformly for \(a\) near \(a_c\), Taylor expansion of the critical-point equation at its nonzero solution yields

\[
0=\delta-\frac{a^2(1+\delta)}{3}t_*^2+O(t_*^4),
\]

hence \(t_*^2=3\delta/a_c^2+O(\delta^2)\). The previously derived derivative has the local expansion

\[
G'(t)=2C\varphi(a)\left[\delta t-\frac{a_c^2}{3}t^3+O(\delta t^3+t^5)\right].
\]

Integrating from zero to \(t_*\) gives the stated positive quadratic gain. At \(\delta=0\), integration instead gives exactly the negative quartic leading coefficient stated above. All remainders are ordinary one-variable analytic remainders for fixed positive transverse halfwidths.

## Verification

The included `verify.py` uses only the Python standard library. It evaluates the Gaussian density directly over every facet using independent Simpson quadrature for planar rectangles and three-dimensional boxes, and compares the result with the exact factorization. It also tests the derivative by centered finite differences, checks both global sign patterns over 280 deterministic random configurations in dimensions two through nine, and checks critical scaling in a near-threshold family. Run `python3 verify.py` in the same directory; the tested script reports 3,046 passed checks.

These finite computations are corroborative and do not establish the all-dimensional theorem. The all-dimensional proof is the facet decomposition and strict concavity argument above.

## Relationship to prior work

Csató and Giovagnoli (arXiv:2610.11677v1, publicly posted 8 October 2026) establish continuity of general radial weighted perimeters, inclusion monotonicity for appropriate *increasing* radial weights, and certain minimizer-existence results. Their Theorems 1.2 and 1.3, including the counterexamples in Section 3, do not provide a translation-phase classification for the *decreasing* Gaussian weight on orthotopes. The present result holds over a specific restricted translation family and is not a replacement for their general theorems.

Nadimpalli and Pascale (arXiv:2508.20079v1) revisit the global maximum order of Gaussian surface area over all convex sets, a different optimization in which the body itself varies. The geometric Gaussian isoperimetric literature similarly concerns sets under volume or symmetry constraints, rather than extrema of a fixed box's boundary measure under one-axis translations. Historical priority for an equivalent formula under older Gaussian-probability terminology is not conclusively settled.

## Limitations

The theorem does not classify simultaneous multi-coordinate translations, rotations, nonrectangular polytopes, non-Gaussian radial weights, or translated bodies subject to fixed Gaussian mass. The root \(t_*\) is given implicitly, not by a generally elementary expression. The numerical verifier is not an independent mathematical audit and cannot establish historical originality.

## References

1. G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1 (8 October 2026). https://arxiv.org/html/2610.11677v1
2. S. Nadimpalli and C. Pascale, *On the Maximal Gaussian Perimeter of Convex Sets, Revisited*, arXiv:2508.20079v1 (27 August 2025). https://arxiv.org/html/2508.20079v1
3. M. Barchiesi and V. Julin, *Symmetry of minimizers of a Gaussian isoperimetric problem*, arXiv:1805.03161 (8 May 2018). https://arxiv.org/abs/1805.03161
