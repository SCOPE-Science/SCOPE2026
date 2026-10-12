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

# Exact verification notes

The standalone `verify.py` requires Python 3 and its standard library only. Run `python3 verify.py` in the directory containing this file. Its expected stdout is included verbatim in `verification_output.txt`.

The verifier independently constructs the Bernoulli sequence with exact `Fraction` arithmetic rather than inserting coefficients from the proof. For each integer moment from 2 to 20, it chooses an admissible prime, recomputes the polynomial of the sum over coprime residues, evaluates the polynomial at the first two prime powers and compares with a direct integer sum, checks the exact leading and lowest coefficient formulas, and verifies all Eisenstein coefficient valuations. For every pair of distinct moments in the same finite range, it computes the two reduced polynomials at a common admissible prime and performs exact polynomial division, confirming a nonzero remainder.

A complete proof is supplied in `RESULT.md`. Finite verification establishes neither the infinitely many exponent pairs nor uniqueness in outside literature. The infinite step rests on the proof of the polynomial-divisibility lemma and symbolic Eisenstein coefficients, which are independently explained in the proof.
