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

# Verification notes

Run `python3 verify.py` with Python 3.8 or later; no third-party dependencies. The checker independently constructs all vectors in the selected finite fields, computes wedge products from coordinates, and exhaustively compares all noncentral patterns of pairwise-commuting matrices. The checked cases are field size \(2\), tuple lengths \(1,2,3,4\), and field size \(3\), tuple length \(2\). Expected full counts: \(64\), \(1024\), \(12160\), \(138496\), and \(41553\). The checker also compares explicit off-diagonal matrix products for all \(1024\) ordered noncentral matrix-pair patterns over \(\mathbb F_2\).

This is a bounded exact finite-field test. The classification of irreducible components for arbitrary length and characteristic depends on the proof in RESULT.md, especially irreducibility of the incidence quadric, properness of Grassmannian projection, and the exceptional two-tuple degeneration. The test does not certify algebraic-geometric irreducibility or historical uniqueness. Independent audit has not been performed.
