# Universal power-tilt duality for affine sections of prolate and oblate spheroids

## Finding

Fix an integer \(d\ge3\) and an aspect ratio \(\kappa>1\). Define the prolate and oblate spheroids
\[
P_\kappa=\{x\in\mathbb R^d:\sum_{j=1}^{d-1}x_j^2+x_d^2/\kappa^2\le1\},\qquad
O_\kappa=\{x\in\mathbb R^d:\sum_{j=1}^{d-1}x_j^2+\kappa^2x_d^2\le1\}.
\]
Choose an affine hyperplane by Euclidean-motion-invariant hyperplane measure conditioned to intersect the respective body; let \(R_p\) and \(R_o\) be the ratios of longest to shortest semiaxis of the resulting \((d-1)\)-dimensional ellipsoidal sections. These are shape ratios, not section radii. Put \(b=\kappa^2-1\), \(a=(d-3)/2\), and
\[
J_p=\int_0^1\sqrt{1+bu^2}(1-u^2)^a\,du,\qquad
J_o=\frac1\kappa\int_0^1\sqrt{\kappa^2-bu^2}(1-u^2)^a\,du.
\]
For \(1<r<\kappa\), the exact densities are
\[
f_p(r)=\frac{\kappa^d(r^2-1)^a}{b^{(d-2)/2}J_p\,r^d\sqrt{\kappa^2-r^2}},\qquad
f_o(r)=\frac{r^2(r^2-1)^a}{\kappa b^{(d-2)/2}J_o\sqrt{\kappa^2-r^2}}.
\]
In particular, the oblate law is the **exact \((d+2)\)-power tilt** of the prolate law:
\[
\boxed{\quad \frac{f_o(r)}{f_p(r)}=\frac{r^{d+2}}{\mathbb E_p[R_p^{d+2}]},\qquad
\mathbb E_p[R_p^{d+2}]=\kappa^{d+1}\frac{J_o}{J_p}.\quad}
\]
For every bounded measurable function \(\varphi\),
\[
\mathbb E_o[\varphi(R_o)]
=\frac{\mathbb E_p[R_p^{d+2}\varphi(R_p)]}{\mathbb E_p[R_p^{d+2}]}.
\]
The likelihood ratio is strictly increasing, so the oblate shape ratio **strictly stochastically dominates** the prolate shape ratio: \(\Pr(R_o>r)>\Pr(R_p>r)\) for every \(1<r<\kappa\). The unique equal-prior optimal likelihood-ratio rule based on section shape is to classify as oblate exactly when
\[
R>r_*=\left(\kappa^{d+1}J_o/J_p\right)^{1/(d+2)}.
\]
Writing \(S_o(r)=\Pr(R_o>r)\) and \(S_p(r)=\Pr(R_p>r)\), the exact total-variation distance is \(S_o(r_*)-S_p(r_*)\), and the minimum equal-prior classification error is half of one minus that distance.

For fixed \(\kappa>1\) and \(d\to\infty\), with \(Z\) a standard real Gaussian,
\[
d(\kappa-R_p)\ \Longrightarrow\ \frac{\kappa(\kappa^2-1)}2Z^2,
\qquad
d(\kappa-R_o)\ \Longrightarrow\ \frac{\kappa^2-1}{2\kappa}Z^2.
\]
Moreover the shape-based statistical separation has a **strictly positive sharp limit**:
\[
\boxed{\quad\lim_{d\to\infty}\operatorname{TV}(R_p,R_o)
=\operatorname{erf}\left(\sqrt{\frac{\kappa^2\log\kappa}{\kappa^2-1}}\right)
-\operatorname{erf}\left(\sqrt{\frac{\log\kappa}{\kappa^2-1}}\right)>0.\quad}
\]
Thus the two unscaled ratios both converge to \(\kappa\), yet retain nonvanishing optimal discrimination information at their dimension-dependent fluctuation scale.

## Assumptions and scope

Use unoriented affine hyperplanes \(H(n,t)=\{x:n\cdot x=t\}\), with \(n\) Haar-uniform on the unit sphere modulo sign and \(t\) Lebesgue-uniform under the invariant measure. Conditioning on an intersection with a convex body makes the normal density proportional to directional width. Under a fixed orientation \(n\), the permitted offsets form the interval \((-h(n),h(n))\), where \(h(n)\) is its support function. Tangent or singular sections occur with probability zero. The section shape ratio is independent of the permitted offset. No uniform-orientation-only convention is substituted for the conditioned invariant-hyperplane law.

