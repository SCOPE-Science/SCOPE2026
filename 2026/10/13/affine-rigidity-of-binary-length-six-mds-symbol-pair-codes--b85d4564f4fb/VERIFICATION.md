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
The verifier uses only the Python standard library. It constructs all \(64\) binary length-\(6\) words and all \(2016\) unordered pairs, evaluates the cyclic pair-distance directly, and also checks \(d_p(x,y)=w_p(x+y)\) independently on every ordered pair.

A branch-and-bound maximum-clique search with greedy-coloring upper bounds proves that the compatibility graph has clique number \(8\). A separate fixed-cardinality recursion enumerates all size-\(8\) cliques and returns exactly \(32\). Exactly four contain zero, each is checked exhaustively for closure under binary addition, and translating every maximum by each of its own codewords always lands in this four-code linear set.

The natural symmetry check applies all \(64\) translations and all \(12\) dihedral coordinate symmetries to one representative. The resulting orbit is exactly the complete \(32\)-code census, and direct stabilizer counting gives \(24\). The unordered pair-distance profile is recomputed for every maximum and is always \(24\) pairs at distance \(5\) and \(4\) at distance \(6\).

The computation proves only this finite parameter case. It does not establish a general affine-rigidity theorem for other lengths or alphabets, and it does not determine the full graph automorphism group.
