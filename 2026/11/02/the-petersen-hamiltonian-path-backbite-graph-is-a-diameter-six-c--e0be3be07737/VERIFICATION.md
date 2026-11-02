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

From the embedded artifacts, run:

```sh
python3 verify.py
c++ -std=c++17 -O2 verify_alt.cpp -o verify_alt
./verify_alt
```

The Python program exhaustively enumerates all Hamiltonian paths of the Kneser graph, checks their complete rotation graph, tests the regular action of every element of \(S_5\), identifies four generators, and verifies the shortest-path distance shells from all states. It ends with `PRIMARY_CERTIFICATE_OK`.

The independent C++ program uses the pentagon/pentagram model \(GP(5,2)\), complete spanning-path enumeration, one-bit-per-edge masks and all unordered configuration pairs rather than generating rotations. It verifies the path count, all \(240\) single-edge reconfiguration edges, degree \(4\), and the same all-source distance shells. It ends with `ALTERNATE_CERTIFICATE_OK`.

Observed outputs before packaging:

```text
PETERSEN_PATHS_OK 120 ENDPOINT_PAIR_WITNESSES 4
REGULAR_S5_ACTION_OK 120 GENERATORS ((1, 0, 3, 2, 4), (3, 1, 2, 0, 4), (3, 1, 4, 2, 0), (4, 1, 3, 0, 2))
BACKBITE_CAYLEY_OK 240 EDGES
EXACT_METRIC_OK [1, 4, 11, 25, 39, 29, 11] RADIUS 6 DIAMETER 6
PRIMARY_CERTIFICATE_OK
INDEPENDENT_GP_ENUMERATION_OK paths=120 endpoint_pairs=30
INDEPENDENT_EDGE_FLIP_OK edges=240 degree=4
INDEPENDENT_METRIC_OK shells=1,4,11,25,39,29,11 diameter=6
ALTERNATE_CERTIFICATE_OK
```

Limits: the proof is exhaustive because the finite state space is fully enumerated, not because of random trials. The programs make no assertion concerning graphs other than Petersen. Program agreement does not constitute an independent scholarly audit.
