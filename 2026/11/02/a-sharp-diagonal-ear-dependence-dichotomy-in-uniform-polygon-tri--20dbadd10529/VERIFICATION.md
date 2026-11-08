---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

A fixed diagonal splits independent Catalan triangulations C_a C_b. Original ear tips are nonendpoint boundary-arc vertices; j simultaneous tips are nonadjacent subsets of a path, counted by binom(r-j+1,j), and deletion leaves C_(r-j) triangulations. Hence H_r factorial moments and the conditional product follow. Unconditional tips are nonadjacent subsets on a cycle; one-point ratio p_r=(r+1)/(2(2r-1)) gives the rational Δ numerator 2n²+n−1−(n+7)ab. For a=1 its numerator (n−2)(n−3); for a,b≥2 use ab≥2(n−2) to get negativity for n≥4. n=2,3 are zero; octagon probabilities (16,16,1)/33 vs (16,8,1)/25 on E=2,3,4 exhibit crossing tails. Independently generated exact triangulations for polygons n=2..7 and compared every fixed diagonal conditional law and sign; combinatorial proof supplies all n.

## originality

PASS

Global ear count and Catalan marginal formulas are old (Hurtado–Noy; Mansour–Rastegar). The original joint conditioning on a specified labeled diagonal, complete sign dichotomy and sharp stochastic-order counterexample were not located in the inspected original work; fixed diagonal is not a rotation-invariant local triangle weight. Broader generating-function recurrences might imply the result after further nontrivial extraction.

## value

PASS

A natural dependence question for two fundamental Catalan triangulation statistics is classified at every size and location, with a precise warning that a signed mean association does not imply stochastic domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
