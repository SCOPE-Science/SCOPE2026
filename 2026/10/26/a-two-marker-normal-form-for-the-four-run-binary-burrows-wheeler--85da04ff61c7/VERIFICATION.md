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

# Verification of the sentinel-BWT theorem

The supplied standalone `verify_bwt.py` uses Python 3.9 or later. Execute `python verify_bwt.py` in the same directory as the six scientific files; there are no external dependencies.

The program sorts **literal suffixes** of \(0^a1^b0^c1^d\$\), obtains their preceding characters and computes the run count independently of the arithmetic normal form. It checks full BWT word equality and count equality on all \(8^4=4096\) positive quadruples with components at most eight, then checks 1000 deterministic random quadruples with components as large as 150. It tests the nine-run equality criteria and the reversal lower bound throughout the complete small box; it enumerates every positive composition at lengths \(4\) through \(28\) to verify the exact finite maxima, coefficient formula, and generic eight/nine cases. It also independently checks the ratio-attaining witness \((a,b,c,d)=(3,3,1,2)\).

Observed output from the packaged script:

```
VERIFY_OK direct_suffix_quadruples=4096 random_large=1000 complete_length_censuses=4..28 nine_run_generating_function=true reverse_ratio_witness=9/4
```

The code is an executable finite consistency check, not a replacement for the proof over arbitrary positive integers. In particular, the generating function and limiting law are analytically established in the proof; no numerical extrapolation has been used as an infinite certificate. Independent audit has not been performed.
