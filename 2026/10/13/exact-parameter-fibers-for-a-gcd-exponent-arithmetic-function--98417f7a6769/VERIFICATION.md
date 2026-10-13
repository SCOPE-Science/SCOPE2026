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
The symbolic proof checks the exact fiber equivalence using unique factorization and the identity
\[
\operatorname{lcm}_i\gcd(e_i,\alpha)=\gcd(\operatorname{lcm}_i e_i,\alpha).
\]
It then derives the orbit size, the \(\varphi(L/d)\) fiber counts, and minimality of the period.

`verify.py` independently exhausts all exponent tuples with support size at most four and exponents from \(1\) through \(5\), and checks every parameter in one complete period. It reports:

`VERIFY_OK exponent_tuples=780 parameter_pairs=479656 max_exponent=5 max_support=4`

This finite computation is a regression check only; it does not establish the unbounded theorem.
