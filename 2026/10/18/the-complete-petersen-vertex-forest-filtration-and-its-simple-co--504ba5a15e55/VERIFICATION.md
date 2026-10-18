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
# Verification of the Petersen forest filtration

Run the two supplied standard-library Python 3 scripts in the same directory:

```bash
python3 verify_petersen_forest.py
python3 verify_petersen_homology.py
```

The first script enumerates the full \(2^{10}=1024\) vertex subsets and verifies the graph-induced forest predicate at degree bounds \(0,1,2,3\), the complete Morse matchings and topological-sort acyclicity for bounds \(0,2,3\), and all \(180\) actual elementary free-face collapses of \(\mathcal F_2(P)\) onto \(\mathcal F_1(P)\). The second script uses its own induced-cycle test and exact signed cellular chain ranks over prime fields to cross-check the Betti numbers. `verification_output.txt` records actual program output.

The discrete-Morse certificates are finite exhaustive proofs of the homotopy types for this graph; finite-field calculations are supplementary and are not used to rule out integral torsion. The strong equivalence at the intermediate inclusion comes from the checked sequence of elementary collapses, not from matching Betti numbers. No classification is claimed for other graphs or unbounded vertex counts.
