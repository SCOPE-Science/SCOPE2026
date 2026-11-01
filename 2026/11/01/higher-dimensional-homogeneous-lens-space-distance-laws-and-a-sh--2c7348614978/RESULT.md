# Higher-dimensional homogeneous lens-space distance laws and a sharp diameter-tail transition

## Finding

For integers \(d\ge3\) and \(p\ge2\), let \(M_{d,p}=S^{2d-1}/\langle\omega\rangle\), where the unit round sphere sits in \(\mathbb C^d\) and \(\omega=e^{2\pi i/p}\) multiplies **all** complex coordinates simultaneously. Equip the quotient with the induced Riemannian distance and normalized Riemannian volume. For two independent uniformly distributed points, write \(D_{d,p}\) for their geodesic distance and \(F_{d,p}(t)=\Pr(D_{d,p}\le t)\).

**Exact law.** For \(0<t<\pi/2\),
\[
F_{d,p}(t)=\frac p\pi\int_0^{\min(t,\pi/p)}
\left(1-\frac{\cos^2t}{\cos^2\theta}\right)^{d-1}\,d\theta.
\]
Here \(F_{d,p}(t)=0\) for \(t\le0\) and \(F_{d,p}(t)=1\) for \(t\ge\pi/2\); these expressions determine the volume of every geodesic ball because the space is homogeneous. Specifically,
\[
\operatorname{Vol}(B_t)=\frac{2\pi^d}{p\Gamma(d)}F_{d,p}(t).
\]

**Two strict stochastic orders.** At fixed dimension \(d\), increasing the cyclic order \(p\) strictly increases \(F_{d,p}(t)\) at each \(0<t<\pi/2\). At fixed order \(p\), increasing \(d\) strictly decreases \(F_{d,p}(t)\) there. Thus quotienting by more scalar phases makes distances shorter, while raising the complex dimension makes them longer, in first-order stochastic order.

**Exact near-diameter polynomial and exponent transition.** Set \(a=\pi/p\), \(u=\tan a\), and
\[
J_j(u)=\sum_{k=0}^{j-1}\binom{j-1}{k}\frac{u^{2k+1}}{2k+1}.
\]
For each \(p\ge3\) and \(0<\varepsilon<\pi/2-\pi/p\), the tail probability is the following **finite exact polynomial** in \(\sin^2\varepsilon\):
\[
\Pr\!\left(D_{d,p}>\frac\pi2-\varepsilon\right)
=\frac p\pi\sum_{j=1}^{d-1}(-1)^{j+1}
\binom{d-1}{j}J_j\!\left(\tan\frac\pi p\right)
\sin^{2j}\varepsilon.
\]
In particular,
\[
\Pr\!\left(D_{d,p}>\frac\pi2-\varepsilon\right)
=(d-1)\frac p\pi\tan\frac\pi p\,\varepsilon^2+O_{d,p}(\varepsilon^4)
\quad(p\ge3).
\]
For \(p=2\), the order changes sharply:
\[
\Pr\!\left(D_{d,2}>\frac\pi2-\varepsilon\right)
=\frac{2\Gamma(d)}{\sqrt\pi\Gamma(d-\tfrac12)}\,\varepsilon+o_d(\varepsilon).
\]
Consequently, the diameter-tail exponent is exactly one for the projective quotient \(p=2\), but exactly two for every scalar cyclic quotient of order at least three, in **all odd dimensions at least five**.

As \(p\to\infty\) at fixed \(d\), \(F_{d,p}(t)\to\sin^{2d-2}t\) at every \(t\in[0,\pi/2]\), the distance law associated with the Hopf-base complex projective space with its induced quotient metric.

## Assumptions and scope

