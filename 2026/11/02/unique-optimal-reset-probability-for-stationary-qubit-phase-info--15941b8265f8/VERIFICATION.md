---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For 0<p<1, theta∈(0,2pi), channel contraction gives one stationary qubit with coherence z=p/[1-(1-p)e^{i theta}]. The full-rank equatorial SLD formula yields the rational QFI in x=p/(1-p), t=sin²(theta/2). Independently SymPy factorization checked dF/dx=xP_t(x)/A^4 identically, and at t=1 F=x²/(x+2)^4, unique maximizer x=2, F=1/64. Descartes one sign change of P_t across 0<t≤1 plus endpoint signs proves exactly one simple positive root. Scaling x=delta*y yields limiting -4y^4+4y²+2 with unique positive root and optimum QFI constant 2sqrt3/9. The excluded identity resonance is rank-changing; finite-difference SLD tests in inspected source do not replace proof.

## originality

PASS

PASS qualified: Wald et al. 2024 establish geometric steady-state resolvent and correlations, not stationary single-qubit phase-QFI optimizer; Li–Tong–Bao 2026 general reset-rate QFI response concerns continuous-time Lindblad dynamics. All-phase Descartes characterization and punctured-resonance asymptotic are distinct. The latter source full text unavailable; priority risk remains.

## value

PASS

The globally optimal reset probability removes ambiguity in stationary phase sensing under a common gate/reset channel; exact half-turn and near-resonance regimes give nontrivial complete parameter control, not a generic SLD formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
