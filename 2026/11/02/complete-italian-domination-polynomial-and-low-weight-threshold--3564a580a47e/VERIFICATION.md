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

The included `verify.py` uses standard Python only. It independently builds each crown graph from explicit pairs of vertices, checks every required inequality at each zero vertex, and counts every feasible labeling by weight for \(n=3,4,5,6\), examining exactly \(597{,}780\) raw labelings. A distinct exact dynamic program conditions on the two side totals and generates valid column-pair configurations directly from the neighborhood inequalities for \(n=3,\ldots,10\). It verifies full polynomial equality for \(n=4,\ldots,10\), plus the lower-weight and highest-weight checks. The \(n=3\) case is a cross-check rather than part of the asserted theorem.

Replay: run `python3 verify.py` from the directory containing this document. The recorded output after a successful run is

```
VERIFY_OK direct_graph_labelings=597780 n=3..6 independent_pair_DP_n=3..10 full_coefficient_matches_n=4..10
```

The general theorem rests on the side-total partition and exact support-count proof, not on finite sampling. Independent mathematical audit has not been performed. The proof assumes integer \(n\ge4\) and graph edges precisely the complement of a fixed perfect matching between the two labelled parts.
