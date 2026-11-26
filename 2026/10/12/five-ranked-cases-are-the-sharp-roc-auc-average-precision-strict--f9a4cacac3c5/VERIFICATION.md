---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For 0<P<N, AUC counts correctly ordered positive-negative pairs divided by P(N-P), and classical AP averages the prefix precisions at positive ranks. These are exactly the two quantities in the frozen proof; neither tied scores nor interpolated PR area is used. A fresh exhaustive calculation using direct pair counts and prefix precisions compared 1, 6, 27 and 110 unordered same-prevalence ranking pairs at N=2,3,4,5. It found no disagreements through 3, just 0110 versus 1001 at 4 (AUC 1/2 for both; AP 7/12 and 3/4), and exactly the two strict reversals at 5: 01100 versus 10001 (AUC 2/3 and 1/2; AP 7/12 and 7/10) and 01110 versus 10011 (AUC 1/2 and 1/3; AP 23/36 and 7/10). The one-class cases do not have ordinary ROC-AUC and are excluded. Reproduce with python3 /workspace/branches/independent_checks.py 2; the uploaded script was inspected, not run.

## originality

PASS

The supported distinct claim is the fixed-prevalence, no-ties boundary and its first-layer classification for empirical AUROC and classical discrete AP, not the known general phenomenon that ROC and PR criteria can disagree.

## value

PASS

This gives a minimal controlled test case for two standard ranking measures: a test of whether the measures actually prefer opposite rankings must use at least five cases, whereas a test of tie behavior needs only four. Exhausting the first strict layer separates the effect of redistributing positive ranks from prevalence changes and makes both witnesses useful as exact metric sanity checks. The contribution is small but the boundary is natural, not an arbitrary instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
