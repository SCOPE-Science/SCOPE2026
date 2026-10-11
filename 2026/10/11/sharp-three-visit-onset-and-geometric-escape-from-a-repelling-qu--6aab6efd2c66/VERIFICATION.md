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

# Scientific verification notes

The exact nonstandard step is the inverse trapping of the entire three-visit polygon. In centered coordinates, \(-u+v<\beta<2\alpha\) establishes the first inverse-quadrant inequality. Combining \(-u+v<\beta\) and \(u<\beta/2\) gives \(u+v<2\beta\), which establishes the second. This argument is strict and uniform for every real \(b>1/2\); it does not depend on finite tests.

The sharpness witness \((u,v)=(\alpha,\alpha+\beta)\) lies on the closure of the two-visit set but has inverse second coordinate \(-\alpha-\beta/2<-\beta\). Continuity gives interior witnesses, so no spurious endpoint convention affects the sharpness conclusion. Both area branches are obtained by exact one-variable integration of polygonal widths. The geometric exit law is a consequence of actual nested-set area ratios, not of an assumed independent-trial model.

Run `python check_exact.py` using standard Python. The checker uses `fractions.Fraction` to clip initial squares against every half-plane defining a finite survivor polygon. It tests exact polygon vertices under inverse similarity and exact area identities for seven rational parameters, up to eleven visits. Its output on success is `Q2_EXACT_RATIONAL_POLYGON_CHECK_OK`. Tested cases support the proof but cannot establish continuous parameter coverage or arbitrarily many iterates.

All source comparisons are at the scientific statement and implication level. The pre-existing qualitative repeller and graph results are attributed; no external validation or publication-priority certification has been obtained.
