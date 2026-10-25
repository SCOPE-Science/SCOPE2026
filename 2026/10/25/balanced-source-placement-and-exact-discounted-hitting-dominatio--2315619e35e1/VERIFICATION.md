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

# Reproducible verification and limits

The accompanying `verify_wheel.py` uses only the Python standard library and exact `fractions.Fraction` arithmetic. Execute `python3 verify_wheel.py` from the directory containing that file. Its output should exactly match `verifier_output.txt`, ending in `VERIFY_OK`.

The program independently reconstructs the wheel and every nonempty source subset for rim sizes \(3\) to \(8\) and discounts \(1/3\), \(3/5\), \(4/5\), including one smaller complete-graph boundary used only as a stress test. For each subset it solves the original graph Dirichlet system by Gaussian elimination, rather than using the proposed transfer formula. This tests \(3006\) individual source choices, compares \(216\) cardinality-constrained optimal support floors with the theorem, and compares \(126\) threshold minimum cardinalities for seven threshold values. It also checks the exact hub-exclusion example with \(n=4\).

The proof's gap transfer, strict discrete convexity, monotonicity and two-case partition are mathematical arguments for arbitrary size. Exhaustive small-size enumeration neither certifies the infinite claim nor resolves bibliographic novelty. No independent audit is claimed.
