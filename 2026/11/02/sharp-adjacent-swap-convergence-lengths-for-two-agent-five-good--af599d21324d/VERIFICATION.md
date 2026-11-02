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

# Verification protocol

Compile and run in the directory containing all bundled files:

```sh
g++ -O3 -std=c++17 -Wall -Wextra verify.cpp -o verify
./verify
python3 crosscheck.py
```

The first standalone program generates all 120 strict rankings, their adjacent swaps, the exact alternating-round-robin allocation mask for each of 14,400 report profiles, and the possible profitable directed transitions for all 120 choices of the second agent's true ranking after fixing the first ranking by good relabeling. It checks the one-item exchange lemma for every candidate and uses depth-first cycle detection and longest-path recursion for every graph. Its main output includes:

```
N=14400 transitions_zero=88800 transitions_one_swap=26400 transitions_multiple=0
true_ranking_profiles=120 cycles=0 best_all=18 best_from_truth=6 sum_longest_truth=117 active_edges_total=1584000
```

The second implementation independently replays all pick sequences, reconstructs gains and losses, and uses Kahn's topological-order algorithm and longest-path dynamic programming. Its output is:

```
VERIFY_INDEPENDENT 14400 120 18 6 1584000
WITNESSES_OK 18 6
```

`WITNESSES.json` contains every reported-ranking pair and first-agent bundle mask along each sharpness path. `crosscheck.py` verifies their masks, that exactly one adjacent transposition occurs at every step, and that the changed agent's gained good is strictly preferred to the lost good according to the stated true ranking. These are direct integer checks, not numerical approximations. The certificate does not use Monte Carlo, random seeds, optimization solvers, external datasets, or a timeout interpreted as nonexistence.

**Limits:** These checks cover the entire **five-good** finite state space under the stated preference and action assumptions, not six or more goods. The utilities are assumed strictly rank-consistent and additive; the reduction to ordinal comparisons relies on the verified one-item exchange property. The published-source comparison is an originality assessment and not independent publication-priority certification. The independent audit status is unperformed.
