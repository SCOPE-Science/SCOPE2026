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

# Reproducibility

Execute `python verify.py` with Python 3 (standard library only). It uses the irreducible polynomial \(t^3-t-1\) over \(\mathbf F_3\) and \(t^3+t+1\) over \(\mathbf F_2\), reconstructing the rational curve points and the rational secant lines directly. The tests cover all 729 affine nonvertical rational lines in the first field, all 117 maximal three-secants, 13 parallel spreads, eight switched spreads, all 28 characteristic-two secants over \(\mathbf F_8\), and all 4725 distinct minimum line covers classified by finer incidence patterns. The expected output is two lines beginning `VERIFY_OK`.

The verifier demonstrates finite-field instances only. For all extension degrees, the proof relies on a gcd identity for multiplicative groups, the affine first-moment identity in odd characteristic, and a complete matching enumeration in characteristic two. No unperformed independent audit or computational infinite proof is asserted.
