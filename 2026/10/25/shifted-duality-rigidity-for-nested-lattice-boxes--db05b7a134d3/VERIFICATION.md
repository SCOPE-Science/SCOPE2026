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

The proof derives the eventual translation-count formulas by independent coordinate counting, compares the normalized polynomial root multisets, and uses the bounds on the roots given by containment. The classification and nonnested witness follow as stated in RESULT.md.

The standalone file `proof_check.py` performs exact rational root comparisons across nested boxes through dimension four and independent brute-force translation enumeration on small boxes. It must be run with Python 3 (standard library only): `python proof_check.py`. Finite checks supplement but do not replace the full proof. Independent audit has not been performed.
