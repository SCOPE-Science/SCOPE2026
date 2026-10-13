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

# Reproducibility and verification limits

The self-contained `verify.py` program builds the incidence graph directly from all \(10\) two-subsets and \(10\) three-subsets of a five-element ground set. It reconstructs the oriented simplicial boundary matrix, computes its exact rational rank \(6\), verifies the boundary composition, and enumerates every \(\binom{10}{4}^2=44\,100\) balanced eight-element initial configuration. Two separately implemented color-change closures agree on every configuration. It finds exactly \(13\,520\) successful configurations.

The code generates all ground-set permutations and the complement duality, checks all \(240\) adjacency-preserving maps, and verifies the \(67\) CSV orbit representatives, orbit sizes, disjointness, and complete coverage. The size multiset is \(\{20,60,120^{\times18},240^{\times47}\}\).

The independent source `verify_gp.cpp` reconstructs \(P(10,3)\) from its outer cycle, inner chords and spokes, verifies its graph isomorphism to the incidence model, exhausts all \(\binom{20}{8}=125\,970\) eight-vertex subsets, and obtains \(13\,520\) successful configurations, all four-and-four across the incidence classes.

Run `python3 verify.py` and `g++ -O2 -std=c++17 verify_gp.cpp -o verify_gp && ./verify_gp` in the extracted package directory. The Python program requires no packages; the C++ program requires a standards-conforming C++17 compiler. Neither executable needs downloaded data. The general minimum-size claim follows symbolically from the signed-boundary kernel argument and an explicit forcing sequence. The two finite enumerations prove the claimed *finite* counts by exhaustive coverage, not by sampling or extrapolation. No independent mathematical audit has been performed.
