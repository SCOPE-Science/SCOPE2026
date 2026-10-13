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

The proof is symbolic and unbounded. The key identity is
\[
\gcd(k,\alpha)=\gcd(\gcd(k,L),\alpha)\quad\text{whenever }\alpha\mid L.
\]
The count of parameters with \(\gcd(k,L)=d\) in one complete block is exactly \(\varphi(L/d)\). Exactness of the period follows from the unique maximal gcd condition, and the mean follows from the finite gcd-sum identity.

`verify.py` exhausts every ordered exponent tuple of support size \(1\) through \(4\), with each exponent in \(\{1,\ldots,8\}\). It verifies the projection formula, full weighted distribution, extrema and their multiplicities, the absence of a smaller divisor-period, and the first-moment formula. The recorded output is:

`VERIFY_OK exponent_tuples=4680 parameter_checks=323280 max_L=840 support_max=4 exponent_max=8`

The computation is a regression check only; it is not an exhaustive proof over all exponents.
