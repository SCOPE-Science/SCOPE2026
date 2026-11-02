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

# Reproducibility

Run from the package root:

```
python3 verify/infinite_fort_dfa.py
python3 verify/direct_grid.py
```

The first program compares the exact fort-recognizing automaton to a pattern-language NFA over all input lengths, by closure of its reachable finite product graph. It proves the 26-template formula for every width-three rectangular grid of length at least five and proves the lower bound of three initial vertices for all lengths at least three. The finite closures contain respectively 926 and 245 reachable states; both counts are assertions in the verifier.

The second program builds actual undirected grid adjacency, applies ordinary zero forcing to every three-set for lengths three through ten, constructs the token-jump exchange graphs and all-pairs distances, and checks the 13-vertex reference component from the explicit templates. It independently verifies the two exceptional small-grid counts, the fixed 26 configurations from length five onward, and the component-degree and eccentricity distributions.

Both scripts were executed on the packaged versions and their assertions passed. No third-party software, private data, external paper, random initialization, or precomputed result file is needed. These are self-review; no independent audit has been performed.
