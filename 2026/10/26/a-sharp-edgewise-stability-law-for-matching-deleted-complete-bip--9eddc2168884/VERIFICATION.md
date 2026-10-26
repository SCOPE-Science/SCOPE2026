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

# Verification

The standalone `checker.py` uses only the Python 3 standard library. From the present package's directory, run `python3 checker.py` to reconstruct the orthogonal edge-gradient projector by grounding one vertex and exactly inverting the incidence Gram matrix over rational numbers. It does not use the claimed projection formula to compute the test matrix.

The recorded run passed **123,977 exact-rational assertions** for all \(3\le n\le9\) and \(0\le t\le n\). It checks the kernel, every row sum, three row-type norms, the maximum row sum, a sign-vector sharpness witness, strict deletion monotonicity and the exceptional terminal-step ratio.

The all-parameter proof is the algebraic argument in RESULT.md. The finite check is supporting evidence only. Historical priority has not been independently certified; the claim remains restricted to unweighted balanced bicliques with a deleted matching. No independent audit has been performed.
