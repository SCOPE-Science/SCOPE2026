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

Run `python3 verify.py` with Python's standard library. The expected deterministic output is `VERIFY_OK 5390 exact-rational assertions`.

The checker uses exact `fractions.Fraction` polygon clipping for the centered triangle \(\operatorname{conv}\{(-1,-1),(2,-1),(-1,2)\}\). It tests four scales \(r\in\{1/8,1/4,1/3,1/2\}\) and every coefficient triple \((a,b,t)\in\{-5,\ldots,5\}^3\) for the halfspace \(ax+by+t(i-1)\ge0\). It then tests explicit equality halfspaces, the planar normalized-mass identity, and exact barycentric threshold and positivity calculations for dimensions \(2\le d\le30\). Every individual arithmetic assertion is rational; the resulting finite check does not prove a universal statement.

The proof's universal coverage depends on two facts independent of the checker: excluded lower-slice points reflect into included upper-slice points under \(-rK\subseteq K\); and arbitrarily steep ambient halfspaces isolate a desired planar cap on any chosen slice. Those facts establish both directions of the exact depth formula. The simplex corollary additionally invokes the standard Grünbaum centroid theorem. No independent mathematical audit or certification has been carried out.
