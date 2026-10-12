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

# Finite-state verification

The complete C++17 verifier `verify_fep5.cpp` enumerates all configurations with \(h=1,\ldots,8\) vacant sites on the \(5\times5\) torus, checks all 100 oriented possible jumps at each configuration, computes every strongly connected component using Kosaraju's algorithm, tests all outgoing edges, and verifies recurrent-set membership separately for each state against the plaquette condition. The largest sector has 1,081,575 configurations and 17,054,400 directed edges. The verifier was built and run successfully and printed `VERIFY_OK eight high-density sectors and plaquette-free characterization`.

The separate Python 3 script `count_plaquette_free.py` computes the exact coefficient sequence of a 32-state row-transfer polynomial for configurations containing no vacant elementary plaquette, without using the transition-graph computation. It was executed and printed `COUNT_OK` after reproducing all eight exact recurrent-size counts.

For replication:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -Werror verify_fep5.cpp -o verify_fep5
./verify_fep5
python3 count_plaquette_free.py
```

The proof is exhaustive only because this is a fixed finite state space. The reproduced findings do not certify any general statement about all lattice sizes, nor do they independently reprove the published result used for \(K\le16\).
