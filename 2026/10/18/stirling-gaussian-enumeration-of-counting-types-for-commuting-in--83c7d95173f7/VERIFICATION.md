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

# Reproducibility and proof scope

The mathematical theorem and full proof are in `RESULT.md`. The code verifies finite instances of its structural lemmas and enumeration formulas. All scripts use Python 3 standard-library modules only and are intended to be executed from a directory containing all three programs.

Execute `python3 verify_subgroups.py`, `python3 verify_series.py`, and `python3 verify_witness.py`. The complete successful outputs are in `verify_subgroups.out`, `verify_series.out`, and `verify_witness.out`. A successful subgroup check ends with `VERIFY_SUBGROUPS_OK`, the series check ends with `VERIFY_SERIES_OK`, and the explicit-witness check ends with `VERIFY_WITNESS_OK`.

`verify_subgroups.py` independently generates every subgroup for one through three generators. It constructs every orbit-multiset type through twelve vertices for the first two cases and through eight vertices for the three-generator case, computes the local equality signature histogram and verifies the exact first collision. It additionally checks rank-at-most-two kernel reconstruction through six generators.

`verify_series.py` compares independent Gaussian-coefficient counts of subgroup indices and Stirling-number counts of local signature classes with direct subspace calculations through four generators. It also checks all coefficients through eight vertices of the isomorphism and two-variable-equivalence generating series by direct enumeration for one, two, and three named involutions.

`verify_witness.py` tests total bijections, involutivity, commutativity, orbits, relational atomic pair types and the separating three-variable sentence for both eight-element structures. It extends the pair to four through seven named involutions using additional identity maps.

The full proof is mathematical. Finite enumeration checks do not certify all parameter values, a running script does not certify originality, and the recorded review is not an independent audit.