The sphere has sectional curvature one and intrinsic great-circle distance; the cyclic group acts freely by simultaneous scalar rotation, not by unequal coordinate weights. The Riemannian quotient is the homogeneous lens space \(L(p;1,\ldots,1)\) of dimension \(2d-1\), with \(d\ge3\). All random points are independent and uniform by normalized Riemannian volume. The diameter is \(\pi/2\) for \(p\ge2\). The interval restrictions on the exact finite tail polynomial are essential; only the leading tail expansions are asserted as \(\varepsilon\downarrow0\).

## Proof

**1. Reduce to one sphere coordinate.** The standard unitary group acts transitively on the quotient and commutes with the scalar cyclic action. A first random point may therefore be placed at the orbit of \(e_1=(1,0,\ldots,0)\). For a uniform random \(V\in S^{2d-1}\), the distance between the two orbits is
\[
D_{d,p}=\min_{0\le k<p}\arccos\bigl(\operatorname{Re}(\omega^k V_1)\bigr)
=\arccos(R\cos\Theta),
\]
where \(R=|V_1|\), and \(\Theta\in[-\pi/p,\pi/p]\) is the signed angular displacement of \(V_1\) from its closest cyclic phase. The possible sign of the inner product convention does not affect the minimum. This establishes the diameter \(\pi/2\), since the maximum possible minimum inner product is nonnegative and points with \(V_1=0\) realize the upper boundary.

**2. Determine the factor distributions.** Normalize \(d\) independent standard complex Gaussian coordinates. Their squared moduli are independent exponentials, so
\[
R^2\sim\operatorname{Beta}(1,d-1),\qquad
\Pr(R^2\ge s)=(1-s)^{d-1}\quad(0\le s\le1).
\]
The argument of \(V_1\) is uniform and independent of \(R\), hence \(\Theta\) is uniform on \([-\pi/p,\pi/p]\) and independent of \(R\).

**3. Compute every distance quantile.** For \(0<t<\pi/2\), the event \(D_{d,p}\le t\) is exactly \(R\cos\Theta\ge\cos t\). It is possible only for \(|\Theta|\le t\). Conditioning on \(\Theta\) and using the beta survival function gives the integral in the Finding. Transitivity and the spherical volume identity \(\operatorname{Vol}(S^{2d-1})=2\pi^d/\Gamma(d)\) establish the ball-volume formula.

**4. Establish both strict stochastic comparisons.** Use a common \(R>0\) and \(U\sim\operatorname{Uniform}(0,1)\). Then \(D_{d,p}\) has the same law as \(\arccos(R\cos(\pi U/p))\). Increasing \(p\) strictly decreases this distance almost surely. It also gives strictly ordered CDFs at all interior thresholds because \(R\) has a positive density on \((0,1)\) and the angular windows are strictly nested on a set of positive measure at each threshold. At fixed \(p\), the beta law may be coupled as \(R_d=\sqrt{1-U_1^{1/(d-1)}}\), where \(U_1\) is a shared uniform random variable. This decreases strictly with \(d\), so \(D_{d,p}\) increases; the same positive-density argument makes the CDF inequality strict for \(0<t<\pi/2\).

**5. Derive the finite polynomial.** For \(p\ge3\) and \(0<\varepsilon<\pi/2-\pi/p\), the distance threshold \(t=\pi/2-\varepsilon\) exceeds \(\pi/p\), so conditioning on the full angle window gives
\[
1-F_{d,p}(t)=\frac p\pi\int_0^{\pi/p}
\left[1-\left(1-\sin^2\varepsilon\sec^2\theta\right)^{d-1}\right]d\theta.
\]
Expand by the finite binomial theorem. Under \(v=\tan\theta\), each coefficient satisfies
\[
\int_0^{\pi/p}\sec^{2j}\theta\,d\theta
=\int_0^{\tan(\pi/p)}(1+v^2)^{j-1}dv
=J_j\!\left(\tan\frac\pi p\right).
\]
This proves the complete polynomial. Its \(j=1\) term is positive and equals the displayed quadratic coefficient, while all remaining terms are \(O(\varepsilon^4)\).

