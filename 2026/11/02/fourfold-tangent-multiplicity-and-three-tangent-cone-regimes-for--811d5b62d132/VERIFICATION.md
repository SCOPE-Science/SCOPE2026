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

For p≥5, r in [2,p), n=p+r, Newton identities identify the 1..4 power-sum ideal with e1..e4; freeness over symmetric polynomial invariants makes this a regular sequence of degree 1·2·3·4=24. Vandermonde Jacobian rank equals number of distinct coordinates capped at 4; a singular projective zero has <=3 values. First s nonzero power sums and invertible Vandermonde imply multiplicities of each distinct nonzero value are divisible by p, forcing exactly p equal nonzero entries and r zeros; hence binom(n,p) singular support points. The finite singular locus and dimension n−5≥2, plus CI Cohen–Macaulay, give normality and geometric integrality via connectedness. In a chart at an indicator point, two independent linear initial forms and two quadratic forms U,V form a regular initial sequence, with restricted Gram determinants p−1 and r both nonzero; associated graded is k[u,v]/(q_{p−2}(u),q_{r−1}(v)), Hilbert–Samuel multiplicity 4, and r=2,3,≥4 produce nonreduced, reduced reducible and integral normal regimes. Independently exhaustive F5 projective points for n7 and n8 recovered exactly 21 and 56 predicted indicator singular points; Gram determinants checked across p=5,7. Computation corroborates but not replaces proof over algebraic closures.

## originality

PASS

Qualified best-of-knowledge PASS for the local multiplicity-four tangent cone classification, not for classical regular-sequence background. Giménez et al. arxiv:2610.32056 (first posted 2026-10-23) is VERY closely relevant to power-sum varieties including singularities and normality, and could already cover the global normality/singular-support part. Accessible abstract/record does not exhibit the exact r-dependent associated-graded ring or 3 tangent-cone regimes; arXiv/preprint/OA full-text retrieval failed and authorized institution returned vpn_disconnected. This material non-exclusion is a priority risk, not proof of coverage, and needs primary full-text human comparison before publication.

## value

PASS

Exact local scheme-level tangent cones and the nonreduced/reducible/normal degeneration boundary of a natural finite-field four-moment variety are substantive geometric invariants, not arbitrary finite counts. Set-theoretic support and Hilbert–Samuel multiplicity supply a sharp family result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
