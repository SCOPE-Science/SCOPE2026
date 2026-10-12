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
The embedded `verify_copeland_uncovered_decisiveness.py` performs a complete exact replay using only the Python standard library.

For every labeled tournament through five alternatives it computes the Copeland set independently from:
1. explicit out-neighborhood cardinalities;
2. an independently accumulated pairwise-win score vector.

It computes the uncovered set independently from:
1. the covering relation;
2. the equivalent two-step tournament-king criterion.

The replay verifies:
- total tournament counts \(1,2,8,64,1024\);
- \(CO(T)\subseteq UC(T)\) in every tested tournament;
- equality through order \(3\);
- exactly \(24\) strict order-four cases, all with \((|CO|,|UC|)=(2,3)\), in one orbit of size \(24\);
- no order-four strict case with a unique Copeland winner;
- exactly \(600\) order-five tournaments with a unique Copeland winner;
- exactly \(280\) order-five tournaments with a unique Copeland winner and \(CO(T)\subsetneq UC(T)\);
- exact fractions \(35/128\) unconditionally and \(7/15\) conditional on a unique Copeland winner;
- uncovered-set-size counts \(120,120,40\) for sizes \(3,4,5\);
- exactly three decisive isomorphism classes with orbit sizes \(120,120,40\);
- outdegree multiset \(\{3,2,2,2,1\}\) for every decisive first-layer tournament;
- top cycle equal to all five alternatives throughout that layer.

Run:

`python3 verify_copeland_uncovered_decisiveness.py`

The first output line must be:

`VERIFY_OK`

The exhaustive classification stops at five alternatives.
