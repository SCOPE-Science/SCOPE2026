# Marked Wendel law and convex-order optimal sampling for random inscribed polygons

## Finding

Let \(\Gamma\) be a strictly convex, centrally symmetric, \(C^2\) closed plane curve enclosing the origin, expressed in polar coordinates as \(x(\theta)=r(\theta)(\cos\theta,\sin\theta)\), where \(r>0\) is \(C^2\) and \(\pi\)-periodic. Let \(f>0\) be a \(C^1\), \(\pi\)-periodic angular probability density, with \(\int_0^{2\pi}f(\theta)\,d\theta=1\). For each integer \(n\ge3\), sample \(\Theta_1,\ldots,\Theta_n\) independently from \(f\), let \(K_n=\operatorname{conv}\{x(\Theta_1),\ldots,x(\Theta_n)\}\), and put \(D_n=\operatorname{dist}(0,K_n)\). Write \(M_n=\{D_n>0\}\).

The probability of a miss is the classical Wendel value \(\Pr(M_n)=n/2^{n-1}\). More precisely, conditional on \(M_n\), mark the uniquely defined initial angle \(T_n\) of the open semicircle that contains all sampled points. Then \(T_n\) has density \(f\) *exactly for every* \(n\), and

\[
(T_n,nD_n)\ \Longrightarrow\ \left(T,\frac{r(T)}{4f(T)}E\right),
\]

where \(T\) has density \(f\) on \([0,2\pi)\) and \(E\) is an independent unit-rate exponential variable. Consequently, for every \(z\ge0\),

\[
\lim_{n\to\infty}\Pr(nD_n>z\mid M_n)
=\int_0^{2\pi}f(\theta)\exp\left(-\frac{4f(\theta)z}{r(\theta)}\right)\,d\theta.
\]

Every fixed positive moment converges. In particular,

\[
\lim_{n\to\infty}n\,\mathbb E[D_n\mid M_n]
=\frac14\int_0^{2\pi}r(\theta)\,d\theta,
\qquad
\lim_{n\to\infty}n^2\,\mathbb E[D_n^2\mid M_n]
=\frac18\int_0^{2\pi}\frac{r(\theta)^2}{f(\theta)}\,d\theta.
\]

The first limit is **independent of the angular sampling density**. Put \(Z=\int_0^{2\pi}r(\theta)\,d\theta\). Among all strictly positive symmetric angular densities, the unique density minimizing the limiting conditional distribution in **convex order** is

\[
f_*(\theta)=\frac{r(\theta)}{Z}.
\]

It gives a pure exponential limit with mean \(Z/4\); every other admissible density gives a (nontrivial) exponential scale mixture of that same mean and has strictly larger limiting variance. In particular, the minimum limiting conditional second moment is \(Z^2/8\).

For the unit circle with uniform sampling, an exact finite-sample calibration is

\[
\Pr(D_n>t)=n\left(\frac{\arccos t}{\pi}\right)^{n-1}
\quad (0\le t\le1),
\]

and \(nD_n\mid M_n\) tends to an exponential variable of rate \(2/\pi\). This circle formula is included as a check, not asserted to be historically new.

## Assumptions and scope

The distance is Euclidean and \(D_n=0\) whenever the center belongs to the random hull. Angles denote radial, not necessarily eccentric-anomaly, coordinates. Central symmetry is imposed both on the curve and on the sampling law. The strict convexity hypothesis makes the segment connecting the two extreme sample points of any arc a hull edge. All conditional laws are defined because \(\Pr(M_n)>0\). The convergence statements keep the curve and density fixed as \(n\to\infty\).

## Proof

**1. Unique semicircle anchor and exact marking law.** Except on a probability-zero event, the origin lies outside the hull exactly when a circular angular gap exceeds \(\pi\), equivalently when all sample points lie in an open angular semicircle. Two such gaps cannot coexist. Its complementary occupied semicircle has a unique initial sampled angle \(T_n\). For a candidate initial angle in \(d\theta\), there are \(n\) choices of its sample index, density \(f(\theta)d\theta\), and probability \((1/2)^{n-1}\) that all remaining angles lie counterclockwise in \((\theta,\theta+\pi)\). The last equality uses \(f(\theta+\pi)=f(\theta)\). Integration gives both the exact Wendel probability and the conditional density \(f\) of \(T_n\).

**2. Exact angular endpoint law.** Conditional on \(T_n=\theta\) and \(M_n\), all other \(n-1\) angles are independent with normalized density \(2f\) on \((\theta,\theta+\pi)\). Denote their largest angle by \(\theta+\pi-\delta_n\), where \(0<\delta_n<\pi\). For \(0\le s\le\pi\),

\[
\Pr(\delta_n>s\mid T_n=\theta,M_n)
=\left(1-2\int_{\theta-s}^{\theta}f(u)\,du\right)^{n-1}.
\]

The periodic extension of \(f\) is understood. Since \(f\) is positive and continuous, \(n\delta_n\) converges conditionally to \(\operatorname{Exp}(2f(\theta))\). This convergence is uniform in the anchor angle for each fixed survival threshold.

**3. The Euclidean miss depth.** The closing chord of the random hull has endpoints \(x(\theta)\) and \(x(\theta+\pi-\delta_n)=-x(\theta-\delta_n)\). It separates the center from every other sampled point. For sufficiently small \(\delta\), uniformly in \(\theta\), the orthogonal projection of the origin onto the chord's line lies in its relative interior (the limiting segment is the diameter from \(x(\theta)\) to \(-x(\theta)\)). Thus on that event the hull distance equals the line distance

