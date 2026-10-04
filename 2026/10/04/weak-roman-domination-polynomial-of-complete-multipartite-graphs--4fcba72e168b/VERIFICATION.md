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

The standalone `verify.py` implements two definitions independently: the literal weak Roman transfer rule, and the structural criterion stated in RESULT.md. For every ordered composition \((n_1,\ldots,n_r)\) of every total order \(2\le N\le8\) with \(r\ge2\), it enumerates all \(3^N\) vertex labelings and requires the two predicates to agree. It also constructs the coefficient vector of the displayed polynomial from the part sizes and compares it with the brute-force weight histogram.

The actual packaged replay returned `VERIFY_OK graph_profiles=247 labelings=997929 coefficient_checks=3761 max_order=8`. The finite exhaustive check does not prove the arbitrary-order theorem; the general proof is the support-structure argument in RESULT.md.
