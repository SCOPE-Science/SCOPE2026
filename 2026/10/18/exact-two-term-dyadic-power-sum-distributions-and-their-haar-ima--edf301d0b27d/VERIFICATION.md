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

# Reproduction and limits

Run `python3 verify.py` using a standard Python 3 interpreter. It independently enumerates residues of each \(d\)-th power modulo \(2^n\), convolves their frequency histogram, and compares each target with the closed recursion, for 44 complete residue distributions. Expected line: `VERIFIED 44 complete residue distributions`.

The exact proof uses the classical finite unit-group decomposition, explicit parity counts, induction through even/even divisibility by \(2^d\), and a geometric-series Haar computation. The verifier is finite evidence, not an exhaustive proof for arbitrary exponent or modulus. No independent audit has been performed.
