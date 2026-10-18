# Boundary-localized max-norm decoupling and absence of strongly extreme Garsia points

## Finding

For every complex \(f\in\mathrm{BMO}(\mathbb T)\), there is a boundary point \(\zeta\) and a family of rational analytic functions \(h_{r\zeta}\in\mathrm{VMOA}_0\) such that \(\|h_{r\zeta}\|_G=1\) and, for each fixed \(t\in\mathbb C\),
\[
\lim_{r\uparrow1}\|f+t h_{r\zeta}\|_G=\max\{\|f\|_G,|t|\}.
\]
Consequently no point of the closed Garsia unit ball of complex \(\mathrm{BMO}/\mathbb C\), \(\mathrm{BMOA}/\mathbb C\), \(\mathrm{VMO}/\mathbb C\), or \(\mathrm{VMOA}/\mathbb C\) is strongly extreme. In particular this conclusion applies to Garsia norm-one points that are ordinary extreme points.

## Assumptions and scope

Write \(\mathbb D\) for the open unit disk, \(\mathbb T\) for its boundary, and \(m\) for normalized arc measure. The Poisson integral \(P g(z)=\int_{\mathbb T}g(\xi)(1-|z|^2)/|\xi-z|^2\,dm(\xi)\) is used for \(g\in L^1(\mathbb T)\). For \(f\in L^2(\mathbb T)\), define
\[
\Phi_f(z)=P(|f|^2)(z)-|Pf(z)|^2,\qquad
\|f\|_G=\sup_{z\in\mathbb D}\sqrt{\Phi_f(z)}.
\]
The function class \(\mathrm{BMO}(\mathbb T)\) consists exactly of those \(L^2\) boundary functions with finite Garsia seminorm; it is a norm after quotienting by constant functions. The analytic subspace is \(\mathrm{BMOA}\), the vanishing-mean-oscillation subspaces are \(\mathrm{VMO}\) and \(\mathrm{VMOA}\); all are considered modulo constants. In analytic spaces, the equivalent normalized representative has value zero at the origin. These are complex Banach spaces with this exact norm.

A point \(x\) of the closed unit ball of a Banach space is *strongly extreme* if whenever \(\|x+y_n\|\to1\) and \(\|x-y_n\|\to1\), then necessarily \(\|y_n\|\to0\). Equivalently, for every \(\varepsilon>0\), some \(\delta>0\) makes \(\|x\pm y\|<1+\delta\) imply \(\|y\|<\varepsilon\).

Fix any common Lebesgue point \(\zeta\in\mathbb T\) of \(f\) and \(|f|^2\) (such points form a set of full measure). For \(a=r\zeta\), \(0<r<1\), put
\[
b_a(z)=\frac{a-z}{1-\overline a z},\qquad
h_a(z)=b_a(z)-b_a(0)=b_a(z)-a.
\]
The parameter \(r\) tends to \(1\) from below; \(t\in\mathbb C\) is fixed. Neither a uniform estimate over unbounded \(t\) nor convergence in Garsia norm of \(h_a\) is asserted.

## Proof

**1. A moving unit-norm analytic perturbation.** Each \(b_a\) is a finite Blaschke factor with boundary modulus one. Since \(b_a\) is analytic across \(\overline{\mathbb D}\) for \(|a|<1\), the function \(h_a\) lies in \(\mathrm{VMOA}_0\). Constants do not affect the variance. For every \(z\in\mathbb D\),
\[
\Phi_{h_a}(z)=P(|b_a|^2)(z)-|b_a(z)|^2
=1-|b_a(z)|^2
=1-\rho(a,z)^2,
\]
where \(\rho(a,z)=|(a-z)/(1-\overline a z)|\) is pseudohyperbolic distance. At \(z=a\) the variance is exactly \(1\); elsewhere it is at most \(1\). Thus \(\|h_a\|_G=1\).

**2. Localization of the background variance.** At a common Lebesgue point \(\zeta\) of \(f\) and \(|f|^2\), their Poisson integrals converge to the respective boundary values in every fixed Stolz cone. Hence \(\Phi_f(z)\to0\) uniformly as \(z\to\zeta\) through any one such cone. Fix \(0<s<1\) and define \(E_{a,s}=\{z\in\mathbb D:\rho(a,z)\le s\}\). As \(a=r\zeta\to\zeta\), this pseudohyperbolic disk lies in a Stolz cone whose aperture depends only on \(s\), and all its points converge uniformly to \(\zeta\). In particular,
\[
\sup_{z\in E_{r\zeta,s}}\sqrt{\Phi_f(z)}\longrightarrow0.
\]
One way to check the cone claim is to use the disk automorphism identity
\(1-\rho(a,z)^2=(1-|a|^2)(1-|z|^2)/|1-\overline a z|^2\), together with \(\rho(a,z)\le s\): the Euclidean center and radius of \(E_{a,s}\) are \((1-s^2)a/(1-s^2|a|^2)\) and \(s(1-|a|^2)/(1-s^2|a|^2)\). Both are within \(O_s(1-r)\) of \(\zeta\), while \(1-|z|\) is bounded below by a positive multiple of \(1-r\) uniformly on that disk.

