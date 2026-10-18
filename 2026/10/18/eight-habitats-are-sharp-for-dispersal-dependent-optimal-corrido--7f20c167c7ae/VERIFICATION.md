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

# Reproduction and limits

Run `python3 verify_corridors.py` from the directory containing this file. Only Python 3 standard-library modules are used; there are no additional data files. The script checks the standard Prüfer-bijection census for trees with \(2\le n\le8\), exact edge-polynomial coefficient vectors, coefficientwise maximal candidates, and the five nontrivial polynomial comparisons. For the two labeled eight-node witnesses it also directly sums the exact probabilities of all configurations of operating edges at \(p=1/4\) and \(p=3/4\).

Observed successful output:

```
VERIFY_OK Prüfer_isomorphism_classes {2: 1, 3: 1, 4: 2, 5: 3, 6: 6, 7: 11, 8: 23}
VERIFY_OK nontrivial_coefficient_frontier {7: {(0, 1, -1): 1}, 8: {(0, 2, -1): 1, (0, 1, 0, -1): 1, (0, -1, 2): 1, (0, -1, 1, 1): 1}}
VERIFY_OK switching_shapes=2 thresholds=1/2,(sqrt(5)-1)/2 exact_witness_coefficients=5
VERIFY_OK independent_reliability_enumerations= 10
```

The continuum statement does not follow from finitely many evaluated probabilities. It follows because every edge polynomial is explicitly generated, dominated choices have coefficientwise smaller coefficients, and the remaining exact polynomial differences have proven fixed signs or single roots on \((0,1)\). The finite census relies on Prüfer enumeration and rooted-tree canonicalization; it does not cover larger trees, general graphs, heterogeneous areas, or dependent dispersal events. These calculations do not supply independent scientific auditing.
