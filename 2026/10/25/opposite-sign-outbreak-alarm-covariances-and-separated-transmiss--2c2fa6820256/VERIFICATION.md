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

# Reproducibility

Run `python verify.py` in the same directory, with Python 3 and no third-party packages. It constructs each finite edge-state/source mixture with `fractions.Fraction`, checks all four analytic moments, verifies the exact four-vertex opposite-sign covariances, and tests sample polynomial identities. The deterministic output is preserved in `certificate.json`.

The checked range is stars with 2–8 leaves and six rational probabilities per size (42 cases, 24,552 weighted source/edge possibilities). Additional rational sign samples cover 2–1000 leaves. These samples do not establish uniqueness of real roots, the all-parameter sign ordering, or either asymptotic theorem: the proof of those facts is entirely analytical in `RESULT.md`.

There is no independent audit, external proof certification, or claim of results outside this independent-bond, single-uniform-source model.
