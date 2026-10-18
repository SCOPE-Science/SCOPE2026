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

# Verification notes

Execute `python3 verify.py` with Python 3 (standard library only). The executable checker exhausts binary incidence rows for every guild split through eight total species, rejects disconnected graphs, and groups surviving graphs by labeled plant degrees, labeled pair-common-neighbor counts, and the pollinator-degree multiset. The grouping criterion is exactly equivalent to matching the first- and second-order plant-loss laws under independent homogeneous failures, together with pollinator degrees. All members of each group have the same capacity profile.

The run examined 36,317 connected labeled matrices for the largest four-by-four case, producing 1,986 signature classes. For five-by-three it examined 14,221 connected matrices and 2,476 classes; for three-by-five it examined 14,221 connected matrices and 336 classes. Every listed split is printed by the program. The matching recursion is a finite dynamic program over used-pollinator masks, keeping both options of leaving a plant unmatched and assigning it any currently uncommitted surviving pollinator. Hence it returns an exact maximum matching size, not a heuristic.

The four-plant/five-pollinator witnesses are encoded by plant-row bitmasks `(25,6,5,3)` and `(22,9,5,3)`, where bit positions zero through four correspond to pollinators `a,b,c,d,e`. All 32 surviving-pollinator subsets are checked. Their exact cardinality-sum profiles are `(0,5,19,27,17,4)` and `(0,5,20,30,20,4)`. Pointwise matching improvement holds for seven subsets and equality for the others. Expanding the associated Bernstein-basis sums gives the stated polynomial.

The finite enumeration proves no separation through eight species; it does not classify all nine-species witnesses, arbitrary heterogeneous loss probabilities, or capacity definitions permitting one pollinator to visit multiple plants. Scientific review here is not independent validation.
