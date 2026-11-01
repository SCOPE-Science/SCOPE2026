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

Direct-neighborhood enumeration was performed with two standalone implementations, not by treating the paper's recurrence as the update rule. The Python implementation checked every state of the \((3,4)\) and \((3,6)\) graphs; the C++ implementation checked those graphs and the \((5,4)\) graph. Both checked the global equality \(F^3=F^2\), the terminal state of each input, every individual basin's exact cardinality, and sharpness of two-round stabilization. Their packaged outputs report successful executions.

The normal crossover is proved with Stirling's asymptotic and a binomial central limit theorem; finite state enumeration does not establish the asymptotic. The numerical check covers only listed finite parameter pairs, while the symbolic proof covers all odd \(n\ge3\) and even \(m\ge4\). No independent mathematical audit has been conducted.
