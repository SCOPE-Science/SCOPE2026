# Independent mathematical audit — 2026-10-01

## Final claim

Sharp dispersive tails of the degenerate mKdV-Burgers shock

## Correctness — PASS

PASS. The asymptotics were reconstructed from the actual profile ODE. At the upstream state, the linearized characteristic polynomial gives the two stated spatial roots, and the source logarithmic-slope bound excludes the fast eigendirection in the strict monotone regime. At the repeated-root boundary, the linear operator has a size-two Jordan form; after exponential rescaling, strict convexity together with the profile slope sign forces the generalized-eigenvector coefficient to be nonzero. At the downstream contact state, a center-manifold expansion gives the quadratic and cubic velocity coefficients, and integrating the reciprocal variable produces exactly the stated logarithmic correction. The repository symbolic verifier independently reproduces those coefficients and the repeated-root factorization.

## Originality — PASS

PASS to the best of current knowledge. The 2026 source gives coarse dispersion-uniform two-sided tail bounds but its accessible indexed statement does not supply the sharp dispersion-dependent exponent, critical Jordan factor, or logarithmic contact correction. Published-record search found a later 19 September result that builds on the same logarithmic correction; because it postdates this 18 September record, it is follow-up coverage rather than prior art. The closest older primary paper, Jacobs-McKinney-Shearer (1995), could not be obtained in verified full text: open-access searches failed and authorized institutional retrieval was interrupted by an expired verification tab. That source remains a named residual originality risk.

### equivalent_formulations

Searches: mKdV Burgers degenerate shock sharp tail logarithmic correction Jordan repeated root; modified KdV Burgers Oleinik shock contact tail logarithm

Evidence: The exact published-record search found the audited record and a later follow-up exploiting the same logarithmic coefficient.

Reasoning: Equivalent phase-plane and reciprocal-tail formulations were considered; no earlier exact coefficient statement was located.

### broader_coverage

Searches: Eun Han Kim 2609.20591 degenerate shock tail bounds; Jacobs McKinney Shearer 1995 travelling wave modified KdV Burgers

Evidence: The 2026 source gives dispersion-uniform two-sided decay scales; the 1995 paper is a highly relevant older phase-plane source but was inaccessible in verified full text.

Reasoning: Coarse exponential and algebraic bounds do not mechanically determine the exact spatial root, Jordan coefficient, or logarithmic correction.

### exact_database_or_table

Searches: published mathematical record semantic search exact mKdV-Burgers log coefficient

Evidence: No natural database/table governs these asymptotic coefficients, and no earlier exact record was found.

Reasoning: The relevant exact comparison is theorem-level asymptotics, not numerical table lookup.

### claim_vs_prior_implication

Searches: arXiv:2609.20591 exact decay rate; Jacobs McKinney Shearer endpoint asymptotics

Evidence: The accessible source statement provides uniform decay classes, while the later 19 September record treats the audited logarithmic term as input for a comparison law.

Reasoning: The sharp coefficients require a center-manifold and repeated-root calculation beyond the inspected prior statements.

## Scientific value — PASS

PASS. The claim refines natural asymptotic invariants of a canonical degenerate shock rather than reporting a cosmetic higher-order term. It identifies the exact dispersion-dependent upstream rate, a resonance transition at the monotonicity boundary, and the first translation-invariant downstream correction; the latter also recovers the dispersion coefficient from the profile.

## Source inspections

- **Large-Time Behavior towards Composite Waves of Degenerate Shock and Rarefaction Wave for Modified KdV-Burgers Equation** — https://arxiv.org/abs/2609.20591. Material read: Abstract and indexed result material describing dispersion-uniform two-sided decay bounds. Assessment: GENERAL_BOUNDS_NOT_EXACT_ASYMPTOTICS. Evidence: The accessible statement identifies exponential and algebraic scales but not the audited exact exponent, Jordan tail, or logarithmic coefficient.
- **Travelling wave solutions of the modified Korteweg-de Vries-Burgers equation** — https://doi.org/10.1006/jdeq.1995.1043. Material read: Bibliographic metadata and later references only; verified full text was not obtained. Assessment: INACCESSIBLE_PLAUSIBLE_PRIOR_SOURCE. Evidence: The institutional retrieval attempt was interrupted by an expired verification step; no whole-document noncoverage claim is made.
- **Universal logarithmic dispersion fingerprint in degenerate mKdV-Burgers shocks** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-logarithmic-dispersion-fingerprint-degenerate-mkdvb--0e2c73e7cd5a. Material read: Published title and summary. Assessment: LATER_FOLLOW_UP_NOT_PRIOR_ART. Evidence: Dated 19 September 2026, it uses the same logarithmic correction to compare two dispersion strengths and therefore postdates the audited 18 September record.

## Limitations and residual risks

The theorem concerns only the monotone degenerate shock in the stated monotonicity regime. It does not cover oscillatory, nondegenerate, or undercompressive shocks, nor nonlinear time-dependent convergence rates. Tail amplitudes and additive constants depend on translation; the displayed exponents and logarithmic coefficients do not.

- Jacobs-McKinney-Shearer (1995) remains a genuine originality risk because verified full text could not be read in this run.
- The theorem is restricted to the monotone degenerate shock regime and does not extend to oscillatory or undercompressive profiles.

## Disposition

**passed**
