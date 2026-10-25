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

# Reproducible arithmetic checks

Run `python3 verify_dyadic_richardson.py` with Python 3 standard library. Expected terminal marker: `VERIFY_OK`.

The code verifies the unique mandatory length-eight subword for the chosen \(S_8\) interval; all \(2^{12}=4096\) fixed points and all \(12\cdot2^{11}=24576\) intrinsic-torus invariant edges; the equality of opposite tangent characters at endpoints; the character-vector identity \(S(b)-S(b')=(-K_X\cdot C)\chi\) component by component in \(\mathbb Z^8\); the full histogram, per-coordinate multiplicities, and a negative-degree witness.

The geometric inputs (smooth toric Richardson structure, skew-sub-Bott–Samelson charts, cube combinatorics) are cited primary theorems and are not independently re-proved by enumeration. Independent mathematical audit is not performed. Exhaustion applies to the stated finite edge set, not to a family of all dimensions.
