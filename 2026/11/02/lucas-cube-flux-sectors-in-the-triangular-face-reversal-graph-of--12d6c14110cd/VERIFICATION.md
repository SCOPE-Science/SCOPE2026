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

# Exact verification and boundaries

Reproduce using only standard Python 3 and a C++17 compiler:

```sh
python3 verify_antiprism_transfer.py
g++ -std=c++17 -O2 -Wall -Wextra verify_antiprism_direct.cpp -o verify_antiprism_direct
./verify_antiprism_direct
```

The first checker constructs both flux sectors from independent cyclic binary words, reconstructs all oriented edges, verifies outdegree two and legal belt-triangle reversals, and checks equality with independent-set toggles for each \(3\le n\le9\). It also checks the exact counts and graph connectivity. The independent C++17 checker uses a raw backtracking enumeration of all balanced orientations (not the cyclic-state generation), constructs reversals of the specified faces, and verifies flux, components, exact counts and toggle rules for \(3\le n\le8\).

Expected final markers are `TRANSFER_VERIFIER_PASS` and `DIRECT_VERIFIER_PASS`. At \(n=8\), direct enumeration finds \(4416\) Eulerian orientations, \(19520\) reconfiguration edges and four components; at \(n=9\), the transfer checker finds \(11558\) orientations and \(57492\) edges. Neither program checks cases beyond its stated range. Mathematical completeness rests on the sectorwise bijective proof, not on extrapolation from these finite tests.
