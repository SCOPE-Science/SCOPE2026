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

The checker constructs \(H_n\) directly from
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

For every labeling it checks both defining conditions without using the proof:
1. the zero-labeled vertices form an independent set;
2. every vertex labeled \(0\) or \(1\) has closed-neighborhood weight at least \(3\).

The exhaustive portion checks every labeling for \(H_4\) and \(H_5\), a total of
\[
4^8+4^{10}=1{,}114{,}112
\]
labelings. It finds the exact optima \(8\) and \(9\), respectively, and verifies that the complete minimum sets have sizes \(12\) and \(16\), exactly the stated \(4(n-1)\).

The construction portion generates every theorem-predicted minimum function for each
\[
4\le n\le50
\]
and directly verifies feasibility, weight \(n+4\), and the count \(4(n-1)\).

Recorded output:

```text
VERIFY_OK
n=4: gamma_oidI=8, minimum_functions=12
n=5: gamma_oidI=9, minimum_functions=16
full_labelings_checked = 1114112
constructed_parameter_range = 4..50
all exhaustive minima matched the threshold classification
all constructed threshold functions satisfied the definition
```

The finite checks do not prove the arbitrary-\(n\) lower bound or uniqueness. Those follow from the symbolic endpoint-surplus and staircase argument in `RESULT.md`.
