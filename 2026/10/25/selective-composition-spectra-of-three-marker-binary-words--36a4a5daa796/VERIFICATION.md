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

## What was checked

Running `python verify.py` with Python 3 and no third-party dependencies verifies, by literal occurrence enumeration, the claimed two-class profile for partial layers with zero and three ones, and injectivity after adding the one-one layer, for every weight-three binary word of length \(3\le n\le24\). It also checks explicit ambiguity witnesses and the separate historical weight-four full-spectrum ambiguity example. The expected success report counts exactly 12,650 weight-three strings.

## Proof boundaries

The finite check does not prove the infinite theorem. Infinite correctness rests on the zero-run histogram inversion, outer-gap retrieval from \(G_aG_d\), and the nonvanishing product identity in the proof. The absence of observed equalities in limited searches is not an originality certificate. Independent validation has not been performed.
