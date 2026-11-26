---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Disjoint consecutive overlaps ensure the two front types close under updates: the only mixed edge of each type has either s or k−s A voters, and its update moves the front to the adjacent edge, or absorbs at an endpoint. At k=2s, R_j and V_{j+1} describe the same configuration when both exist; their mapped neighbors and probabilities agree since p=q=1/2. From every transient front, continuing in its direction reaches consensus within L rings with probability at least p^L, which bounds the mean by a geometric block argument. Every transient front has exactly one rate-one clock. Independently of the two-state recurrences, the total A count M has mean-zero increment at a ring and conditional second moment a(k−a)=s(k−s), where a is the A count of the active edge. Thus the bounded stopped count gives fixation M_0/N, and the stopped squared-count identity gives s(k−s) E[T]=N M_0−M_0². Substitution of M_0=j(k−s)+s yields the exact stated mean and the stated L² limit. L=2 gives k/s directly.

## originality

PASS

Best of current knowledge for the invariant polarized front on the specified geometry and its exact physical-time first moment. Proportional whole-edge updating, magnetization martingales and general random-walk first-step analysis are established. Fixation M_0/N conditional on absorption is not a standalone novelty claim. On the invariant front, the active-edge index with its last direction is a persistent nearest-neighbor walk; its arithmetic is not claimed as a new abstract ruin law. The exact mapping with one physical rate-one clock and absorption boundaries is substantive and was not identified in the closest inspected hypergraph sources.

## value

PASS

The result resolves finite-size time and the optimal scale constant for a simple repeated-overlap family, rather than a qualitative diffusion analogy. The path-front closure explains why the A-count's quadratic variation is constant and why the physical time changes with overlap s. The degenerate geometry 2s=k and the two-group case remain within the same law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
