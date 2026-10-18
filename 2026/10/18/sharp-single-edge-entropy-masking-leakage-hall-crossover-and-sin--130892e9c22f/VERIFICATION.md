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

The accompanying `verify.py` needs Python 3 and NumPy (version 1.20 or later). Run `python verify.py` from the extracted package directory. The verifier generated 8,467 PASS checks on exact rational balanced cases, randomized transport plans for 2–7 rows and columns, positive entries, both sets of marginals, the exceptional-cell odds identity, full-whitened singular values, Jacobian eigenvalues, non-gauge contraction bounds, independent finite differences of the complete row/column iteration, the hard-mask total variation identity, strict Hall-slack formulas and matched boundary-layer limits.

The proof of the infinite-dimensional-range statement (arbitrary *finite* matrix sizes), all real positive parameter ranges, sharpness, and uniqueness of extremizers is analytical in RESULT.md. Finite checks do not prove universal mathematical statements, publication priority, numerical conditioning in finite precision, global iteration complexity, or results for multiple prohibited edges.

Scientific review is same-model only. Independent audit is not performed.
