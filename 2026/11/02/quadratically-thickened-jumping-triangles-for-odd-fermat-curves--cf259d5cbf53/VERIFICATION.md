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

# Reproducibility and limits

Run the provided standalone exact arithmetic checker with:

`python3 artifacts/verify_jumping.py`

The program has no dependencies beyond the Python 3 standard library. It independently assembles the full \(3r\)-by-\(3r\) binary restriction matrix and computes its integer determinant by fraction-free elimination for \(1\le r\le5\) at three pairs of coefficients; it also verifies Gram identities, positive determinant constants and the Chern-class formula for \(1\le r\le8\). The observed final line was:

`VERIFY_OK: 23 exact determinant/Gram/Chern test sets`

The proof for arbitrary \(r\ge2\) is the algebraic binomial-identity and Gram-matrix argument in `RESULT.md`, not the finite checker. No claim of independent mathematical validation or exhaustive computational proof is made. Characteristic zero and the canonical first determinant jumping divisor are essential scope conditions.
