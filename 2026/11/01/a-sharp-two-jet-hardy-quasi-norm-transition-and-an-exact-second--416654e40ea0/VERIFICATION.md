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

# Reproducibility and scientific limits

Run `python3 checker.py` using the Python standard library. The checker verifies exact rational contact, the pure-second-coefficient endpoint, numerical normalization and coefficient identities for each explicit analytic extremizer, 5,500 reproducible complex-coefficient competitors, and fixed-origin frontier sample evaluations. The exact mathematical proof uses the external outer-extremizer theorem [1], fourth-root reduction, Parseval, equality in the triangle inequality and exact one-variable calculus; no finite checks are substituted for those steps. The terminal first-coefficient identity relies on published Theorem 12 [3]. All admitted parameters, boundary inclusions and unproved extrapolations are stated in `RESULT.md`. No independent review is claimed.
