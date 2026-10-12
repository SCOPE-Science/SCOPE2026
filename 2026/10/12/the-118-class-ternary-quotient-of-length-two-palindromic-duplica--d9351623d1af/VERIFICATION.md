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

# Reproduction of the finite multiplication certificate

Compile `verify.cpp` with any conforming C++17 compiler (using the standard library only):

```sh
c++ -O2 -std=c++17 -Wall -Wextra verify.cpp -o verify
./verify
```

Expected successful output:

```text
VERIFY_OK ternary_classes=118 table_transitions=354 graph_vertices=7174453 graph_edges=8370198 invariant_edges=18045 stable_length_classes=57 length_bound=14
```

The checker enumerates *all* words of length at most \(14\), joins words related by one application of the defining replacement, computes the shortest lexicographic representative for each of the \(118\) distinct signatures reached by length \(7\), and verifies that the representative multiplication table is correct for all \(354\) letter extensions. It separately checks all signature counts through length \(7\) and tests invariant preservation on \(18{,}045\) short edges. No external data, enumerated path list, random source, or network access is needed.

The finite lemma certified by connectivity is precisely \(r_s a\equiv r_{\operatorname{sig}(r_s a)}\) for every signature \(s\) and alphabet symbol \(a\). The proof of the infinite theorem additionally requires the symbolic facts that signatures are invariant, that every signature has a representative of length at most \(7\), and that signatures are compatible with appending letters. The graph computation alone does not certify a bounded rewrite length for arbitrary long words. The classification concerns symmetric equivalence; it does not compute common forward descendants or optimal error-correcting codes.
