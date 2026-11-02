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

# Reproducible checks and scope

Run the included standalone `verify.py` with Python 3. Its only dependencies are the standard library. The first-vertex recursion evaluates the probability-generating functions exactly using `fractions.Fraction`. A separate implementation iterates all \(9!=362880\) vertex orders of each displayed tree and obtains the same four nonzero distribution coefficients. The exact expectations are \(73/15\) and \(34/7\), whose difference is \(-1/105\).

For the minimum-order assertion, the script generates all unlabelled trees from order one to nine by adding every possible leaf and deduplicating via canonical tree-center codes. The class counts are \(1,1,1,2,3,6,11,23,47\). For every class it considers all ordered endpoint pairs satisfying the bare-path and properness conditions and computes exact expectation differences. The numbers of oriented proper moves at orders four through nine are \(2,8,26,70,186,470\); the strict decreases are \(0,0,0,0,0,4\), respectively.

The recurrence and full permutation census are independent computational routes for the explicit negative witness, and all comparisons are rational, not floating-point approximations. The finite search's exhaustivity follows from the fact that deleting a leaf from any tree of order at least two yields a smaller tree, plus completeness of canonical unlabelled-tree coding.

This does not independently certify historical priority, and no independent mathematical audit is recorded. The work concerns a finite counterexample to the KC-monotonicity suggestion; it does not challenge the proved path-minimization theorem.
