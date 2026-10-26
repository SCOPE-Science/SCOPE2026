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
# Finite verification of the Hamiltonian-cycle closure formulas

Execute `python verify.py` with a standard Python 3 installation. The program independently generates every undirected Hamiltonian cycle, computes premise closure by intersecting all cycles containing a premise, and compares this direct semantics with both the component-structure prediction and the separate one-round Horn-rule construction. It exhausts every subset of the edge sets of complete graphs with four, five, and six vertices, and checks 4,211 reproducibly selected inputs at order seven (including all proposed critical antecedents). It tests one-round indispensability of every critical antecedent at orders five and six, and the complete closed-set census through order six.

Recorded execution:
```
EXHAUSTIVE n=4 subsets=64 hamilton_cycles=3 closed=8 direct_rules=6 PASS
EXHAUSTIVE n=5 subsets=1024 hamilton_cycles=12 closed=69 direct_rules=75 PASS
EXHAUSTIVE n=6 subsets=32768 hamilton_cycles=60 closed=647 direct_rules=377 PASS
SAMPLED n=7 subsets=4211 hamilton_cycles=360 direct_rules=2212 PASS
VERIFY_OK checked_inputs=38067 exact_closure=PASS closed_count=PASS one_round=PASS sharp_direct_premises=PASS
```

The case \(n=7\) is not exhausted, and no computation establishes an infinite theorem. The general proofs appear in `RESULT.md`. This check does not independently establish publication priority or mathematical significance. The checker does not depend on external services or data.