The statements hold exactly for all finite integers \(d\ge3\) and every real \(\kappa>1\). Dimension two is excluded because a hyperplane section has only one intrinsic semiaxis and its shape ratio is always one. The limiting statements fix \(\kappa\) while \(d\) tends to infinity; they do not assert uniformity when \(\kappa\) varies with dimension.

## Proof

**Offset elimination and eigenvalues.** Let \(Q\) be the positive-definite quadratic-form matrix of an ellipsoid. Its affine hyperplane section is centered at
\[
x_0=\frac{tQ^{-1}n}{n^{\mathsf T}Q^{-1}n}.
\]
Writing \(h(n)^2=n^{\mathsf T}Q^{-1}n\), any point of the section has the form \(x_0+y\) with \(y\perp n\), and the defining inequality becomes
\[
y^{\mathsf T}Qy\le1-\frac{t^2}{h(n)^2}.
\]
The scalar on the right multiplies all squared section semiaxes equally and therefore cancels from their ratio.

Let \(u=|n_d|\). A unit vector in \(n^\perp\) within the plane spanned by the symmetry axis and \(n\) has squared symmetry-axis coordinate \(1-u^2\). The remaining \(d-2\) orthogonal vectors lie in the equatorial subspace. Consequently, restriction of \(Q_p=\operatorname{diag}(1,\ldots,1,\kappa^{-2})\) to \(n^\perp\) has eigenvalues \(1\), repeated \(d-2\) times, and \(\kappa^{-2}(1+bu^2)\) once. The oblate restriction has eigenvalues \(1\), repeated \(d-2\) times, and \(\kappa^2-bu^2\) once. Thus
\[
R_p(u)=\frac{\kappa}{\sqrt{1+bu^2}},\qquad
R_o(u)=\sqrt{\kappa^2-bu^2}.
\]
The support functions are respectively
\[
h_p(u)=\sqrt{1+bu^2},\qquad h_o(u)=\frac1\kappa\sqrt{\kappa^2-bu^2}.
\]

**Conditioned invariant-hyperplane law and the exact densities.** The absolute last coordinate of a Haar-uniform unit normal in \(\mathbb R^d\) has density proportional to \((1-u^2)^{(d-3)/2}\) on \([0,1]\). Integrating Lebesgue offsets over the intersection interval of length \(2h_i(u)\) reweights by \(h_i(u)\). Hence the two normalized densities of \(u\) are exactly \(h_p(u)(1-u^2)^a/J_p\) and \(h_o(u)(1-u^2)^a/J_o\).

Both shape maps are strictly decreasing and map \([0,1]\) onto \([\kappa,1]\). Their inverse functions are
\[
u_p(r)=\sqrt{\frac{\kappa^2-r^2}{br^2}},\qquad
u_o(r)=\sqrt{\frac{\kappa^2-r^2}{b}}.
\]
Changing variables using the corresponding Jacobians yields the two displayed densities. Dividing them cancels the shared \((r^2-1)^a/\sqrt{\kappa^2-r^2}\) factors and gives
\[
\frac{f_o(r)}{f_p(r)}=\frac{J_p}{\kappa^{d+1}J_o}r^{d+2}.
\]
Since both densities integrate to one, the normalizing constant equals the inverse prolate \((d+2)\)-moment. This proves the power-tilt identity.

**Stochastic ordering and the optimal test.** The likelihood ratio \(f_o/f_p\) increases strictly from one endpoint to the other and has expectation one under the prolate law; therefore it crosses one at exactly one interior point \(r_*\). On each side of the crossing the sign of \(f_o-f_p\) is fixed, proving strict stochastic dominance. The total variation is the integral of the positive difference over \((r_*,\kappa)\), which is exactly \(S_o(r_*)-S_p(r_*)\). Neyman–Pearson classification under equal priors and zero-one loss gives the asserted unique threshold rule up to a null set.

For numerical evaluation without differentiating singular endpoint densities, the survival functions are the nonsingular orientation quadratures
\[
S_p(r)=\frac1{J_p}\int_0^{\nu_p(r)}\sqrt{1+bu^2}(1-u^2)^a\,du,\quad
S_o(r)=\frac1{\kappa J_o}\int_0^{\nu_o(r)}\sqrt{\kappa^2-bu^2}(1-u^2)^a\,du.
\]

