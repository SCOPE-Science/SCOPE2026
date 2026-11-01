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

Run `python3 verify.py` with standard Python 3.9 or later; no external packages or downloads are required. The checker constructs the graph from the three-hub definition, enumerates every subset, calculates induced connected-component orders, builds augmented simplicial boundary matrices over \(\mathbb F_2\), and computes reduced homology in all dimensions. It compares those ranks with the two closed binomial formulas for every \(1\le a,c\le4\), \(1\le r\le a+c+3\). The observed output is `VERIFY_OK 128 parameters 54249 face instances 5 mixed-degree instances`.

These exhaustive finite cases are evidence of consistency, not a certificate for infinitely many parameters or for torsion-freeness. The mathematical proof in RESULT.md establishes the unrestricted integral homotopy equivalence. The cited 2020 double-star classification is an invoked prior theorem; this checker does not reprove it. Scientific originality remains subject to unindexed literature, and independent validation has not been performed.
