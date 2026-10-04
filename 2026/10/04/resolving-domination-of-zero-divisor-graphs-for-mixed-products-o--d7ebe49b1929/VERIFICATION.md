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
The proof was reconstructed directly from the support partition of a finite product of fields.

Critical checks:
- every nonzero zero-divisor has a unique nonempty proper support \(S\subset[n]\);
- a support class has size \(\prod_{i\in S}(q_i-1)\);
- two support classes are completely joined exactly when their supports are disjoint;
- vertices within one support class are false twins, giving the all-but-one resolving lower bound;
- if \(q_i=2\), every vertex with support \([n]\setminus\{i\}\) has the unique neighbor supported on \(\{i\}\), yielding one extra domination charge;
- for \(n\ge3\), the charged support-class pairs are disjoint across binary indices;
- the explicit upper-bound set contains a singleton-support landmark for every coordinate, which resolves and dominates every omitted representative.

`artifacts/verify.py` independently builds the support-class blow-up graph, checks the construction and lower-bound accounting for every field-order pattern with \(3\le n\le5\) and \(q_i\in\{2,3,4\}\), and exhaustively computes the optimum for all tested graphs having at most twelve vertices. The replay returns `VERIFY_OK`.

Finite computation is not used as a proof of the universal statement.
