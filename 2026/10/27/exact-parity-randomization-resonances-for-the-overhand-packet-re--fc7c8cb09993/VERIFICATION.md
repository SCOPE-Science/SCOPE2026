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
# Verification of exact parity resonances

Run the pure-Python script `parity_verify.py`. It independently enumerates each subset of the \(n-1\) gaps for \(1\le n\le10\) and computes the signed permutation parity directly from its packet sizes. For each of four rational cut probabilities \(1/5,1/2,3/4,9/10\), it compares the exhaustive weighted expectation with the polynomial recurrence. The recorded successful output is in `verification_output.txt`: 40 exact-rational assertions pass, with two displayed sanity checks.

The all-size root count and limiting density are certified by the trigonometric proof in RESULT.md: the phase is strictly increasing and spans an explicitly computed interval, and the inverse parameter transformation is differentiable and strictly monotone. Neither root count nor its limiting density is inferred from finite enumeration. The physical-convention sign adjustment uses the deterministic global reversal.

Limits: no external independent audit; no direct historical full-text comparison for the 1989 overhand mixing article; no claim of full-permutation stationarity when parity is stationary.
