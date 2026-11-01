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
The standalone Python script `verify_cubocta_pm.py` requires only Python 3.9 or later and no external libraries. Run it from this package to reproduce the exact JSON in `VERIFIER_OUTPUT.txt`. The checker explicitly builds the cube and its line graph, independently enumerates all perfect matchings, takes their full simplicial downset, and verifies extension to a perfect matching for every included face.

The exact augmented face count is 1,429 (1,428 nonempty), its f-vector is \((24,192,520,468,192,32)\), and the 32 facets each contain six edges. A matching of 693 face pairs is checked acyclic against all 4,992 Hasse cover relations by a complete directed topological sort. Exactly 43 critical two-cells remain; the empty face is paired. Forman's CW theorem therefore proves the integral homotopy equivalence with a wedge of 43 two-spheres. Independent full-boundary mod-two ranks in degrees one through five are \((23,169,308,160,32)\), agreeing with the predicted homology.

The complete signed simplicial Lefschetz trace of each of the 48 coordinate-permutation/translation symmetries is calculated from every fixed oriented face, then grouped by signed cycle class. Every one of the ten signed-coordinate conjugacy types has a consistent character value. The identity trace is 43, and character averaging gives \(\dim H_2^{B_3}=2\). The action preserves the complex because it comes from graph automorphisms; no equivariant CW decomposition is assumed.

**Limits.** All calculations are exact and exhaustive for this explicitly defined graph, rather than evidence for a universal family theorem. The use of standard discrete-Morse, chain-level Lefschetz, and finite-group representation principles is explained in `RESULT.md`. No independent audit has been performed.
