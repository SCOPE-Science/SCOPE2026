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
# Verification

The proof was checked at three levels.

1. **Exact index algebra.** For \(k=2^m\), substitution \(r=m-j\) converts every factor in the source product exactly to \(\binom{2^{r+1}}{2^r}\), and the exponent sum is exactly \(2^\ell-1\).
2. **Asymptotics.** Stirling's formula gives the fixed-level entropy rate. For growing levels, the elementary bounds \(\binom{k}{k/s}\leq(es)^{k/s}\) and \(\binom{2n}{n}\leq4^n\) produce the stated \(O(\sqrt{k\log k})\) logarithmic upper bound when \(s=2^\ell\asymp\sqrt{k\log k}\).
3. **Replay.** `artifacts/verify.py` checks the exact identities for many dyadic sizes, numerically confirms convergence to the fixed-level rate, and checks the shrinking normalized exponent for a growing-level sequence. A successful replay prints `VERIFY_OK`.

The finite replay is not used as proof of the asymptotic statements. No verification here establishes the completeness of the source algorithm's cost accounting; that is explicitly outside the claim.
