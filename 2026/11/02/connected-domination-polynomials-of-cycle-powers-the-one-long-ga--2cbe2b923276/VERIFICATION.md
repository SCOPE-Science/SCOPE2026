---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For selected vertices listed cyclically, a gap >2r+1 has an undominated interior vertex. Two gaps >r disconnect the induced selected subgraph; conversely all short gaps or exactly one long gap form a connected spanning chain. Anchor-gap counting divides n ordered-rooted tuples by k, giving [z^k]Q=(n/k)[u^n]A^k+n[u^n]BA^(k-1). The maximum allowed total rk+r+1 gives k_min=ceil((n-r-1)/r), and stars-and-bars deficits give n*binom(k+r-d,r+1-d); 2r omitted vertices sharply obstruct large-set saturation. Independently checked adjacency/BFS vs coefficient formula in small n,r; the all-parameter argument is combinatorial, not experimental.

## originality

PASS

Best-of-knowledge originality: compared exact mathematical statement and logical implication against the listed primary sources and semantically searched published Resultary records. Mojdeh–Emadi r=1 is a special case and is excluded from novelty. Galvin–Zhang gives domination without the at-most-one-long-gap criterion, so the full connected polynomial is not a stated consequence of its formula. Failed search is not novelty proof; residual risks remain.

## value

PASS

Connected domination of cycle powers is a natural graph invariant. The all-n,r size distribution with a simple exact gap characterization, minimum-set multiplicity and sharp saturation threshold goes meaningfully beyond a single easy special case; it is not merely the known ordinary domination polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
