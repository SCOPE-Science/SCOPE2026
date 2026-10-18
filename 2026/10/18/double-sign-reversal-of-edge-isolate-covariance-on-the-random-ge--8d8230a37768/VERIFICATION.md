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

# Mathematical verification

The proof in `RESULT.md` establishes the identity for every integer \(n\ge2\) and radius \(0<r<1/2\). The crucial conditional geometric step is reproducible directly: for an isolated tagged point all remaining points lie independently on its complementary arc of length \(a=1-2r\), and a conditional pair-edge probability equals \(1-(1-r/a)^2\) when \(r\le a\), or one otherwise.

Run `python verify_edges_isolates.py` using Python 3's standard library. The script performs exact-rational identity/sign tests for \(n=2,\ldots,40\) over \(99\) rational radii in the interval \((0,1/2)\), and independent-seed Monte Carlo comparisons for six representative parameter pairs. Both collections passed upon preparing this package. The Monte Carlo error and finite parameter grid are only diagnostics, not a general proof or a full enumeration of continuously many radii.

No independent audit has been performed; source-text comparison may not exhaust inaccessible literature.
