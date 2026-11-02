---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Identify T(n) vertices with K_n edges. Induced selected degree≤1 exactly means selected K_n edges decompose into vertex-disjoint P3 paths, isolated edges, unused vertices. The equations 3a+2b+c=n and 2a+b=max=floor(2n/3) force the three residue patterns. When n=3k, a maximum-preserving one-edge exchange cannot change a path triple block and three centers per block form K3, so components are K3 Cartesian powers and count n!/(6^k k!). When n=3k+1, the unused label exchanges with any leaf after center flip and the two-K2 type attaches to singleton type; all configurations connected. When n=3k+2, legal two-step exchanges between the distinguished K2 and any triple plus internal center changes allow arbitrary block permutations; connectedness follows. Counting block partitions and local swaps yields formulae and degrees 2k, 8k or 10k−2, and 6k. Independently enumerated n=3..7 graph states/component degrees, notably n=6 ten components each K3² and n=7 degrees 16/18.

## originality

PASS

Orlovich et al. prove the scalar dissociation maximum for L(G) when G has Hamiltonian path, hence cover this n-scalar and P3/K2 structural reduction. Their theorem does not classify maximum-only token-jump exchange graphs. No exact residue-three connectedness theorem for T(n), L(K_n), or J(n,2) was identified in mathematical research-record searches and compared related work; qualified best knowledge.

## value

PASS

The structure of optimal solutions is a meaningful refinement of a known optimization problem: a factorially large fixed-triple fragmentation exactly when 3|n versus connectedness with a spare vertex or edge otherwise. The complete component graphs, degrees and counts provide exact infinite-family reconfiguration information beyond a scalar optimum or finite census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
