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

# Reproducibility and verification

The claim is proved analytically for every integer \(n\ge2\) using the explicitly inverted tridiagonal matrix \(L_{P_n}+2I\), a signed classification of rung and rail electrical currents, and inequalities that compare every absolute projection-column sum. Section 5 of `RESULT.md` proves that no rail column maximizes at lengths at least three, and Section 6 proves both sharp family suprema and strict cut-versus-cycle dominance.

The standalone `check_ladder_endpoint.py` uses exact rational grounded-Laplacian inversion and independently reconstructs every cut and cycle column in ladder lengths \(2\) through \(12\). It checks all four candidate current formulas, both global norms, equality cases, and strict dominance. The actual local execution completed with:

`LADDER_ENDPOINT_EXACT_OK graphs=11 checked_projection_columns=209`

The checker requires Python 3 with SymPy and can be replayed as `python check_ladder_endpoint.py`. Finite verification is not an exhaustive proof of the unrestricted theorem. No independent audit has been performed.
