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

# Reproducible mathematical verification

Run `python verify.py` with Python 3 and its standard library. It reconstructs the unordered two-particle cubical cells from the graph edge list, checks every two-cell boundary via the signed formula, and uses sparse exact finite-field Gaussian elimination (moduli 101 and 2). For every \(3\le t\le8\), the model has \(\binom{t+3}{2}\) zero-cells, \((3t+2)(t+1)\) one-cells, and \(3t^2-t\) two-cells; the rank over \(\mathbb F_{101}\) is \(3t^2-t-t(t-3)/2\), and the rank over \(\mathbb F_2\) is one smaller, consistent with known first-homology two-torsion. For \(4\le t\le8\), the checker creates signed quadrilateral matrices and verifies that their integral boundaries vanish and that all tested classes transform correctly under generators of \(S_t\) and the transposition in \(S_2\). The expected last line is `VERIFY_OK_K12T_NON_TORIC_INTEGRAL_SECOND_HOMOLOGY_MODULE`.

The proof for all \(t\) is **not** inferred from these tests: it comes from an exact, symbolically solved incidence condition on all two-cells, with no higher cells. The rational Specht-module identification uses the classical permutation representation on two-element subsets; its integral counterpart is the explicit \(\ker B_t\) lattice, not the rational Specht lattice assumed by extension. The combinatorial argument excluding pairs of disjoint cycles is valid for all parameters.

No independent audit or certification has been performed. Literature-priority uncertainty is documented in the accompanying review.
