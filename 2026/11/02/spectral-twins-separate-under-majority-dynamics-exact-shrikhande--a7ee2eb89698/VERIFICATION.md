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

# Exact finite-state verification

The vertex indexing is \((i,j)\mapsto4i+j\), for \(0\le i,j<4\). Both self-contained source files generate adjacency directly from the graph definitions; they do not read precomputed transition tables.

Run `python3 verify_functional.py` and `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct` from the directory containing those files. The full run outputs recorded in `functional_output.json` and `direct_output.txt` were reproduced. The Python implementation builds the full successor array and decomposes the directed functional graph; the C++ implementation uses a separately written signed-neighbor update and direct finite iteration for each state.

Graph prerequisites were checked, for both graphs: 16 vertices, six neighbors per vertex, exactly two common neighbors for every two distinct vertices, no loops, symmetric adjacency. Four-clique counts were eight (rook) and zero (Shrikhande).

## First-periodic-entry times

| Time \(t\) | Rook | Shrikhande |
|---|---:|---:|
| 0 | 2,696 | 1,512 |
| 1 | 14,136 | 9,304 |
| 2 | 29,984 | 26,240 |
| 3 | 18,720 | 18,496 |
| 4 | 0 | 9,024 |
| 5 | 0 | 960 |
| Total | 65,536 | 65,536 |

The following stronger finite identities were checked on all 65,536 states: \(F_R^5=F_R^3\) and \(F_S^7=F_S^5\). Each is sharp, witnessed by the explicit state trajectories in `RESULT.md`.

## Basin histograms

Each entry lists *basin size : number of recurrent orbits with that basin size*.

Rook fixed points: 1:144, 7:96, 10:32, 413:12, 715:16, 20789:2.

Rook two-cycles: 2:405, 4:288, 8:288, 10:216.

Shrikhande fixed points: 1:96, 22:32, 433:12, 28221:2.

Shrikhande two-cycles: 2:205, 4:288, 6:48, 8:96, 10:48.

The basin-size weighted sums separately equal 65,536, and the orbit frequencies reproduce 302/1,197 for the rook graph and 142/685 for the Shrikhande graph. The two global-consensus basins are the equal largest fixed-point basins in each graph, by bit-complement symmetry.

## Boundaries

These are exhaustive calculations for two specified finite graphs, not infinite-family proofs. Replay of exact code verifies all asserted state outcomes; recorded stdout by itself is not a proof. An independent external mathematical audit has not been performed.
