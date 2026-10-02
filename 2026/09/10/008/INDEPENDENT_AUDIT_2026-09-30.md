---
audit_date: 2026-09-30
status: passed
---

# Independent mathematical audit

## Final claim

For the asymmetric L-space census knot t12533 represented by the committed positive 4-braid, there is no distinct chirally cosmetic surgery pair with |H1|<=30; the exact knot data a2=52, a4=681 and v3=323/4 give the same-sign obstruction constant 6033/323.

## Correctness — PASS

The exact polynomial arithmetic was independently checked from the committed Jones expression: V''(1)=-312, V'''(1)=-10692 and the stated normalization gives v3=323/4. With a2=52 and a4=681, 7a2^2-a2-10a4=12066 and the Ichihara-Ito-Saito ratio is 6033/323 in lowest terms. Their Theorem 1.3 therefore forces the common surgery numerator m to be a multiple of 6033 whenever n+n' is nonzero in the ±-type case, excluding 0<|m|<=30. Theorem 1.1 excludes 0-type because v3 is nonzero, and Varvarezos Theorem 1.8 excludes opposite-sign slopes for a nontrivial L-space knot. The inspected master verifier recomputes Alexander/Conway and Jones data from the frozen braid word with exact arithmetic and trefoil controls.

## Originality — PASS

Ichihara-Ito-Saito and Varvarezos provide general obstruction theorems, not the t12533-specific finite-type constants or the resulting exact ratio 6033/323. The t12533 literature identifies the knot and its L-space/asymmetric context, but the searched primary and corpus sources did not state this chirally-cosmetic exclusion or the same per-knot constant. Applying the general theorem therefore still requires the nontrivial exact invariant computation supplied here.

### Equivalent formulations

The audited claim is the specialization of this general necessary condition to a specific natural knot after computing its exact invariants.

### Broader coverage

That theorem covers one sign regime broadly; it does not determine the same-sign arithmetic for t12533.

### Exact database or table comparison

No prior exact per-knot obstruction table was located.

### Claim versus prior implication

The literature theorems do not mechanically supply the knot-specific constant without those computed invariants.

## Value — PASS

Chirally cosmetic surgery is a named open classification problem, and t12533 is a natural sporadic asymmetric L-space census knot. The reusable mathematical datum is the exact per-knot obstruction constant, which in fact gives a much wider same-sign numerator gap than the conservative |H1|<=30 headline. This is a motivated boundary computation rather than an arbitrary random-knot statistic.

## Sources inspected

- Git tree/blobs: RESULT.md, Alexander, Jones, chiral-analysis and master verifier sources. Checked conventions, exact invariant chain and the finite-scope exclusion.
- Ichihara-Ito-Saito, arXiv:2112.04156: full PDF statements of Theorems 1.1 and 1.3. Confirms the zero-type v3 obstruction and the exact ±-type ratio formula used.
- Varvarezos, arXiv:2112.03144: full PDF introduction and Theorem 1.8. Confirms opposite-sign cosmetic surgeries are excluded for nontrivial L-space knots.
- t12533 primary literature cited in the package: knot identification, L-space/asymmetric context and recorded quasi-alternating slopes. Provides object/context rather than the audited finite-type constant.

## Residual risks

- The exclusion depends on the cited general surgery theorems and the knot being the stated nontrivial L-space knot. The |H1|<=30 cutoff is conservative: the same-sign divisibility argument itself excludes every positive common numerator below 6033, but no stronger public headline is introduced in this audit.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
