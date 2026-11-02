---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Inspected the actual RESULT.md proof and verify_subdivision.py graph construction. The false-twin classes A\{a0}, B\{b0} each force at most one initially white vertex in any forcing set, since any twin pair is a fort. With x=a0,y=b0,t=s,u in A\{a0},v in B\{b0}, direct neighborhood checks show {x,t,u}, {y,t,v} and {x,y,u,v} are forts. Every four-white choice among representatives contains one of these, so admissible white sets have at most three vertices. Exactly eight types of three whites avoid the obstruction patterns; the explicit force schedules in RESULT.md are valid with p,q≥3 because alternative blue twin-class vertices exist. By monotonicity, all their subsets force, giving a necessary and sufficient avoidance criterion. Any nonforcing white set contains a listed fort, and listed forts are incomparable, so five families exhaust inclusion-minimal forts. Counting admissible whites at sizes 0,1,2,3 gives the displayed complete polynomial. Fresh independent direct zero-forcing simulation enumerated all 2^(p+q+1) white sets and minimal forts for (p,q)=(3,3),(3,4),(4,4), obtaining coefficient vectors [21,19,7,1], [29,24,8,1], [40,30,9,1] at increasing forcing sizes and 10,15,21 minimal forts respectively. Those bounded tests corroborate the symbolic infinite-family proof.

## originality

PASS

The exact polynomial for the unsubdivided complete bipartite graph is known from Boyer et al, but a one-edge subdivided Kpq is not complete multipartite and even contains an odd five-cycle; the known formula is not a legitimate substitution case. Menon-Singh study graph operations and bounds but do not supply all coefficients or the minimal-fort classification in the sections read. Existing chain-graph and complete-multipartite fort results concern bipartite original families, not the nonbipartite one-edge perturbation. A graph may be indexed under a different name, and this possibility remains an explicit priority risk.

## value

PASS

Single-edge subdivision is a canonical local graph transformation. Beyond a routine minimum value, this theorem gives the complete all-cardinality zero-forcing distribution and a minimal-fort obstruction hypergraph on an infinite two-parameter family, quantifying a sharp increase from pq to 3pq-p-q optimum sets despite an unchanged minimum size. Exact fort families and the count can be independently used in transversal, forcing and graph-operation comparisons; the all-coefficient and structural classification has substantive natural motivation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
