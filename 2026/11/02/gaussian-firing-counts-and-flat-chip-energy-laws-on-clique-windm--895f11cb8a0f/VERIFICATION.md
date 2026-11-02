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

The standalone Python file `verify_windmill.py` is self-contained and uses only the Python standard library. Run `python3 verify_windmill.py` from the directory containing the file.

It independently constructs the labelled windmill adjacency lists, simulates two synchronous updates, isolates center-firing representatives of primitive two-cycles, and compares exact counts by firing-population size against the closed polynomial. It exhaustively checks 846922 normalized labelled candidate states across ten small parameter pairs, including the friendship-graph family through four triangles and the four-vertex-clique windmills through two blocks. It checks the exact chip-energy complement symmetry and mean formula for every tested pair. The recorded output in `verification_output.txt` concludes with `WINDMILL_CHIPFIRING_VERIFY_OK`.

The test range is finite. General validity and the joint Gaussian–uniform limit rely on the algebraic interval count, product-measure tilting argument, and convergence proof in RESULT.md; the verifier does not claim to certify those infinite assertions or to rule out unindexed prior coverage. Independent audit has not been performed.
