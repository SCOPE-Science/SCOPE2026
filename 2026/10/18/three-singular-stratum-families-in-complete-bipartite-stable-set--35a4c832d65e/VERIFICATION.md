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

# Reproducible mathematical checks

Run `python verify.py` in the same directory as the other files. Only the Python standard library is required. The output terminates with `VERIFY_OK`.

The program independently constructs the stable-set vertices and all proposed facets of \(\operatorname{STAB}(K_{p,q})\) for the part sizes \((2,2),(2,3),(3,3),(2,4),(3,4)\). It exhausts their face intersections; for each face, it computes the exact rational rank of the primitive active normals and compares it to the face codimension. It verifies the inclusion-maximal singular faces are precisely those predicted by the three families. It also checks the bounded-degree Segre semigroup generators and the square relation of the conifold.

Sample census of (vertices, faces, singular faces, maximal singular faces): \((2,2)\to(7,51,11,5)\), \((2,3)\to(11,151,31,8)\), \((3,3)\to(15,463,87,15)\), \((2,4)\to(19,459,103,12)\), \((3,4)\to(23,1447,315,25)\).

Finite experiments are not a proof for all parameters. The all-parameter argument rests on the graphic-incidence forest criterion, classification of cyclic active graphs, and explicit dual semigroup computations in RESULT.md. No external independent audit is represented or implied.