\[
h(\theta,\delta)
=\frac{|\det(x(\theta),x(\theta-\delta))|}
{|x(\theta)+x(\theta-\delta)|}
=\frac{r(\theta)}2\delta+O(\delta^2),
\]

uniformly in \(\theta\). The last equality follows from \(\det(x(\theta),x'(\theta))=r(\theta)^2\) and \(|x(\theta)|=r(\theta)\). As \(\delta_n\to0\) conditionally in probability, these relations yield the marked exponential-mixture limit and its stated survival function.

**4. Convergence of all fixed positive moments.** For any \(\delta\), the midpoint of the closing edge belongs to the hull, so

\[
D_n\le\tfrac12|x(\theta)-x(\theta-\delta_n)|
\le\tfrac12\|x'\|_\infty\delta_n.
\]

Writing \(c=\min f>0\), the exact endpoint law implies \(\Pr(\delta_n>s\mid T_n=\theta,M_n)\le\exp(-2c(n-1)s)\). Hence \(nD_n\) has uniformly bounded moments of every fixed order conditional on \(M_n\), including uniform integrability of the corresponding powers. The convergence of moments therefore follows from the marked limit. Conditional on \(T=\theta\), the limiting variable has mean \(r(\theta)/(4f(\theta))\) and \(k\)-th moment \(k![r(\theta)/(4f(\theta))]^k\), giving the displayed formulas upon integrating against \(f\).

**5. Sharp sampling optimization.** For an independent \(E\sim\operatorname{Exp}(1)\), put \(m(\theta)=r(\theta)/(4f(\theta))\) and \(\mu=\int f(\theta)m(\theta)d\theta=Z/4\). For any convex test function \(\Psi\) with finite expectations, conditioning on \(E\) and applying Jensen yields

\[
\mathbb E[\Psi(m(T)E)]\ge\mathbb E[\Psi(\mu E)].
\]

Equality for the strictly convex test \(\Psi(z)=z^2\) requires \(m\) to be constant almost everywhere, which, after normalizing the density, is equivalent to \(f=f_*\). This proves both convex-order minimality and uniqueness. Alternatively, Cauchy–Schwarz gives \(\int r^2/f\ge(\int r)^2\), with exactly the same equality criterion.

**6. Circle check.** With a uniform circle sample, the normalized circular gaps are Dirichlet with all parameters one. For a threshold \(t\in[0,1]\), the event \(D_n>t\) is exactly that one circular gap exceeds \(2\pi-2\arccos t\). The gaps are mutually exclusive above \(\pi\), and each gap has \(\operatorname{Beta}(1,n-1)\) marginal distribution, giving the stated exact formula.

## Verification

Run `python check_marked_wendel.py` with NumPy and SciPy. The checker independently reconstructs convex-hull edge distances and evaluates them on conditionally sampled configurations, compares the exact circle probability law with unconditional simulations, checks the limiting first and second moments and tail mixtures for circular and elliptic examples, and verifies the strict second-moment decrease under the optimal angular density. The finite simulations and quadratures corroborate but cannot certify the infinite-sample statements; their proof is above.

## Relationship to prior work

Wendel (1962) establishes the exact center-exclusion probability for symmetric random points; this paper retains that known probability and instead resolves the **marked distance given exclusion**, its conditional limiting law, and the optimizing density. Liu and Yang (2014, Theorem 3.1) derive a nonzero-distance event for points sampled **uniformly inside a disk**, not on a smooth symmetric boundary under an arbitrary angular density; their formula does not determine the mixed-exponential limit or density-invariant mean here. Tikhomirov (2023) extends center-containment probabilities to certain discrete coordinate distributions rather than conditional Euclidean clearance. Standard Hausdorff-error results for random inscribed polygons concern typical, rather than exponentially rare, center-exclusion events. The results here are not claimed to settle the historical priority of every related conditional-distance question.

## Limitations

The theorem is planar and requires strict convexity, \(C^2\) regularity and positive, symmetric angular sampling density. It is not asserted for polygons with corners, nonsymmetric curves, interior sampling, or dimensions greater than two. The exact circle tail is a calibration rather than the new contribution. The remaining historical-priority risk is literature using different terms for center-clearance margins; independent mathematical validation has not been performed.

## References

1. J. G. Wendel, “A Problem in Geometric Probability,” *Mathematica Scandinavica* **11** (1962), 109–112, DOI: 10.7146/math.scand.a-10655. Publicly dated 1962-06-01. Full text: https://journals.msp.org/mscand/article/download/2688/2687/2719.
2. Z. Liu and X. Yang, “Probabilities of hitting a convex hull,” *Comptes Rendus Mathématique* **352** (2014), 935–940, DOI: 10.1016/j.crma.2014.08.015. Full text: https://www.numdam.org/item/CRMATH_2014__352_11_935_0.pdf.
3. K. Tikhomirov, “On the probability that the convex hull of random points contains the origin,” arXiv:2304.13133 (first posted 2023-04-25), https://arxiv.org/html/2304.13133v5.
4. I. Bárány, D. Hug, M. Reitzner and R. Schneider, “Random points in halfspheres,” arXiv:1505.04672 (2015), https://arxiv.org/abs/1505.04672 (different random spherical-cap model).
