# Scientific review

## Correctness — PASS

The stationary projection equations are derived directly from the feedback signs. Capped-demand inversion reduces subtarget equilibria to one scalar strictly increasing function, giving uniqueness below the explicit threshold. The full-target condition reduces exactly to a closed interval, giving a singleton at equality and a continuum above it. Piecewise-linear inversion proves the sharp matching-volume derivative; the full Jacobian is checked by its aggregate/difference decomposition; and the homogeneous symmetric flow supplies an exact clipped-initial-imbalance selection law. No inference from finite tests to infinite claims is used. The standalone checker passed 88,985 exact-rational equilibrium checks over 2,405 balanced profiles and 384 numerical selection trials.

## Originality — PASS (same mathematical model literature evaluation only)

The closest source is Gelastopoulos, arXiv:2606.31802v1. The paper proves uniqueness and global convergence when the aggregate desired match rates differ, while expressly excluding the equal-total case from its main conclusion. Its Propositions 3.3–3.4 establish an implicit capped fixed-point representation, and Lemma 3.6 establishes monotonicity of an auxiliary function; these are used as foundations rather than claimed anew here. Their statements do not give the equal-total encounter-rate threshold, explicit complete equilibrium classification, derivative cusp, transverse neutral eigenvalue, or exact homogeneous initial-condition selection. The added parameter/spectral/dynamical analysis is required to extract those conclusions. Search under balanced target-rate, saturation, and continuum-equilibrium formulations found no statement-equivalent published result. Distinct steady-state search-market balance results concern different population dynamics. A residual possibility of equivalent treatment under alternative terminology remains; there has been no independent historical-priority audit.

## Mathematical value — PASS

The motivating paper explicitly leaves balanced target totals unresolved despite their being a natural symmetry boundary. The result identifies the only encounter threshold separating failure to meet demand from an entire set of equilibria meeting every target. The first-order shortfall coefficient depends only on the largest demand values and their multiplicities, and the homogeneous selection law shows mathematically how outcomes become path dependent exactly when equilibria cease to be unique. These address interpretation of the model's equilibrium predictions and their robustness, rather than being a routine change of notation.

## Closest literature and limitations

Primary source: Alexandros Gelastopoulos, *Feedback dynamics in matching networks drive behavioral differentiation despite overlapping objectives*, arXiv:2606.31802v1 (2026). The paper's Section 2.2 explicitly sets aside equality of the two aggregate target rates. The capped-equilibrium and monotonicity propositions in Section 3 remain applicable and make the derivation feasible; the theorem here does not claim those lemmas as novel. Related economically motivated balance results by Lauermann, Nöldeke, and Tröger (2020) and the 2025 *Matching with Frictions* survey concern different frictions and matching-flow structures. Only the primary paper's relevant technical sections were inspected in full. The other sources were available here principally through abstracts and descriptions, so their entire contents are not certified to lack an equivalent specialization.

The result uses an idealized continuously adjusted acceptance model. The universal equilibrium classification extends to monotone sign-correct feedbacks, but the explicit neutral spectrum and trajectory-selection formula require the stated linear common-rate dynamics; the latter further requires homogeneous target rates and homogeneous initial acceptances within each side.

Self-review: passed. Independent audit: not yet performed.
