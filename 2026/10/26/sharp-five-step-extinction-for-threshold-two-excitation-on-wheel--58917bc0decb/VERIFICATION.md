---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For W_n=K1 join C_n, n>=3, synchronous Greenberg–Hastings states 0 resting,1 excited,2 refractory; 1->2->0 unconditionally, 0->1 iff >=2 distinct excited neighbours. Two-step rim-exclusion lemma: if H_{t-1}!=1, every rim excitation at t required both rim neighbors excited at t-1, which then become refractory at t, so no resting rim vertex can be newly excited at t+1. Cases H_0=0,1,2 imply F_n^5=all-rest uniformly. Exhaustive initial-state search for each fixed n=3..8 independently found exact maximal hitting times [3,4,4,4,4,5]. An explicit hub=1 rim pattern marks {0,4} for n=8, {0,4,8} for n>=9, gives a hub excitation at t=3 and refractory t=4, establishing depth5 for every n>=8. Witnesses checked to n=80. Thus all-rest sole recurrent state and no periodic orbit. Fixed small n exceptions legitimately use full finite exhaustive search, not a finite experiment extrapolated to infinite n.

## originality

PASS

Known threshold Greenberg–Hastings lattice behavior and different graph families do not establish the exact wheel cutoff under distinct-neighbour threshold two. Threshold-one wheel and bipartite threshold>=2 behavior do not imply uniform extinction. Novelty bounded by source reading and semantic searches.

## value

PASS

A uniform five-step nilpotence theorem across arbitrarily large wheels is a meaningful and surprisingly strong dynamical classification, including exact short-circumference exceptions and a sharp family of witnesses. The graph geometry and threshold are mathematically motivated, not arbitrary simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
