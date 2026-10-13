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

# Reproducible mathematical verification
Run `python3 verify.py` using the attached source and the Python standard library. Successful output:

```
VERIFY_OK transfer_states=81 core_states=27 core_edges=47 determinant_degree_t=10 exact_newton_orders=1..27 recurrence_orders=28..70 extremal_formulas=5..70 brute_orders=5..8 all_checks=passed
```

Checks performed: the independently enumerated local constraints; Tarjan decomposition and absence of external cyclic strongly connected components; all 47 explicit integer potential inequalities; ten explicit closed-walk witnesses and their weights; exact polynomial Newton determinant reconstruction to the full 27-state degree (including all zero coefficients above degree ten); exact polynomial trace recurrence up to order 70; 66 residue-extremal coefficient checks; and direct brute-force maximal-independent-set enumeration on all subsets of orders 5 through 8. The direct subset range is finite and is not asserted to establish the infinite theorem. Formal determinant and coefficient-extraction arguments supporting all orders are written in `RESULT.md`.
