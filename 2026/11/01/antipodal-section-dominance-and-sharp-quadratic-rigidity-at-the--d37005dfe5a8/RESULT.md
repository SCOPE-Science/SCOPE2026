# Antipodal section dominance and sharp quadratic rigidity at the critical ellipsoid radius

## Finding
For each integer \(d\ge2\), the Euclidean ball of radius \(\sqrt d\) is the unique equal-volume ellipsoid whose pair of sections by opposite supporting hyperplanes of the unit ball is **pointwise optimal** among ellipsoids containing the unit ball. More precisely, let
\[
E(c,A)=\{c+A^{1/2}z:\|z\|_2\le1\}\subset\mathbb R^d,
\quad A=A^T>0,\quad \det A=d^d,
\quad B_2^d\subset\operatorname{int}E(c,A).
\]
For every unit vector \(u\), write \(S_E(u)=\operatorname{vol}_{d-1}(E\cap\{x:u\cdot x=1\})\). Then
\[
\sqrt{S_E(u)S_E(-u)}\le
\kappa_{d-1}(d-1)^{(d-1)/2},
\quad \kappa_j=\frac{\pi^{j/2}}{\Gamma(j/2+1)}.
\]
Equality in a given direction holds precisely when \(u\cdot c=0\) and \(u^TAu=d\). Equality for all directions, or equality of the spherical geometric mean, holds precisely for \(E=\sqrt d B_2^d\).

The reference radius is itself rigid: for every \(\lambda>1\) different from \(d\), there are centered, equal-volume ellipsoids arbitrarily close to \(\sqrt\lambda B_2^d\), still strictly containing \(B_2^d\), and a normal \(u\) for which their antipodal section geometric mean is **strictly larger** than that of \(\sqrt\lambda B_2^d\).

The inequality has an exact local quadratic stability law. Let \(H\) be any real symmetric trace-zero \(d\times d\) matrix, \(b\in\mathbb R^d\), and for sufficiently small real \(\varepsilon\) put
\[
A_\varepsilon=d\exp(\varepsilon H),\qquad c_\varepsilon=\varepsilon b.
\]
With \(\sigma\) normalized spherical surface measure, and \(S_\varepsilon=S_{E(c_\varepsilon,A_\varepsilon)}\), one has the uniform pointwise expansion
\[
\log\frac{\sqrt{S_\varepsilon(u)S_\varepsilon(-u)}}{\kappa_{d-1}(d-1)^{(d-1)/2}}
=-\varepsilon^2\left[
\frac{d}{4(d-1)}(u^THu)^2+
\frac{d+1}{2(d-1)}(u\cdot b)^2
\right]+O_{d,H,b}(\varepsilon^3),
\]
and hence the sharp integrated Hessian
\[
\int_{S^{d-1}}\log\frac{\sqrt{S_\varepsilon(u)S_\varepsilon(-u)}}{\kappa_{d-1}(d-1)^{(d-1)/2}}\,d\sigma(u)
=-\varepsilon^2\left[
\frac{\operatorname{tr}(H^2)}{2(d-1)(d+2)}+
\frac{d+1}{2d(d-1)}\|b\|_2^2
\right]+O_{d,H,b}(\varepsilon^3).
\]
The quadratic form is positive definite on all volume-preserving ellipsoid deformations modulo the trivial zero perturbation.

## Assumptions and scope
The sections use the two hyperplanes \(\{x:u\cdot x=\pm1\}\), tangent to the **inner unit ball**, not tangent to the variable ellipsoid. A general affine ellipsoid is specified by its center \(c\) and positive-definite squared-semiaxis matrix \(A\). The normalization \(\det A=d^d\) is equivalent to \(\operatorname{vol}_d(E)=\kappa_d d^{d/2}\). Strict containment ensures both sectional volumes are positive and the logarithms well defined. The local expansions hold for fixed \(d,H,b\), uniformly in unit \(u\) as \(\varepsilon\to0\).

