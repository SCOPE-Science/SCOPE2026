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

# Reproducibility and proof boundary

The accompanying `verify.py` requires only Python 3's standard library. Invoke `python3 verify.py`; a successful run ends with `VERIFY_OK` and identifies the exact exhaustive configuration counts. Reproduce the mathematics from the full derivation in `RESULT.md` and the independent-parent construction in arXiv:1906.08806, Section 2.2.

The checker enumerates all eligible parent-choice tuples for orders 3 through 7, and checks exact rational finite-sum identities and strict mean-influence ordering through order 120. The symbolic proof is needed for every larger order, the conditional stochastic coupling and the variance/correlation limits. This is not independent audit evidence.
