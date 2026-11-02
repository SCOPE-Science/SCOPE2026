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
# Reproducible checks and boundaries

Run `python3 verify_mobius.py` from the directory containing this file and that checker. Python's standard library is sufficient. The checker uses exact fractions and performs: (i) the two proposed invariant-column norm evaluations and dual signed inequality for every integer width from 10 through 150; (ii) explicit rational incidence-matrix and projection reconstruction for widths 10 through 18; (iii) exact zero-divergence, idempotence, and every projected edge-column norm check. The actual run completed with:

`CHECK_OK rational_formula_orders=141 exact_matrix_projection_orders=9`

All-dimensional correctness rests on the analytic proof in RESULT.md: especially the dihedral reduction, the variable-cancelling signed certificate, and two complete coefficient regimes. No finite script proves the infinite quantifier. None of these checks is an independent audit or external certification.
