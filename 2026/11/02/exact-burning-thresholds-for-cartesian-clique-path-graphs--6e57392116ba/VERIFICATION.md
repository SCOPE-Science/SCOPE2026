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

A self-contained Python 3 verifier accompanies the proof as `verify.py`. Run it with `python3 verify.py` from the extracted package. It checks explicit burning source constructions across 236 width-and-horizon cases, independent exact subset-cover recursion for 30 small graph instances, and 891 interval endpoint-overlap budget instances. The observed output was `VERIFY_OK 236 constructive infinite-family witness samples; 30 independent exact burning instances; 891 endpoint-budget instances`. It uses only the standard library.

All nontrivial steps of the infinite proof are mathematical: exact Cartesian graph distances; the interval-length sum; a pointwise charging bound for tips beside unfilled columns; sharp three-row and higher-row consequences; and constructive coverings. Finite tests cannot establish the general claim and are not invoked as its proof.

The prior-art comparison used the accessible original 2024 arXiv full-text HTML and indexed original 2018 product-paper material, with explicit retrieval limitations noted. Publication priority and independent mathematical validation are not certified.
