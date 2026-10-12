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

# Reproducible checks and their scope

Run `python3 verify.py` with Python 3.8 or newer. The script independently builds the complete polynomial from the zero-, one-, and two-hub closed formulas. For each \(3\le n\le6\), it enumerates all \(2^{\binom n2}\) edge subsets and classifies them without using hubs, by checking every possible two-vertex cover. It also compares every coefficient in the high-cardinality identity for \(5\le n\le30\), and checks minimum-cardinality counts.

Observed output:

```
VERIFY_OK exhaustive_n=3..6 subsets=33864 top_band_n=5..30 endpoints_and_coefficients=passed
PETERSEN [(4, 10), (5, 72), (6, 140), (7, 110), (8, 45), (9, 10), (10, 1)]
```

For an independently written C99 implementation on \(n=7\), run `cc -O2 -std=c99 verify_n7.c -o verify_n7 && ./verify_n7` and compare its hardcoded expected coefficient vector (calculated from the closed polynomial) against its direct two-cover enumeration:

```
VERIFY_N7_OK all_2097152_subsets_and_22_coefficients
```

The two exhaustive programs enumerate \(2,131,016\) individual edge subsets in total. These finite checks are not an infinite proof. The all-order result follows from the explicit component and degree classification and the uniqueness argument proved in `RESULT.md`. Independent mathematical audit has not been performed.
