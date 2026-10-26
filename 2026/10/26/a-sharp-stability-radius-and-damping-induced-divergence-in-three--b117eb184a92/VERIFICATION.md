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

# Computational and analytic verification

Unpack the standalone files into one directory and execute `python verify.py` with Python 3 and the `sympy>=1.12` dependency stated in `requirements.txt`. The verifier checks the exact polynomial resolvent identity, symbolic elimination resultant, Descartes substitution, rational root bracket, exact rational expanding matrix, and a small regression grid.

The proof's universal radius classification is **not** inferred from that grid. It rests on explicit norm and sign formulas, compactness of the angular parameter interval, a resultant that captures every possible first interior contact, and Descartes' rule proving uniqueness of the contact radius.

No third-party certificate or independent validation is asserted. The value \(0.940521095740431\ldots\) is a decimal approximation to the precisely defined root, and the example's matrix identity uses exact arithmetic in \(\mathbb Q(\sqrt5)\).
