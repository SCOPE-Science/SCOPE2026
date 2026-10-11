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

Run `python3 verify.py`. Its only dependency is the standard Python library. A successful complete run prints `VERIFY_OK facets 76 simplices 3762 matching_pairs 1870 Hasse_incidences 21576 critical_0 1 critical_6 22 homology_rank_6 22 automorphisms 24`.

The program enumerates all 220 three-vertex subsets, filters by graph independence, constructs their facet complements and all simplices, and performs the specified filtered element matching. It checks every ordinary face-to-facet incidence in the resulting directed Hasse diagram by topological sorting, not by sampling. Separate exact mod-two chain computations corroborate the homology. For every one of 24 graph symmetries it checks edge preservation, orientation signs and reduced Lefschetz traces, then applies rational character orthogonality.

The infinite validity of general discrete-Morse and character theory is used as standard mathematics; the program's exhaustive assertions certify only this twelve-vertex instance. No independent external review is asserted.
