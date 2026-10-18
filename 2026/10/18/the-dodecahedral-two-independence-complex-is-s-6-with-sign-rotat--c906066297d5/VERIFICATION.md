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

Compile the included `dodecahedron_ind2_verify.cpp` using any C++17 compiler, or run `dodecahedron_ind2_crosscheck.py` with the Python 3 standard library. They do not depend on internet access, external datasets, or other package rows.

```sh
g++ -O2 -std=c++17 dodecahedron_ind2_verify.cpp -o verify
./verify
python3 dodecahedron_ind2_crosscheck.py
```

The actual captured stdout appears in the two included `*_output.txt` files. The first implementation checks the cubic graph construction, all induced-degree-constrained vertex subsets, every matching pair, all 410500 oriented Hasse incidences and their topological order, all integer Morse gradient-path matrices, the primitive attaching-minor determinant, and signed fixed-face Lefschetz numbers of all ten powers. The second independently builds the 60 forbidden connected triples and reproduces the face vector, facet profile and Euler characteristic.

Key checked values are 63142 nonempty faces, 31565 matched pairs, 410500 Hasse covers, critical cell counts 1,1,6,4 in dimensions 0,5,6,7, Morse \(\partial_6\) row \((0,0,-1,0,1,0)\), and a rank-four \(\partial_7\) image primitive in the rank-five kernel with determinant \(-1\) on an explicit maximal minor. Lefschetz traces on the sole reduced homology group, for rotation powers zero through nine, are \((1,-1,1,-1,1,-1,1,-1,1,-1)\).

The mathematical proof also uses standard finite discrete-Morse theory, degree classification of attaching maps to wedges of high-dimensional spheres, and the Lefschetz fixed-simplex formula. Exhaustive finite computations are exact for the specified graph; they are not a general proof for all cubic graphs. No independent mathematical audit has been performed.
