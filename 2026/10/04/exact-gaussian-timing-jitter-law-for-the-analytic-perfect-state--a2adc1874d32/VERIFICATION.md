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

`verify_gaussian_timing.py` independently reconstructs the small-chain single-excitation Hamiltonian and checks its endpoint amplitude against the closed \(J_x\)-rotation formula.

It then compares the exact finite Gaussian average
\[
\mathcal P_m(s)
=
4^{-m}
\left[
\binom{2m}{m}
+
2\sum_{k=1}^{m}
\binom{2m}{m-k}e^{-k^2s^2/2}
\right]
\]
with direct numerical Gaussian integration.

The replay also verifies monotone decrease, the universal
\[
s=c/\sqrt m
\]
profile, the fixed-\(s\) theta-series constant, and the asymptotic target-jitter threshold.

The computations are finite checks. The infinite-size statements are proved analytically in `RESULT.md` by dominated convergence and central-binomial asymptotics.

No independent audit has been performed.
