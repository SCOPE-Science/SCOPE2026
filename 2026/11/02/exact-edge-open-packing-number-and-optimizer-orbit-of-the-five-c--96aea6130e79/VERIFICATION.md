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

A self-contained C++17 file, `verify.cpp`, builds the five-cube edge set and the compatibility graph from the defining endpoint condition, without reading an external table or graph file. It directly counts size-12 and size-13 cliques using exhaustive ordered branching with mathematically valid greedy-color upper bounds. Every size-12 clique is checked for the four-star shape, center parity, and pair-distance pattern. An independently generated family parametrized by two binary masks is tested for legality and compared as a set with the exhaustive list.

Command executed against the packaged code:

```text
g++ -std=c++17 -O2 -Wall -Wextra -Werror verify.cpp -o verify
./verify
```

Observed output:

```text
Q5 edge-open packing: maximum=12; extremizers=80; parity_split=40+40; one affine-coordinate orbit.
conflicting_pairs=1120; 12_cliques=80; 13_cliques=0; nodes_12=22772; nodes_13=7499
VERIFY_OK
```

The no-size-13 result rules out every larger packing, since every larger clique contains a 13-clique. The independently checked 12-edge geometric construction gives the matching lower bound. The full-list comparison establishes the optimizer classification, not just the numerical maximum.

Limits: This is an exhaustive finite certificate for this one graph, not a general theorem about other dimensions. Correctness depends on the transparent enumeration and pruning logic in the supplied source, not on runtime measurements or an external solver's termination status. No independent external validation is asserted.
