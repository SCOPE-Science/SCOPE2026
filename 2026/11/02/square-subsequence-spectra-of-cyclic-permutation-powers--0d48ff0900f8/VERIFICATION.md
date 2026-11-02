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
# Reproducibility checks

Run with Python 3 and only its standard library:

```sh
python3 verify.py
```

Observed output from the accompanying source file:

```text
VERIFY_OK literal_parameter_cases=24 distinct_square_roots=861 formal_identity_coefficients=780 q=2..8
```

The literal test enumerates indexed subsequences of each host and collects the distinct roots of even-length subsequences whose halves agree; a separate candidate enumeration uses the proved weak-descent threshold. It checks actual root sets, not merely equal totals. The cases are \(q=2\) through \(k=7\), \(q=3\) through \(k=5\), \(q=4,5\) through \(k=3\), and \(q=6,7,8\) through \(k=2\), all periods from \(1\) to each bound. A distinct transfer-state program computes the weak-descent cost distribution for each root length, checks exact algebraic coefficients in the cleared rational identity for \(q=2,\ldots,7\), \(k\le12\), and root length \(m\le9\), including zeros.

This is exhaustive only within the enumerated parameter windows. The uniform theorem beyond these windows follows from the printed proof, not computational extrapolation. No external independent audit has been carried out.
