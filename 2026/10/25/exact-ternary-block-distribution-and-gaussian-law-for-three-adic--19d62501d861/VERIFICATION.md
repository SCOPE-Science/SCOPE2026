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

# Reproducible arithmetic verification

Run `python3 verify.py` in the same directory. Only Python's standard library is used. The program computes factorial valuations by Legendre's formula, then exhaustively counts \(\nu_3(C_n)\) for every \(0\leq n<3^L\) and \(0\leq L\leq9\). It independently obtains the predictions from the polynomial recurrence and verifies exact rational first and second moments. It also compares the carry formula with factorial valuations for the first 10000 indices.

Observed successful output:

`VERIFY_OK: 29524 valuation-census instances through L=9; 10000 digit-carry comparisons; exact rational moments and polynomial normalization`

The verifier separately checks all block-polynomial normalizations up to \(L=14\), nonnegative coefficients on the exhaustively tested blocks, exact support \(\{0,\ldots,L-1\}\), and the \(3\cdot2^{L-1}\) zero-valuation count. These finite checks do not validate the infinite identities or central limit theorem without their proofs. Independent mathematical validation has not been performed.
