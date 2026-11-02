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

The original definition requires each competitor to lie in the complement, to have exactly the same size, and to dominate the original Cartesian rook graph. A set dominates iff it meets every row or every column, since an unhit row and unhit column leave their intersection undominated. If 2k<=pq, a dominating k-subset in the complement would exist whenever all its rows or all its columns were met (choose one from each relevant class and extend), so accuracy forces D to contain a whole row AND a whole column. Conversely both full classes make every complement subset nondominating. If 2k>pq, no rival fits. Inclusion-exclusion over selected full rows/columns gives the claimed F_{p,q}; over omitted rows/columns gives B_{p,q}. Since 2(p+q-2)<=pq and the smallest full row+column union has p+q-1 cells, gamma_a=p+q-1. The exceptional minimum counts for p=2 and (3,3) follow from p+q-1>pq/2. Independently enumerated all graph-defined dominating rivals for every subset of the 2x2,2x3,2x4,2x5,3x3,3x4 boards and matched every polynomial coefficient. This is finite corroboration; the lemmas prove all p,q.

## originality

PASS

The general half-order principle is directly present in Alikhani–Safazadeh–Ghanbari Theorem 2.3, while that paper treats paths, cycles, ladders, books and hypercubes, not the all-cardinality two-factor rook-graph enumeration. Cyman–Henning–Topp supplies the accurate-domination framework. The two-parameter row/column structural classification, alternating double sums, and exact exception-stratified minimum multiplicity are not stated in inspected primary material or nearby published results. Best-of-knowledge PASS, not a guarantee of absolute priority.

## value

PASS

Rook graphs encode incidences of K_{p,q} and have a natural full-polynomial question. The formula counts every accurately dominating set at every cardinality, gives the first possible size and all minimum-level multiplicities including nontrivial exceptional boards. These are useful exact graph parameters, not merely a renamed general half-order lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
