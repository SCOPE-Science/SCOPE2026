---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Each nonempty ideal has the root and an independently chosen prefix on every arm, giving 1+∏b_i including the extra empty ideal. For a single arm with b prefixes, binary search shatters depth floor(log₂ b) (split into two sets of at least 2^(floor(log₂ b)−1) when b≥2) and the hypothesis count prevents any greater depth. For the pure disjoint-domain product, concatenate factor trees to attain the sum; conversely each query splits only one factor, whose smaller-dimensional nonempty child has dimension at most the original factor dimension minus one. Induction on version-space size gives the summed upper bound. In the augmented product keep the distinguished root even during negative restrictions, and allow a coordinate count of 1. The root query contributes one, and a depth-j query along arm i gives a pure product with count b_i−j on the positive side and an augmented product with count j on the negative side. This exhausts nonconstant queries; an all-ones augmented box, including zero arms, has rank one. For A=∑floor(log₂ b_i)>0, the induction hypothesis and the pure positive child bound every split by A+1. To achieve A+1 both children must have rank at least A; with a=floor(log₂ b_i), positivity forces j≤b_i−2^a≤2^a−1. The negative baseline has lost at least one level. Equality can only be rescued by its bonus, so j=2^a−1 and all other counts are Mersenne. Then b_i−j≥2^a forces b_i=2^(a+1)−1. Conversely this very split gives two children of rank A when all counts are Mersenne. The root query cannot supply the bonus for A>0, and monotonicity gives the baseline when no bonus is possible. This proves the formula in the full stated family; the 183-case frozen verifier and recorded output were inspected, not executed or used as the infinite proof.

## originality

PASS

The supported contribution is the exact one-bit change after adjoining the empty ideal and allowing the shared root query. Independent-arm binary search and additive rank are standard. The strongest identical restricted classification is for lengths 1 and 2, in a later catalogue record; an earlier two-row ideal problem uses coupled cuts and does not cover a spider with arbitrary arm lengths. The inspected broader definitions and algorithms do not themselves determine the Mersenne bonus.

## value

PASS

Rooted spiders are a natural first branching family of order-ideal concept classes. The exact rank quantifies when one additional hypothesis and the shared-root query improve the worst-case adaptive mistake depth despite independent-arm additivity. The equality criterion is substantive: two arms with b=3 and b=5 and one arm with b=15 both give 16 ideals, but their dimensions are 3 and 4, respectively. The formula supplies a sharp baseline for studying which branching features beyond a single root alter online rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
