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

The exact-arithmetic program `verify.py` independently enumerates every four-column Fourier minor at orders \(7,8,9,11,16,25,27,32,49,64\). It computes cyclotomic reductions by integer coefficient comparison and matches all 915,793 column selections against the theorem's two binary orbits, fifth-power orbit, or empty defect class. It separately checks all 625 ordered four-residue tuples modulo five for the residue lemma and fifth-root identity. Its recorded output is in `verification-output.txt`.

These finite enumerations corroborate the symbolic proof. The infinite-family assertion relies on the Vandermonde--Schur determinant factorization, cyclotomic evaluation at one, prime-power field decompositions, and an exact five-residue combinatorial argument. No untested numerical extrapolation or independent validation is asserted.
