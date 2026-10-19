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

# Verification record

The standalone script `verify_elliptic.py` was run with Python 3 and SymPy and completed successfully. It checks exact rational identities for the invariant quadratic form, the original six-by-six word-return matrix, both intermediate bisection edge-length vectors, two Gram leading principal minors and determinant, and the algebraic threshold/contact. It also checks four finite rotation samples: \(q=1.5\), \(q=63/32\), \(q=1.975\), and \(q=2\), using 180000 iterates each and a tolerance of \(0.0009\) for comparison with the analytical forbidden-frequency formula.

The exact geometric proof, not the numerical samples, establishes both the infinite-orbit and the frequency claims. The verifier requires no downloaded papers, hidden inputs, private tools, or other files. The source paper's formulas have been transcribed into the code for independent algebraic checking; no external formal proof certificate or independent audit is asserted.
