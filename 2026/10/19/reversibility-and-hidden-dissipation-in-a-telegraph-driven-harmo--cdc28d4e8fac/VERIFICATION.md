---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The original headline is correct, but the purported all-orders identity in frozen RESULT.md line 36 is false as written: it sorts the reflected times while keeping the output coordinates in their original order. At equal rates take times (0,epsilon,3epsilon); the first two coordinates on the two sides would have covariances at lags epsilon and 2epsilon, respectively. Their diagonal covariance has derivative -kq at zero, so they differ for sufficiently small epsilon. repairs/4/RESULT.md gives the complete corrected statement with reflected times in their corresponding coordinate slots. For the repaired claim, conditional Gaussian stationarity follows from the orthogonal fundamental matrix, and sign-chain coalescence plus contraction gives uniqueness. The jump adjoint keeps the rates by detailed balance; its diffusion component reverses rotation. Equal-rate sign conjugacy gives the corrected path identity, whereas the derivative of the antisymmetric lag covariance is 2D omega (b-a)/(k(a+b)), proving necessity. At fixed sign parity the drift difference is 2 omega S JX and the likelihood factor is 1/(4D), yielding 2 omega^2/k. The conditional-mean semigroup obstruction uses m'(0)=0 and m''(0)=-omega^2. The event of exactly one jump gives the random phase a continuous component, making the conditional Wick contribution strictly positive at any positive lag. The rotating frame removes the skew drift pathwise without changing the conditional Brownian law, proving the equilibrium radial alias for all rates. Inspected frozen VERIFICATION.md and verify.py; its checks corroborate identities but do not check the faulty time ordering or replace the analytic audit. No uploaded script was executed.

## originality

PASS

Best of available evidence for the repaired, model-specific result only. Neither masking irreversibility by a symmetric hidden telegraph variable nor the fixed-drive OU entropy coefficient is claimed as new. The closest compared statements do not cover the sharp classification together with the complete radial law and explicit position diagnostics for a telegraph coefficient multiplying JX.

## value

PASS

The sharp boundary resolves when ordinary trajectory reversal can see a hidden circulation in a natural linear switching model. The full radial-law equivalence and explicit unequal-time squared-coordinate statistic separate three genuinely different observation capabilities: neither radius nor time-antisymmetry reveals the symmetric hidden drive, but even multi-time position statistics can identify its strength under the model. This is a concrete limitation on interpreting entropy diagnostics, not simply a restatement of the general hidden-state principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
