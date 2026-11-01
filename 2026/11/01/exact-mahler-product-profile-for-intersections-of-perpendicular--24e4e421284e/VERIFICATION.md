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

The exact statements are for all real \(t\ge1\). The analytic argument in `RESULT.md` proves the theorem, including strict monotonicity and endpoint expansions. All numerical work below is finite corroboration only.

The included standalone program `check.py` has no data-file dependency. Running `python check.py` with installed SymPy and SciPy checks the symbolic derivative factorization, four symbolic endpoint limits/coefficients, independent radial quadrature for primal area, independent support-function quadrature for polar area, agreement of two exact product formulas, elementary bounds, and strict ordering over 129+ finite parameter values. The observed execution completed 649 checks with no errors.

The polar-area quadrature is analytically independent of the convex-hull Green computation: on the fundamental sector its support function uses the active ellipse for angles below \(\arctan(t^{-2})\) and the diagonal corner above that angle. This cross-check is sensitive to an incorrect segment factor, polarity normalization, or angular transition.

No external independent audit or mathematical certification has been performed. The originality assessment is a bounded targeted literature comparison and does not establish global historical priority.
