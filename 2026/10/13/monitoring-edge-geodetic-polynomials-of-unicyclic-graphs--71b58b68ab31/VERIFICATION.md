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

Reconstructed the all-subset criterion: every leaf must be selected because its incident edge requires that vertex as an endpoint; projecting selected vertices onto the unique n-cycle forces all attachment roots A. A cycle edge lies on every shortest path of some selected pair precisely when every successive positive selected-root gap is <= m=floor((n-1)/2); longer/equal half-cycle gaps cannot be uniquely shortest. Each off-cycle bridge then lies on the unique path from its away-side selected leaf to a selected vertex at another cycle root. This proves the iff condition for all finite connected simple unweighted unicyclic graphs. For an attachment gap d, j additional cycle vertices split it into j+1 positive parts <=m, counted by [t^d](t+...+t^m)^(j+1); multiplication across fixed gaps and arbitrary interior nonleaf choices proves z^ell (1+z)^(N-n-ell+|A|)*prod R_d,m(z). For a bare cycle each k-set appears k times among n marked-start compositions, giving (n/k)*c_m(n,k). Minimum-size coefficients follow from minimal number ceil(d/m) of pieces. Independently enumerated all subsets on 30 small test graphs and got the predicted polynomial; this is bounded corroboration, not proof for all n.

## originality

PASS

Exact monitoring edge-geodetic all-subset polynomial, gap-multiset invariance, and multiplicities refine earlier scalar unicyclic monitoring number. Prior notions, forced leaf ideas, and minimum cardinality are acknowledged; no inspected prior result implies the generating polynomial without the new all-set short-gap classification. Best-of-knowledge only.

## value

PASS

A natural combinatorial statistic extending the monitoring edge-geodetic number to all vertex sets and sizes; gives independent gap factors, sharp minimum multiplicities, invariance under large classes of graph modifications, and usable exact enumeration for arbitrary unicyclic graphs, not an artificial tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
