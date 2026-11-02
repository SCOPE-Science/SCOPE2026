---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For uniformly sampled rank-r weakly isotone maps on [n], the ordered positive kernel composition λ and strictly increasing image b are uniform and independent: there are C(n−1,r−1)C(n,r) maps. An inverse β must have one image point in each α-kernel interval (∏λ choices), and its r−1 kernel cuts c_i must satisfy b_i<=c_i<b_(i+1), independently giving ∏(b_(i+1)−b_i) choices; converse crossed-transversal criterion establishes αβα=α, βαβ=β. Independent full direct computation checked all 35 maps at n=4 and all 126 at n=5 against both composition identities, not merely source claimed logs. Summing products over λ compositions and b gaps proves coefficient expression for every k>=0. Positive integer compositions converge to independent uniform Dirichlet simplex measures by Riemann-sum argument, product continuous mapping gives n^{-(2r−1)}X→Y_r in law; uniform boundedness gives all moments and simplex beta integrals yield factorial formula. Integer balancing proves sharp maximum; n=r and rank-one excluded from limit handled explicitly.

## originality

PASS

Qualified PASS: the semigroup-theoretic crossed-transversal inverse criterion is prior work (Higgins 2014/2024) and 2026 Higgins provides a permutation matching for O_n, but existence of one matching does not determine vertex degrees, all moments or a Dirichlet-product weak limit. The actual new contribution is quantitative rank-conditioned inverse-degree distribution and its exact extremizers. The full October 2026 Higgins paper could not be retrieved here; priority risk remains rather than fabricated negative inspection.

## value

PASS

The inverse graph of the natural order-preserving transformation monoid is an established structural object. The exact rank-conditioned inverse-degree moments and nondegenerate Dirichlet product limit quantify typical inverse multiplicity, while balanced extremizers characterize the maximum—natural nontrivial statistics not determined by existence of inverse matchings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
