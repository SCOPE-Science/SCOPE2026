# Exact minimum-width law for a circle-inscribed random triangle

## Finding

Choose three points independently and uniformly by arclength from the Euclidean unit circle. Let \(T\) be their convex hull and let \(W\) be its minimum Euclidean width (the minimum distance between parallel supporting lines, over all orientations). Almost surely \(T\) is a nondegenerate triangle. The **complete distribution** of \(W\) is supported on \([0,3/2]\), is given by the one-dimensional integral below, and has exactly computable first two moments and endpoint tails.

For \(0<t<3/2\), let \(b_0=b_0(t)\) denote the **unique** root in \((0,\pi/3)\) of
\[
2\sin b_0\cos(b_0/2)=t,
\]
and let \(b_1=\arcsin\sqrt{t/2}\). Then
\[
\boxed{\Pr(W\le t)=\frac{12}{\pi^2}\left[\frac{\pi b_0}{2}-\frac{3b_0^2}{4}+\int_{b_0}^{b_1}\left(\arcsin\frac{t}{2\sin b}-b\right)\,db\right].}
\]
The cumulative distribution is zero for \(t\le0\) and one for \(t\ge 3/2\). Its exact mean, second moment, and variance are
\[
\boxed{\mathbb E W=\frac5{\pi^2},\qquad \mathbb E W^2=1-\frac{47}{8\pi^2},\qquad \operatorname{Var}(W)=1-\frac{47}{8\pi^2}-\frac{25}{\pi^4}.}
\]
There are two distinct sharp endpoint laws. The thin-triangle tail has a logarithmic enhancement and an exact next term:
\[
\boxed{\Pr(W\le t)=\frac{3t}{\pi^2}\left[\log\frac8t+1\right]+o(t)\qquad(t\downarrow0).}
\]
The near-equilateral upper tail is quadratic:
\[
\boxed{\Pr(W>3/2-\varepsilon)\sim\frac{12}{\pi^2}\varepsilon^2\qquad(\varepsilon\downarrow0).}
\]

## Assumptions and scope

The three points are independent with uniform *arclength* measure on one fixed unit circle. Width is intrinsic planar minimum caliper thickness, not average width, minimum side length, shortest chord, area, or circumradius. All probabilities are with respect to the three-point sampling law. Equal sampled vertices and gap ties form null sets. A circle of radius \(R>0\) multiplies every stated width and endpoint by \(R\), with moments scaling by the corresponding power of \(R\).

## Proof

**1. Uniform semicircular gap simplex.** Rotate the configuration so its first independently sampled point lies at angular position zero. The remaining two angles are independent uniform points of \([0,2\pi)\). After sorting them, the three successive circular arc lengths, divided by two, are nonnegative angles \(\alpha,\beta,\gamma\) satisfying \(\alpha+\beta+\gamma=\pi\). Their joint density in two coordinates is constant \(2/\pi^2\) on the simplex. Since width is symmetric in the gaps, sort them as \(\alpha\ge\gamma\ge\beta\). The six disjoint ordering chambers give density \(12/\pi^2\) in the two-dimensional region
\[
0\le\beta\le\pi/3,\qquad \beta\le\gamma\le(\pi-\beta)/2,
\]
whose Euclidean area is \(\pi^2/12\).

**2. Exactly the minimum altitude.** A triangle achieves its minimum supporting-line separation in a direction normal to one of its sides. These three candidates are its altitudes; therefore \(W=2\Delta/L_{\max}\), where \(\Delta\) is triangle area and \(L_{\max}\) the longest side. The three sides are \(2\sin\alpha\), \(2\sin\beta\), \(2\sin\gamma\). If \(\alpha\le\pi/2\), sine is increasing through all three. If \(\alpha>\pi/2\), then \(\sin\alpha=\sin(\beta+\gamma)\) exceeds both \(\sin\beta\) and \(\sin\gamma\), because \(\beta+\gamma<\pi/2\). Thus the longest side always corresponds to the largest gap \(\alpha\). Using the unit-circumcircle sine rule and area formula, the altitude to this side is exactly
\[
\boxed{W=2\sin\beta\sin\gamma.}
\]
The ordered domain implies \(0<W\le3/2\), with equality only at the equilateral configuration.

**3. Exact distribution.** For a fixed \(\beta=b\), the allowable \(\gamma\) range is \([b,(\pi-b)/2]\). Throughout it, \(\sin\gamma\) is increasing. The smallest width on this interval is \(2\sin^2b\), and the largest is \(2\sin b\cos(b/2)\). Both functions strictly increase for \(0\le b\le\pi/3\): for the latter, write \(u=\sin(b/2)\) and \(2\sin b\cos(b/2)=4u(1-u^2)\) with \(0\le u\le1/2\). Hence for \(0<t<3/2\), the entire slice is accepted if \(b\le b_0\), a proper initial subinterval of \(\gamma\) is accepted if \(b_0<b\le b_1\), and no point is accepted for \(b>b_1\). On the middle interval the upper permissible \(\gamma\) is \(\arcsin(t/(2\sin b))\). Integrating the constant density yields precisely the displayed cumulative distribution. The formula integrates the complete support and has no missing atoms.

