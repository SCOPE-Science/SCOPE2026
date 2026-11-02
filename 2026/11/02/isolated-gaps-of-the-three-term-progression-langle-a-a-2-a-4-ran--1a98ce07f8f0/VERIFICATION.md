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
# Verification of the isolated-gap classification

Run `python verify.py` using Python 3 with only its standard library. This checks all odd \(a\) from \(3\) through \(301\) inclusive. It independently builds membership up to the predicted Frobenius number using generators \(a\), \(a+2\), \(a+4\), enumerates actual gaps and their neighbors, and compares the full set of isolated gaps against the closed formula. It separately confirms the genus, Frobenius number, total isolated count, and both extreme isolated gaps.

Observed output:

```
PASS: 150 odd multiplicities 3..301
PASS: 1158925 directly enumerated gaps, 579425 isolated gaps
PASS: exact sets, genus, isolated counts, Frobenius bounds, and endpoints
```

The verified finite range does not establish the theorem beyond \(a=301\). The proof in `RESULT.md` is an exact analytic argument covering all odd \(a\ge3\); it requires only elementary number theory, modular residues, and counting. An independent audit of the proof has not been performed.
