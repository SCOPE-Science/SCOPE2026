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

# Reproducible verification

Run `python3 check_split_graph.py` with a standard Python 3 interpreter; no external packages are required. The script builds each electrical graph from its edges and inverts a grounded weighted Laplacian over `fractions.Fraction`. Every cut- and cycle-projection column is reconstructed directly from its source potential, and both absolute column sums are compared with the theorem's formulas.

The actual successful run reported:

`WEIGHTED_SPLIT_ENDPOINT_EXACT_OK graphs=120 columns=3280 boundary_spotchecks=2`

The main loop covers clique orders from 2 through 7, independent-set orders from 2 through 6, and conductance square roots 1/3, 1, 6/5 and 2. Two additional rational tests include the low-order cases. A separate symbolic simplification checked the displayed comparisons between column differences and their two threshold polynomials, and the phase-alignment identity was checked by substituting its explicit positive square root. The analytical proof establishes the unrestricted theorem independently of finite verification.

The checker does not enumerate all real conductances, prove noncoverage by prior work, establish independent validation, or address nonorthogonal projections.