## Proof
Put \(q=u^TAu\), \(t=u\cdot c\), and \(a=(d-1)/2\). The affine slice Jacobian gives, for either sign,
\[
S_E(\pm u)=\kappa_{d-1}\frac{\sqrt{\det A}}{q^{d/2}}
\bigl(q-(1\mp t)^2\bigr)^a.
\]
Because the inner unit ball lies strictly in \(E\), the two factors are positive. Their product before taking powers satisfies
\[
(q-(1-t)^2)(q-(1+t)^2)=(q-1-t^2)^2-4t^2\le(q-1)^2.
\]
Here \(q-(1+|t|)^2>0\) implies \(q-1-t^2>0\), so the inequality is strict unless \(t=0\). Therefore
\[
\sqrt{S_E(u)S_E(-u)}\le\kappa_{d-1}d^{d/2}\,
\frac{(q-1)^a}{q^{d/2}}.
\]
The logarithmic derivative of \(f(q)=(q-1)^a q^{-d/2}\), for \(q>1\), is
\[
\frac{f'(q)}{f(q)}=\frac{d-q}{2q(q-1)}.
\]
Thus \(f\) increases up to \(q=d\) and decreases thereafter. Its unique maximum yields the desired bound and exactly the two stated directional equality conditions. If the spherical geometric mean attains equality, the continuous nonnegative directional deficit is identically zero. Then \(u\cdot c=0\) and \(u^TAu=d\) for all \(u\), which forces \(c=0\), \(A=dI\). The converse is direct.

For uniqueness of the radius, take \(A_\varepsilon=\lambda\exp(\varepsilon H)\) with a nonzero symmetric trace-free matrix \(H\). Then \(\det A_\varepsilon=\lambda^d\) and for small \(\varepsilon\) all semiaxes exceed one. When \(\lambda\ne d\), the displayed derivative of \(f\) is nonzero at \(\lambda\). Choose a unit eigenvector and the sign of \(\varepsilon\) so that its Rayleigh quotient moves toward \(d\). This strictly increases the corresponding pair-of-sections volume, disproving pointwise maximality for every other ball radius.

For the local expansion, define
\[
L(q,t)=\frac{d-1}{4}\log\bigl[(q-(1-t)^2)(q-(1+t)^2)\bigr]-\frac d2\log q.
\]
At \((q,t)=(d,0)\), both first derivatives vanish, the mixed second derivative is zero, and
\[
L_{qq}=-\frac1{2d(d-1)},\qquad L_{tt}=-\frac{d+1}{d-1}.
\]
Since \(q=d+\varepsilon d(u^THu)+O(\varepsilon^2)\) and \(t=\varepsilon u\cdot b\), Taylor's theorem proves the uniform pointwise expansion. Finally the rotational identities
\[
\int(u^THu)^2\,d\sigma(u)=\frac{2\operatorname{tr}(H^2)+(\operatorname{tr}H)^2}{d(d+2)},
\qquad\int(u\cdot b)^2\,d\sigma(u)=\frac{\|b\|_2^2}{d}
\]
yield the integrated expression. Its Hessian vanishes only if \(H=0\) and \(b=0\).

## Verification
The accompanying standalone `verify.py` uses deterministic randomized positive-definite matrices of constant determinant to check the exact section formulas and pairwise bound, verifies sharp local perturbations for noncritical ball radii, and evaluates the analytic Hessian through numerical finite differences. These are diagnostic finite checks only; the inequalities and expansions are proved above for all dimensions and all admissible parameters.

## Relationship to prior work
The exact formula for sections of a general, nonconcentric ellipsoid appears in the proof of *Global Barker–Larman rigidity for ellipsoids* (2026), whose principal conclusion is injectivity of all tangent-section data. The present statement asks instead for a **sharp all-direction antipodal inequality under a fixed-volume constraint**, for the unique critical radius, and for its full translation-and-shape Hessian. The older exact formula is explicitly used as a starting identity, not claimed as new. *Uniform alpha-section dominance for nested ellipsoids in every dimension* (2026) treats **cap-volume fractions** in one suitable direction, with no fixed-volume antipodal sectional extremum. Haddad and Ryabogin's 2026 work on noncentral sections provides the current geometric-tomography motivation, not this sharp optimized pairwise section inequality.

## Limitations
The result applies to ellipsoids, not arbitrary convex bodies. The sharp radius selection concerns universal pointwise dominance over all equal-volume ellipsoids; it says nothing about single-section maximality at each direction for translated bodies. The local quadratic coefficients are exact infinitesimal stability data, not a claimed global metric stability constant. The explicit prior sectional formula makes the extremal inequality elementary after appropriate pairing and optimization, and historical priority for an equivalent statement cannot be ruled out; independent validation has not been performed.

## References
1. *Global Barker–Larman rigidity for ellipsoids*, 2026, public result identifier `2026/10/4/SCOPE-global-barker-larman-rigidity-for-ellipsoids--75abc96cf1f6`, section-volume formula and rigidity theorem.
2. *Uniform alpha-section dominance for nested ellipsoids in every dimension*, 2026, public result identifier `2026/10/4/SCOPE-uniform-alpha-section-dominance-for-nested-ellipsoids-in-every-d--a9c59a3c2e6e`.
3. A. Haddad and D. Ryabogin, *On convex bodies with constant non-central sections*, arXiv:2605.00299v1, first public 2026-05-01.
4. D. Larman, L. Montejano and E. Morales-Amaya, *Characterization of ellipsoids by means of parallel translated sections*, Mathematika 56 (2010), 363–378, DOI:10.1112/S0025579310000379.
