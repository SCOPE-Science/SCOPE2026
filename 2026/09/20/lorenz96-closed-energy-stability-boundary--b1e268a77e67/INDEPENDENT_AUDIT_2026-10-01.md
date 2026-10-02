# Independent audit — 2026-10-01

## Record

**Closed energy-stability boundary for Lorenz-96-like quadratic advection**

Final claim: For homogeneous cyclic quadratic energy-preserving Lorenz-96-like systems, the constant equilibrium is globally asymptotically stable exactly on the closed spectral energy-stability window, including the marginal zero-real-part boundary; strict interior stability is exponential.

Disposition: **PASSED**

## Correctness — PASS

Fresh reconstruction verifies the centered energy identity and the polarization identity \(\mathbf e^T G(y)=-y^T A y\). At a nonzero zero-dissipation boundary state, the mean derivative equals \(-\|y\|^2/F\), so no nonzero trajectory can remain in the LaSalle set. A positive-real-part linear mode gives instability. Independent numerical checks reproduced the two quadratic identities.

## Originality — PASS

Kerin–Engler Proposition 1 proves only the strict inequalities \(Fp_+<1\) and \(Fp_-<1\). Full-text inspection confirms the proof uses negative definiteness and does not include equality. The audited theorem adds the marginal closure and exact iff criterion. A later 2026-09-21 published record states the same closure but postdates this record and therefore is not prior coverage.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Primary-source inspections and residual access risks are also recorded there.

## Scientific value — PASS

The theorem closes a nonhyperbolic boundary left open by the standard strict energy estimate and rules out hidden finite-amplitude recurrence exactly at the first spectral threshold, a natural and useful stability boundary.

## Checked scientific sources

- Kerin–Engler, On the Lorenz '96 model and some generalizations, DCDS-B 27 (2022), DOI:10.3934/dcdsb.2021064 / arXiv:2005.07767.
- Published-record semantic search for Lorenz-96 critical global-stability closure.

## Residual risks

- The equality argument is short and classical once the polarization identity is noticed, so an unindexed earlier observation remains possible.

## Verification boundary

The audit reconstructed the argument and performed fresh algebraic or logical checks where needed. Existing package logs were treated as supporting evidence only. No formal proof-assistant or expert attestation is asserted.
