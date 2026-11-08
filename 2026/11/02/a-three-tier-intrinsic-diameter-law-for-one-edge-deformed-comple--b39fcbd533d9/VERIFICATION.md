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

In the continuous realization of K_n, n>=3, with one edge ab of arbitrary length λ>0 and all others length 1, vertex distances are min(λ,2) for a,b and 1 for all other distinct vertices. For two points on distinct edges their geodesic distance is the minimum of four endpoint-route affine expressions. Pairwise cases same edge, incident edges, exceptional/disjoint and normal/disjoint bound all distances by the stated formula, with exact midpoint witnesses. Thus D_3=(λ+2)/2 (metric circle), D_4=(λ+3)/2, D_n=max(2,(λ+3)/2) for n>=5. L=binom(n,2)-1+λ; differentiation yields n=3 constant ratio, n=4 strictly increasing ratio with unattained 3/10 limit, n>=5 strictly decreasing on (0,1] and increasing on [1,infty), unique minimum 2/binom(n,2) at λ=1. Independently computed all-edge grid geodesic diameter for n=3..6 at six distinct λ values and matched; edge-pair inequalities prove continuum result.

## originality

PASS

Best-of-knowledge qualification: actual Resultary searches and directly compared primary mathematical results show no decisive prior implication of this exact final claim; component methods, previously known examples, accessible full-text scope and named inaccessible-source risks are explicitly distinguished.

## value

PASS

Continuous geometric network diameter is a natural intrinsic quantity distinct from discrete vertex diameter. The exact one-exceptional-edge complete-graph classification and sharp length-normalized minimizer change at n=4/5 yield a useful boundary phenomenon for metric network design without implying global optimality among all weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
