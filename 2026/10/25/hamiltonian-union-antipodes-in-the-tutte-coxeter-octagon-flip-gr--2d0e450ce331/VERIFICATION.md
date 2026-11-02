---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The 30-vertex duad/syntheme incidence graph is specified by 15 pair vertices and 15 perfect pair partitions, with 45 edges. Each perfect matching is a 15-entry distinct duad assignment to synthemes; complete backtracking enumerates exactly 288. Two separately inspected source verifiers use (a) relative-permutation cycles and (b) explicit simple eight-cycle flips. Independently written exhaustive Python enumeration reconstructed the 288 matchings, exactly 1440 undirected exchanges, ten regular neighbors, the complement (10,20) and (30) strata of 144 matchings each, radius 5, diameter 6 and the complete stated distance profiles. All 41,328 pairs were evaluated by breadth-first search and tested for one Hamiltonian 30-cycle symmetric difference; exactly 144 unordered pairs meet both conditions. The computation is exhaustive for this one finite explicitly specified graph, not for other graphs or flip lengths.

## originality

PASS

Classical Tutte–Coxeter incidence, girth and matching count are acknowledged. Known 4-cycle switch chains cannot move on girth-eight T, and general arbitrary alternating-cycle reconfiguration does not imply the exact fixed eight-cycle metric. The exhaustive 288-vertex distance stratification and Hamiltonian-antipode equivalence were not found under Resultary or inspected primary references. A differently named finite graph computation remains a historical risk.

## value

PASS

The Tutte–Coxeter graph is a canonical girth-eight cubic cage. Since shorter alternating-cycle switches do not exist, its first possible flip length is mathematically forced; the exact distance geometry at that threshold and Hamiltonian characterization of antipodes are structural finite invariants beyond known matching count, even without a general-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
