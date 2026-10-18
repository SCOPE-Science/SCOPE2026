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

Execute `python check.py` using Python 3 with NumPy and SciPy. The script produces `PASS: 1520 finite matrix/formula/asymptotic assertions` and the example trace coefficients. Exact finite matrix coordinates are calculated separately from the derived weight expression. It also numerically checks direct sums of squares against the exact Hilbert--Schmidt identity, approximate Haar-periodic phase residues against finite geometric sequences, and the boundary-layer norm maximum.

The proof of the infinite trace-norm residues requires weighted equidistribution and a summable exponential tail, not merely finite numerics. The phase is fixed before taking the radial limit. The published source comparison does not establish exhaustive bibliographic uniqueness. Independent assessment has not been performed.
