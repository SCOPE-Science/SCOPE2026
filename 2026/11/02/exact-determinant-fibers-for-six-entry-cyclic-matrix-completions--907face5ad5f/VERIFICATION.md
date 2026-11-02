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

# Exact checks and boundaries

Run the included standalone program with `python verify.py`. It uses Python's standard library and exact integer or finite-field operations. The order-nine extension is represented as \(\mathbb F_3[\alpha]/(\alpha^2+1)\), with coefficient-pair arithmetic performed modulo three. The squareclass discriminant is computed in the appropriate finite field, not in the integers.

The replay completed with `PASS 4544 six-entry choices; 24128 determinant fibers; 4544 total-count checks`. Counts are obtained independently by evaluating \(\det M(x,y,z)\) for all \((x,y,z)\in\mathbb F_q^3\), then compared to the formula for each target. The program verifies \(\sum_t N_t=q^3\) for every parameter choice. It exhausts nonzero six-tuples for \(q=3,5\), and tests deterministic nonzero six-tuples for \(q=7,9,11\).

Finite execution checks only those fields and parameter choices; the proof applies to all odd prime powers and nonzero prescribed values. No independent scientific audit or external verification was performed.
