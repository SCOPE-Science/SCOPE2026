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
# Reproduction and boundaries

From the containing package, save \(\texttt{verify.py}\) beside this document and execute \(\texttt{python3 verify.py}\) in a standard Python 3 environment; no third-party modules are required. The program computes all first and mixed moments with exact \(\texttt{fractions.Fraction}\) arithmetic for \(1\le n\le100\), compares the exact conjectured covariance at every size \(n\ge2\), and independently constructs BSTs from every permutation for \(1\le n\le8\). Expected output:

```
PASS: all exact moment/covariance recurrences through n=100; 46233 exhaustive BST permutations through n=8.
```

The analytic proof in \(\texttt{RESULT.md}\) establishes all integers \(n\ge2\); the finite program cannot establish an infinite assertion. No proof assistant, external certification, or independent audit was used. The open mathematical risk concerns historical priority, not evidence of an erroneous finite check.
