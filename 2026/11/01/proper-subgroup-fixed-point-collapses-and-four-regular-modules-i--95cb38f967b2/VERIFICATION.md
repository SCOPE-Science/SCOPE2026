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

Run `python3 verify.py` alongside this document, using Python 3 standard library. The script reconstructs the tetrahedral Hasse diagrams and all 30 generated subgroups, enumerates the orbit-barycenter triangulations of the 29 nontrivial subgroup fixed spaces and their embedded boundary subcomplexes, and checks all elementary free-face collapses (42/2/0 depending on 2/1/0 globally fixed base labels). It constructs the 2122-face link, checks the 1049-pair augmented matching and full acyclicity of its reversed Hasse digraph, leaving 24 degree-three critical faces. It reconstructs the four incompatible top facet edge stars and the dimension-96 relative integral homology. All claims in RESULT.md that depend on these calculations have finite exhaustive algorithms and explicit assertions.

The relative rank 96 and nonequivariant wedge decompositions have independent primary-literature precedent; those ingredients are not claimed to be new. The rational character follows by theoretical equivariant Euler--Poincaré from the 29 actual fixed-point collapse certificates, not by assuming the integral module splits. No extension to other tetrahedral representations, simplex dimensions, or the identity-subgroup fixed collapse was tested or claimed. Independent external review has not been performed.
