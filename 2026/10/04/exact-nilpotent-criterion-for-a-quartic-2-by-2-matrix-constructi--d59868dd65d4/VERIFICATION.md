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

The proof is symbolic and exact. The key checks are:

1. For the displayed traceless singular matrix \(V\), Cayley--Hamilton gives \(V^2=0\).
2. Direct noncommutative expansion gives \(X^4+Y^4-2Z^4=2(UV+VU)^2\).
3. Entrywise multiplication gives \(UV+VU=\operatorname{tr}(U)V+\operatorname{tr}(UV)I_2\).
4. With \(V^2=0\), the trace of \((UV+VU)^2\) is \(2\operatorname{tr}(UV)^2\), so vanishing is equivalent to \(\operatorname{tr}(UV)=0\) in characteristic zero.
5. The explicit integer pair \(V=\begin{pmatrix}2&1\\-4&-2\end{pmatrix}\), \(U=\begin{pmatrix}1&0\\-2&0\end{pmatrix}\) satisfies the source theorem's hypotheses but has unequal diagonal entries and still satisfies the quartic equation.

`verify.py` performs exact integer matrix arithmetic, directly checks the counterexample, and exhaustively compares the quartic equation with the trace criterion for 26,244 bounded pairs. Its expected final status line is:

`VERIFY_OK explicit_counterexample=1 exhaustive_pairs=26244 criterion=trace(UV)==0`

The finite replay is not used as proof of the universal statement. It is an independent arithmetic stress test of the symbolic identities and the packaged witness.
