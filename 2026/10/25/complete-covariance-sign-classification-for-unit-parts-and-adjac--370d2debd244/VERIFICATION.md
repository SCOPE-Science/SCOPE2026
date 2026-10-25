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

The proof uses an exact coefficient identity for the covariance, not numerical extrapolation. The standalone standard-library verifier independently enumerates all compositions for \(n\le18\), checks first- and mixed-moment formulas, and compares the coefficient identity through \(n=140\). It reports 19,745 successful exact assertions. Run `python verify_composition_covariance.py`.

These finite checks do not prove the unrestricted theorem; the formal-series derivation and coefficient monotonicity in `RESULT.md` do. No independent mathematical audit or historical-priority validation has been carried out. The complete text of one relevant 1998 source was inaccessible; consequently priority remains subject to further review.
