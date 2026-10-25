---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For each three-vertex edge, pure agreeing leaves overwrite only hub, whereas mixed leaves acquire hub color on first activation; pure petals are irrevocable. Positive independent edge-selection weights guarantee almost-sure eventual purification. The first chosen pure-vs-mixed petal decides whether an initially opposed hub succeeds when all pure petals have one color; two pure colors forbid consensus. Direct Bernoulli independent-initial calculation yields P0=(1−p)²(1+2p)(1−p²)^(m−1) and P1=p²(3−2p)[p(2−p)]^(m−1), independent of weights; total at p=1/2=(3/4)^(m−1), p=λ/sqrt(m)→e^(−λ²). After purification, fresh weighted draws give i.i.d hub opinions, while uniform coupon collection yields mH_r or 1+mH_r conditional means. Independent exact enumeration of all binary states, with unequal positive rational edge weights for m=1..6 and three p choices (18 parameter cases), matched both color probabilities; full m proof uses state invariants.

## originality

PASS

The local three-agent majority rule is established literature; the exact classification for disjoint two-leaf petals on a single shared hub, with arbitrary positive meeting probabilities, i.i.d initialization law and persistent disagreement is a distinct solved topology. Full primary majority-rule paper of Noonan–Lambiotte studies complete/tripartite/modular/degree-heterogeneous hypergraphs rather than exact weighted sunflower absorbing classes; Lanchier–Neufer concerns spatial hypergraphs, and adaptive-rewiring models differ. Equivalent hyperstar wording searched. Best knowledge PASS with possible unindexed model-specific enumeration risk.

## value

PASS

A simple connected majority-interaction topology unexpectedly exhibits permanent nonconsensus with probability tending to one exponentially despite every group being updated infinitely often. Exact weight-invariant consensus probabilities, every-initial-state class and coupon-collector timing are mathematically motivated benchmarks and structural insights for hypergraph opinion dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
