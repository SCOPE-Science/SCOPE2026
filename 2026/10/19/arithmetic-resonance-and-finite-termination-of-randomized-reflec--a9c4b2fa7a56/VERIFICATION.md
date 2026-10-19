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

Exact algebraic checks used `verify_reflection_resonance.py` with `sympy==1.14.0` (see `requirements.txt`). The executable enumerates all \(2^r\) ordered reflection words for \(r=1,\ldots,7\) at \(\theta=\pi/4\) and \(\theta=\pi/6\), checking every composition matrix against the derived parity form in exact symbolic arithmetic; it verifies all binomial support counts, and computes the odd three-reflection killed-chain expectations in exact rational arithmetic. All 508 reflection-word comparisons, the expectations \(61/9\) and \(36\), and the even four-reflection success probability \(1/8\) passed.

The general proof is analytic: the alternating-sign reflection exponent, its binomial Laurent polynomial, the invertibility/zero dichotomy for even words, the orthogonal-projection adjacency criterion for odd words, positive-probability repeated pair events, and the reduced-denominator argument. Finite enumeration verifies implementation of representative cases, not the infinite/all-angle theorems. No independent audit, external certification, noisy-data guarantee, or finite-precision guarantee is claimed.
