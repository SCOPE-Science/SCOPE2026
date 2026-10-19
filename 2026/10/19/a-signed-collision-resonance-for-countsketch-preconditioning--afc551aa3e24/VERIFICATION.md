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

The finite checker `verify.py` is included as a complete standalone source. Execute `python3 verify.py` from the extracted package directory. It uses only Python's standard library. It counts the entire discrete hash/sign sample spaces for 2, 3 and 6 buckets and verifies the exact rank-loss probabilities on and off the tight-frame resonance. It also tests exact determinant identities numerically at two perturbation values and compares the sharp predicted conditional mean pole coefficient against small positive perturbations. A direct Gram-based QR preconditioning calculation checks the transfer of conditioning. All of these finite calculations are secondary checks: the proof in RESULT.md establishes the statements for every bucket size and admissible perturbation direction.

This package has received self-review of correctness, originality and mathematical value. Independent scientific audit has not been performed.
