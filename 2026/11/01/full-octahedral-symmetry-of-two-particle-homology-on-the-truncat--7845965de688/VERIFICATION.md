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

# Reproducibility

The only executable is `verification/verify.py`, written for Python 3.9 or newer with the standard library. From the directory containing this file and the `verification` folder, run `python3 verification/verify.py > replay.json`; compare the resulting file with `verification/output.json` as UTF-8 bytes. No external dataset, third-party package, publication server or arbitrary seed is required.

## Checks actually performed

The graph is reconstructed from the 24 signed coordinate permutations and squared Euclidean edge-distance rule. The fourteen faces are reconstructed as convex coordinate facets, comprising six quadrilaterals and eight hexagons. The 55 disjoint face pairs yield explicit integer two-chains whose boundaries are computed and checked zero. The complete degree-two cellular matrix has mod-two rank 503, and the 55 integral cycles have independent mod-two reductions. This forces rational second-homology rank 55, with first-homology rank 14 by connectivity and Euler characteristic.

All 48 signed coordinate permutations are independently mapped to their vertex, edge, face and cell actions. The two cellular boundary maps commute with each group action. For each symmetry, each product-torus chain is mapped to the predicted signed product-torus chain. The 55 face pairs form five group orbits of sizes 3, 12, 4, 12 and 24; the first four have face-interchanging stabilizers, while the 24-element mixed square–hexagon orbit does not. Homology traces are computed both from the geometric face-pair action in degree two and by cellular Lefschetz traces in degree one; ten group classes give constant values within each class. Inner products with the five rational \(S_4\) characters and both central parities yield integral nonnegative multiplicities, and their weighted dimensions agree with ranks 14 and 55. Full, rotation and central-inversion averages are checked exactly.

## Exact proof dependencies and limits

Mod-two computations serve only as complementary rank inequalities over \(\mathbb Q\) together with 55 explicit closed cycles; they are not used alone to assert integer Smith normal form or torsion-freeness of first homology. The fact that the 55 tori are an **integral** top-homology basis additionally uses the 2009 Barnett–Farber ordered planar-configuration theorem and a two-sheeted-cover transfer argument. The code does not claim to prove the general historical theorem. The ordinary topological quotient cohomology statements use rational averaging for a finite group. No independent verification has been performed.
