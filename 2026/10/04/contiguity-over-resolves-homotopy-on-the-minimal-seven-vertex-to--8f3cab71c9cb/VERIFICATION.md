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

The embedded `verify.py` is standalone and uses only the Python standard library. It reconstructs the seven-vertex complex from the fourteen listed facets and performs the following checks:

- enumerates all \(7^7=823{,}543\) vertex maps and tests simpliciality;
- verifies exactly \(27{,}979\) simplicial self-maps and the image-size distribution \(1:7,2:2646,3:25284,7:42\);
- verifies that every non-automorphism has simplex image;
- identifies exactly \(42\) automorphisms and checks that they are exactly the affine maps \(i\mapsto ai+b\) on \(\mathbb Z/7\);
- constructs the full one-coordinate contiguity graph and verifies component sizes \(27{,}937\) and \(42\) singletons;
- checks the facet-intersection criterion used to isolate automorphisms;
- reconstructs the integral first-cohomology system, verifies rank two, and computes all \(42\) pullback matrices;
- verifies that exactly six matrices occur, each with multiplicity seven.

Successful replay prints:

`VERIFY_OK maps=27979 image_sizes=1:7,2:2646,3:25284,7:42 contiguity=27937+42x1 autos=AGL(1,7) h1_actions=6x7`

The finite computation certifies the exact direct-map census. The proof in `RESULT.md` supplies the symbolic implications from simplex image to null contiguity class, from maximal-facet intersections to automorphism isolation, and from the six induced matrices to the seven represented ordinary homotopy classes. No claim is made that the finite enumeration classifies arbitrary continuous self-maps of the torus.
