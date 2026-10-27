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

# Verification details

From the extracted package root, run `python3 verification/verify.py` with standard Python 3 and no third-party packages. The program calculates coefficients of the odd strongly unimodal generating function modulo four using exact polynomial arithmetic, independently factors each odd index's associated integer for the published residue criterion, and enumerates the two arithmetic prime-square branches using a prime sieve.

In the verified execution the program printed:

```
COEFFICIENT_CLASSIFICATION_OK 1250 odd indices
EXACT_COUNTS 100 7 14 21
EXACT_COUNTS 1000 52 100 152
EXACT_COUNTS 10000 398 740 1138
EXACT_COUNTS 100000 3061 5724 8785
VERIFY_OK
```

The two arithmetic family counts in each row are disjoint. For \(X\le10000\) the parametric count is separately compared with a direct integer-factor classification. This checks the algebraic and implementation boundaries for finite inputs; it does not certify an asymptotic for infinitely many inputs.

The infinite proof relies on the explicitly identified published coefficient-residue theorem, fixed-modulus PNT and a uniform two-term prime-counting expansion. The argument independently bounds the higher prime powers and inadmissible shared prime factors. The arithmetic constants are recomputed from restricted Dirichlet series and their logarithmic derivatives. Independent mathematical validation of that proof has not been performed.
