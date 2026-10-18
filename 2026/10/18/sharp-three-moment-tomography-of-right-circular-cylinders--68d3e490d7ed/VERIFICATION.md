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

The proof uses exact spherical integrations and a cubic divided difference on the two possible roots of a quadratic moment equation. Its decisive sign certificate is \(Q(22/7)=-104/2401\) for \(Q(z)=z^4-6z^3+4z^2+36z-64\), together with \(Q'(3)=6\), \(Q''(z)>0\) for \(z\ge3\), and \(3<\pi<22/7\). These imply a negative discriminant for the third-moment divided-difference quadratic.

Run `python verify.py` in this directory; Python 3 with SymPy and mpmath is required. The script checks the exact polynomial identities, 25 high-precision numerical integrations of all three moments, and one positive-dimensional example where two cylinders share the first two moments but not the third. The algebraic theorem does not depend on numerical sampling.

The original derivation of the full cylinder width law is due to the cited 2026 source. The new finite-moment bound does not claim independent historical priority certification. No outside audit or validation has been conducted.