**4. Exact moments.** For any nonnegative integer \(k\),
\[
\mathbb E[W^k]=\frac{12}{\pi^2}\int_0^{\pi/3}\int_b^{(\pi-b)/2}(2\sin b\sin g)^k\,dg\,db.
\]
For \(k=0\) the result is one. For \(k=1\), inner integration gives \(\cos b-\sin(b/2)\), followed by
\[
\int_0^{\pi/3}\sin b\,[\cos b-\sin(b/2)]\,db=\frac5{24},
\]
so \(\mathbb E W=5/\pi^2\). For \(k=2\), use \(\int\sin^2g\,dg=g/2-\sin(2g)/4\). The remaining outer integral is
\[
\int_0^{\pi/3}\sin^2b\left[\frac{\pi-3b}{4}-\frac{\sin(\pi-b)-\sin(2b)}4\right]db=\frac{\pi^2}{48}-\frac{47}{384}.
\]
Multiplication by \(48/\pi^2\) establishes the claimed second moment.

**5. Sharp thin tail.** As \(t\downarrow0\), the integration endpoints satisfy
\[
b_0=t/2+O(t^3),\qquad b_1=\sqrt{t/2}+O(t^{3/2}).
\]
The initial-slice area is \(\pi t/4+o(t)\). In the second slice, replacing \(\sin b\) by \(b\) in the inverse-sine integrand changes the integral by \(o(t)\) (split at a fixed multiple of \(t\), and use \(\sin b=b+O(b^3)\) and integrability of the inverse-square-root endpoint singularity). Substituting \(u=2b/t\) gives
\[
\int_{t/2}^{\sqrt{t/2}}\arcsin\frac{t}{2b}\,db
=\frac{t}{2}\left[1+\log\sqrt{\frac8t}-\frac\pi2\right]+o(t),
\]
using the exact antiderivative \(u\arcsin(1/u)+\operatorname{arcosh}u\). Subtracting \(\int b\,db=t/4+o(t)\), then adding the initial area, leaves
\[
\frac t4\left[\log(8/t)+1\right]+o(t).
\]
Multiplication by the density \(12/\pi^2\) gives the two-term logarithmic expression.

**6. Sharp near-equilateral tail.** Write \(b=\pi/3-x\), \(g=\pi/3+y\). Near the unique maximizer, the ordered chamber becomes \(x\ge0\), \(-x\le y\le x/2\), and
\[
\frac32-2\sin b\sin g=\frac{\sqrt3}{2}(x-y)+O(x^2+y^2).
\]
The set where the leading deficit is below \(\varepsilon\) has area \(\varepsilon^2\): for \(\delta=2\varepsilon/\sqrt3\), integrate in \(x\) the widths \(3x/2\) for \(0<x<\delta/2\) and \(\delta-x/2\) for \(\delta/2<x<2\delta\). Their sum is \(3\delta^2/4=\varepsilon^2\). Standard linear rescaling and the quadratic remainder justify the asymptotic. Multiplying by \(12/\pi^2\) concludes the proof.

## Verification

Run `python verify_inscribed_triangle_width.py` with NumPy, SciPy, and SymPy. This script independently recomputes normalization and both moments symbolically, compares direct Cartesian cross-product altitudes with the gap formula, checks numerical two-dimensional moment integration, and compares the CDF against 450,000 direct uniform-circle samples. It also checks both endpoint expansions by CDF quadrature. The checked mathematical statements rest on the proof, not on finite simulation.

## Relationship to prior work

Koroleva and Nikitin (arXiv:1301.1360, first posted 7 January 2013) study perimeters and areas of polygons inscribed using exactly the same uniform-circle point model, including extreme-value laws. Their explicitly inspected perimeter and area results do not supply the minimum directional thickness law, its moments, or its logarithmically singular small-width tail. Silverman and Brown (1978) study spatial collinearity statistics and Poisson limits rather than the full minimum-width law for a three-point sample on a circle. Daley, Ebert, and Swift (2016) consider random triangles with independent side directions, a materially different sampling law. These distinctions establish non-implication of the present statement from the cited statements; they do not establish exhaustive historical priority.

## Limitations

The theorem does not cover points uniform in a disk, triangles formed by independent line directions, nonuniform arclength sampling, or random point counts greater than three. The cumulative distribution is represented by a one-dimensional definite integral, not claimed to have an elementary antiderivative. Prior-art searches cannot exclude an unindexed earlier calculation; independent review remains outstanding.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (2013), https://arxiv.org/abs/1301.1360.
2. B. W. Silverman and T. C. Brown, *Short distances, flat triangles and Poisson limits*, Journal of Applied Probability **15** (1978), 815–825, https://doi.org/10.2307/3213436.
3. D. J. Daley, S. Ebert and R. J. Swift, *Size distributions in random triangles*, Journal of Applied Probability, online 30 March 2016, https://www.cambridge.org/core/journals/journal-of-applied-probability/article/size-distributions-in-random-triangles/117ED3787DE9B79B1AC3862B0B6C3EAB.
