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
# Reproducibility record

Execute `python3 verify.py` with Python 3 and the standard library only. The actual embedded verifier performs exact-rational coefficient checks for \((k,\ell)=(3,5),(3,7),(5,7)\) on all \(1\le n\le1000\), including equality between the exact Fourier coefficient and the normalized divisor-power expression and the previously known prime-detection positivity. It additionally tests \(30\) adjacent local prime-parameter monotonicity pairs; its observed output is `VERIFY_OK exact_coefficients=3000 monotonic_pairs=30`.

The mathematical proof is self-contained in `RESULT.md`. Its unbounded steps are the CRT limit for a fixed finite prime set; uniform absolute convergence of Euler tails for \(k\ge3\); a strictly monotone conditional prime-identity argument with infinitely many independent prime blocks; and an entropy/Mertens/zero-one/Hausdorff-cover argument. These analytical steps cannot be certified by a finite verifier. No independent external audit or validation has been conducted.
