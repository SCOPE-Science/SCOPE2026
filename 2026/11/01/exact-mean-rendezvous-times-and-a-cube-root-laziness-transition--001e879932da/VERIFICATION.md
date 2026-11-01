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

# Verification record

The claimed finite expectation was verified in exact rational arithmetic against the independently assembled full two-walker absorbing product chain for every positive part-size pair at most four with total vertex count at most six, at holding probabilities \(1/5\), \(1/3\), \(1/2\), \(2/3\), and \(4/5\). The three-type first-step equations were separately solved for all part-size pairs through four, and the derivative sign structure was checked for part sizes through eighteen. Large balanced instances were compared numerically with the asymptotic prediction. The included standalone Python program reports **793 exact/algebraic assertions and 3 asymptotic numerical diagnostics passing**.

These computations are bounded finite checks. The rational formula, unique optimizer and all unbounded asymptotic limits are supported by the algebraic and analytic arguments in RESULT.md, not inferred from the tests. A full independent mathematical audit has not occurred. The scientific scope excludes asynchronous walks, unequal or state-dependent holding probabilities, and general graphs.
