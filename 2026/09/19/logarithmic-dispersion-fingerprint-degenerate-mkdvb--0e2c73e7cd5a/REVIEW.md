# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The source paper supplies the exact traveling-wave equation, the monotone profile in the full monotone regime, the right-tail comparability needed to control the asymptotic variable, and the center-manifold expansion through the cubic term. Rewriting that expansion for v=s-U gives a Riccati-type asymptotic equation. Passing to y=1/v and integrating once yields the logarithmic inverse-tail term; a second bootstrap makes the remainder integrable and produces a finite constant. Rescaling recovers arbitrary viscosity. Direct symbolic substitution into the general-viscosity profile equation reproduces the same coefficients. Translation affects the ordinary xi^-2 term but not the logarithmic coefficient, so the pairwise comparison limit is invariant under fixed profile translations.

Potential failure modes were checked. The sign of the dispersive contribution was verified both from the center-manifold graph and directly from the integrated profile equation. The pure-viscous limit agrees with the first-order viscous profile ODE. The argument remains local at the degenerate right endpoint and therefore does not rely on a stronger global center-manifold claim than the source establishes.

## Originality

**PASS, to the best of current knowledge, with a material residual literature risk.** The claim is deliberately narrower than the source paper's center-manifold calculation: the coefficients a2=3 and a3=1+18 nu are already in arXiv:2609.20591v1 and are not claimed as new. The source theorem itself states two-sided algebraic bounds, not an exact leading coefficient or a logarithmic second term. The 2025 purely viscous composite-wave paper gives the explicit first-order viscous shock ODE and coarse tail bounds; it does not cover the dispersive correction.

Repository searches by arXiv identifier, degenerate-shock terminology, logarithmic-tail terminology, and equivalent mKdV–Burgers wording found no existing SCOPE record for this claim. External searches covered the exact source title, degenerate viscous-dispersive shock terminology, logarithmic/asymptotic-tail variants, the 2025 purely viscous precursor, the 2016 phase-plane paper, and the 2020 algebraic-traveling-wave paper.

The principal unresolved originality risk is D. Jacobs, B. McKinney and M. Shearer, *Travelling wave solutions of the modified Korteweg-de Vries-Burgers equation*, JDE 116 (1995), DOI 10.1006/jdeq.1995.1043. It studies the same traveling-wave equation and is therefore capable in principle of containing an endpoint expansion. Its complete body was not inspected. Available bibliographic records and later citations describe it as a traveling-wave existence/classification work; no concrete evidence of the logarithmic coefficient or the pairwise dispersion limit was found. This is residual risk, not evidence of prior coverage.

Claudia Valls (2020), DOI 10.14232/ejqtde.2020.1.48, was inspected sufficiently in full text to resolve a terminology trap: “algebraic traveling wave” there means a wave corresponding to an invariant algebraic curve in the phase plane, explicitly not algebraic convergence to end states. Zhang et al. (2016), DOI 10.3934/dcdsb.2016078, was inspected at the article/abstract/reference level; it focuses on phase portraits, existence counts, and bounded traveling waves, and no matching endpoint expansion was located.

## Value

**PASS.** The result makes precise a point that the source theorem intentionally treats only at scale level: dispersion leaves the leading 1/xi degenerate tail unchanged but produces the first profile-dependent correction. The comparison law isolates this effect in a translation-independent observable and shows that the dispersive-versus-viscous difference is integrable on the degenerate side even though each individual shock deficit has a nonintegrable 1/xi tail. This is potentially useful in refined shock–rarefaction interaction estimates, profile matching, and numerical far-field boundary conditions.

## Limitations

The result is a profile asymptotic, not a new nonlinear stability theorem. It applies to the monotone degenerate branch and does not cover oscillatory profiles outside the monotonicity regime. Higher-order terms are not classified. The broad local quadratic-degeneracy calculation is supplied only as a mechanism; no broad originality claim is made for it.
