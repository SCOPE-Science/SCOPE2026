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

# Reproducibility

From the directory containing this document, run `python3 checker.py`. The executable requires Python 3.8 or newer and no third-party packages. It computes periodic autocorrelation by integer arithmetic, enumerates the full anchored finite domains at prime orders \(5,7,11\), and groups by the explicitly enumerated translation-reflection-sign orbits. At order \(11\) it also enumerates all \(5280\) full-support/sign assignments independently of anchoring and checks that every canonical orbit is represented by the anchored census. It compares each of the five exceptional profiles exactly, and verifies that there are precisely five doubleton fibers and no larger fibers.

Observed completed run:

```text
p=5 normalized=32 spectra=6 orbits=6 ambiguous_spectra=0
p=7 normalized=160 spectra=26 orbits=26 ambiguous_spectra=0
p=11 normalized=960 spectra=135 orbits=140 ambiguous_spectra=5
CHECK_PASS exact enumerated base configurations = 1152
```

The pairwise integer Laurent autocorrelation of the universal witness agrees exactly. Tests at finitely many additional primes check the witness but do **not** prove the infinite-prime assertion: that rests on the exact reciprocal-factor identity and the position/sign argument in `RESULT.md`. This document does not assert an independent audit or external formal certification.
