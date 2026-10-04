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
# Verification

The verifier constructs \(K_n\square K_2\) directly from two complete graphs and a perfect matching. It tests the Roman \(\{3\}\) definition vertex by vertex.

For \(n=4\) and \(n=5\), every one of the \(4^{2n}\) labelings is checked. The true minimum weight, every minimum function, and the structural classification are compared with the theorem.

A second exact dynamic program does not use the theorem's counting formula. For fixed layer sums it derives the locally feasible matched label pairs from the defining inequalities and counts all labeled assignments. It verifies the minimum value and minimum-function count for every \(4\le n\le60\).

Recorded output:

```text
VERIFY_OK
full_bruteforce_n = 4,5
direct_labelings_checked = 1114112
direct_minimum_functions_checked = 1243
aggregate_exact_DP_n = 4..60
aggregate_parameter_values_checked = 57
all Roman-{3} domination numbers matched
all minimum-function counts matched
all n=4 and n=5 minimum functions matched the structural classification
```

The finite computations are corroborative only. The theorem for arbitrary \(n\ge4\) follows from the layer-sum proof.
