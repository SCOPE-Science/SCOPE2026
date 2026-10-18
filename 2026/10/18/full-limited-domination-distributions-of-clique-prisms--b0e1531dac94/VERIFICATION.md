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

Run `python3 verify.py` next to this file. The standalone program computes the complete \(k\)-limited domination polynomial in two independent ways: direct examination of all labelled vertex subsets using literal graph neighbourhoods, and the theorem's multinomial column-type sum. It also checks both the minimum size and the coefficient of the lowest-degree term.

The completed execution returned `VERIFY_OK exhaustive_graph_parameter_pairs=42 feasible_sets_total=286117 n_range=2..8; analytic_min_cases=9..35`. The forty-two exhaustive parameter pairs cover every integer capacity from zero to the graph degree for each order two through eight. Additional analytic-formula-versus-minimizer comparisons are made at capacities zero, one, near half the order, just below the order, and at the order for twenty-seven further graph orders. All comparisons passed.

Proof obligations remain mathematical rather than computational: the essential all-set equivalence is shown explicitly in Steps 1 and 2 of `RESULT.md`; the counting uses unique type assignments, and the minimum classification uses a tight two-layer omission bound and equality rigidity. Finite checks cannot prove these universal implications. Neither source priority nor independent validation is established by the program.
