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

# Reproducible verification

The standalone `verify.py` is executable using Python 3.9 or later with no nonstandard packages. Run `python verify.py` alongside this document. The captured result in `verify_output.txt` reports `VERIFY_OK`.

It checks three exact difference-of-cubes factorization identities for every integer index from 1 to 500, the congruence needed for the coprime-factor argument, and for every admissible index through 400 computes both original Jacobsthal quotients by integer arithmetic and compares their gcd with the proposed common factor. There are 267 admissible indices in that range. It independently checks the order of 11 modulo 19 and the sharp exceptional case at index 1.

These computations prove only their finite checked assertions. The infinite result follows from the symbolic difference-of-cubes, cubic-root congruence, and polynomial gcd proof in `RESULT.md`; no probabilistic, extrapolated or software-only proof is asserted.
