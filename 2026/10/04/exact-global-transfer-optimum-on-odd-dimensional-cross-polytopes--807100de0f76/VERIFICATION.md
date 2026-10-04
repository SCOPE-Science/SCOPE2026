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

`verify_cross_polytope_optimum.py` constructs each cocktail-party adjacency matrix directly and compares its antipodal transition amplitude with the closed formula.

For several sizes with
\[
N=4k+2,
\]
the script checks the predicted optimum
\[
\cos^2(\pi/N),
\]
the source-time value
\[
(1-2/N)^2,
\]
the two attaining times, and the deficit identity used in the proof.

It also performs a dense full-period scan as a numerical cross-check. The scan is not used to prove global optimality; the trigonometric argument in `RESULT.md` supplies that proof.

No independent audit has been performed.
