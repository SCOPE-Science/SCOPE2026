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

The checker constructs every graph of the form
\[
K_1\vee(K_{k_1}\cup\cdots\cup K_{k_r})
\]
whose total peripheral order lies between \(4\) and \(10\), with \(r\ge2\) and every \(k_i\ge2\).

For each graph it computes all-pairs shortest-path distances by breadth-first search, enumerates every vertex subset, forms the distance multiset of every outside vertex directly, and tests pairwise distinctness.

The direct result is compared with the theorem's structural criterion, every coefficient of
\[
(1+z)\prod_{q\in Q}\left(z^{qm_q}+m_q q\,z^{qm_q-1}\right),
\]
the minimum \(K-|Q|\), and the minimum-basis count \(\prod_{q\in Q}m_q q\).

Recorded output:

```text
VERIFY_OK
heterogeneous_windmill_types_checked = 32
peripheral_orders = 4..10
vertex_subsets_checked = 34016
minimum_bases_checked = 481
all direct outer-multiset tests matched the distinct-omitted-clique-size classification
all cardinality enumerators matched the product formula
all dimensions and minimum-basis counts matched
```

The finite enumeration is corroborative only. The arbitrary-order theorem follows from the exact distance-multiset formula in the proof.
