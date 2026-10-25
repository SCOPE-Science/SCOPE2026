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

# Reproducibility and verification

Running `python verification.py` with Python 3.10 or newer yielded `PASS: 19109 finite exact or path checks`. The script verifies invertibility of the Pascal parity map through length eight, at least \(2^{w(t)-1}\) differing binomial parity bits for all \(0\le s<t<193\), exact rational pair correlations for seven independent nonidentically distributed Bernoulli coefficients, and pathwise occupation identities with a seeded random input. All checks passed in the recorded run.

These finite computations do not prove a.s. Cesàro convergence or weak functional convergence. Those assertions are supported by the renewal strong-law argument, Lucas' theorem and summable spatial second-moment bound, and the martingale functional CLT and its necessary predictable-bracket condition. The coefficient-probability restriction, the precise count process, and the degeneration at correlations \(\pm1\) are material scope conditions. No independent audit has been performed.
