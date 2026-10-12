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

The checker evaluates the quasi-total Roman conditions directly for every ternary labeling of
\[
\operatorname{Cr}_n
\]
for
\[
3\le n\le7.
\]

For \(4\le n\le7\), it independently confirms minimum weight \(6\), verifies that every minimum labeling belongs to exactly one of the two structural families in the theorem, and checks the exact count
\[
n^2(n-1).
\]

Recorded output:

```text
n=3: gamma_qtR=6, minimum_functions=37
n=4: gamma_qtR=6, minimum_functions=48
n=5: gamma_qtR=6, minimum_functions=100
n=6: gamma_qtR=6, minimum_functions=180
n=7: gamma_qtR=6, minimum_functions=294
VERIFY_OK
n_range = 3..7
ternary_labelings_checked = 5380749
Cr_3 minimum-function count = 37
for n=4..7 every minimum function matched exactly one of the two structural families
minimum-function formula for n>=4 = n^2(n-1)
```

The checker examines \(5{,}380{,}749\) ternary labelings in total. The finite computation is corroborative only; the arbitrary-\(n\) theorem follows from the proof.
