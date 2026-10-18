# Scientific review: rank-one exponential Carleman perturbation

## Correctness

**PASS.** The unitary Mellin multiplier \(m(\xi)=\pi/\cosh(\pi\xi)\) and the transform of the normalized vector \(g(t)=\sqrt2e^{-t}\) yield the exact spectral density \(w(\xi)=1/\cosh(\pi\xi)\). The rank-one eigenvalue condition reduces to a scalar Stieltjes transform, which integrates to the stated arctangent/artanh formulas. Its strict monotonicity gives precisely one simple exterior eigenvalue of the appropriate sign; pole and endpoint integrability exclude embedded eigenvalues. The threshold expansions give a quadratic gap at \(\pi\) and exponential gap at zero with the displayed coefficients. Exact normalization, signs, limiting ranges, and coupling landmarks were checked. The 83 standalone numerical assertions are supporting checks rather than a proof of universal statements.

## Originality

**PASS, with residual historical-priority risk.** Yafaev, arXiv:1210.5709, establishes the Carleman Mellin dispersion relation, general resolvent, and qualitative existence of an upper-band eigenvalue under a positive perturbation (Theorem 6.4). Yafaev, arXiv:1304.2677, Theorem 1.3, already establishes the negative eigenvalue count for finite-rank Hankel perturbations. These qualitative statements are not presented as novel. The contribution is the explicit scalar secular equation for this normalized exponential direction, together with both sharp, asymmetric threshold prefactors and coupling landmarks. The inspected relevant sections of both complete primary texts did not state those two quantitative edge laws. A differently worded earlier calculation or a result implicit in broad resolvent formulae remains a genuine priority risk.

## Value

**PASS.** The Carleman operator is a natural bounded noncompact Hankel operator with spectral edges of different analytic types. The exact example shows that the same fixed rank-one direction produces a power-law upper-edge bound state and a beyond-all-orders lower-edge state, and identifies constants rather than only qualitative existence. This makes the lower-edge logarithmic spectral-response singularity quantitatively accessible and illustrates a structural distinction not captured by eigenvalue counting alone.

## Limitations and relation to literature

The claim is for one explicitly normalized exponential rank-one perturbation, not all compact or Hankel perturbations. No exact scattering operator or eigenvalue law for other directions is asserted. Similar published-finding corpus records about normal Cesàro operators concern different unperturbed spectra and do not imply this Carleman threshold pair; absence of a near-identical record is not a uniqueness certificate. Sources: Yafaev, arXiv:1210.5709 (Sections 1–3, 6); Yafaev, arXiv:1304.2677 (Theorem 1.3, Sections 1.2, 3.4). Independent mathematical and bibliographic reviews remain unperformed.

Self-review: passed. Independent audit: not yet performed.
