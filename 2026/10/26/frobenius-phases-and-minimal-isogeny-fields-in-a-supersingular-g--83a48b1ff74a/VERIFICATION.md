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

# Verification of the genus-six Frobenius classification

Run `python verify.py` in the same directory as this document. The checker uses polynomial-basis arithmetic over \(\mathbb F_2\), with exact irreducible moduli \(u^2+u+1\) and \(v^4+v+1\). Under these identifications, the chosen cube root is \(u\) in \(\mathbb F_4\) and \(v^2+v\) in \(\mathbb F_{16}\). The code enumerates all \(4\) or \(16\) affine abscissae and uses the absolute trace criterion to count points on each genus-two quotient; there is one rational point at infinity. It reconstructs the quartic Weil numerators, their genus-six products and the Jacobian orders. It separately compares the exact eigenvalue-exponent multisets of roots of unity to check extension degrees through \(120\).

Observed output:

```
QUOTIENTS 0 [(5, 33), (5, 33), (5, 33)] JAC 15625
QUOTIENTS 1 [(5, 33), (5, 9), (5, 9)] JAC 4225
QUOTIENTS alpha [(5, 33), (7, 21), (7, 21)] JAC 24025
QUOTIENTS alpha2 [(5, 33), (7, 21), (7, 21)] JAC 24025
ISOGENY_EXTENSION 0 1 3
ISOGENY_EXTENSION 0 alpha 20
ISOGENY_EXTENSION 1 alpha 60
VERIFY_OK
```

The completed mathematical proof additionally requires the standard connectedness/genus results for the Artin–Schreier cover, the character decomposition of cohomology and the Tate isogeny criterion. The script tests those consequences only through explicit numerical consistency; it does not independently prove these general theorems. The cyclotomic-order argument in `RESULT.md`, rather than the finite search bound, proves the infinite statement about every extension degree. No external or independent audit has been performed.
