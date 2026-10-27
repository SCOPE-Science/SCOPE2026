# Scientific review

## Correctness

**PASS.** The proof defines all cyclic windows and variations and handles the zero-seminorm quotient. Finite maximums are piecewise affine along input segments; their derivatives select perturbation coordinates. For contiguous windows, the rightmost maximizers move monotonically across unwrapped input indices, so the selected cyclic edges cannot repeat. For the gapped two-tap window, each adjacent pair of selected coordinates is separated by at most three input edges, while the oscillation-level-set bound improves small-dimension cases. Four explicit strict-selector constructions attain every sharp two-input factor. The one-input factor follows from the lattice sorting inequality with an isolated-impulse extremizer. A stand-alone exact-selector regression and randomized test are included; no infinite assertion depends on enumeration.

## Originality

**PASS subject to residual historical risk.** The flat-dilation definition is classical, but the exact two-input bounded-variation constants, contiguous-versus-disconnected window mechanism, dimension threshold, and one-input/two-input separation were not implied by the materially inspected propositions in Maragos–Schafer (1987), Heijmans (1995, §6), or Aldaz–Pérez Lázaro (2006). The older publications cover the lattice/max representation and a distinct Hardy–Littlewood average maximal operator. Relevant mathematical-search records and existing accessible claims were compared by implication, not title. The possible presence of an equivalent formula in older nonlinear signal-filter or stack-filter literature remains a nonzero uncertainty.

## Mathematical value

**PASS.** The result isolates support connectivity as an exact stability criterion for the canonical sliding maximum: contiguous windows have sharp constant one, while the first disconnected support has sharp constants up to three. These are the relevant perturbation norms for finite cyclic grey-scale filtering, with exact smallest dimension and attainable bounds. The one-input multiplier of at most two makes the nonlinear two-input instability mathematically visible; this is not a mere relabeling of the classical dilation definition.

## Closest literature and limits

Maragos–Schafer, doi:10.1109/TASSP.1987.1165259; Heijmans, SIAM Review **37** (1995), §6; Aldaz–Pérez Lázaro, arXiv:math/0601044. The result is restricted to finite cycles and the specified flat windows. No independent external scientific verification is represented.

Self-review: passed. Independent audit: not yet performed.
