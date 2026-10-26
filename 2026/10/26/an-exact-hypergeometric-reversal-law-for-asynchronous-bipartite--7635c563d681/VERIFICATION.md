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

# Computational verification

Run `python verify.py` with a standard Python 3 installation; no third-party libraries are needed. It checks the exact hypergeometric first-flip conditional formula against an independently coded absorbing-state Markov recurrence for \(784\) initial-count states over the \(16\) ordered sizes with each part in \(\{3,5,7,9\}\), verifies three exact sample values, and enumerates all labeled initial binary profiles of three small network sizes for their total inversion probabilities.

Observed output:

```
K_{3,3}: inversion=9/160 approximately 0.0562500000
K_{3,5}: inversion=131/1792 approximately 0.0731026786
K_{3,9}: inversion=233/2048 approximately 0.1137695312
K_{5,7}: inversion=5233/67584 approximately 0.0774295691
K_{7,21}: inversion=8970593/67108864 approximately 0.1336722523
K_{11,33}: inversion=8007083634787/57174604644352 approximately 0.1400461566
PASS 784 conditional cases, 3 exhaustive binary-profile tests, 3 rational sample checks
```

These checks have finite range, do not constitute a machine proof of universal formulas, and do not establish originality. The proof in RESULT.md supplies the infinite-domain argument. No independent audit or validation has been performed.
