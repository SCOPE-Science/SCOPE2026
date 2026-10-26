---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification

**Proof-level checks.** The group-conditioned focal-payoff subtraction in `RESULT.md` is derived from the specified failure probability \(1-\rho^{\#D}\) and activated multiplier \(1-\omega\). The Bernstein coefficient jump is at the pivotal coplayer count \(M-1\). The transformed polynomial \((1+t)^n(f(t/(1+t))-h)\) has the same nonzero coefficient sign sequence as \(b_j-h\), so Descartes' theorem is applicable with multiplicities. The derivative has positive initial value and at most two interior zeros counted with multiplicities, excluding a second negative-slope band. The four-player instance uses exact rational coefficients and explicitly checks the transverse growth of the missing strategy at the middle root.

**Reproduction.** Save the complete embedded `verify.py` and run `python verify.py` with a standard Python 3 interpreter. Expected output: `PASS: 2169 exact checks; 3 simple D/S roots in disjoint rational intervals`. The program enumerates raw conditional payoffs independently of the derived Bernstein formula, over all permissible quorum counts through ten-player groups and rational values for risk, protection, and frequency. Its arithmetic uses Python `fractions.Fraction` without floating-point comparisons.

**Limitations.** Finite exact-arithmetic checks corroborate only the enumerated inputs and explicit algebraic witness. The infinite-family conclusions rely on the fully stated analytic proof. The check neither asserts a proof assistant certification nor independent audit. Originality remains subject to fuller priority examination.
