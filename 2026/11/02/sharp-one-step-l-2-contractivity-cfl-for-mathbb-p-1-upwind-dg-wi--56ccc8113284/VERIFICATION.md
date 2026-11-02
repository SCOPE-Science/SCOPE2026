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

# Reproducibility checks

Run `python VERIFY.py` from this directory using Python 3's standard library. It checks the two central polynomial identities in `RESULT.md` exactly, with thirteen rational sample nodes in each variable and degree bounds establishing them identically rather than approximately. It derives the entire tensor-Bernstein coefficient table by rational interpolation and exact power-to-Bernstein conversion and confirms all entries are strictly positive. It also brackets the unique critical quartic root and tests the relevant factor signs. The recorded output is `VERIFY_OK 562 threshold_interval=(0.186457,0.186458) min_Bernstein 1232/3125`.

These computations certify algebraic steps of the analytic argument; the all-grid conclusion also relies on the explicitly written Hermitian positive-semidefiniteness and Fourier-density arguments. No external independent audit has occurred. The result does not address nonlinear convex entropies, higher-degree DG, nonuniform grids, numerical roundoff, or full historical priority.
