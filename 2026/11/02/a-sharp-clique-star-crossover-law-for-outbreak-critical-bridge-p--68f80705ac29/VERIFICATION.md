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

# Reproducible mathematical checks

Run `python3 verify_bridge.py` alongside the other files. The script requires only Python 3 standard-library `fractions` and `math`; it produces `PASS` messages or raises an exception. It tests exact rational adjacency inverses for \(3\le r\le6\), \(1\le s\le10\), with 88 tested admissible parameter triples, including feasible points around predicted crossover ratios. The script directly checks all diagonal entries and the strict inferiority of both nonconnector vertex orbits.

It also checks the \((r,s)=(3,3)\) example at \(q=5/2\), \(3\) and \(4\) and the weighted cross-network Schur criterion for 54 cases using receiving graphs on 1, 2 and 3 vertices. It verifies the exact polynomial sign identity for integers \(3\le r\le23\) and the documented ranges of \(s\).

Observed output:

```
PASS: exact matrix inverses and endpoint maxima on 88 clique-star trials
PASS: witness diagonal values at q=5/2,3,4
PASS: Schur criterion at 54 weighted external couplings
PASS: exact crossover polynomial identity for all r=3..23, s in tested ranges
```

All inverses use exact fractions. Positive definiteness is checked via a rational \(LDL^{\mathsf T}\) decomposition, not floating-point tolerance. No numerical enumeration is presented as an infinite proof. The analytical proof in `RESULT.md` establishes the universal theorem, including strict inequalities, domain boundaries, tie treatment and the critical coupling formula.
