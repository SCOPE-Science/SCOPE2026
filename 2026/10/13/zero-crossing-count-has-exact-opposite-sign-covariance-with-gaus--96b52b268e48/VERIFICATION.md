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

The theorem is proved analytically in `RESULT.md`; the executable check is supplementary and does not replace the proof.

Running `python verify.py` performs three independent finite checks:

1. It evaluates \(2\int_0^{10} z^2\phi(z)\Phi(-az)\,dz\) by high-resolution Simpson integration for seven correlations and compares it with the closed bivariate formula. The omitted normal tail is far below the stated numerical tolerance at this cutoff.
2. On 632 pairs \((n,\rho)\), it compares the final closed covariance formula with the direct sum of all edge-to-site geometric covariance contributions.
3. On 731 cases, it verifies the opposite-sign law for nonzero \(\rho\) and exact zero covariance at \(\rho=0\).

The replay used the packaged `verify.py` from the same package path and returned:

`VERIFY_OK`

with counts `local_integral_checks=7`, `closed_vs_edge_sum_checks=632`, and `sign_and_independence_checks=731`.

Limits: these numerical checks test representative finite instances only. The universal quantifiers in \(n\), \(\rho\), and \(\sigma^2\) are justified by the symbolic proof, especially the Gaussian conditional-second-moment identity and the finite geometric summation.
