---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The deterministic graft identity H=max_v(K_v+sum_{external edges}(1+left/right record spine length of parent)) reduces the problem to finitely many independent uniform BST blocks. Independent online relative ranks give left/right record path means log m+O(1), variances log m+O(1) and covariance O(1), hence asymptotically independent Gaussian edge labels by multivariate Lindeberg. Positive fixed block masses give N_i proportional to n; published Reed uniform BST mean c*log n-beta loglog n+O(1), bounded variance, make internal K_v deviations o(sqrt(log n)). Shallow external vertices have at least log n deterministic deficit, so only deepest v survive. Uniform integrability follows second-moment bounds and finite external k; first moment converges. Separately constructed 1350 small BSTs and computed heights from grafting and direct insertion, all agreeing.

## originality

PASS

Best-of-knowledge PASS. Peca-Medlin–Zhong already prove the grafting identity and first-order c*+h law, while Corsini–Dubach–Féray develop permuton-sampled BST; neither inspected result states the second-order correlated Gaussian tree maximum or exact positive sqrt(log n) mean correction by deepest-branch multiplicity.

## value

PASS

Second-order height fluctuations and expectation corrections directly quantify search-tree performance and distinguish balanced from skew fixed external block structures; a natural general fixed-k classification rather than renaming the known leading-order bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
