---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The M-matrix resolvent has nonnegative entries and the Cayley formula gives C=2R-I. Walsh eigenvalues 2 sum_{j in J} a_j yield a common diagonal return F_a(s)=E[1/(1+2s sum a_i X_i)], strictly falling from 1 to 2^-d<1/2. The positive-definite Hessian (singleton Bernoulli events) makes F strictly Schur-convex, so s_* follows the strict majorization order and the equal and capped-extreme configurations are the unique fixed-budget extremizers. Leave-one-out binomial convex order proves Theta_d strictly decreases toward 1, centered-moment expansion gives 1+1/(2d)+5/(8d^2)+O(d^-3), and the two-branch Bernoulli decomposition proves the epsilon^-1/2 singular coefficient. Independently checked exact d=2 cubic and its positive roots.

## originality

PASS

The published reversible-generator result already proves the general diagonal-resolvent positivity test, which is credited and included as a prior implication. It does not optimize the crossing over weighted-cube directional rates or compute the strict anisotropy comparison and two sharp limits. The 1993 hypercube spectral-majorization paper is a close thematic predecessor but its accessible abstract concerns Hamming-distance spectra; full access was blocked, leaving residual priority risk. Best-of-knowledge PASS for comparative rate law and asymptotics.

## value

PASS

A quantitative design principle for a natural product diffusion graph: at fixed total conductance greater anisotropy provably relaxes the sharp positivity time step despite fixed top eigenvalue. Dimension growth and nearly disconnected rate-floor limits expose nontrivial numerical-analysis boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
