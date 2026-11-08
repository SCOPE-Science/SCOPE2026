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

With T(z,u)=z(u+T/(1-T)) marking vertices and leaves, Lagrange inversion gives [z^m u^k]T^d=(d/m)binom(m,k)binom(m-d-1,k-d) for d<m; the exceptional star d=m has leaf count m. Normalize by sum_k A=(d/m)binom(2m-d-1,m-d). The adjacent-degree ratio A_(d+1,k)/A_(d,k)=((d+1)/d)*((k-d)/(m-d-1)) rises strictly in k, and supports [d,m-1] shift right, proving TP2 including zeros and star. This yields strict stochastic increase for any strictly increasing h, with positive covariance by symmetrizing E[(D-Dprime)(g(D)-g(Dprime))]. Narayana leaf variance and root-degree generating-function derivatives give ED=3m/(m+2), EL=(m+1)/2, EDL=(3m-1)/2 and the displayed covariance/correlation. Independently enumerated plane trees m=2..8 and checked all table coefficients, pair minors through m=29. Neither finite test is a proof for all m.

## originality

PASS

Classical valency enumeration and Narayana leaf-count marginals provide much of the counting scaffold. The specific conditional root-degree vs total-leaf-count likelihood-ratio TP2 property and every-strictly-increasing-transform covariance, together with the exact covariance/correlation decay for uniform plane trees, are the substantive assessed contribution. A nontrivial specialization of fully general marked-valency formulas may already imply the joint array; no inspected source establishes its stochastic order directly. Published Resultary covariance for random recursive trees concerns a different distribution/model, and does not dominate Catalan-plane-tree TP2.

## value

PASS

A natural pair of tree statistics exhibits a strong finite-size monotone-likelihood-ratio dependence even though Pearson correlation decays as m^-1/2. This all-m classification of dependence is structurally meaningful and not just a Narayana marginal recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
