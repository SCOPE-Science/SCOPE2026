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

# Verification summary

Run `python3 check_cayley.py` alongside the scientific files. The program uses exact integer arithmetic and Python's standard library; its success marker is `CAYLEY_HSTAR_EXACT_OK`. It independently evaluates the published Cayley lattice-slice count and Ehrhart numerator reconstruction for all 192 parameter pairs with \(1\le a\le12\), \(1\le b\le16\), at dilations zero through six, checks the difference polynomial at each, and checks 200 values on the exact ray.

The analytical proof covers unbounded positive integer parameters through polynomial algebra, Descartes's rule and two scaling limits. The finite computations are consistency tests, not exhaustive proofs. Geometric smoothness and regular unimodular flag triangulation are deductions from the stated hypotheses of Ferroni's Propositions 2.2--2.3, not computationally certified properties. Historical originality and the mathematical significance judgment have been examined without external independent review.
