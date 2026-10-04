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

The analytic proof is the primary verification. It was reconstructed against the source's definitions of the combined limit process and its branching-process threshold.

1. **Parameter nesting.** With common app marks \(U\) and manual-link marks \(V\), the traceable-edge predicate is monotone under \((p_1,\pi_1)\le(p_2,\pi_2)\).
2. **Pruning lemma.** An earliest-discrepant-birth argument rules out an infection occurring with stronger tracing but not with weaker tracing. The argument uses the genealogical-tree structure, common clocks, and recursive tracing through recovered infected vertices.
3. **Threshold transfer.** The source proves that its limiting component branching process dies out almost surely for \(R_{\mathrm{DM}}\le1\) and grows without bound with positive probability for \(R_{\mathrm{DM}}>1\). Pathwise inclusion therefore transfers directly to the sign of \(R_{\mathrm{DM}}-1\).
4. **Finite checker.** `verify.py` exhaustively checks the edge-predicate nesting on a rational grid and tests the pruning direction over nested trace-edge sets on finite event trees that include backward tracing, branching, and recovered tracing intermediates. Successful finite replay is a regression check only; it is not substituted for the infinite proof.

Limits: no computation verifies continuity, differentiability, or numerical monotonicity of \(R_{\mathrm{DM}}\), and none is claimed. The proof depends on instantaneous iterative tracing and common infection-contact dynamics; models with delay or one-step tracing require separate analysis.
