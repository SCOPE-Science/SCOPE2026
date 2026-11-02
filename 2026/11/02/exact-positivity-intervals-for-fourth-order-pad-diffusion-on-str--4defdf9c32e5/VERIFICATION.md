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
# Verification of the exact Padé sign theorem

The supplied standalone `verify_srg_pade.py` implements rational Gaussian elimination and constructs the full matrix Padé rational map, separately from the two closed formulas for graph edges and nonedges. Execute in Python 3: `python3 verify_srg_pade.py`.

The program was executed from the supplied source and reported `VERIFY_OK 10 graph instances; 50 exact rational matrices; 8740 entry comparisons`. It checks strongly regular parameters by counting common neighbors, complete rational transition matrices at five positive rational times per graph, all off-diagonal entries, unit row sums, positive diagonals, and the exact sign quadratic. Families: Petersen, Paley 5 and 13, triangular 4, 5, 6, 7, rook 3 and 4, and complement of triangular 7. Exact rational finite checks support implementation fidelity only. They do not prove a statement for arbitrary graphs or all real times; the spectral-algebraic proof in RESULT.md supplies that implication.

Scientific scope excludes internal integrator stage positivity, nonuniform conductances, other graph families, and independence of review.\n