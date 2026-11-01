# A logarithmic collision cusp and complete monotonicity for nested-circle random chords

## Finding

Let \(R\geq1\). Choose \(A,B\) independently and uniformly by arclength on the unit circle in the Euclidean plane; independently choose \(C,D\) uniformly by arclength on the concentric circle of radius \(R\). Let \(p(R)\) be the probability that the closed segments \([A,B]\) and \([C,D]\) intersect. All intersections are transverse almost surely.

**Theorem.** Define \(G(x)=\tfrac12-\tfrac2{\pi^2}(\arcsin x)^2\) for \(-1\le x\le1\). For every \(R\ge1\),
\[
p(R)=\frac1\pi\int_{-1}^1\frac{G(x)}{\sqrt{R^2-x^2}}\,dx
=\sum_{n=0}^{\infty}\frac{c_n}{R^{2n+1}},\qquad
c_n=\frac1\pi\frac{\binom{2n}{n}}{4^n}
\int_{-1}^1x^{2n}G(x)\,dx>0.
\]
The series converges absolutely also at \(R=1\). Thus \(p\) is strictly completely monotone on \((1,\infty)\): \((-1)^kp^{(k)}(R)>0\) for every integer \(k\ge0\). The rescaled function \(Rp(R)\) is strictly decreasing, with the globally sharp inequalities
\[
\frac{8}{\pi^3R}<p(R)\le\frac1{3R},\qquad R\ge1.
\]
The upper equality holds exactly at \(R=1\); the lower bound is unattained but asymptotically sharp as \(R\to\infty\). The genuinely singular equal-radius transition is
\[
\boxed{p(1+\varepsilon)=\frac13-\frac2{\pi^2}\varepsilon\log\frac1\varepsilon+O(\varepsilon)}
\qquad(\varepsilon\downarrow0).
\]
In particular, the right derivative at \(R=1\) is \(-\infty\). At large radius,
\[
p(R)=\frac8{\pi^3R}+\frac{28}{27\pi^3R^3}
+\frac{149}{375\pi^3R^5}+O(R^{-7}).
\]
Moreover, putting \(S(R)\) equal to the displayed three-term sum, a nonasymptotic remainder estimate valid for all \(R\ge1\) is
\[
0\le p(R)-S(R)\le\frac{C}{R^7},\qquad
C=\frac13-\frac8{\pi^3}-\frac{28}{27\pi^3}-\frac{149}{375\pi^3}.
\]

The structural contribution is the sharp logarithmic radius-collision cusp, complete monotonicity, and sharp scale-corrected global bounds. The underlying line-intersection integral is related by polarization to an existing general same-law intersection formula, and is not claimed as a wholly new integral representation.

## Assumptions and scope

The circles are concentric, have fixed radii \(1\) and \(R\ge1\), and all four endpoints are mutually independent with their respective uniform angular distributions. Chords mean finite straight line **segments**, not full affine lines, and touching events have probability zero. Scaling both radii leaves the law unchanged. Every assertion is exact for each fixed \(R\), rather than a claim about other random-chord conventions.

## Proof

**1. Projection and random-line reduction.** A chord with two independent uniform endpoints on a circle of radius \(R\) has an isotropically uniform supporting-line normal; independently, its oriented signed line offset \(H\) has arcsine density \(f_R(h)=1/(\pi\sqrt{R^2-h^2})\) for \(|h|<R\). This follows by writing the two endpoint angles in sum-and-difference coordinates: the normal direction is uniform while the signed offset equals \(R\cos\Phi\), with \(\Phi\) uniform on \([0,\pi]\). One may choose either sign of the normal consistently, without changing the unoriented line law.

The inner segment lies in the closed unit disk, itself contained in the outer disk. Consequently the outer *supporting line* meets the inner segment if and only if the two finite chords meet: any intersection point on the inner segment automatically belongs to the outer chord, which is precisely the portion of that line inside the outer disk.

Condition on the outer line's normal direction \(u\). The inner endpoint projections \(X=A\cdot u\) and \(Y=B\cdot u\) are independent with the arcsine distribution \(F(x)=\tfrac12+\pi^{-1}\arcsin x\) on \([-1,1]\). An intersection occurs exactly when \(H\) lies between \(X\) and \(Y\), so
\[
p(R)=\mathbb E\!\left[\int_{\min(X,Y)}^{\max(X,Y)}
\frac{dh}{\pi\sqrt{R^2-h^2}}\right].
\]
For fixed \(h\), the probability that \(h\) lies between \(X\) and \(Y\) is \(2F(h)(1-F(h))=G(h)\). Tonelli's theorem proves the stated one-dimensional integral.

**2. Series and sharp global ordering.** For \(R>1\), expand the positive binomial series
\[
(R^2-x^2)^{-1/2}=R^{-1}\sum_{n\ge0}
\frac{\binom{2n}{n}}{4^n}(x/R)^{2n}.
\]
The integrands are nonnegative, so monotone convergence extends the series to \(R=1\) (where the original integral is finite). Since \(G(x)>0\) for \(|x|<1\), every coefficient \(c_n\) is strictly positive. Termwise differentiation is valid locally uniformly for \(R>1\). Consequently every derivative has the indicated strict alternating sign, while \(Rp(R)=c_0+\sum_{n\ge1}c_nR^{-2n}\) is strictly decreasing.

