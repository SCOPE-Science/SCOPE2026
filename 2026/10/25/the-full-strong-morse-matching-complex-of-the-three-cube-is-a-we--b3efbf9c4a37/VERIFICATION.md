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

Run `python3 verify_cube_strong.py` on Python 3.10 or later. This re-generates the complete set of \(8!=40320\) vertex orders and all gradients, verifies that their downward closure has 216 four-element facets, and checks the face counts \((24,168,392,216)\). It explicitly finds and checks 216 free triangle–tetrahedron collapses, followed by a 23-edge spanning tree and 145 triangle-attaching relations that successively eliminate all non-tree edges. These finite checks are exhaustive for the specified cube, not experiments on a larger family.

The independently calculated mod-two chain ranks are \((23,145,216)\). The topology conclusion uses elementary-collapse invariance, the van Kampen presentation of the residual two-complex, integral Euler characteristic, Hurewicz and homology Whitehead. The script does not constitute independent external review and makes no assertion about larger cubes or absolute literature novelty.
