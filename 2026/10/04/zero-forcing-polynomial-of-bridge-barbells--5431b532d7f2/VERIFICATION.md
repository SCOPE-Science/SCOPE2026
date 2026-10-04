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

The checker constructs each bridge barbell directly from two cliques and one bridge. It enumerates every vertex subset and applies the zero forcing color-change rule without using the theorem’s structural criterion.

For each \(3\le a,b\le7\), it separately evaluates the claimed threshold criterion, compares the full coefficient vector with
\[
x^{a+b-3}\left(x^3+(a+b)x^2+(ab+a+b-2)x+(2ab-a-b)\right),
\]
and checks the zero forcing number, number of minimum sets, and total number of forcing sets.

Recorded output:

```text
VERIFY_OK
barbell_parameter_pairs_checked = 25
vertex_subsets_checked = 61504
zero_forcing_sets_checked = 2100
parameters a,b = 3..7
all direct color-change tests matched the structural classification
all polynomial coefficients matched the closed formula
all zero-forcing numbers, minimum-set counts, and total counts matched
```

The exhaustive computation is finite corroboration only. The theorem for all \(a,b\ge3\) follows from the proof.
