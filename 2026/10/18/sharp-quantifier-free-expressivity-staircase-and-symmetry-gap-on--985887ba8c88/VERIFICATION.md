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

# Reproducibility and limits

Run `python check_cycle_types.py` with Python 3. The checker independently enumerates concrete adjacency signatures of injective tuples for cycle lengths 3 through 10 and tuple sizes up to 5, computes the path-forest numbers via the component-containing-label-one recurrence, and compares the two. It independently enumerates the full dihedral group action on tuples of lengths 1 through 4 for cycle lengths 3 through 8, checks the orbit formula, and tests exact type-count stabilization and strict cutoff for arities 2 through 6. The extracted script executed successfully from the completed new package with output:

`VERIFY_OK injective_cases=37 injective_assignments=68888 dihedral_cases=24 orbit_tuples=10274 sharp_cutoff_k2..6=YES cycle3_k3= 5 cycle5_k3= 13 cycle6_k3= 14`

The finite checks cannot establish claims over all cycle sizes, all arities, or bibliographic originality. Those mathematical claims require the argument in `RESULT.md`; any independent external audit is not performed.
