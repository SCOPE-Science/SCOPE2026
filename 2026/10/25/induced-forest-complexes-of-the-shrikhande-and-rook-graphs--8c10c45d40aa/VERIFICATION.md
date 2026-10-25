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

# Reproduction of the finite homotopy certificates

Execute `python3 verify.py` using Python 3 and standard-library modules only. A successful run prints a JSON report and terminates with `VERIFY_OK`; the expected report is retained in `verify_output.txt` for exact comparison. No downloaded paper, external library, network call or precomputed chain boundary is needed.

The verifier constructs both graphs explicitly, exhaustively evaluates all \(65,536\) possible vertex subsets of each with two different cycle-detection algorithms, and checks both face vectors. It forms the deterministic sequential-vertex matching on the augmented face poset, verifies the entire oriented Hasse diagram is a DAG, and independently derives the exact signed Morse boundary matrices by recursive gradient-path elimination. It checks that the sixth-to-fifth differential vanishes identically and that the fifth-to-fourth matrix contains the displayed maximal unit-determinant minor, in the indicated critical-face order. It also constructs independent full simplicial mod-two boundaries and checks their ranks.

The critical-face masks and actual minor matrices are printed in the JSON report. An apparent match in a mod-two Betti vector or Euler characteristic alone would not establish the integral conclusion; the decisive evidence is the integral signed Morse differential, the unit determinant, and the low-dimensional attaching-map argument in `RESULT.md`.

The exact finite proof covers only the two sixteen-vertex graphs. It does not establish an equivariant homology representation, an infinite-graph statement, or absolute novelty. Independent mathematical validation is not performed.
