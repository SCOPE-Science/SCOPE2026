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
# Reproduction of finite anti-forcing classification

Execute `python3 verify_permutohedron.py` in the directory containing the program. The only requirement is the standard Python library. Its successful output includes:

```
VERTICES=24 EDGES=36 MATCHINGS=169 RYSER=169
ANTI_FORCING_POLYNOMIAL=4z^4+16z^5+44z^6+48z^7+39z^8+16z^9+2z^10
NATURAL_AUTOMORPHISMS=48 MATCHING_ORBITS=17
TRANSVERSAL_CHECKS=17
VERIFY_OK
```

The verifier constructs data from the permutation adjacency rule without external files. The recursive perfect-matching enumeration is cross-checked by an independent \(12\)-by-\(12\) permanent computation; all \(169\) matchings are checked by subset dynamic programming over \(2^{12}\) contracted-graph vertex subsets; the \(17\) class representatives are independently checked by a minimum-transversal search using the alternative perfect matchings. The checker also validates the complete \(17\)-row orbit table, not merely its aggregate counts.

This is a finite exhaustion with a proved recurrence. It does not prove formulas for other orders. Novelty is necessarily limited by the inaccessible full text of certain (4,6)-fullerene studies. No external or independent audit has been performed.