**3. The upper limit.** The square root of a Poisson variance is the norm of the centered boundary function in the Hilbert space \(L^2(\mathbb T,P_z\,dm)\). Its triangle inequality gives
\[
\sqrt{\Phi_{f+t h_a}(z)}\le\sqrt{\Phi_f(z)}+|t|\sqrt{\Phi_{h_a}(z)}.
\]
On \(E_{a,s}\), the right side has supremum at most \(|t|+o_s(1)\). Outside \(E_{a,s}\) the inequality \(\sqrt{\Phi_{h_a}(z)}\le\sqrt{1-s^2}\) gives the bound \(\|f\|_G+|t|\sqrt{1-s^2}\). Taking the supremum, then the limit superior as \(r\uparrow1\), yields
\[
\limsup_{r\uparrow1}\|f+t h_{r\zeta}\|_G
\le\max\bigl\{|t|,\,\|f\|_G+|t|\sqrt{1-s^2}\bigr\}.
\]
Finally let \(s\uparrow1\) to obtain the bound \(\max\{\|f\|_G,|t|\}\).

**4. Both lower limits.** For each fixed interior point \(z\), the identity in Step 1 implies \(\Phi_{h_{r\zeta}}(z)\to0\). The reverse triangle inequality for centered Poisson \(L^2\) vectors gives \(\sqrt{\Phi_{f+t h_{r\zeta}}(z)}\to\sqrt{\Phi_f(z)}\). Taking the supremum over fixed \(z\) yields
\(\liminf_{r\uparrow1}\|f+t h_{r\zeta}\|_G\ge\|f\|_G\).
At the moving point \(z=a=r\zeta\), the reverse triangle inequality and Step 1 give
\[
\sqrt{\Phi_{f+t h_a}(a)}\ge |t|-\sqrt{\Phi_f(a)}\longrightarrow |t|.
\]
Combining the two lower bounds with Step 3 proves the exact max-norm limit.

**5. Strong extremity.** Let \(x\) be any Garsia unit vector in one of the four spaces, represented by \(f\) with \(\|f\|_G=1\). The perturbations \(y_r=h_{r\zeta}\) belong to every one of these spaces, have norm one, and obey
\(\|x+y_r\|_G\to1\), \(\|x-y_r\|_G\to1\).
This contradicts strong extremity. A point of norm strictly less than one is not even ordinary extreme, since a nonzero sufficiently small vector may be added and subtracted while remaining in the ball. Thus the entire closed unit ball has no strongly extreme points.

## Verification

The proof relies on exact finite-Blaschke variance, the standard non-tangential convergence of Poisson integrals at simultaneous Lebesgue points, elementary pseudohyperbolic disk geometry, and Hilbert-space Minkowski/reverse triangle inequalities. All extrema are suprema over the full open disk; no mesh approximation or finite experiment is used to establish the theorem.

For a direct check, set \(f(z)=z\), \(\zeta=1\) and \(a=r\). In this case \(\Phi_f(z)=1-|z|^2\) and
\[
\Phi_{h_r}(z)=\frac{(1-r^2)(1-|z|^2)}{|1-rz|^2},\qquad
\operatorname{Cov}_{P_z}(f,h_r)=-\frac{(1-r^2)(1-|z|^2)}{1-r\overline z}.
\]
The exact pointwise formula \(\Phi_{f\pm h_r}=\Phi_f+\Phi_{h_r}\pm2\operatorname{Re}\operatorname{Cov}_{P_z}(f,h_r)\) provides a symbolic and numerical spot check. It is not a substitute for the global proof above.

## Relationship to prior work

Dyakonov's 2026 preprint [1, Problem 2 and closing paragraph of Section 2] proposes investigating strongly extreme points of precisely the Garsia unit balls of BMO and BMOA, while focusing its explicit results on the distinct Hankel-operator kernel thesis. The present statement gives an empty classification and, more strongly, a quantified max-norm decoupling mechanism with perturbations from the small analytic disk algebra. Dyakonov's 2024/2025 paper [2] proves that Garsia norm-attaining unit vectors are *ordinary* extreme points and that every unit VMO vector is ordinary extreme; ordinary and strong extremity are different properties, so these earlier theorems do not imply the present result. Classical strong-extreme results for inner functions in \(H^\infty\) use its supremum norm, not the Garsia norm [3]. The usual arc-oscillation BMO norms need not have identical unit-ball geometry; no replacement of the exact Garsia norm occurs here.

## Limitations

The theorem applies to the complex spaces over the unit circle and to the exact Poisson-variance Garsia norm modulo constants. It does not classify ordinary extreme points, does not address equivalent alternative BMO norms, and makes no claim about stronger metric properties beyond failure of strong extremity. The maximum law holds for each fixed \(f,t\) and chosen common Lebesgue point, not uniformly over arbitrary bounded families of boundary functions or growing \(t\). An unindexed prior result on strongly extreme Garsia points would affect priority, not the proved implication.

## References

[1] K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242v1 (first public version 2026-09-27), https://arxiv.org/html/2609.33242v1. Section 2 defines the Garsia unit balls and proposes the strongly extreme point question.

[2] K. M. Dyakonov, *Extremal Problems in BMO and VMO Involving the Garsia Norm*, arXiv:2404.05565v2 (2024), https://arxiv.org/abs/2404.05565. Theorem 2.7 and Corollary 2.8 concern ordinary extreme points and VMO, respectively.

[3] K. M. Dyakonov, *Inner Functions as Strongly Extreme Points: Stability Properties*, arXiv:2301.11162 (2023), https://arxiv.org/abs/2301.11162. This concerns the supremum norm on constrained Hardy spaces.