Substitute \(x=\sin t\) into the integral at \(R=1\). Then
\[
p(1)=\frac1\pi\int_{-\pi/2}^{\pi/2}
\left(\frac12-\frac{2t^2}{\pi^2}\right)dt=\frac13.
\]
Direct elementary integration gives \(\int_{-1}^1G(x)dx=8/\pi^2\), hence \(c_0=8/\pi^3\). Since \(\sum c_n=p(1)=1/3\), strict monotonicity of \(Rp(R)\) proves both sharp scale-corrected inequalities and their equality conditions.

**3. Coefficients and a certified global remainder.** Set \(J_n=\int_{-1}^1x^{2n}G(x)dx\). Integration by parts, using \(x=\sin t\), gives
\[
J_0=\frac8{\pi^2},\qquad
J_1=\frac{56}{27\pi^2},\qquad
J_2=\frac{1192}{1125\pi^2}.
\]
Together with the binomial factors \(1,1/2,3/8\), this yields the three displayed \(c_n\). Positivity gives
\[
0\le\sum_{n\ge3}c_nR^{-(2n+1)}
\le R^{-7}\sum_{n\ge3}c_n=CR^{-7},
\]
without numerical truncation assumptions.

**4. The logarithmic singularity.** From the Taylor expansion of \(\arcsin\) at the endpoint, as \(x\uparrow1\),
\[
G(x)=\frac{2\sqrt2}{\pi}\sqrt{1-x}+O(1-x).
\]
The same holds with \(x\) replaced by \(-x\). Beta-integral asymptotics imply
\[
J_n=\frac1{\sqrt\pi\,n^{3/2}}+O(n^{-2}),\qquad
\frac{\binom{2n}{n}}{4^n}=\frac1{\sqrt{\pi n}}+O(n^{-3/2}),
\]
and thus \(c_n=\pi^{-2}n^{-2}+O(n^{-5/2})\). The error sequence has a convergent first weighted absolute moment, \(\sum_{n\ge1}n|c_n-\pi^{-2}n^{-2}|<\infty\).

Put \(\delta=\log R\). Since \(p(1)=\sum_{n\ge0}c_n\),
\[
p(1)-p(e^\delta)=\sum_{n\ge0}c_n(1-e^{-(2n+1)\delta})
=\frac1{\pi^2}\sum_{n\ge1}\frac{1-e^{-2n\delta}}{n^2}+O(\delta).
\]
The sum has derivative \(-2\log(1-e^{-2\delta})=2\log(1/\delta)+O(1)\). Integration from zero proves that it equals \(2\delta\log(1/\delta)+O(\delta)\). Finally \(\delta=\log(1+\varepsilon)=\varepsilon+O(\varepsilon^2)\), proving the sharp cusp coefficient and the infinite negative right derivative. All error constants are absolute in a sufficiently small right neighborhood of one.

## Verification

The standalone `check.py` recomputes the first three coefficients using independent quadrature, compares two separate integral representations at eight radii, verifies the sharp bounds and positive-series remainder, checks the logarithmic cusp numerically at four small detunings, and compares the analytic probability with direct four-endpoint geometric segment-intersection simulations. Run `python check.py` with NumPy and SciPy installed. Its successful final line is `ALL_CHECKS_PASSED`. Finite checks corroborate, but do not replace, the analytic proof.

## Relationship to prior work

Bortolotto and Ramos investigate crossings of **two chords whose four endpoints all lie on the same outer circle**, with the crossing constrained to a smaller concentric disk and with varying endpoint laws; their experiment is different from crossing an inner-circle chord with an outer-circle chord. Bortolotto and Souza establish a general intersection-radius law for two **same-law isotropic supporting lines**; polarizing that theorem with a mixture of two line laws can recover the present basic one-dimensional probability integral. Therefore the exact integral and the classical equal-radius value \(1/3\) are background reductions, not the priority assertion. The sharp \(\varepsilon\log(1/\varepsilon)\) cusp, strict complete monotonicity along the unequal-radius family, and sharp \(R^{-1}\) global constants require additional coefficient and boundary analysis not present in those inspected results. A separate classical one-chord question asks whether a random outer chord intersects the inner disk; it does not ask whether it meets an independently random *inner segment*.

## Limitations

The law depends on independently sampled endpoints, concentric circular boundaries, and Euclidean straight segments. It does not apply to Buffon-invariant random lines, offsets sampled uniformly, nonconcentric circles, or endpoint-dependent chord laws. The larger same-law theorem supplies a route to the integral, so novelty should be attributed to the nontrivial sharp parameter analysis rather than the reduction itself. A fully exhaustive search of older integral-geometric literature has not been established; historical priority remains provisional.

## References

1. Cynthia Bortolotto and João P. G. Ramos, *On Extremal Problems Associated with Random Chords on a Circle*, first public arXiv posting June 10, 2024, arXiv:2406.06771; subsequently *Mathematika* **71** (2025), e70024, DOI: 10.1112/mtk.70024. https://arxiv.org/abs/2406.06771
2. Cynthia Bortolotto and Victor Souza, *Intersections of Random Chords of a Circle*, *American Mathematical Monthly* **133** (2026), 661–680, DOI: 10.1080/00029890.2026.2662833. https://www.tandfonline.com/doi/full/10.1080/00029890.2026.2662833
3. Rick Wicklin, *The probability that two random chords of a circle intersect*, SAS DO Loop, July 11, 2018. https://blogs.sas.com/content/iml/2018/07/11/probability-two-chords-intersect.html
4. Eric W. Weisstein, *Concentric Circles*, MathWorld, Wolfram Research. https://mathworld.wolfram.com/ConcentricCircles.html
