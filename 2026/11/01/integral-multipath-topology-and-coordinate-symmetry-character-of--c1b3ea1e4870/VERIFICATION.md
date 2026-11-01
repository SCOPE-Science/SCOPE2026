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

# Verification of the rank-oriented four-cube multipath result

The package contains `verify_boolean_cube_multipath.py` and `morse_certificate.json`, and the complete exact output from an execution of the program in `verification_output.txt`. Execute the program with Python 3.9 or later in the same directory as the certificate. It uses only standard-library modules.

The source independently builds the four rank-incidence bipartite graphs, exhaustively enumerates their matching simplices and reconstructs the deterministic greedy discrete-Morse pairs. On each of the two middle graphs it checks 78 pairs on 162 nonempty faces, confirms exactly one critical vertex and five critical triangles, and topologically sorts all 432 directed Hasse incidences after reversing paired arrows. Exact mod-two boundary elimination independently gives ranks 11, 37 and 30 and second Betti number five in each middle factor. The five critical triangles and no critical edges imply the integral homotopy wedge, rather than only numerical field homology.

An independent recursive dynamic program processes all 32 original digraph arcs directly from incoming/outgoing-degree restrictions, generating 664225 admissible subsets including the empty subset. It agrees coefficientwise with the product of four factor enumerators and checks the complete face polynomial. All 24 coordinate permutations are processed using exact signed fixed-face Lefschetz traces, with full consistency across conjugacy classes; the rational irreducible decomposition is computed by integer character inner products.

The checks establish this finite four-dimensional case and a rank-level combinatorial decomposition. They do not establish a general formula for higher-dimensional Boolean lattices, an equivariant wedge splitting, or the uniqueness of the result in the literature. The independent audit has not been performed.
