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

Run `python verify.py` with the standard Python library and no external dependencies. The script was executed successfully from its package path. Its printed PASS certificate covers the polynomial identities defining the involution, the three additional invariants, the exact relation, the quotient hypersurface partial derivatives, and the Jacobian ideal reduction identity. It also exhaustively verifies the map on all \(16\) points over \(\mathbb F_2\), obtaining \(10\) fixed points and \(3\) two-cycles.

The checker works by finite sparse-polynomial arithmetic with coefficients in \(\mathbb F_2\). It does not establish algebraic normality, invariant-field equality, irreducibility, or the intrinsic obstruction to linearization; those rely on the full human-readable proof in `RESULT.md`. Characteristic \(2\) is essential, and neither the computations nor proof address polynomial tameness. No independent external audit has been performed.
