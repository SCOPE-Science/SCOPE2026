# Self-review

## Correctness — PASS

The response kernel is the convolution of two positive one-stage linear-reservoir kernels, with continuous rate-coincidence limit. The baseline global peak follows from \(\beta\ge1\); the modified peak is rigorously localized after the second pulse because the first routed response is strictly below its unattenuated unit maximum. The derivative-weighting calculation ensures at most one postarrival crest; differentiating the envelope gives a strict crossing at \(\delta=m(r)\). Finally, \(\delta=2m(r)\) is the unique worst lag and the elementary inequality \(\tanh u<u\) establishes the globally sharp \(e^{-2}\) bound. The included checker independently tests 280,478 assertions; the continuum claim is proved analytically in `RESULT.md`. No unproved convergence or numerical exhaustion is invoked.

## Originality — PASS with explicit historical-priority uncertainty

McCuen (1979) establishes the qualitative downstream detention paradox, and Pattison et al. (2014) treats timing changes and their downstream effects in full-text hydrodynamic scenarios. Neither is claimed to have discovered the present general phenomenology. The assessed narrower new contribution is the explicit complete rate-contrast and delay criterion, the invariant twice-mode extremizer, and its universal exact penalty ceiling. The available full 2014 source does not imply this analytic classification. Earlier single-reservoir routing literature and the McCuen field study were compared from accessible abstracts only; uninspected full manuscripts and alternate linear-systems language remain genuine residual historical-priority risks.

## Value — PASS

The confluence peak is the mathematically natural risk observable for localized detention. Even with first-stage attenuation, shifting an upstream pulse may increase the joint outlet peak; the theorem quantifies precisely when this reverses and how large the worst possible increase can be. The bound is meaningful for every positive added-reservoir rate and every downstream pulse volume at least as large as the first. This is a sharp structural benchmark, not an applied flood forecast or a claim for nonlinear streams.

## Source limitations

Full text examined: Pattison et al. (2014), https://doi.org/10.1002/2013WR014067. Abstract-only comparisons: McCuen (1979), https://doi.org/10.1061/JYCEAJ.0005300; Błażejewski and Murat-Błażejewska (2003), https://doi.org/10.1623/hysj.48.4.665.51413. Standard hypoexponential identities are not treated as a novel method. An independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
