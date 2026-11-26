---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The five placement orbits exhaust the two-element sets, including at m=3. I reproduced the displayed minimum and all four gap identities symbolically, by a log-determinant calculation independent of the equitable quotient. For each clique with r pins let d_i=m+t+κ1_{i pinned}, P=∏d_i, f=1−Σ1/d_i and h=1/d_hub. The shifted clique determinant is Pf and its hub cofactor is Ph(f+h). The bridge is one rank-one update, so the full shifted determinant is the product of clique determinants plus the two products of one determinant and the other clique's hub cofactor. This polynomial identity handles an unpinned clique without dividing by its singular Laplacian at t=0. The derivative of the full log determinant at t=0 is the inverse trace. All four verified gaps are strictly positive for m≥3 and κ>0. The covariance normalization divides the trace by two and does not change the optimizer.

## originality

PASS

The supported distinct result is the strict optimizer classification and exact minimum at every finite positive gain for the balanced unit bridge barbell. Neither the general formulation nor the bridge-barbell results inspected establish the finite-gain inequalities. The perfect-pinning overlap is expressly excluded from the originality credit.

## value

PASS

The bridge endpoints are natural candidate leaders on this dense bottleneck graph. The exact strict classification shows that both endpoints are inferior at every positive gain, not merely in a hard-pinning asymptotic or at selected parameters. The positive gaps and minimum give an explicit placement benchmark without minimizing a general formula case by case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
