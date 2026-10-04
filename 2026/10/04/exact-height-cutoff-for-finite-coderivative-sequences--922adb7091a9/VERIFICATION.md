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

The proof was checked from the strict-successor definition of the coderivative.

For an upset \(X\) in a finite poset \(K\), the complement \(K\setminus X\) is a downset. Induction on \(k\) shows that \(w\notin\nabla^k(X)\) exactly when a chain of \(k+1\) complement points starts at \(w\). Thus the least \(k\) with \(\nabla^k(X)=K\) is exactly \(\operatorname{ht}(K\setminus X)\).

A proper upset cannot be fixed: a maximal complement point has all strict successors in the upset and is therefore added by \(\nabla\). Hence \(M\), which denotes the least fixed point, is top in every finite upset algebra.

For the truncated sequence, repeated use of \(\nabla(P_{j+1})\subseteq P_j\) gives \(\nabla^{N-i}(P_N)\subseteq P_i\). When \(N-i\) reaches the poset height, the left side is top for every \(P_N\). Below that threshold, the valuation \(P_j=\nabla^{N-j}(\varnothing)\) is a sharp counterexample.

The bundled checker exhaustively verifies all labelled posets of order at most four for the iterate and fixed-point claims. It also exhaustively checks all truncated-sequence valuations on labelled posets of order at most three for \(N\le3\). It prints `VERIFY_OK`.

## Limits

The checker is finite corroboration only; the proof is uniform for all finite posets. Infinite posets and transfinite iterations are outside the claim.
