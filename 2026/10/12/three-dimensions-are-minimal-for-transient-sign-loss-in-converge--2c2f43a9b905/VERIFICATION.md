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

The proof is analytic. The bundled `verify.py` uses exact rational arithmetic to verify the three-dimensional witness: positive leading principal minors of \(A\) and \(2I-A\), the displayed inverse, the first two Newton–Schulz updates, the residual-squaring identity, and the negative entry \((X_2)_{13}=-1/500\).

The universal statement for dimensions one and two is not inferred from finite experiments. It follows from the exact polynomial formula
\[
X_k=q_{2^k}(A)
\]
and the analytic fact that \(q_m\) is positive and strictly decreasing on \((0,2/\alpha)\) for even \(m\). Two-dimensional functional calculus then forces the off-diagonal of \(q_m(A)\) to be nonnegative for every Stieltjes matrix in the convergence range.

Unproved extensions include nonsymmetric \(M\)-matrices, arbitrary starting matrices, dropping or rounding, other hyperpower orders, and a quantitative bound on the duration of transient negativity in higher dimensions.
