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
# Reproducible verification and limits

Execute `python3 verify.py` with Python 3 and no third-party dependencies. The script builds \(Z_n\) from \(1+\nu_2(j)\), independently from the substitution recursion used in the proof. It compares direct sorting of all full rotations and sentinel-terminated suffixes through \(n=9\), then independently implemented cyclic and suffix-doubling algorithms through \(n=16\), including comparison of the order of odd-position rotations with the parent sentinel-suffix array. It also checks the exact small cases and linear run count.

Actual observed output:

```text
VERIFY_OK zimin_BWT direct_cyclic=9 direct_sentinel=9 independent_doubling_levels=16 odd_rotation_suffix_order_levels=15 max_level=16 max_word_length=65535 max_cyclic_runs=31
```

Both formulas have been checked through \(n=16\), the largest source word having \(65{,}535\) symbols. These finite tests cannot establish the claims for every \(n\); the induction and odd-rotation order comparison in `RESULT.md` provide the mathematical proof. There is no externally performed independent audit.
