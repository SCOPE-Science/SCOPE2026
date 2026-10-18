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
# Reproducible verification

From the directory containing `verify_morse.py` and `verify_character.py`, run:

```sh
python3 verify_morse.py
python3 verify_character.py
```

The first program uses exact integer combinatorics. It enumerates all 12,800 faces, checks the complete greedy matching and 60,456 oriented Hasse arrows for acyclicity, and computes the entire integral discrete-Morse boundary by signed gradient-path elimination. The first two unit pivot columns are explicit and imply the homotopy wedge of 432 five-spheres.

The second program independently enumerates the rooted forests, compares each face count to the Laplacian matrix-forest polynomial, computes the top simplicial mod-two boundary rank, calculates every signed reduced Lefschetz trace under the 144 bipartition-preserving automorphisms, and decomposes the result using exact class-weighted inner products with all irreducible rational characters.

Expected successful output includes `VERIFY_OK`, a full Hasse sort of 12,799 faces, an integral two-by-two minor of determinant minus one, top mod-two rank 2592, and the stated 15-entry rational character and multiplicity matrices. Both checks were executed successfully. These are exhaustive checks of the finite graph \(K_{3,4}\); no conclusion about larger complete bipartite graphs follows from running them.

