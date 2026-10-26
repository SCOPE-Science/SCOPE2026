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

# Reproduction notes

Run `python verify.py` with a conventional Python 3 interpreter; only standard-library modules are imported. It compares the two double compositions, tests the exact algebraic formula at rational values, uses 85-digit decimal arithmetic to bisect both level-set roots and invert the strictly increasing baseline map, and checks 3,000 seeded parameter draws. Observed initial-stock thresholds were approximately \(0.20055782314646192476\) and \(0.87699149923997316002\); all programmed checks completed successfully.

The analytical uniqueness theorem follows instead from the strict unimodality of the derivative of the quadratic saturating recycling law; finite random tests cannot establish this theorem or comprehensive originality. A fully independent mathematical review has not been performed. The calculation has no hidden data, network, or non-standard software dependencies.
