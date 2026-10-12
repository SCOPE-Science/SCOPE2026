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
The proof was reconstructed from the exact crown adjacency rule. Writing \(X=\sum_i f(a_i)\) and \(Y=\sum_i f(b_i)\), the Italian constraints reduce to
\[
f(a_i)=0\Rightarrow Y-f(b_i)\ge2,\qquad
f(b_i)=0\Rightarrow X-f(a_i)\ge2.
\]
These implications give the lower bounds and force the complete weight-\(4\) classification.

The packaged `verify_crown_italian.py` was replayed after extraction from the finding row. It exhaustively enumerates all labelings for \(2\le n\le6\) and directly checks the neighborhood condition. Output:
`ALL CHECKS PASSED; n_range=2..6; exhaustive_labelings=597861; minima=(2:4/9,3:3/2,4:4/12,5:4/15,6:4/21)`

The exhaustive range is finite and is not used as proof for arbitrary \(n\). The theorem outside that range rests on the analytic shore-total argument in `RESULT.md`. The result does not determine coefficients above the minimum weight.
