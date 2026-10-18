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

Run `python3 artifacts/verify.py` with Python 3.10 or newer and no third-party packages. It constructs the defining window over \(\mathbb F_q\) for \(q=3,5,7,9,11\), including an explicitly programmed extension-field trace at \(q=9\). It compares the four-term character-sum expression with direct finite sums for 3,856 cases; evaluates all 121,545 possible ambiguity coefficients over the five displayed test weights; tests the optimal minimum normalized ambiguity, its exact multiplicity, and elementary root-of-unity geometry. Expected final output:

`VERIFY_OK exhaustive_formulas=121545 direct_reconstructions=3856 optimal_examples=5 extension_field=F9`

The program uses floating-point tolerances for exact finite computations; those computations are only an independent numerical consistency check. The proof's universal inequalities, complex equality condition, dimension-free Weyl diagonalization, and uniform finite-field character-fiber counts do not rely on the numerical test.

No independent audit or external validation was performed.
