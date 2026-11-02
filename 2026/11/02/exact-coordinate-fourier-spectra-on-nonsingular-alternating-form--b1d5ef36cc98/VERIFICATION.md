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

# Reproducibility checks

Execute `python3 checks/check_alternating.py` with Python 3. The checker uses only the standard library, enumerates all alternating matrices in four finite prime-field cases, independently selects the nonsingular ones with exact modular Pfaffians, computes 183 character moments from exact integer zero counts, and verifies the universal spectral trace and determinant identities in these cases. The prime-power and unbounded-dimensional conclusions are established by the proof, not by the enumerations.

The exact upper-mode comparison is the sign of \(p(\lambda_2)\), where \(p(z)=(z-1)(z-\lambda_0)-Ea^2\). The proof gives its factorization as \((d-1)[(8-d)V^2-2(d-6)V-(d-4)]/(2U^2V^2)\). The sign is strictly positive at \(d=6\) and strictly negative at every even \(d\ge8\), for all \(q\ge2\). This explicit symbolic identity is the universal certificate; checker logs cannot replace it.

Known limits: only one nontrivial coordinate-frequency label is selected per upper-triangular entry, and all observations use uniform probability measure on the full-rank alternating orbit. The work has undergone self-review only; independent audit and validation have not been performed.
