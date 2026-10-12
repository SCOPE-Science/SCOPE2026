---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The full relation space is exactly \(2^8=256\) bitmasks, where the bit at \(4u+2v+w\) records \(R(u,v,w)\). Every candidate is filtered by both persistence clauses, not by a heuristic preselection. For each admissible relation, the program evaluates both binary modalities on every pair of the three upward-closed sets and compares all 27 triples for associativity. It also compares the 16 quadruples for ternary relational associativity.

The asserted chain totals are 67 admissible relations, partitioned into 32 relationally associative with both modalities associative, 11 with both modalities associative but the relation nonassociative, and 24 with only the existential modality associative. The six disjoint upper-coordinate row counts are also asserted. The program separately enumerates the singleton order and the discrete two-world order for minimality and checks two explicit semantic witnesses.

The computational check is exhaustive for the stated finite bases. It is **not** an infinite-frame completeness or decidability argument. Independent audit is not performed.
