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

# Verification and scope

Run `python3 verify.py` using a standard Python 3 interpreter. The file is standalone and imports only `fractions` and `math`. It recomputes quadratic-binomial coefficients exactly as rational numbers, checks unique negative two-adic minima for \(58{,}800\) rational examples with odd squarepart multipliers, and evaluates the constructive cases for exponent one, even exponents, and odd exponents when the first radicand is divisible by four. The explicit \(m=8\), \(n=50\), \(b=3\) witness is checked.

Successful execution prints:

```text
VERIFY_OK squarefree_d=20 odd_k_rational_samples=58800 unique_negative_2adic_minima=58800 odd_b_even_k_constructions=480 even_b_constructions=900 exponent_one_constructions=180 b1_boundary=PASS example_8_50=PASS
```

These tests are finite consistency checks only. The proof of the unrestricted classification uses quadratic-field intersection and a unique minimal rational \(2\)-adic valuation for each odd exponent. It relies on no computational completeness assumption. A separate independent audit has not been performed.
