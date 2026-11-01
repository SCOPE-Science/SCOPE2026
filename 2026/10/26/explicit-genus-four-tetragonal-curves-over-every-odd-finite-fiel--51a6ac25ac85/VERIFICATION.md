---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Over the algebraic closure, split the quadric using u=z+sqrt(c)w, v=z−sqrt(c)w, giving xy=uv. The Segre parametrization converts the cubic to (s_1³+s_1 s_0²)(t_1³+t_1 t_0²)=kappa s_0³t_0³, a fiber product of f(z)=z³+z with kappa/f(z). In characteristic3, their branch values are {infinity} and {0}; otherwise the branch values of f are {infinity,±v_0}, v_0²=−4/27, and those of kappa/f are {0,±kappa/v_0}. These are disjoint iff (27kappa)²≠16. For generic t=1, (27·4)²−16=2^7·7·13; the t substitutions at p=7,13 prevent degeneracy and kappa is nonzero. Disjoint ramification implies the fiber-product divisor is smooth over the algebraic closure; positive intersection of effective (3,3) divisors gives geometric irreducibility. Adjunction yields g=4 and canonical embedding. The nonsplit smooth quadric excludes an F_q-trigonal ruling and hence degrees <=3; the displayed rational point together with Riemann–Roch on K−2P gives a basepoint-free map after removing base divisors of degree at most4. Thus the gonality is exactly4. Independent symbolic Segre and parameter checks, and rational affine/projective smoothness examples at p=3,5,7, corroborate but do not prove geometric smoothness for all q.

## originality

PASS

Compared precise theorems against their implication directions and alternate formulations using inspected primary literature and Resultary; no covering statement identified; residual priority risks remain and absence of a match is not a novelty proof.

## value

PASS

This is a uniform constructive answer to a precise genus-four odd-field existence problem, supplying explicit equations and a characteristic-complete smoothness proof rather than relying on finite field enumerations or a heuristic nonsplit-quadric strategy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
