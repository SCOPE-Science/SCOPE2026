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

# Reproducible finite checks

Run `python3 verify_heawood.py` from the directory containing the accompanying file. This script uses only the Python standard library, builds the fourteen vertices and twenty-one graph edges from the cyclic incidence rule, and examines every nonempty vertex subset. It checks the complete face vector, closure, exactly 1121 eligible matched pairs, 14 remaining critical cells, and the orientation of all 10150 cover relations in the complete Hasse graph. A topological sort visits all 2256 faces. Independently, exact mod-two boundary-matrix reduction yields ranks `(13,78,244,407,321,58)` and reduced Betti ranks `(0,0,0,0,0,13,0)`. The file `verification_output.txt` is a captured successful execution.

The proof of the **integral** homotopy classification relies on the exhaustive acyclic matching and the elementary CW attaching-map argument. The mod-two ranks are corroboration only; no finite experiment has been extrapolated to an infinite graph family. Independent external validation is not performed.
