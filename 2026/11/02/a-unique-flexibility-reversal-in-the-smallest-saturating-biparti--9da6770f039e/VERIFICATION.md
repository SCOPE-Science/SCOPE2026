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

# Reproducible exact verification

Run `python3 verify.py` in the folder containing `verify.py` and `bernstein_certificate.json`. Only the Python standard library is required. The program independently computes matching cardinalities for all 16 four-edge graphs and all 512 nine-edge graphs by a subset dynamic program and by maximizing over vertex permutations. It then expands graph-state probabilities into exact integer-coefficient expectation polynomials, verifies both theorem factorizations, independently generates all 45 degree-eight derivative certificate coefficients, checks the two zero coefficients and 43 positive ones, and performs supplementary exact-rational boundary checks. Expected successful output begins with `PASS: K2=16 graphs and K3=512 graphs`.

The universal result rests on the exact graph-state expansion and the strictly positive homogeneous polynomial certificate, not on any finite parameter grid. No independent verification, formal theorem-prover certificate or external scientific audit is represented by this document. The theorem's interpretation requires the *saturating* edge-probability convention: the probability for two flexible endpoints stays \(q\).
