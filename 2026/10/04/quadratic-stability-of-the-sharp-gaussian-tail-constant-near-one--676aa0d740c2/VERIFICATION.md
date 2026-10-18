---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For |R|<=r=sum_{j>1}|a_j|, conditioning on R gives P(|a1*U1+R|>t)=1-t/a1 whenever 0<t<a1-r: exactly flat uniform density on all shifted central intervals. The coupling sup difference from U1 is <=|1-a1|+r and compact support plus positive Q(t) localize ALL global maximizing cutoffs near the source’s unique t0 as r→0. Within that plateau, F=(a1-t)/(a1*Q(t)) and the sign of derivative is a1-t-h(t), with (t+h(t))’=3t*h(t)>0; hence unique optimizer. With a1=sqrt(1-s), implicit derivative gives dt/ds=-1/[6t0(1-t0)]; envelope gives dK/ds=-t0/[2Q(t0)]. Independent numeric root gave t0=0.64290833503198, C*=1.34511821204919, kappa=1.21087635888558. Finite numeric checks are not proof of dimension-free eta.

## originality

PASS

He–Tkocz–Wyczesany establish the best GLOBAL Gaussian comparison constant and unique extremal one-uniform cutoff. They do not state the local optimized Hessian in coefficient space, exact direction-independent plateau reduction, or the kappa deficit. Barthe–Koldobsky supply central thin-slab extremal geometry, not this threshold-optimized coefficient, while related cube-slicing stability bounds cover a different functional or exclude a1 near 1. No dominating statement found in Resultary semantic search.

## value

PASS

Sharp global inequalities naturally invite near-extremizer stability. This yields a dimension-free local structural theorem, an exact dependence of optimized tail ratio on dominant weight, and a computable tangent-space quadratic deficit for all finite dimensions. The analysis is substantive because the maximum ranges over thresholds and global localization is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
