---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Because A∈GL_n(Fq), pairwise distinct natural basis vectors have linearly independent squares, so images under any algebra automorphism have disjoint coordinate supports; every invertible automorphism is monomial t_i e_{σ(i)}. The coefficient condition is t_j a_ij=t_i² a_{σ(i),σ(j)}. Averaging fixed matrix counts, scalar restriction sum Z_r(q)-1=O_q(r q^-r) bounds perturbations on fixed coordinates; permutations moving ≥3 indices impose at least (2sn-s²)/2 orbit constraints, negligible compared with β=binom(n,2)(q−1)²q^{1−2n}. A diagonal nontrivial symmetry in an invertible matrix requires periodic orbits under scalar squaring, forcing extra zeros; its contribution is lower order. A transposition survives only with reciprocal scalars, (q−1) possible choices, and its GL centralizer has leading ratio (q−1)q^{1−2n}; combinations produce exactly β. Products of distinct transpositions force negligible other symmetries, hence conditional stabilizer C2 and probability β(1+o_q(1)); Burnside gives the orbit-class correction. Independent exact finite GF3 enumeration: n=2 has 48 nonsingular, 8 nonrigid, seven classes; n=3 has 11232 nonsingular, 576 nonrigid and 249 classes. This verifies small cases but not fixed-q n→∞ error estimates. No claim q=2 or algebra schemes.

## originality

PASS

Wei–Zou derive the general exact monomial Burnside orbit count and explicit low-dimensional classifications, while Sriwongsa–Zou classify automorphism structures. Neither inspected theorem evaluates the rare transposition probability, first nontrivial stabilizer coefficient or the asymptotic class-count correction for fixed q≥3 and large dimension. The source states a genuine probabilistic refinement of those prerequisites; possible implicit monomial fixed-point estimates remain priority risk.

## value

PASS

Exact first-order deviation from generic automorphism rigidity and orbit count for a natural uniform random finite-field algebra ensemble answers a specifically motivated classification/probability problem. The concentration of exceptional automorphisms on a single two-cycle is a meaningful structural phenomenon, not merely an approximate count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
