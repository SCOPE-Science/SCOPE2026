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

# Reproducibility and verification

Both included scripts use Python 3's standard library only and have no external files or dependencies. Run in the same directory as this document:

```
python3 verify_bidirected_k2n.py
python3 verify_integer_cancellation.py
```

The first enumerates all arc subsets of sizes zero through four, rejects repeated incoming/outgoing arcs and directed cycles, checks all codimension-one faces, builds the prescribed disjoint sequential arc-toggle pairing, orients every Hasse incidence, and topologically sorts the full directed Hasse graph. It computes the signed Morse incidence via an acyclic gradient-path projection, and separately computes augmented reduced mod-two simplicial homology. It produces:

```
n=3 faces=115 pairs=54 Hasse_arcs=288 critical={2: 6, 1: 1} F2_Betti={1: 1, 2: 6} signed_Morse_boundary_shape=(1, 6) content=0 nonzeros=0
n=4 faces=313 pairs=152 Hasse_arcs=896 critical={2: 8, 3: 1} F2_Betti={2: 8, 3: 1} signed_Morse_boundary_shape=(8, 1) content=2 nonzeros=6
n=5 faces=711 pairs=339 Hasse_arcs=2200 critical={3: 32, 2: 1} F2_Betti={2: 1, 3: 32} signed_Morse_boundary_shape=(1, 32) content=2 nonzeros=26
n=6 faces=1417 pairs=624 Hasse_arcs=4608 critical={3: 169} F2_Betti={3: 169} signed_Morse_boundary_shape=(0, 169) content=0 nonzeros=0
VERIFY_OK
```

The second rebuilds the faces and signed integral simplicial boundaries from scratch, performs each indicated gradient-pair cancellation as an actual integral elementary chain cancellation with pivot \(\pm1\), and checks the remaining incidence entries and their gcd. It produces:

```
CANCEL_OK 3 faces 115 pairs 54 critical (1, 6) matrix_content 0 matrix_nonzeros 0
CANCEL_OK 4 faces 313 pairs 152 critical (8, 1) matrix_content 2 matrix_nonzeros 6
CANCEL_OK 5 faces 711 pairs 339 critical (1, 32) matrix_content 2 matrix_nonzeros 26
CANCEL_OK 6 faces 1417 pairs 624 critical (0, 169) matrix_content 0 matrix_nonzeros 0
```

The finite complex is exhaustively enumerated because each arc uses one of the two degree-limited central vertices; no complex face can have more than four arcs. The signed matrices and their Smith contents are the proof-critical certificates: mod-two homology alone would not establish either integral torsion or the precise homotopy type. Both programs verify only the four reported inputs and do not claim an infinite generalization. The dynamical-module property is established separately by the two-/four-cycle closure argument in `RESULT.md`, not by these code outputs. The review is same-model only; no independent external audit has occurred.
