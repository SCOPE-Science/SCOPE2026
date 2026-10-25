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

# Verification notes

The proof uses exact group-averaging reduction, an analytic spectral decomposition and an explicitly nonnegative convex subgradient certificate. In the high-size branch, the weights \(\alpha,\beta,\gamma\) are nonnegative by the algebraic inequality \(2/(3n-2)<x_*<1/n\), and their weighted gradient is identically zero. These analytical checks extend to every integer \(n\) in the stated domain.

`verify_fmmc.py` uses only Python's standard library and checks the displayed candidate formulas for integer part sizes three through five hundred. The script additionally computes an illustrative deterministic finite grid of feasible edge weights at selected part sizes; the grid and floating-point checks are not exhaustive proofs. The exact infinite-family conclusion depends on the symbolic argument in RESULT.md, not on test coverage.

Literature searches examined the relevant intact-biclique and symmetry-reduction derivations in two primary full texts. An exact preexisting formula for the one-edge-deficient biclique cannot be ruled out solely from targeted retrieval. The supplied evidence is self-reviewed and is not an independent audit, certification, or third-party validation.
