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

# Reproducibility and verification

Run `python3 check_biclique.py` with Python 3 and the standard library. The completed check reported `PASS: 136524 exact-rational assertions`. It enumerates all cut-size pairs on specified finite bicliques and independently evaluates the three graph-ball averages. It also checks the strict and quantitative bounds for rational one-sided data and both exact threshold factorizations over a larger integer grid. No external datasets or packages are required.

The proof, not enumeration, establishes the full quantified claim. In particular, numerical or finite rational experiments cannot establish the all-order statement by themselves. The global edge-variation norm over inputs simultaneously nonzero on both bipartition classes is not proved. Publication priority against inaccessible older full texts remains open. No independent scientific audit has occurred.
