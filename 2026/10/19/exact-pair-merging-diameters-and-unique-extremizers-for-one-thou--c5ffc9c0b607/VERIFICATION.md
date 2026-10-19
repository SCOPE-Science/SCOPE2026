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
# Reproduction of the finite theorem

The theorem applies **only** to the integer interval \(1\le k\le1000\). Its proof uses complete multi-source shortest-path computation in the unordered pair automaton; it does not infer infinitely many cases from sampled data.

From the directory containing all included files, compile `pair_census.cpp` with `c++ -O3 -std=c++17 -Wall -Wextra -pedantic pair_census.cpp -o pair_census` and run `./pair_census 1000 > recomputed.tsv`; compare `recomputed.tsv` byte for byte against `pair_census.tsv`. Each row is computed from scratch by fully visiting pair states, not looked up in a table. A nonzero exit indicates a failed completeness, diameter or uniqueness check.

Run the separately written Python oracle with `python3 crosscheck_small.py pair_census.tsv`; it reconstructs every pair arc explicitly for parameters \(1\le k\le40\) and checks exact maximum and all maximizing pairs. Compile `crosscheck_forward.cpp` with `c++ -O3 -std=c++17 crosscheck_forward.cpp -o crosscheck_forward` and execute `./crosscheck_forward`; it independently finds a shortest collision path by forward BFS for the proposed hardest pair at ten selected parameters, including the largest. Their expected console results are in `verification_output.txt`.

Recorded `pair_census.tsv` SHA-256: `f88e9f5eb6626e581f2ffb6d19660280904394a77ad6bd590d8c8db8b81c2128`. The verifier uses integer arithmetic and stores pair graph distances exactly. The original originating thesis could not be inspected; the equality for \(k>1000\) and independent mathematical validation are not established by these finite checks.
