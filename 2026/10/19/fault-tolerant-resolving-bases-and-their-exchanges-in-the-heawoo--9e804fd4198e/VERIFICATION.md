---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The cyclic triples give the Fano plane: each nonzero residue occurs once among the ordered nonzero differences of {0,1,3}, so every point pair is on one line and, dually, every two lines meet at one point. Distances for these same-side pairs are 2, and cross-side distances are 1 for incidences and 3 otherwise. Hence the same-side inequalities count the distinguishing members exactly, and all selected landmarks distinguish opposite-side pairs by parity. Independently computed the full metric with Floyd–Warshall and tested every subset of size at most seven against the 91 distance-difference masks, without executing the supplied programs. All sizes below seven had zero solutions; there were 282 at seven with point counts 0:1, 3:140, 4:140, 7:1. Independently compared each noncollinear triple's exact four-element choices with the five claimed patterns, and no choice for collinear triples; the dual classification agreed as well. Grouping the states by common six-subsets constructed precisely the token-jump edges, and bitset distances confirmed 784 edges, components of sizes 1,1,280, degrees 0:2, 4:56, 6:224, and 224 eccentricities 6 and 56 eccentricities 7 inside the large component. The degree-zero states were exactly the two bipartition classes; the eccentricity-seven states were exactly the claimed U0∪U1 cases and duals. Compared every basis mask, edge, large component index and eccentricity with the frozen certificate. The independently read SHA-256 is bdab9a6ad701d378ceb4e18a4bd79f8e1afe78ffac338b3ac75c1b2be94aaf7a.

## originality

PASS

Ordinary Heawood dimension, the fault-tolerant invariant, and the token-jump move are established prior work. The supported distinct result is the exact two-fold minimum and geometric basis classification together with complete exchange invariants for the canonical Fano incidence graph. The closest exact-graph tables use different objectives; the closest fault-tolerance sources give bounds or exact results in other regimes. No inspected source or its direct implications supplies the claimed family and exchange distances.

## value

PASS

The Fano incidence graph is a canonical small projective-plane graph and ordinary resolving bases are a known baseline. Selecting a minimum fault-tolerant installation and asking if it can be updated by single replacements while retaining optimal fault tolerance is a natural next question. The answer exhibits both isolated and mobile optimal installations on the same graph, with an exact and geometrically characterized periphery; it gives an explicit finite test case for distance, redundancy and constrained reconfiguration rather than a bare count on an arbitrary small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
