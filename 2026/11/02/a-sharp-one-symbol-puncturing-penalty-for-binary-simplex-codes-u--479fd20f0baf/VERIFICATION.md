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

# Verification and boundaries

Run `python3 verify.py` with Python 3.8 or later. No external dependencies are required. A successful run prints degree-by-degree nonzero pair-weight histograms and ends with `VERIFY_OK`.

The checker verifies the construction, the claimed difference-color multiset, exact enumerators and bounds for field degrees \(3\) through \(8\); it exhaustively enumerates all \(720\) cyclic coordinate lists in dimension three, finding \(96\) with optimum distance \(5\). Field generator polynomials are specified in the source and checked for a full multiplicative cycle before use. The all-degree proof is combinatorial and does not rely on the finite range of the checker.

Historical originality comparison uses the published full-text material listed in the scientific review, together with limited-access summaries of further work. This is not independent validation or external certification. Only two-symbol cyclic reads and one punctured column are addressed.
