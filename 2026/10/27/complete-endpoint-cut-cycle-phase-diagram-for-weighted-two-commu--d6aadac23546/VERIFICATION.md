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

# Verification of two-community endpoint norms

Run `python3 two_community_checker.py` using Python 3 standard library only. The checker rebuilds the weighted graph as a list of all edges, forms the grounded Laplacian from conductance squares, inverts it by exact rational Gauss–Jordan elimination, calculates each edge-source potential, then computes *every* weighted transfer-current column of \(Q\) and \(P=I-Q\). It compares each exact column sum to the independently derived rational within- and cross-class formulas, verifies equality within each orbit, and checks the relevant maximizing-class inequalities.

Actual completed execution:

```
TWO_COMMUNITY_HODGE_EXACT_OK graphs=54 verified_full_columns=3285
```

The check covered community sizes \(n\in\{3,4,5,6,7,8\}\), and for each size the nine exact rational square-root conductance parameters \(x\in\{1/5,3/7,2/3,4/5,1,6/5,2,3,5\}\). In particular it included the special five-community crossover and the uniform-weight tie. These are finite corroborations only; the proof in RESULT.md is required for the statements concerning every \(n\) and real \(x>0\), uniqueness of irrational weight optima, and limiting suprema. No external or independent audit was conducted.
