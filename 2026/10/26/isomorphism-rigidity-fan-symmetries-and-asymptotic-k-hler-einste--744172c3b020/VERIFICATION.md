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

# Verification scope

Reproduce with `python3 verify.py` (Python standard library). The checker explicitly enumerates all zero-sum six-root multiplicity vectors for base lengths \(2\) through \(14\), takes orbits under all twelve root-hexagon symmetries and compares with the unique normal-form parameters. It also compares exact coefficient arrays of the three rational generating functions through length \(99\) and prints sample full fan-symmetry group orders.

The universal classification, symmetry group description, generating series and asymptotic are established by the proof in `RESULT.md`. Finite enumeration cannot certify all dimensions or historical originality. The Fano, tangent stability, and Kähler–Einstein inputs are from Wuebben, arXiv:2608.20411v1, and are not independently reproved. Independent audit has not been performed.
