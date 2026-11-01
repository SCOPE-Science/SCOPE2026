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

# Verification and limits

The theorem is proved analytically by strict alternating-branch trapping, the uniform two-step contraction estimate \(G'_a\le cd^2/b<1\), convergence of parity subsequences, and the invariant-measure contradiction obtained from universal empirical limits. The quantitative exponents follow from the fixed-point equation and derivative chain rule. All initial points, including the discontinuity and endpoint, are explicitly handled.

The provided standalone `verify.py` checks exact rational identities for the affine case and finite sample inequalities for nonlinear exponents. Finite checks do not certify the quantified conclusions: these are justified by the proof, not by enumeration. Specifically, the empirical limit \(\nu=(\delta_0+\delta_b)/2\) is **not** invariant, and it would be incorrect to invoke compactness to infer an invariant probability for a discontinuous map. The strong contraction condition is sufficient only, and stronger results outside it remain unproved. Independently conducted verification has not been performed.
