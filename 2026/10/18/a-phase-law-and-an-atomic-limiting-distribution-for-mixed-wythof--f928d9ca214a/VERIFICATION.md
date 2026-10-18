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

# Reproducibility and proof boundary

The companion `verify.py` executes with Python 3.10+ and only the standard library. It builds exact lower-Wythoff membership indicators using integer square roots, computes their exact convolution with the complementary upper-Wythoff indicators for all integers through \(8192\), and independently enumerates the literal lower-plus-upper Beatty pairs through \(2048\). The two independent counting procedures agree at every checked input. The program checks the first eleven values of OEIS A259598, calculates phase residuals, and compares the finite sample mean with the derived limiting first moment.

Run command: `python verify.py`

Observed output from the included source:

```
VERIFY_OK exact_convolution_to=8192 pair_enumeration_to=2048 min_phase_error=-1.850303 max_phase_error=1.715518 finite_mean=0.235794222 limit_mean=0.236067977
```

All computations are finite and supportive only. The uniform \(O(\log(n+1))\) error is proved by irrational-rotation interval discrepancy via continued fractions, not by enumeration. The limiting distribution and atom are derived using equidistribution and pushforward of Lebesgue measure, not numerical fitting. The same source `verify.py` is embedded alongside this document. Independent review remains unperformed.
