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

# Verification methods and limits

Execute `python3 verify.py` with Python 3.9 or later. The script is self-contained, deterministic, and uses only `collections` and `itertools`. It reconstructs the literal cyclic factor multispectrum for each weight-three necklace (not merely an abbreviated count statistic).

The executable checks all rotation classes through length 25, all read lengths through the claimed sharp threshold, all chiral classes through length 50 at the proposed individual boundary, three residue-class families of sharp witnesses for parameters 2 through 64, and the constructive two-branch read decoder through length 30. The computed proof-support output is:

```text
VERIFY_OK exhaustive_necklaces=772 exact_all_length_thresholds_n=3..25 chiral_orientation_cases=5944 explicit_sharpness_pairs=189 decoder_cases=1356 spectrum_comparisons=22010
```

These finite checks detect many possible off-by-one, boundary, and factor-multiplicity errors. They are not exhaustive over unbounded length. The all-length proof is the combinatorial factor-count analysis in `RESULT.md`; it does not depend on any extrapolation from the test output.
