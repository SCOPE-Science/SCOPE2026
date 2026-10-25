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

# Verification

Run `python3 verify.py` using Python 3 and no third-party modules. The checker enumerates all normalized Boolean-cube maps in dimensions zero to three for six specified finite flag complexes, constructs integer signed boundaries before reducing ranks modulo two, verifies the corner chain-map identity on every simplex, and checks the simplex-cone chain homotopy equation on all cubes up to dimension two. It reconstructs the degree-zero and degree-one mod-two Betti numbers separately from simplicial boundaries, not by assuming the theorem.

Observed final marker: `VERIFY_OK cases=6 simplices=41 normalized_cubes=20874`. The checker neither exhausts all finite hypergraphs nor verifies high-dimensional integral torsion. The four-step integral proof in RESULT.md establishes the universal claim independently.
