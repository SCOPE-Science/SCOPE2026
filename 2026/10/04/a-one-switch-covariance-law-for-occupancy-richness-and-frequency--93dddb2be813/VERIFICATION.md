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

The proof is analytic and exact.

The accompanying checker independently recomputes the covariance in two ways. First, it uses the closed same-box/off-diagonal multinomial decomposition. Second, for a bounded grid it enumerates every allocation of \(n\) labeled balls to \(m\) boxes, computes \(K\) and each \(K_r\), and compares the exact rational covariance with the formula in `RESULT.md`.

On a larger parameter grid the checker verifies that:

- \(\operatorname{Cov}(K,K_1)>0\);
- \(\operatorname{Cov}(K,K_n)<0\);
- no covariance is zero;
- the sign sequence across \(r=1,\ldots,n\) has exactly one transition from positive to negative.

The all-parameter no-zero assertion is not based on that finite replay. It is proved in `RESULT.md` by the coprimality contradiction
\[
(m-1)^{n+k-1}=m^{n-1}(m-2)^k.
\]

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK formula_checks=80 brute_checks=80 singleton_checks=9801 nton_checks=9801 nozero_checks=499851 one_switch_checks=9801`.
