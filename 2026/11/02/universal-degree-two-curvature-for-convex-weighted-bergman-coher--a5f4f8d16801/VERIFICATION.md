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

# Verification and reproducibility

For \(\beta>1\), one checks directly that \(\int_\mathbb D |e_n|^2(\beta-1)(1-|z|^2)^\beta d\mu=1\). The phase-space pointwise estimate bounds the argument of \(G\) in \([0,1]\), so its first two derivatives are bounded. Expansion of the normalized path gives the exact quadratic form in `RESULT.md`. Its separation into hinge functions is justified by the \(C^2\) integral representation of \(G\), and angular orthogonality removes all cross-mode terms.

The critical coefficient identity follows from differentiating \(t^{\beta-1}(1-t)^{n+1}\), integrating on \([a,1]\), and retaining the delta/endpoint term \(a^{\beta-1}(1-a)^n/\beta\). Both terms are necessary: deleting the endpoint term would falsely spoil the degree-one flat mode.

The bundled `verify_modes.py` uses standard-library exact rational arithmetic for integer \(\beta\) and integer power \(p\). Executing `python verify_modes.py` produced `PASS 704 rational identities and Taylor checks`. Its finite tests cover \(\beta\in\{2,3,5,9\}\), \(p\in\{2,3,4,6\}\), and finitely many modes and perturbation sizes. They do not certify all real \(\beta\), arbitrary \(G\), the tail limit, or any globally uniform estimate.

The original weighted Bergman maximization theorem and the comparison literature can be checked through the identifiers listed in `RESULT.md`. The present mathematical review is not independent validation.
