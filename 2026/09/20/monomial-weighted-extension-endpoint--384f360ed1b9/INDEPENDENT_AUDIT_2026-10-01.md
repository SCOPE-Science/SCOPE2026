---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every real k at least 3, Vergara's monomial normal-direction energy controls the weighted L4 Fourier extension norm at the endpoint iota equal to (k−1)/k; together with the known subendpoint obstruction, this is the exact monomial threshold.

## Correctness — PASS

Squaring the extension and using Plancherel in the linear coordinate gives an exact one-dimensional quadratic form. At the critical spatial weight the Fourier kernel is positive, has the required fractional singularity near zero, and decays quadratically at infinity. Flat and curved Schur estimates recover the exact terminal cutoff used by the source. This closes the stationary region and gives the endpoint inequality for every real k at least 3. No finite experiment is used.

**Checked sources.** Assigned RESULT.md at tree cd23c641779f16872d312ee09961396716c4607e; Vergara arXiv:2609.20643v1 full HTML; Bulj--Inami--Shiraki 2026 public theorem material; Schippa 2024 public theorem material

**Residual risks.** The argument is model-specific and does not settle the general finite-type endpoint.

## Originality — PASS

Vergara's full primary text proves the monomial result only for strict superendpoint exponents, proves failure below the threshold, and explicitly states that equality remains open. Searches found no earlier theorem implying the same endpoint normal-direction-energy estimate.

### Equivalent formulations

Equivalent energy, radial-weight, and terminal-cutoff formulations were compared; the source leaves precisely this endpoint open.

### Broader coverage

No inspected broader theorem dominates Vergara's endpoint normal-direction-energy statement.

### Exact database or table

No finite database or table can settle this analytic endpoint theorem.

### Claim versus prior implication

The source theorem does not imply the equality endpoint by a limiting argument.

**Checked sources.** https://arxiv.org/abs/2609.20643; arXiv:2602.03167; arXiv:2408.07248

**Residual risks.** The source is very recent, so unindexed contemporaneous overlap remains possible.

## Value — PASS

This closes an explicit endpoint gap in a sharp threshold theorem and gives a mechanism that succeeds exactly where the source proof loses a logarithm.

**Checked sources.** Vergara 2026; related power-curve extension literature

**Residual risks.** It is a model endpoint theorem rather than the general finite-type result.

## Limitations

- This is only the monomial graph model, not every finite-type convex curve.
- The proof uses the globally linear first coordinate and explicit power-law geometry.
- No extremizer, stability, weak-type, Lorentz, or optimized-constant statement is included.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
