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

The exact domain is a connected complete multipartite graph \(K_{n_1,\ldots,n_r}\) with \(r\ge2\) and \(2\le k\le N-1\). The critical proof split is whether a terminal \(k\)-set lies inside one part or meets at least two parts. In the first case the minimum Steiner tree has one extra outside center; in the second case the terminal-induced graph is connected and a minimum Steiner tree uses no extra vertex.

The bundled `verify.py` independently builds graph adjacency, enumerates every candidate vertex set, computes minimum Steiner-tree edge counts by exhaustive connected-superset search, and checks whether any selected nonterminal can lie in a minimum Steiner tree. It then compares the observed set-size distribution with the displayed enumerator.

Recorded output:

```text
VERIFY_OK
multipartite_k_instances = 264
vertex_subset_checks = 44496
orders = 2..8; all k = 2..N-1
```

The finite run covers all complete multipartite isomorphism types of orders two through eight and every admissible \(k\). It is corroborative only; the infinite theorem is supplied by the symbolic proof. No claim is made beyond complete multipartite graphs, and no independent audit has been performed.
