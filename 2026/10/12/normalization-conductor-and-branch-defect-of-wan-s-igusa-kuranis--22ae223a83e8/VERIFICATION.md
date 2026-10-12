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

The exact proof starts from
\[
R=\mathbb C[a,b,c,d,e,f]/(ab,bc,ca,de,ef,fd)
\]
and its nine minimal-prime quotients \(\mathbb C[x,y]\). The normalization is their product. The conductor proof uses the exact boundary-compatibility description of the image of \(R\) and the nine component idempotents.

The bundled `verify_normalization_conductor.py` uses exact integer/combinatorial arithmetic. It checks the six original and nine conductor quadratic generators, nine normalized components, the fiber-count pattern \(1,3,9\), and that \(\dim(\widetilde R/R)_0=8\) while \(\dim(\widetilde R/R)_n=12\) for every tested \(1\le n\le19\). The stored output ends in `VERIFY_OK`.

The finite replay is not used as an infinite proof. The conductor equality and Hilbert-series identity are proved symbolically in `RESULT.md`. Primary full-text access was unavailable during source inspection; the exact germ itself is visible in the primary abstract and indexed Theorem 1.5 material, while originality against unseen portions remains a stated residual risk.
