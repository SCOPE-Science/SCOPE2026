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

The formal variable counts codewords, two at a time because the complement has no fixed letters and the word length is odd.

Execute in the same directory:

```
python3 verify.py
python3 crosscheck.py
```

Successful local replay produced `VERIFY_OK` and `CROSSCHECK_OK`. `verify.py` expands the proved all-alphabet polynomial for \(h=1,\ldots,9\), validates its top coefficient, and constructs valid extremizers. `crosscheck.py` independently enumerates all pairwise compatible reverse-complement orbits for alphabet sizes \(2,4,6\) and counts every clique, without invoking the generating formula. Its exact distributions are available in `small_spectra.csv`.

The all-alphabet result follows from the combinatorial argument in `RESULT.md`; computational checks cover finite parameters only. No outside scientific audit has been performed. The full source-comparison details and remaining priority uncertainty are in `REVIEW.md` and `AUDIT.json`.
