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

Run `python3 verify.py` beside `census.cpp` and `certificate.json`.

The C++ census generates every nondecreasing self-map of the normalized chain \(0<1<\cdots<n-1\). For each binary pair of maps, it works in the pair automaton on \((i,j)\) with \(i\le j\). Reverse breadth-first search from all diagonal pairs gives the exact shortest synchronization distance for every synchronizable pair.

Because a monotonic word synchronizes a subset if and only if it synchronizes that subset's minimum and maximum, these pair distances are the exact subset distances.

The exhaustive maxima for \(n=1,\ldots,9\) are \(0,1,2,3,4,5,6,7,9\). At \(n=9\), exactly two unordered normalized map pairs have a state pair at distance \(9\), hence exactly four ordered normalized transition pairs are extremal.

The Python verifier independently performs a forward breadth-first search on the displayed first extremal, obtaining shortest word `babbaabbb` and checking the full pair trajectory. It also checks the binomial count of nondecreasing maps and the reversal-plus-letter-swap relation between the two unordered extremals.

Independent audit has not been performed.
