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

The analytic proof evaluates the complete fiber at \(x=t=0\). The two rows indexed 1 and 2 have identical entries \(c(b)=2-3/b\) on \(11/4\le b\le13/4\), while the initial top-left entry differs by \(|b-3|/b\). This proves rank two except at \(b=3\) (rank one). A single deficient continuous fiber excludes any positive lower frame bound by the standard rational-density Gabor criterion.

Run `python checker.py` with the Python standard library to independently reconstruct the finite periodization matrix using exact fractions at 406 rational values inside the interval, including its boundaries, and at two points outside. The finite check cannot prove the statement for every real parameter; the interval inequalities in RESULT.md perform that step.

Scientific limits: no claim of the globally optimal non-frame interval, no generalization to other windows, and no independent audit has been performed.
