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

Execute `python verify_nested_stability.py` with Python 3; it uses only the standard library. Its completed tests produced:

- PASS: 144 direct Hamiltonian enumeration comparisons for connected one- and two-spin flips.
- PASS: four critical exact finite-window order probabilities (the fifth follows from the same routine).
- PASS: three exact covariance constants.
- PASS: complete enumeration of all \(9!\) cyclic orderings to check the finite-volume covariance matrix.

The analytic integrals and the finite-dependent central limit theorem prove the all-size and asymptotic claims, respectively. Permutation enumeration alone does not prove an infinite-family result; no external or independent audit has been performed.
