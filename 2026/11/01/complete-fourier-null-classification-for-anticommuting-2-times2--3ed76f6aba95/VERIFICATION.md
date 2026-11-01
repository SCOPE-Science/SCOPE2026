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

# Verification of the Fourier-null criterion
The analytic proof is given in `RESULT.md`. The accompanying standalone C++17 checker independently enumerates matrix-pair Fourier sums for small prime fields and checks the exact closed multiplier at additional frequencies. Use `c++ -O3 -std=c++17 check_antico_fourier.cpp -o check && ./check`.

Expected successful output:
```
EXACT_ANTICOMMUTATOR_OK p=3 frequencies=6561 zeros=384 direct_checked=6561
EXACT_ANTICOMMUTATOR_OK p=5 frequencies=390625 zeros=15360 direct_checked=411
EXACT_ANTICOMMUTATOR_OK p=7 frequencies=5764801 zeros=217728 direct_checked=0
ANTICOMMUTING_FOURIER_NULLITY_ALL_CHECKS_OK
```
The checker uses exact modular arithmetic and tests cyclotomic character sums by integer coefficient equality. For prime seven it verifies the exact multiplier and predicted-zero rule at every frequency, but does not enumerate all anti-commuting pairs for independent direct Fourier calculations; for prime five it directly checks 411 deterministic frequencies, and prime three is completely directly checked but excluded from the theorem. These tests do not independently certify the infinite prime-power theorem or the literature comparison.

An independent extension-field test can be run with `python3 check_gf9.py`. It constructs \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\) exactly and checks \(2850\) deterministic frequencies, including \(152\) samples of the predicted zero family. Its output is `EXACT_EXTENSION_FIELD_GF9_OK trials=2850 zero_family_hits=152`. This is a sampled finite test and does not prove the all-prime-powers theorem.
