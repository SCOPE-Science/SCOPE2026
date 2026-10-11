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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 and no external packages. On the included deterministic inputs the program prints `VERIFY_OK 8054`. The verification checks exact integer determinant volumes of zonotopes built from coordinate segments and two additional arbitrary segments, matching the \(t\), \(s\), and \(ts\) coefficients of the mixed-volume polynomial; it also uses exact rational convolution for the multi-factor product coefficient and tests sharp coordinate-direction witnesses. All its arithmetic comparisons are exact; it is not a formal proof checker.

The mathematical proof is in `RESULT.md`: (i) product supported-normal first-variation identity, (ii) Minkowski-polynomial coefficient comparison, (iii) bound from the factor constants, and (iv) sharpness from concentrated or separated test segments. The finite verifier does not establish surface-area-measure support for general convex bodies, prove the universal planar Bézout inequality, or exhaust arbitrary factor shapes and dimensions. Those premises are supported respectively by elementary convex geometry and the cited planar theorem. Independent mathematical and originality audits have not been performed.
