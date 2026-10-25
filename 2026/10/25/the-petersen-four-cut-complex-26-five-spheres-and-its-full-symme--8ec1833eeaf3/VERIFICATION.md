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

# Reproduction and finite proof checks

Run `python3 verify.py` with Python 3.10 or later. The script constructs the ten vertices of the Petersen graph as two-subsets of five labels. It builds the ordinary four-cut facets from all 210 four-vertex subsets and verifies 70 connected and 140 disconnected induced sets.

The independently enumerated reduced complex has 765 nonempty faces, the face vector \((10,45,120,210,240,140)\), 3,330 nonempty face-poset cover relations, 369 matched pairs and one critical vertex plus 26 critical five-simplices. Exhaustive topological sorting of every directed cover relation proves acyclicity. The augmented mod-two boundary ranks are \((1,9,36,84,126,114)\); these are cross-checks and not a substitute for the integral homotopy argument.

For the symmetry conclusion the program checks all 120 elements of \(S_5\), computes their signed simplicial Lefschetz traces, verifies the seven cycle-type values, and performs exact Murnaghan–Nakayama character inner products to obtain multiplicities \((1,2,1,2,0,0,0)\) in descending-partition order. No downloaded dataset or external executable is needed.

The integer homotopy type follows from the verified complete acyclic discrete-Morse matching and the resulting CW cell dimensions. The full character is rational, not a claim about an integral equivariant lattice. An external independent mathematical audit is not available.
