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

# Reproducibility

Extract this package into one directory, then execute `python3 verify.py` there. Compare standard output with `verification_output.txt`; the program exits nonzero if any check fails. No dependencies beyond the Python standard library are needed.

The code constructs every graph directly as a universal center joined to disjoint cliques. It examines every vertex subset and tests the original definition: every vertex has a selected open neighbor, and every nonselected vertex has an adjacent selected defender whose removal and replacement preserve total domination. Only then does it compare with the proposed occupancy rule and count all qualifying sets by cardinality. It determines inclusion-minimality from strict containment among actual qualifying sets, without using the claimed structural formula for this step.

The finite test checked 66 ordered clique-size vectors with \(t\in\{2,3,4\}\), each \(r_i\in\{2,3,4\}\), \(\sum_i r_i\le11\). Exactly 127904 vertex subsets were examined. It verified the full polynomial and inclusion-minimal polynomial coefficient by coefficient, including the triple-triangle example.

The general statement for all parameter vectors is proved in `RESULT.md`; no finite enumeration can replace its argument. No formal proof assistant or independent mathematical validation has been used.
