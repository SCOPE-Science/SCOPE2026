# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The source's full-text Eq. (55) was used without changing its assumptions: three identical Stuart–Landau oscillators, \(a>0\), \(c=-1\), straight isochrones \(d=0\), and no linear self-coupling. On the uncoupled radius \(R=\sqrt a\), a cubic monomial \(Cz_pz_q\bar z_r\) contributes
\[
R^{-1}\operatorname{Im}(e^{-i\theta_i}Cz_pz_q\bar z_r)
=
a\,\operatorname{Im}(Ce^{i(\theta_p+\theta_q-\theta_r-\theta_i)})
\]
to the \(i\)-th phase equation. Expanding the proposed \(Q_i\) reproduces every sine term in the source's Eq. (55), with the same weight and phase shift, and the prefactor \(-1/(4a^2)\) therefore contributes exactly \(-f_i^{(2)}\).

The perturbative order is consistent: the new physical term is multiplied by \(\varepsilon^2\), so its evaluation on the order-\(\varepsilon\) deformation of the invariant torus first affects order \(\varepsilon^3\). It cannot alter the order-\(\varepsilon\) phase coupling.

The additional monomial \(z_j^2\bar z_i\) follows directly from the source's own general cubic formula (57)--(58): choosing \(p=q=j,r=i\) gives the second harmonic \(2(\theta_j-\theta_i)+\xi\). A deterministic numerical identity check for all three components gives a maximum double-precision residual \(4.441\times10^{-16}\) over 375 evaluations.

Adversarial checks included arbitrary nonsymmetric real weights, negative weights, nonzero phase lag, and all three target oscillators. No symmetry of the weight matrix is required by the algebra.

## Originality

PASS, to the best of our knowledge.

The primary source arXiv:2609.20632v1, submitted 17 September 2026, was inspected in full-text HTML. It explicitly states that its engineered cancellation is necessarily partial and that a single engineered strength cannot cancel the asymmetric and symmetric emergent nonpairwise terms simultaneously under its chosen weights. Its Methods section says it discusses all resonant cubic terms, but the nonlinear-pairwise list in Eqs. (59)--(60) does not include \(z_j^2\bar z_i\), despite that monomial being allowed by the immediately preceding general formula (57)--(58).

The present claim is deliberately narrower than the general theory of synchronization engineering. Earlier work shows that nonlinear feedback can be designed to realize desired phase interaction functions, and higher-order phase-reduction papers derive multibody corrections for Stuart–Landau networks. No originality is claimed for those general principles, for the elementary polar projection of a cubic monomial, or for second-order phase reduction itself.

Searches using the source title and identifier together with "exact cancellation", "counterterm", "cubic coupling", "second harmonic", and equivalent Stuart–Landau phase-reduction terminology did not locate a prior source-specific complete counterterm or a correction identifying this omitted monomial. The source is extremely recent, so unindexed author revisions or discussions are the main residual originality risk. No inaccessible paper was identified that is specifically likely to contain this exact source-specific formula.

## Value

PASS.

The result changes the interpretation of the source's design limitation. Partial compensation is a limitation of the restricted physical-nonpairwise ansatz used there, not of the full resonant cubic coupling space. The explicit counterterm provides a constructive way to recover the first-order Kuramoto--Sakaguchi phase model through order \(\varepsilon^2\), and the missing pairwise second-harmonic monomial supplies exactly the control direction needed for the terms that the source's chosen PN basis cannot touch.

The result is also practically modular: the coefficients are explicit quadratic functions of the original network weights and can be implemented componentwise without computing a new second-order reduction of the added coupling.

## Sources checked

- R. Muolo, H. Nakao, and C. Bick, *Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design*, arXiv:2609.20632v1:
  https://arxiv.org/abs/2609.20632
- H. Kori, C. G. Rusin, I. Z. Kiss, and J. L. Hudson, *Synchronization engineering: theoretical framework and application to dynamical clustering*, Chaos 18, 026111 (2008):
  https://doi.org/10.1063/1.2927531
- E. T. K. Mau, O. E. Omel'chenko, and M. Rosenblum, *Phase reduction explains chimera shape: When multibody interaction matters*, Phys. Rev. E 110, L022201 (2024):
  https://doi.org/10.1103/PhysRevE.110.L022201
- E. Gengel, E. Teichmann, M. Rosenblum, and A. Pikovsky, *High-order phase reduction for coupled oscillators*, J. Phys. Complexity 2, 015005 (2021):
  https://doi.org/10.1088/2632-072X/abbed2

## Limitations retained

This is a perturbative cancellation theorem through order \(\varepsilon^2\), not a finite-coupling conjugacy theorem. It does not bound the order-\(\varepsilon^3\) remainder, analyze robustness to coefficient error, or prove experimental realizability of every complex cubic coefficient. The explicit formula is tied to the source's straight-isochrone \(c=-1,d=0\) triad calculation; extending it to curved isochrones or larger networks requires recomputing the relevant second-order harmonics.
