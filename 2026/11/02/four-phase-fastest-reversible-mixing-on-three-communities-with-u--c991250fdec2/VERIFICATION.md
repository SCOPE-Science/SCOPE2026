---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The centered reversible operator norm is convex, and group averaging over within-class permutations and A/B swap preserves all constraints, proving symmetric-flow minimization gives the unrestricted minimum. Explicit invariant eigenspaces give internal u=1-(x+y)/a and v=1-2y/g, antisymmetric w=1-(2x+y)/a, quotient z=1-y/(ag), with feasibility x,y>=0, x+y<=a,2y<=g; m,r>=2 ensure all eigenvalue types appear. For fixed y, max(u,|w|) is bounded by (a-y)/(3a), attained at x=2(a-y)/3. The remaining exact scalar maximum of (1-gt)/3,1-2at,|1-t| on bounded t=y/(ag) yields four analytic branches and canonical flows. Checked the optimizer and thresholds independently by rational LP search for 63 masses and source exact matrix/eigenvector script. The nonnegative aggregate-flow averaging argument supports universal edge absence, but does not imply uniqueness of all nonsymmetric optima.

## originality

PASS

Best-of-knowledge original exact two-equal-class-mass tripartite phase diagram and universal support thresholds. Convex SDP, symmetry averaging and uniform-stationary complete multipartite block decomposition are prior art, but do not supply these biased class-mass formulas.

## value

PASS

Fastest reversible mixing with a fixed *nonuniform* stationary law is a natural optimization problem. The mass-dependent closed form classifies which spectral constraint is active and gives sharp forbidden/optional/forced intercommunity support transitions, information not supplied by the general SDP formulation. This is a motivated exact phase diagram, not merely a numerical optimizer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
