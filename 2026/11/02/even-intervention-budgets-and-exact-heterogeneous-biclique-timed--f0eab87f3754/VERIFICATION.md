---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For each bipartite edge, all t+1 natural neighbors depend on the opposite part at t, separating the two alternating vertex-time strands. One shift from empty initial natural state equates their optimum saturation costs; a fully naturally positive target forces saturation of each strand, and a saturated side propagates naturally after zero-cost updates. On K_{a,b}, natural successor counts are f(v),g(u) regardless of identities, giving exact nonnegative Dijkstra transition weights v-g(u),u-f(v) and optimum twice the minimum distance to a saturated side. Initial source arcs u correctly charge time-0 targeting. Uniform case requires min(alpha,beta) direct activations before first natural event or saturation.

## originality

PASS

Best-of-knowledge original in its precise qualified statement. Soltani et al. already separate odd/even intervention parity and provide exact tree algorithm plus special stars/bicliques, so those ideas are not new; their stated results do not supply exact equal-cost strand saturation and heterogeneous biclique weighted shortest-path with arbitrary positive thresholds. Their bipartite double-cover comparison is a different graph operation. The progressive/static results lack repeated vertex-time targeting. Priority limits are recorded; an inaccessible plausible source alone is not treated as automatic failure.

## value

PASS

Timed intervention cost in non-progressive adoption is a natural exact control invariant; bipartite parity makes it even, and a polynomial algorithm for arbitrarily heterogeneous bicliques supplies schedules and separates timed from static targeting. Nontrivial generalization of previously solved tree class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
