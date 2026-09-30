# Independent audit — Hankel obstruction and multiplier repair for minimal backward-shift projections

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/hankel-obstruction-multiplier-repair-backward-shift-projections--4f079531ab2f`  
**Audited tree:** `46542fa1b13859299175f389bb945519e00fe968`

## Disposition

**PASSED.** All three required axes pass; the record may remain in the validated set.

## Correctness

**PASS.** The record's mathematics survives. The formal coefficient map has Hankel matrix (alpha_{ell+i}); the explicit choice alpha_i=beta_i=(i+1)^(-3/4) lies in ell_2 but produces output coefficients bounded below by a constant times (ell+1)^(-1/2), so the unrestricted H^2-to-H^2 assertion fails. Nehari's theorem gives the BMOA boundedness boundary. For bounded multipliers, direct coefficient comparison gives L_g f=M_{f^sharp}^*g and the norm estimate. The arbitrary-multiplicity repair also checks: for each nonzero coefficient map P_eta, M intersect ker(P_eta) is a proper closed B-invariant subspace, so minimality makes P_eta|_M injective. If two nonzero shadows differ, represent the proper one as K_theta; invariance of M under M_theta^* tensor I (obtained from the shift-invariance of M-perp and bounded analytic functional calculus) produces a nonzero vector in the kernel of the other coefficient map, contradicting injectivity.

## Originality

**PASS.** PASS, but only on a narrowed boundary. The BMOA diagnosis, explicit Hankel obstruction, and paper-specific synthesis gap were already present in earlier SCOPE records `bmoa-boundary-backward-shift-hankel-operator--a39ad574fb44` (committed before this record) and `hankel-bmoa-boundary-backward-shift-synthesis--90c4302807ea`. The source preprint itself advertises the common projection-rigidity phenomenon. The surviving distinct contribution is the new multiplier/model-space proof that recovers the common-shadow theorem for a backward shift of arbitrary Hilbert multiplicity without using the invalid all-H^2 synthesis lemma. Repository commit searches for the repair mechanism and targeted literature searches did not locate an earlier equivalent source-specific proof. Classical Nehari/BMOA theory is expressly excluded from the novelty claim.

## Scientific value

**PASS.** The surviving repair is scientifically useful: it turns a diagnosed proof gap in a current invariant-subspace argument into a valid theorem of broader Hilbert multiplicity. That is more than a duplicate correction, while the record correctly avoids claiming a solution of the invariant subspace problem.

## Independent checks

- Recomputed the (n+1)^(-3/4) output lower bound and finite-section N^(1/4) growth.
- Checked the multiplier identity coefficient-by-coefficient and its H^infinity norm bound.
- Reconstructed the coefficient-map injectivity/minimality argument and the inner-multiplier contradiction.
- Compared against earlier SCOPE Hankel/BMOA records; treated those components as prior art rather than novelty.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.19311 — Ferreira--do Carmo preprint containing the defective Lemma 2.1 and projection-rigidity chain.
- https://arxiv.org/abs/2309.03427 — Earlier related bidisk invariant-subspace work by the same authors.
- https://doi.org/10.1112/jlms.12588 — Modern Hankel/BMOA context cited by the record.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/bmoa-boundary-backward-shift-hankel-operator--a39ad574fb44 — Earlier SCOPE record already establishing the sharp BMOA boundary/counterexample.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/19/hankel-bmoa-boundary-backward-shift-synthesis--90c4302807ea — Earlier same-day SCOPE record tracing the synthesis gap.

## Limitations

- The BMOA boundedness criterion and Hankel identification are classical/not new.
- The audit does not claim the invariant subspace problem is solved or validate unrelated arguments in the source papers.
- A residual prior-art risk remains that the arbitrary-multiplicity common-shadow lemma is implicit in older vector-valued model-space literature.

## Repository identity

The assigned source-tree SHA `46542fa1b13859299175f389bb945519e00fe968` exactly matched the current tree at the audited path on `main`; no stale-tree substitution was used. GitHub was read only during this audit.
