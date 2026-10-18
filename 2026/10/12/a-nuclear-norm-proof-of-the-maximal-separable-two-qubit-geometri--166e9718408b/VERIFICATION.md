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

For any separable two-qubit state, use a finite pure-product Bloch decomposition with unit vectors a_k,b_k and M=[x T]=sum p_k a_k(1,b_k)^T. By convexity of nuclear norm each product term has nuclear norm sqrt(2), giving ||M||_*<=sqrt(2). Write singular values s1>=s2>=s3; D=(s2^2+s3^2)/2; 2s2+s3<=sqrt(2), 0<=s3<=sqrt(2)/3. The exact quadratic upper bound 1/2-w+(5/2)w^2 for w=s3/sqrt(2) attains 1/2 only at w=0 on [0,1/3]. Thus D<=1/4 with equality forcing singular values (1/sqrt(2),1/sqrt(2),0). Polar rank-two partial isometry Q witnessing ||M||_* forces every positive-weight product vector c=(1,b) into its fixed 2D initial space and fixes a=Qc/sqrt(2); the c0=1 affine-line intersection with the sphere ||c||=sqrt(2) has at most two points. All saturating product states therefore comprise <=2 distinct projectors and rank rho<=2. Published Gharibian rank-two classification then identifies the single LU orbit. Independent exact fractional Gram check for sigma recovers eigenvalues (1/2,1/2,0); scalar inequality checked at 1001 rational values only for corroboration, full proof above infinite-dimensional parameter domain.

## originality

PASS

The sharp augmented one-sided Bloch matrix bound and polar-equality rank-two argument provide an analytic proof of the unrestricted separable two-qubit maximum geometric discord conjecture. Gharibian 2012 established the rank-two extremizer and conjectured no higher-rank maximizers; Rana–Parashar 2013/2014 proves only within separable X-states and derives partial general necessary conditions. Earlier extended-correlation separability trace-norm criteria concern different augmented matrices and do not in the inspected theorems establish this sharp equality condition. The major residual risk is an unlocated 2015–2026 global proof under different terminology.

## value

PASS

This is a globally sharp optimization and rigidity theorem for a canonical two-qubit quantum-correlation quantity, resolving the exact higher-rank equality conjecture left open by Gharibian and Rana–Parashar. The nuclear-norm estimate alone is easy, but its saturation analysis is a motivated structural rank-reduction lemma; recovering every maximizer has independent mathematical interest beyond a numerical bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
