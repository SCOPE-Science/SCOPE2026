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

# Reproducible checks
Run `python3 verify.py` with Python 3 (stdlib only) from the directory containing the embedded files. Its recorded output is `verification_output.txt`. It directly computes the power-residue set modulo each finite power of two, iteratively forms the complete sumset with the specified number of summands, and checks exact equality with the theorem's recursively predicted residue set and cardinality. The 452 test configurations cover the exponents 6, 8, 10, 12, 14, 16, 20, 24, 32; selected subthreshold summand counts; and moduli from 2 to 4096. A passing finite test does **not** imply the infinite theorem; the proof uses the exact odd-unit power subgroup, disjoint parity branches, and Haar scaling.

The proof does not compute tuple multiplicities, solve odd-exponent or odd-prime cases, or claim independent certification. The review recorded separately is a self-review only.
