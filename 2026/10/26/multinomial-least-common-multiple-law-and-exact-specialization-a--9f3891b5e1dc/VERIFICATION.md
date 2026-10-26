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

# Exact checks and limits

`python3 verify_multinomial_lcm.py` was executed in the package directory using Python 3 without third-party packages. Output:

```
VERIFY_OK row_compositions=42310 q_factorizations=2610
```

The first exhaustive loop covers all ordered compositions for \(1\le n\le18\) and \(2\le r\le\min\{5,n\}\). For each modulus \(2\le d\le n\), it compares the actual maximal floor deficit with the closed exponent. For every prime \(p\le n\), it compares the actual largest valuation of the ordinary multinomials with the sum of the predicted prime-power exponents. A separate exact-integer loop directly evaluates q-factorials and cyclotomic factors at \(q=2,3\) for \(n\le10\), checking factorization of each selected Gaussian multinomial.

Finite computations do not establish (1) or (2) for arbitrary \(n,r\). The proof of (1) depends on residue-sum attainment; that of (2) depends on the digit-inequality closure lemma and Legendre's formula. There was no independent validation or external certification.
