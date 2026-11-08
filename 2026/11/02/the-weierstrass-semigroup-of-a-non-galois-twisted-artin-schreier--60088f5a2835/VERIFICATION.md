---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For odd p and d≥2 with p not dividing d−1, W: y^p−y=x f(x^{p−1}) is a connected Artin–Schreier cover of degree p and pole degree M=1+(p−1)d prime to p; standard one-pole AS ramification gives genus (p−1)(M−1)/2. Scalar Fp× acts on (x,y), and invariant u=x^{p−1},v=y/x give C: u v^p−v=f(u), with total scalar ramification at (0,0) and ∞. Tame Riemann–Hurwitz gives g(C)=(p−1)d/2 and unique P∞ over u∞. The polynomials uv^j=x^{p−1−j}y^j give one-pole orders p+j(d−1); the Apéry set mod p of the generated semigroup is {0}∪{p+j(d−1):1≤j<p}. Its gap genus equals g(C), proving semigroup equality, all p minimal generators, Frobenius (p−1)(d−1), conductor +1 and pseudo-Frobenius {j(d−1)}. A second place over u=0 has ramification index p−1 while [k(C):k(u)]=p, proving that projection non-Galois for odd p. Uses normalization and algebraic closure, not a finite-field point-count claim.

## originality

PASS

Qualified PASS: explicitly distinguishes the non-Galois variable-coefficient degree-p projection from Zhang–Zhao's 2026 constant-coefficient separable linearized Galois covers and from Kummer covers. Their 27-page full primary linearized paper was read in its introduction and key gap/generator propositions and does not directly specialize under its stated hypotheses. The tame quotient technique and general AS ramification are established tools; unindexed equivalent quotient semigroup results remain a meaningful residual priority risk.

## value

PASS

Weierstrass semigroups at rational places are natural inputs to Riemann–Roch dimension and AG codes; this theorem gives the entire one-point semigroup, Apéry set, minimal generators, conductor and type uniformly for an infinite non-Galois family and proves independence of all lower polynomial coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
