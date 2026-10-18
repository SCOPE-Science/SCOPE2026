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

Conditioning on a vertex being isolated leaves exactly B=binom(n-1,2) eligible edges, and an exterior motif placement occurs conditionally with probability (m)_e/(B)_e. Summing n-s exterior vertices gives E[UX]=(n-s) M_H q(m)_e/(B)_e with E[X]=M_H(m)_e/(N)_e and E[U]=nq, yielding exact factor Cov=EU EX[(n-s)/n (N)_e/(B)_e-1]. A motif has no isolated vertices, e<=m<=B, so interior placements cannot coexist with isolation; outside that edge-count range U or X is zero. For trees e=s-1, log[(N)_{s-1}/(B)_{s-1}]->2/alpha as n/s->alpha>1; h(x)=log(1-x)+2x has one interior root, sign negative below alpha*=1.2550009749... and positive above, excluding equality alpha*. In G(n,p), disjoint exterior-edge factors yield -s EX (1-p)^(n-1)<0 for 0<p<1. Independently exhaustively computed 36 edge-count strata across small n and path, triangle and star motifs with exact rational moments; finite enumerations corroborate the all-size counting argument.

## originality

PASS

Best-of-knowledge PASS: general exact joint moment is elementary and potentially implicit in general graph-statistic methods, but the tree-shape-independent growing-motif host-to-tree critical ratio and independence from m are not supplied by checked fixed-motif limit theorems.

## value

PASS

A universal phase boundary independent of growing tree shape and graph edge-count density is a motivated exact correlation sign law, where G(n,m) behaves opposite G(n,p) in one parameter region. This is a structural finite formula plus nontrivial asymptotic sign classification, not a routine table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
