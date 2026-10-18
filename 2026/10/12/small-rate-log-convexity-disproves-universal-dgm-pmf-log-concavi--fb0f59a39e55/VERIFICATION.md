---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For p_z=S_z-S_{z+1}, under alpha=eps*a, theta=eps*b, exact one-step hazard eps(a+c r^z) with r=e^mu>1, c=b(r-1)/mu>0, so fixed-index p_z=eps(a+c r^z)+O(eps²); the log-concavity determinant has leading term -eps²*a*c*r^(z-1)*(r-1)^2<0. For each fixed m the finite intersection of small-eps intervals proves strict log-CONVEXITY on indices 1..m; this does NOT assert a uniform infinite-prefix eps. Independent 65-digit decimal calculations from S_z=exp(-.01(z+2^z-1)) yielded p0=.01980132669, p1=.02896924881, p2=.04639200646, determinant=-.0000794058995773977, ratio=.91355988721917, verifying a genuine counterexample to the unrestricted theorem. Source checker inspected but the asymptotic is the proof, not numerical evidence.

## originality

PASS

PASS: The primary 2025 DGM paper's Theorem 1 states universal PMF log-concavity for all positive alpha,theta,mu; Appendix A computes survival-sequence curvature and incorrectly transfers it to the PMF, with its stated (A.2) not algebraically equivalent to PMF log-concavity. A derived strict negative PMF determinant is incompatible with that theorem rather than a reformulation of it; targeted Resultary/publication searches did not locate a previous published low-rate counterexample. Generic continuous reliability log-concavity results do not imply the disputed discrete first-difference assertion. A later unindexed correction remains possible.

## value

PASS

PASS: A systematic low-rate OPEN REGION of counterexamples refutes a stated theorem used to claim PMF structural log-concavity in a recent named statistical distribution; the analytic determinant and arbitrarily long finite initial log-convex segments expose the precise invalid inference, not an unmotivated numerical quirk. Consequences for separate IFR, inferential fits or unimodality were NOT claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
