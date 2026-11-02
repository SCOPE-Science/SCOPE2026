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

# Reproduction and scope

The included standard-library scripts run in a common directory. Execute `python3 verify_cycle_profiles.py`, `python3 verify_cycle_pebbles.py`, and `python3 verify_cycle_census.py`. The three corresponding text files are captured standard output. In the final package, the scripts should be extracted from the same embedded row before replay.

The profile checker examined 84 multisets of zero to three cycles with lengths 3 through 8, 1,188 graph vertices, and 9,504 individual predicate evaluations; its positive 2-regular cases reconstruct each cycle length. The independent logical checker computes the non-counting (set, not multiset) fixed-point refinement of complete reusable-variable tuple types. Its targeted suite contains ten equivalence or distinction comparisons, including a width-four example. The third checker exhaustively compares 19 nonempty 2-regular graph types of total order at most ten, across widths one through three: 570 graph-pair-width comparisons; 381 equivalences; by width, 190, 172, and 19 equivalences out of 190 comparisons. All matched the theorem's predictions. Runtime or memory bounds limit these enumerations to the described finite graphs.

The mathematical proof covers every finite cycle multiset, every variable width, and every quantifier depth. The computational checks do not certify historical originality or replace its quantified proof.
