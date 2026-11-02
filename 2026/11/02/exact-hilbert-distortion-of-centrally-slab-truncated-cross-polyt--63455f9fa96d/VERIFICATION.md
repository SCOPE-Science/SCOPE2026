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

The theorem is proved symbolically for every integer \(n\ge2\) and positive real \(\tau\). A standalone exact rational checker is included at `artifacts/verify_slab.py`. Execute `python3 artifacts/verify_slab.py`; the expected output is `CHECK_OK exact_slab_cases= 60 exact_parameter_comparisons= 600`.

The checker enumerates every sign vector for dimensions \(2\) through \(11\), enumerates cross-polytope/slab candidate vertices at six rational parameter choices, tests the proposed optimum and nine comparison quadratic forms, and evaluates the claimed formulas with exact `fractions.Fraction` arithmetic. For dimensions and parameters not checked by the program, the proof's symmetrization, vertex characterization, dual quadratic maximum, and monotonicity argument are the evidence. A finite checker does not independently certify the quantified theorem or historical novelty. No independent audit has been performed.
