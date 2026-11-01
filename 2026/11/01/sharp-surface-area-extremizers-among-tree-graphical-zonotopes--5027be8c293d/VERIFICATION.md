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

# Verification of tree-zonotope surface-area extrema

Run `python3 verify.py` using Python 3.9 or newer; no nonstandard packages are needed.

The verification enumerates every Prüfer sequence of lengths one through five (orders three through seven), building all \(18{,}247\) labeled trees. For each it independently constructs an integer incidence Gram matrix and evaluates its determinant with the Bareiss algorithm; checks that the full determinant is the number of vertices; deletes each edge column in turn and checks that the Gram determinant is the product of the two resulting component sizes; compares the resulting surface area against both bounds; and checks equality only for stars or paths. It also samples several large integer values to check the explicit asymptotic ratio numerically. Observed terminal output: `ALL_TREE_ZONOTOPE_SURFACE_CHECKS_PASSED`.

This finite computation is not exhaustive for unbounded tree order and is not an independent proof. The proof for every admissible order is the forest minor argument and the strict branch-transfer inequality in RESULT.md; the asymptotic uses an elementary Riemann sum. There was no independent mathematical audit or external certification.
