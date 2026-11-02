---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

Finite product calculations give K_ij= -a_max(i,j) where a_j=1/j-sum_{k=j}^n 1/k^2 is strictly increasing and has zero sum. Absolute row sums have one valley, so their maximum is at an end; exact comparison R1>=Rn (strict n>=3) identifies first-row maximum and the sign-step extremizer, yielding 2m sum_{k=m+1}^n 1/k^2. Euler-Maclaurin applied to b_j=sum_{k=j}^infty 1/k^2-1/j yields m=sqrt(n/2)+O(1) and expansion 2-2sqrt(2/n)+2/(3n)+O(n^-3/2). Infinite J_ij=b_max>=0 has endpoint row norm exactly 1; K_n=P_n J P_n - tau_n 11^T, n*tau_n->1. Independent exact rational finite checks n=2..50 confirmed first row and kernel and read actual checker; asymptotics rely on analytic proof.

## originality

PASS

Classical infinite Cesàro operator theory, hyponormality and essential normality are old, and recently published self-commutator results study Hilbert spectral/weighted quantities. The specific finite-section induced infinity norm, discrete sharp sign-switch and rank-one endpoint doubling are not established by those results.

## value

PASS

A sharp all-size finite operator norm with explicit extremizer and a noncommuting finite-section/infinite-commutator limit, illustrating a mathematically significant boundary effect in a classical operator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
