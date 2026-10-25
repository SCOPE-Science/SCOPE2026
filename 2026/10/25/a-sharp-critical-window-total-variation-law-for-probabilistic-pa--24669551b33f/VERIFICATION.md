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

# Verification record

The provided `check.py` performs these checks using only exact rational arithmetic: exact normalization and reflection of the Abel weights, the decomposition into symmetric and antisymmetric terms, the finite cancellation identity, and an independent recursive enumeration over preference vectors and all coin-search branches for sizes up to five and forward probabilities \(0\), \(1/4\), \(1/2\), \(3/4\), and \(1\).

Observed result: **790 exact assertions passed**. Additional floating-point diagnostics used SciPy's log-gamma function for sizes \(100\), \(1000\), \(10000\), and \(100000\). At \(n=100000\), observed values were \(n\,\mathrm{TV}_{p=1/2}=0.95619706\), \(\sqrt n\,\mathrm{TV}_{p=1}=0.79420057\), and \(n\,\mathrm{TV}_{p=1/2+1/\sqrt n}=2.04423690\). The corresponding proved limits are \(1\), \(\sqrt{2/\pi}\approx0.79788456\), and \((1+\sqrt{1+32/\pi})/2\approx2.17226765\). Convergence is slow because the finite boundary layers have heavy tails; these diagnostics are not the proof of the limits.

Reproduce with `python3 check.py`. NumPy and SciPy are optional and only needed for asymptotic diagnostics. The unrestricted assertion is justified by the factorial/Stirling argument and endpoint mass decomposition in `RESULT.md`, not by finite numerical sampling.

Independent audit: not performed. No external certification is asserted.
