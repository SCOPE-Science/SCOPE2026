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

Finite reproducibility checks use `python check.py` with the standard Python library. The program forms each rotation directly from its digit list, checks the exact gcd identity against integer arithmetic, and verifies the coprimality decomposition on 235455 inputs spanning 49 tested base/length blocks. Its output is `VERIFY_OK: 235455 direct rotation gcd tests across 49 base/length blocks`, followed by observed counts and the decimal example. The universal gcd identity is established by the rotation recurrence in the proof. The uniform error bound uses exact Möbius inversion, divisor bounds, and digit divisibility. The limit formulas use multiplicative orders and the divergence of reciprocal primes, not finite numerical extrapolation.

Scientific limits: only gcd-one rotation sets are counted (not pairwise-coprime sets); no claim of complete classification of all accumulation values is made. Independent audit is not performed.
