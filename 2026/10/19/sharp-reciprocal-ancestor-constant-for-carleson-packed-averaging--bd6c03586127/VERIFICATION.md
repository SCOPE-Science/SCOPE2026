---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Ancestors of a positive-mass S form a chain. Each member P above S has only finitely many ancestors of S below or equal to P, because each such member contributes at least ν(S) to packing at P. Consequently the number of strict predecessors in that chain indexes its members by consecutive nonnegative integers (finite or infinite). For normalized masses x₀=1, packing at Pⱼ says the earlier total is at most (Λ−1)xⱼ; simultaneously xⱼ≥xⱼ₋₁. Taking equality at the larger of the two lower bounds recursively gives a coordinatewise minimum yⱼ by induction. For Λ>1 the first n=⌊Λ⌋ terms, including y₀, equal 1; the next is n/(Λ−1)>1, including at integer Λ. Thereafter the prefix bound binds at every step, multiplying masses by Λ/(Λ−1). The reciprocal tail sums to Λ(Λ−1)/n. For Λ=1 the presence of any proper ancestor already contradicts packing there. For sharpness take a finite prefix chain with successive singleton masses yⱼ−yⱼ₋₁ and initial mass 1; zero-mass added points distinguish equal-mass sets under actual inclusion. For every measurable Ω containing some prefixes, its contained family is the initial segment through a maximal prefix, whose packing ratio bounds that of Ω because ν(Ω) is no smaller. The ratio at prefix n is exactly Λ for each truncation including n, and the normalized reciprocal sums approach the infinite constant. If Λ=n+δ the deficit from 2Λ−1 is δ(1−δ)/n; the quadratic comparison follows from (Λ−1)²≥0. The frozen checker was read, not executed. Separate `python3 /workspace/checks/frozen_math_checks.py 5` passed exact rational packing over every measurable subset of eight finite witnesses, including their least constants and geometric deficits. Those checks corroborate the proof, not the quantifiers over all families and all real packing constants.

## originality

PASS

The scalar ancestor sum, packing convention, chain reduction and a Λ² estimate are directly prior in Conde Alonso–Monti–Rizzo. Credit those inputs. The exact floor-dependent optimal bound and near-extremizing families with exact least packing constant are the distinct contribution; neither follows by substituting parameters into the prior Λ² estimate or into the Carleson/sparse equivalence.

## value

PASS

This is the sharp constant of an existing, motivated positive kernel bound in sparse averaging, not an arbitrary slice of a known estimate. It improves quadratic scaling to sharp linear-order growth and explains the discrete floor effect and the role of repeated equal masses in near-extremizers. The finite examples show the result cannot be lowered even at prescribed least packing constant, without overstating any implication for general operator norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