**High-dimensional limit and its sharp discriminability.** For a Haar-uniform normal, \(\sqrt d\,n_d\Rightarrow Z\). The two width weights are uniformly bounded and converge to one near \(u=0\), where the normal mass concentrates; thus the same Gaussian limit holds after either width reweighting. The Taylor expansions
\[
R_p(u)=\kappa-\frac{\kappa b}{2}u^2+O_\kappa(u^4),\qquad
R_o(u)=\kappa-\frac{b}{2\kappa}u^2+O_\kappa(u^4)
\]
prove the two scaled \(\chi^2_1\) limits. Dominated convergence and concentration yield \(J_p/J_o\to1\). Writing \(r=\kappa-y/d\) gives
\[
\log\frac{f_o(r)}{f_p(r)}=\log(J_p/J_o)-(d+1)\log\kappa+(d+2)\log r
\longrightarrow\log\kappa-y/\kappa.
\]
The crossing is therefore at \(d(\kappa-r_*)\to\kappa\log\kappa\). The limiting total variation, evaluated using the two scaled \(\chi^2_1\) survival probabilities at that threshold, equals the displayed difference of error functions. Its two arguments are strictly ordered for every \(\kappa>1\), proving positivity. Convergence of the crossing and the two scaled distributions with continuous CDFs justifies passage to total variation; no separate claim of density convergence is needed.

## Verification

The standalone file `verify.py` computes the densities by two independent Jacobian expressions across several dimensions, checks the exact likelihood-ratio normalization and strict ordering, numerically compares three-dimensional ellipsoid quadratic-form sections against IUR samples, and compares finite-dimensional total-variation integrals to the sharp limiting expression. Execute with `python3 verify.py`; its successful final line is `ALL_CHECKS_PASSED`. These finite numerical checks supplement, but cannot establish, the all-dimensional analytic theorem.

## Relationship to prior work

Van der Jagt, Jongbloed, and Vittorietti (2023) define the invariant-uniform-random hyperplane convention and examine existence and numerical approximation of cross-section **area** distributions. Their IUR measure explains the essential normal-direction support-function weight here, but their inspected article does not assert the paired prolate–oblate **semiaxis ratio** power-tilt identity or its high-dimensional discrimination limit.

Baaske, Ballani, and Illgen (2016 preprint, 2018 publication) develop stereological planar-section profiles for distributions of spheroids under a vertical-section sampling convention. Their general unfolding relation is relevant to the three-dimensional setting, but the inspected formulas do not assert this paired \((d+2)\)-power tilt under IUR affine hyperplanes or the dimension-asymptotic total-variation constant. The earlier Cruz-Orive spheroid-stereology formulas remain a plausible route to a special-dimensional equivalent and are credited as background, not ruled out.

The previously published exact one-spike ellipsoid random-radius law concerns **central Haar subspaces** and the maximal *radius* of the resulting section. It does not provide the IUR affine-hyperplane section shape ratio, the comparison with oblate spheroids, or the likelihood-ratio duality. Classical studies by Jensen and Møller and by Møller on ellipsoid stereology are plausible prior sources; available summaries do not resolve whether they imply part of the present assertion. This constitutes a historical-priority risk rather than evidence of absence.

## Limitations

The exact duality depends on axial symmetry and the matched reciprocal semiaxis conventions for prolate and oblate bodies. It does not establish a related law for triaxial ellipsoids, arbitrary convex bodies, central-only sampling, or a prescribed nonuniform offset law. The shape ratio alone need not be a sufficient statistic for distinguishing the two *full observed sections*, which may contain orientation, scale, or offset information; optimality is asserted only among classifiers using the intrinsic ratio. The full historical literature on spheroid shape stereology has not been exhaustively accessible. No independent mathematical audit is claimed.

## References

1. T. van der Jagt, G. Jongbloed, and M. Vittorietti, *Existence and approximation of densities of chord length- and cross section area distributions*, arXiv:2305.02864v1 (first posted 4 May 2023); *Image Analysis & Stereology* 42 (2023), 171–184. DOI: 10.5566/ias.2923.
2. M. Baaske, F. Ballani, and A. Illgen, *On the estimation of parameters of a spheroid distribution from planar sections*, arXiv:1609.06697 (2016 preprint; published 2018).
3. J. Cruz-Orive, classical spheroid stereology and size-shape distribution studies (1976), as cited in Baaske, Ballani, and Illgen.
4. *Exact random-radius law for one-spike ellipsoids in every codimension*, publicly indexed mathematical research record (2026), identifier `2026/10/11/SCOPE-exact-random-radius-law-for-one-spike-ellipsoids-in-every-codime--e99f37d3b7ae`.
5. E. B. Jensen and J. Møller, *Stereological versions of integral geometric formulae for n-dimensional ellipsoids*, *Journal of Applied Probability* 23 (1986), 1031–1037. DOI: 10.2307/3214477.
6. J. Møller, *Stereological analysis of particles of varying ellipsoidal shape* (1988).
