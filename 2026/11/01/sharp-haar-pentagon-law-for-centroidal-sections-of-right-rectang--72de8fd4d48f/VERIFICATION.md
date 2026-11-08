---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Reconstructed apex/base signed-height geometry centered at G=(0,0,h/4). For generic oriented n_z>0, section has five vertices iff exactly one of four base vertices has positive height. Each disjoint one-positive sign event is one trivariate Gaussian positive orthant with equal squared normal length S=4a²+4b²+h²; correlations 8a²/S-1, 8b²/S-1, 2h²/S-1. Gaussian arcsine sign formula gives P5=(4/pi)∑asin(sqrt(p_i))-2, where p=(4a²,4b²,h²)/S. For x>y>0, x+y<1, derivative balancing strictly increases ∑asin(sqrt p_i), giving unique optimum p_i=1/3, i.e. a=b,h=2a; positive orthant gives P>0, boundary gives unattained infimum 0. Independently enumerated crossing edges for Gaussian normals for 40,000 directions each for (a,b,h)=(1,1,2),(1,2,3),(1,1,0.1); frequencies agree with formula to sampling precision, not proof.

## originality

PASS

Best-of-knowledge comparison of exact final claim against primary mathematical statements and published semantic records; no inspected result covers it. Source access and residual uncertainty are documented, not construed as certainty of novelty.

## value

PASS

A natural geometric probability law for Haar sections through a polytope centroid, including full anisotropy and a unique optimal aspect/height. Distinguishes sections from better-studied shadows, with exact global shape optimum; potentially useful for stochastic convex geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
