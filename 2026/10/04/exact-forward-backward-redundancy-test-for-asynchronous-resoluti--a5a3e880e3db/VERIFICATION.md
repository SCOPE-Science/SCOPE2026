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

The critical identity is that any suffix acts by union of contributor rows:
\[
(\mathsf U_{\vec S}\mathcal V)_a
=
\bigcup_{q\in\operatorname{see}_a(\vec S)}V_q.
\]
This follows by induction because every resolution update replaces participant rows by their union.

For a history \(\vec P.B.\vec S\), the checker independently computes the views of the full history and of the history with \(B\) deleted. It then verifies the closed-form criterion
\[
Q_a\cap B=\varnothing
\quad\text{or}\quad
U_B\subseteq F_a.
\]

`verify.py` exhaustively tests all nonempty groups on up to four agents with every prefix and suffix of length at most two. It also verifies the immediate equal-view criterion and immediate repetition.

For the all-model necessity direction, the proof uses the explicit model \(W=\{0,1\}^A\), with base relation \({\sim}_c\) given by equality on coordinate \(c\). Intersections indexed by distinct subsets of \(A\) are distinct, so a changed final view necessarily changes a current accessibility relation in some epistemic model.

The finite enumeration is a consistency check only. The general theorem is proved symbolically.

## Limits

The verification concerns final current accessibility relations. It does not claim that deleting a relation-redundant event preserves the full history-sensitive asynchronous semantics.