**6. Prove the exceptional linear tail.** At \(p=2\) the angular window touches \(\pm\pi/2\), invalidating the full-window polynomial expansion because \(\sec\theta\) is unbounded. Conditional on \(R=r\), the probability of \(R\cos\Theta<\sin\varepsilon\) is \(1\) for \(r\le\sin\varepsilon\), and is \((2/\pi)\arcsin(\sin\varepsilon/r)\) otherwise. Dominated convergence after division by \(\sin\varepsilon\) applies because \(\mathbb E[R^{-1}]<\infty\) for \(d\ge2\); for example, \(\arcsin x\le(\pi/2)x\) provides a dominating multiple of \(1/R\). The beta integral gives
\[
\mathbb E[R^{-1}]=(d-1)B(\tfrac12,d-1)
=\frac{\sqrt\pi\,\Gamma(d)}{\Gamma(d-\tfrac12)}.
\]
Combining these identities and \(\sin\varepsilon/\varepsilon\to1\) gives the asserted coefficient. This establishes the strict exponent jump.

**7. Identify the large-order limit.** With \(\Theta=\pi U/p\), dominated convergence yields \(R\cos\Theta\to R\). Therefore the limiting CDF is \(\Pr(R\ge\cos t)=\sin^{2d-2}t\), matching the Hopf quotient by the entire circle.

## Verification

Run `python3 lens_check.py` from this directory using Python's standard library. The verifier independently integrates both conditional angular and conditional radial formulas, reconstructs the three-dimensional predecessor formula, checks the exact polynomial by rational polynomial division, checks the endpoint coefficients, verifies stochastic inequalities on finite grids, and simulates direct shortest-orbit distances on sampled unit spheres. Its recorded successful run reported 951 checks. Computation is a finite consistency check; every universal statement above is proved analytically.

## Relationship to prior work

Herman and Pakianathan (2014, arXiv:1407.5607v1) studied the distributions of distances in arbitrary compact homogeneous metric spaces and obtained universal mean-distance inequalities; their full original text does **not** give the dimension-and-order-dependent ball-volume law above. Balch, Peterson, and Shonkwiler (2020, arXiv:2004.13196v1) gave the full distance laws, moments, and geodesic-ball volumes for **three-dimensional** homogeneous lens spaces. Specializing the integral here to \(d=2\) reproduces their explicitly stated CDF, and **no dimension-three result is claimed as new**. The present claim is the dimension-uniform extension for \(d\ge3\), including the exact finite endpoint-tail polynomial and the strict two-parameter stochastic orders. Related isoperimetric research on lens spaces concerns a distinct geometric question rather than an all-radius ball-volume formula. Relevant mathematical search results were checked for the names, beta-coordinate representation, ball volumes, and sharp endpoint exponents; no implication covering the higher-dimensional statements was found in the inspected primary material.

## Limitations

This is not a classification of distance distributions on general (nonhomogeneous or weighted-coordinate) lens spaces. The 2020 results already cover complex dimension two. The originality comparison is bounded by the inspected full texts, targeted literature searches, and accessible research records; no claim of exhaustive historical priority or independent validation is made. In particular an older or differently named formula using Hopf-fibration coordinates remains possible. Normalization to the unit sphere is essential for the displayed constants; uniform metric scaling modifies all radii accordingly.

## References

1. Mark Herman and Jonathan Pakianathan, *On the distribution of distances in homogeneous compact metric spaces*, arXiv:1407.5607v1, first public 2014-07-21, https://arxiv.org/abs/1407.5607.
2. Brenden Balch, Chris Peterson, and Clayton Shonkwiler, *Distributions of Distances and Volumes of Balls in Homogeneous Lens Spaces*, arXiv:2004.13196v1, first public 2020-04-27, https://arxiv.org/abs/2004.13196.
3. Celso Viana, *The isoperimetric problem for lens spaces*, Mathematische Annalen 374 (2019), https://discovery.ucl.ac.uk/id/eprint/10070801/ (background only; not a prior ball-volume theorem).
