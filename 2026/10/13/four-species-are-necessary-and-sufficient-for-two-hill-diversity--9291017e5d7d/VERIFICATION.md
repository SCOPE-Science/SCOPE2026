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

# Reproducibility and scientific limits

The file `verify_hill_crossings.py` is standalone Python 3 using only the standard library. Run `python3 verify_hill_crossings.py`. The recorded output was:

```
VERIFY_OK witness_integer_moments=3 profiles_checked=950 ordered_pairs_checked=17047 padded_dimensions=4..9
```

The checker confirms that the two listed integer vectors each sum to \(10{,}000\), computes exactly their degree-two, degree-three and degree-four power-sum differences, and establishes the alternating signs. It additionally checks the signed count-function sign-variation bound across all positive nondecreasing compositions of each total below \(23\) for species counts \(2,3,4\); and checks preservation of the witness moments when common positive species are appended. Those finite checks do not prove the universal theorem, whose complete proof is in RESULT.md. In particular, neither sampled parameter values nor finite scans replace the Mellin-transform zero lemma. No independent audit has been performed.
