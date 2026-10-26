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

# Reproducible checks

Run `python3 CHECK.py` with the standard Python library. It exhaustively tests the \(806\) rational Grassmannian points \(\operatorname{Gr}(2,4)(\mathbb F_5)\), obtains \(21\) rational lines on the special cubic, partitions them into six through the node and fifteen away, computes their respective tangent dimensions \(1\) and \(0\), and matches the two explicit families.

The mathematical proof, not this finite enumeration, proves geometric completeness over \(\overline{\mathbb F}_5\), the relative degree, flatness, quadratic coefficient order and integral scheme isomorphism. The coefficient identity for the normalized Plücker ratio is derived from the fifth-root formula, and \(t^2+t-1\) has discriminant \(5\). One-model review of these arguments passed; no independent audit or external formal certification is claimed.
