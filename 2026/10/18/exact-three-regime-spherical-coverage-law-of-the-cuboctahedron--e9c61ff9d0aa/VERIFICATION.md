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

# Verification and reproducibility

Run `python check_cuboctahedral_cap_law.py` with Python 3, NumPy, SciPy and mpmath available. The final scientific package contains the complete checker; it uses only deterministic integer coordinate enumeration and numerical library routines, with a fixed scrambled Sobol seed. Successful execution prints `CUBOCTAHEDRAL_SPHERICAL_CDF_OK vertices=12 edges=24 triangles=8 sample=262144`.

The exact incidence checks enumerate every unordered site pair and every candidate triangle and four-clique, so these finite combinatorial identities are exhaustive. The checker independently integrates lens areas by spherical polar quadrature; compares the derived cumulative distribution with 262,144 directions; and uses 80-digit arithmetic to test the first triple-overlap and final uncovered-area coefficients. These numerical integrations and sampling comparisons only corroborate the mathematical proof: they do not certify closed formulas, historical originality, or all asymptotic cases by themselves.

The proof in `RESULT.md` includes the complete pair/triple inclusion–exclusion argument, cap intersection area formulas by spherical Gauss–Bonnet, the sharp covering-radius Voronoi bound, and the two local tangent-plane asymptotic derivations. No numerical or probabilistic sampling is used to claim that a finite test proves an infinite law. Independent audit status remains unperformed.
