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

The proof was checked directly against Definition 2.8 of arXiv:2609.36397v1. For a factor map \(\pi:X\to Y\), the induced map \(\pi_{\mathcal K}:\mathcal K(X)\to\mathcal K(Y)\) is continuous, onto, and equivariant; onto-ness follows from \(\pi_{\mathcal K}(\pi^{-1}(B))=B\) for every nonempty compact \(B\subseteq Y\).

The invariant-measure lifting step was reconstructed for the locally compact amenable setting: a probability lift exists by weak approximation with finitely supported measures, and averaging that lift over a Følner sequence produces an invariant lift while preserving its pushforward. This is the continuous-group version of the amenable factor fact recorded in arXiv:2605.03993. The remaining compatibility needed for the non-discrete definition is exact: if \(S=\bigcup_{x\in F}\{gx:g\in I_x\}\) with finite \(F\) and compact \(I_x\subset Z(G)\), then equivariance gives \(\pi(S)=\bigcup_{x\in F}\{g\pi(x):g\in I_x\}\), which is an allowed compact in the factor.

The checked proof does not assume finite fibers, injectivity, minimality, unique ergodicity, or mixing. Amenability is retained explicitly because it is used to obtain an invariant lift. No claim is made in the reverse direction or for nonamenable acting groups.
