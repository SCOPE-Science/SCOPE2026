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

# Verification scope and instructions

The finding is the affine classification of all nine-element weak \(B_2\) subsets of \(\mathbb Z_{56}\), not the already-published optimum modulus. All code is supplied as complete standalone C++17 source.

Compile and run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic classify56.cpp -o classify56
./classify56
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_rigidity.cpp -o verify_rigidity
./verify_rigidity
```

Expected exact results: `classify56.cpp` reports `nodes=3455863 normalized_sets=216 affine_orbits=1`. `verify_rigidity.cpp` reports `search_nodes=3455863 exhaustive_zero_containing=216 orbit_zero_containing=216 entire_affine_orbit=1344` and `VERIFY_OK`. The first program canonically minimizes each solution under \(24\) units and \(9\) choices of origin; the second program independently regenerates a Boolean-array search and computes all \(24\cdot56\) images of one fixed witness, then compares complete mask sets, not just counts.

`pair_sums.tsv` contains all \(36\) residues and corresponding contributing distinct pairs for the witness; no sum appears twice. Pruning in either exhaustive program uses only the impossibility of repairing a sum collision and the count of remaining available residues. Termination is by finite loops, with no time cutoff.

Results assert neither a general formula for other group orders nor an independent external certification. The mathematical programs are transparent finite proof certificates; their correct execution can be reassessed externally.
