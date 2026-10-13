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
This package contains a self-contained exact-rational verification program:

`python3 verify_two_partner_robustness.py`

Successful execution starts with `VERIFY_OK` and prints the number of checks. It uses only Python's standard library, including `fractions.Fraction`.

Checks from the actual embedded program are:

- 189 independent elementary survival-probability and random-stage calculations, using complete enumeration of independent primary extinction configurations for \(2\le m\le7\).
- 3,605 degree-multiset optimization instances at \(3\le m\le8\), \(2\le n\le6\), and seven exact rational extinction probabilities.
- 181 instances with tied optimizers, explicitly stress-testing the nonuniqueness boundaries.
- Every enumerated feasible degree multiset is realized by a simple bipartite graph with no isolated primary vertex.
- Each optimizer is checked against the low-probability balanced, high-probability concentrated, boundary, or intermediate normal-form assertions.
- The two-degree transfer expression at extinction probability \(1/2\) and the averaged stage difference are checked exactly.

Separately, a direct census of labeled three-by-three adjacency matrices confirmed that grouping by secondary degree multiset preserves exact expected survival and that all legal edge counts occur with no isolated guild vertices.

The infinite-size theorem is derived by proof from exact marginal-gain identities and exchange arguments. The finite tests are reproducibility and stress tests, **not** substitutes for those proofs. No independent audit has been performed.
