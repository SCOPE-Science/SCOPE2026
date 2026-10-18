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
# Verification of the Grötzsch higher-independence filtration

All three standalone artifact files (`verify.py`, `gr_collapse_1_2.json`, `gr_collapse_2_3.json`) must be placed in one directory. Run `python3 verify.py` with Python 3. The code uses only the standard library and reconstructs every face from the stated graph definition, never relying on external graph files. A successful run prints `GROETZSCH_HIGHER_INDEPENDENCE_FILTRATION_CHECKS_OK`.

The program independently computes all 2,048 induced-subset component sizes by breadth-first components and by union-find, then compares the methods; it separately establishes face closure for every threshold. It replays exactly 90 collapses of the third complex onto the second and 105 collapses of the second onto the first, checking each live free face. For stages one and four through ten it reconstructs all matched face pairs and checks that orienting each matched covering incidence upward and each unmatched incidence downward produces no directed cycle. It asserts the complete critical-cell counts and all total face counts, and independently verifies the mod-two reduced homology of the eleven stages using boundary matrices.

The homotopy deductions use the standard acyclic-matching theorem: one zero-cell together with only critical cells of a single positive dimension constitutes a sphere wedge. No integral torsion can occur in these CW models. The mod-two computation serves as a consistency check; neither field rank computations nor finitely many sampled masks alone establish the integral homotopy classification. No inference is made for a larger Mycielskian or for graph automorphism modules. Independent mathematical audit has not been performed.
