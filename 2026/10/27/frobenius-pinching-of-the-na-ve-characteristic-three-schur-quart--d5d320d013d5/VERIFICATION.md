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

# Verification of the displayed model

Run `python check_schur3.py` with Python 3 and SymPy. The script independently reduces the original and transformed equations modulo \(3\), checks every partial derivative and the global parametrization identity, and enumerates the projective points of \(X\) over \(\mathbb F_3\) and \(\mathbb F_9\). Verified outputs are \(16\) and \(100\) surface points, and \(4\) and \(10\) points on the reduced singular line.

The infinite claims are proved mathematically: absolute irreducibility by Gauss's lemma, the Jacobian scheme by exact derivatives, normalization by the finite birational map from a smooth Hirzebruch surface, and point-count equality by its radicial nature. Finite enumeration alone does not establish a theorem over all finite extensions. No independent external validation has been performed.
