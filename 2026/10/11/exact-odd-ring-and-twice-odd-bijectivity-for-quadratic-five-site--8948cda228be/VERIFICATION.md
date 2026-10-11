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
# Reproducibility and verification

## Build and run
From the directory containing `verify.c`:

```sh
cc -std=c11 -O2 -Wall -Wextra -pedantic verify.c -o verify
./verify
```

Expected line:

`VERIFY_OK: 65472 exact-degree-two rules; odd=32; 2mod4=8; finite counts n9=42 n10=8 n15=32; two independent graph methods agree.`

## Checked mathematical invariants
The source program enumerates each of the 65,472 coefficient masks with nonzero quadratic part, independently computes two strong-component decompositions, and tests exact edge-potential congruences and cycle-period gcd constraints on a 256-vertex equal-output pair graph. Both graph procedures agree for every case and recover precisely the explicit 32 and eight accepted mask sets. The program also enumerates all finite states of rings of size 9, 10 and 15 and compares direct local-rule outputs to test bijectivity.

The full universal quantification over arbitrarily large ring lengths follows from the graph walk-period theorem and the exhaustive finite classification, not just those three direct tests. The eight classical odd-ring bijective elementary rules are a published theorem, not an independent discovery or external certification of the new classification.

## Limitations
The code requires a C11 compiler providing the commonplace `__builtin_ctz` intrinsic (GCC or Clang) and enough memory for fixed-size arrays; no Internet, input files or nonstandard packages are required. Independent audit and independent scientific validation have not been performed. The motivational preprint's full text was not available for priority comparison.
