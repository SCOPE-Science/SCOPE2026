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
Run `python3 verify.py`.

The checker directly enumerates divisors and compares the definition of \(E_s(n)\) against
\[
E_s(n)=\sigma_s(m)\left(\sum_{j=1}^{v_2(n)}2^{js}-1\right)
\]
for representative values \(s\in\{-2,-1,-1/2,0,1/2,1,2\}\) and all \(1\le n\le5000\).

It also checks the exact sign cases, including \(A(-1/2)=2\). As a separate regression, it computes the summatory difference through \(x=200000\) for several negative values of \(s\) and compares the normalized value with \((2^s-1)\zeta(1-s)\).

The finite checks are not used for exhaustiveness. The theorem follows from the exact divisor decomposition and the absolutely convergent summatory rearrangement for \(s<0\).

A successful replay prints `VERIFY_OK`.
