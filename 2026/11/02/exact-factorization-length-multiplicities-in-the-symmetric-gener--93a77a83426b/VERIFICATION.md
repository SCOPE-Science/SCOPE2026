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

# Reproducibility

Execute `python3 verify.py` in a directory containing the standalone script. It computes length *multiplicity* profiles from the formula and independently by iterating all admissible nonnegative coefficient triples for each chosen target. It also verifies the arithmetic properties required by the proof, the zero-target case, and small gap cases. The successful finite tests are a consistency check; the general assertion is justified by the algebraic proof in RESULT.md. The test requires Python 3 standard library only; no external database or software dependency.

The exact proof hinges on the inverse bijection between all factorizations and reduced two-coin solutions, as explained in RESULT.md. The independently audited status remains unperformed.
