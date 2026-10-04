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

The checker constructs \(B_r\) directly from the common spine and the \(r\) square pages. For every vertex subset it performs the domination step and then repeatedly applies the unique-uncolored-neighbor forcing rule.

For each \(2\le r\le8\), it compares this direct process with the theorem's structural criterion, computes the coefficient vector independently, and checks the total number of power dominating sets and the number of minimum sets.

Recorded output:

```text
VERIFY_OK
book_parameters_checked = 7
vertex_subsets_checked = 349504
power_dominating_sets_checked = 296568
parameters r = 2..8
all direct propagation tests matched the page-intersection classification
all polynomial coefficients matched the closed formula
all total-set counts and minimum-set counts matched
```

The finite computation is corroborative only. The theorem for every \(r\ge2\) follows from the structural proof.
