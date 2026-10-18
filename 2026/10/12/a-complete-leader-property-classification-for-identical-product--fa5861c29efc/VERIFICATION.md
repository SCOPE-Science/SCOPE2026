---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: For fixed sample index and one marginal, u_n=E[F(X)^(n-1)] includes ties. Any law without a terminal upper atom admits cutoffs b_j with upper tails t_j downarrow 0. Split integral: u_n<=(1-t_j)^(n-1)+t_j; choosing n_j=ceil(log(1/t_j)/t_j)+1 gives u_n<=2t_j. With d independent coordinate samples, leader probability a_n<=n_j u_n^d<=2^d(t_j^(d-1)log(1/t_j)+2t_j^d)->0 since d>=2. If top atom p>0, chance of observing the all-top vector tends to one. Analytic argument covers arbitrary continuous, discrete, mixed marginals with finite/infinite supremum.

## originality

PASS

PASS (best of knowledge): The new arbitrary-tail cutoff supplies a missing uniform subsequence that neither earlier result implies; terminal top atom is an exact sufficient criterion across d>=2. Known sufficient conditions and dependent-coordinate models do not force zero liminf for every arbitrary common marginal lacking a terminal atom. Residual literature/access risks are explicitly recorded.

## value

PASS

PASS: This all-marginal iff for the canonical iid symmetric subfamily resolves a specifically posed independent-product leader-property question in a natural nontrivial setting. The threshold is a structural endpoint atom, not an arbitrary finite parameter. Prior two-dimensional random-tie criterion does not decide it, and lacunary example shows why liminf rather than full limit is essential.

The dated certificate retains the supplied scientific assessment, sources and limitations.
