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

The self-contained accompanying `verify.py` requires Python 3 and `sympy`, and runs without a network connection or access to external data. It checks exact rational-function identities, not floating-point approximations.

- The first identity transforms the quadratic equation of the fourth-shift series into the first parametric triple at \(t=2\).
- The next three identities verify the entire parameter loop \(\mathcal S_1(t)\to\mathcal S_2(t)\to\mathcal S_3(t)\to\mathcal S_1(t+2)\), with an indeterminate \(t\). Assertions verify each input's leading \(q\)-term, each prescribed denominator truncation, normalization, polynomiality, and the exact successor triple.
- An independent Taylor-series recurrence computes \(50\) coefficients and evaluates every Hankel determinant for sizes \(0,1,\ldots,22\), comparing them to the all-index closed formula.

Successful execution prints:

```
SYMBOLIC_NEXTABC_OK initial_and_three_generic_transitions
INDEPENDENT_HANKEL_OK sizes=0..22 coefficients=50
```

The general Hankel-determinant product identity is taken from Han--Pedon (2026), Theorem 2.2; the code does not reprove it. The infinite part of the new proof is the exact symbolic family of transitions together with that general theorem. The finite determinant checks cannot establish an all-index statement on their own. No independent audit has been performed.
