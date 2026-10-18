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
# Verification

Running `python3 verify.py` confirms by exact integer arithmetic: the original Apéry binomial definition against the binary residue formula for indices through 239; the complete eight-state transition and its matrix polynomial annihilator; that all 24 proposed residue words are distinct and exhaust finite enumerated words; the exact dyadic cell formula at exponents up to 21; and convergence-compatible finite counts. The mathematical proof in `RESULT.md` establishes the infinite assertions. These finite tests neither imply infinite density nor certify originality.
