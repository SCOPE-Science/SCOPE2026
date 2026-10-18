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

The exact finite-field Jacobian sieve flags 49,515 nonzero coefficient masks with genuine singular points over fields of degrees at most six. The remaining 16,020 masks form 252 projective-coordinate orbits; every orbit representative passed exact Jacobian unit-ideal Gröbner checks on all four affine charts. The incidence census was obtained by direct evaluation on the nine rational grid points, and the orbit/stabilizer counts were obtained under all 72 split-quadric automorphisms.

Replay the packaged programs in order: `python3 artifacts/sieve.py`, `python3 artifacts/census.py`, and `python3 artifacts/verify.py`. They must reproduce `artifacts/sieve_survivors.txt`, `artifacts/orbit_representatives.tsv`, `artifacts/stats.txt`, and the saved outputs; SymPy is needed for `artifacts/verify.py`. The positive Gröbner computations are logically essential: the bounded field sieve alone would not certify geometric smoothness. These checks were performed on the exact code and data embedded here. External independent validation remains outstanding.
