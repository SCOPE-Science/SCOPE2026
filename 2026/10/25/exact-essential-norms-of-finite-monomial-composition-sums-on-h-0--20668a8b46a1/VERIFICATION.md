---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

PASS: The associated evaluation weight is exactly v_alpha, since analytic boundary peaks (1-conj(eta)w)^(-alpha) attain (1-r)^(-alpha) and obey the norm bound; Bonet 2022 Theorem 53 supplies the single-symbol essential norm m^(-alpha), and Calkin triangle inequality gives the upper bound. For the lower bound, read all factors of the explicit package peaks u_(j,n), with near-boundary exponent eps=sqrt(1-r)>0 and angular high power floor((1-r)^(-1/2)). Each u belongs to the little growth space (vanishing weighted modulus at every boundary point), satisfies norm<=2^eps and diagonal weighted value ->1 at r^(m_j) eta_j. Pick boundary eta_j=zeta^(m_j) pairwise distinct, so off-diagonal terms vanish uniformly and aligned phase summation has norm ->1. Weighted embeddings into C_0 and dominated convergence against any finite measure show this bounded locally-null sequence is weakly null; compact perturbations vanish. Directly checked asymptotic diagonal limits for alpha=1/2,1,3/2 and m=1,2,3,7; proof, not finite numeric tests, establishes every alpha, N. No repeated symbols, infinite sums or other weights claimed.

## originality

PASS

PASS best-of-knowledge, with material priority risk: Bonet 2022 survey Theorem 53 gives an exact essential norm for ONE weighted composition operator, not the distinct-symbol sum. Wolf/Lindström difference-operator work explicitly covers two operators; accessible abstracts do not prove or exclude N-term extensions. A 2025 primary paper titled Essential Norm of Sum of Generalized Weighted Composition Operators concerns sums of derivative terms composed with a COMMON symbol, not multiple distinct monomial symbols, so its superficially stronger name does not automatically imply the result. The simultaneous separated-boundary-peak lower bound is the surviving contribution. Full texts of close antecedents unavailable; alternative general finite-sum statements remain a significant risk.

## value

PASS

PASS: Essential norms classify distance to compactness and asymptotic operator size. Finite linear combinations need not attain the triangle upper bound because cancellation is possible, so exact additivity for a natural family of boundary-separating monomial symbols provides a useful complete formula, stronger than per-symbol norms. The value lies in the separation mechanism and exact noncancellation, not in a routine three-term numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
