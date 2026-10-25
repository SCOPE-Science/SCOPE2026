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

# Verification details
The proof in `RESULT.md` derives all-dimensional facet support distances, two-level vertex distance shells, strict maximizing integer cardinality, and exact isotropic John/Löwner contact certificates. `check.py` is a standalone Python program using `fractions.Fraction` and `math.comb`. It performs exact-rational full-vertex checks for dimensions \(m-1\) with \(3\le m\le10\), including strict comparison of all integer shells, both frame identities, and a separate maximizing-index check for \(11\le m\le25\). It returned a PASS message when executed on the included file. Finite execution does not establish the theorem beyond the tested range: the all-dimension justification is the analytic proof in `RESULT.md`.

The geometric normalization is the intrinsic metric on the hyperplane \(\sum_i x_i=1\), not the distorted Cartesian coordinates sometimes used to illustrate a tetrahedron. The source publication identifier and date are arXiv:2606.02087v1, 1 June 2026. The source's three-dimensional facet distance and its entire vertex list are acknowledged prior contributions; ellipsoid optimality and the residue contact classification are the claims checked here. No independent audit has been performed.
