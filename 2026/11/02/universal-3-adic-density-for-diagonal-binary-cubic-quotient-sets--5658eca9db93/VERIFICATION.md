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

A 3-adic unit is a cube exactly in the two classes ±1 modulo 9: cubing establishes necessity; after writing (1+3s)^3=1+9(s+3s²+3s³), simple-root lifting gives sufficiency. The subsequent lifting steps use affine reduction as a polynomial modulo 3, not merely agreement as a function on the three residues. For αx³+3βy³, first choose the sign of the required cube residue modulo 3, then y∈{0,±1} to correct modulo 9. The values include all units and 3β, so ratios cover all units in valuation classes 0, 1 and −1. For equal coefficient valuations, a unit root gives all of 9Z₃ by expansion and lifting; absent a root, expanding at the sign r with αr³+β divisible by 3 gives values filling one of the two valuation-one classes modulo 9, and oddness supplies the other. Ratios then again cover all three valuation classes modulo 3. Scaling only the numerator or denominator supplies every valuation shift divisible by 3. Restricting one variable by a positive power of 3 reduces arbitrary coefficient valuation gaps to these cases, including gap 2 modulo 3 after swapping. Zero is represented separately. Continuity at a nonzero denominator and density of integer vectors give density, not exact equality, for the integer ratio set. Other variables can be set to zero. Frozen RESULT.md lines 23–69 are a proof; the inspected finite-residue verifier was not executed and is not needed for the infinite conclusion.

## originality

PASS

The distinct claim retained is the arbitrary-coefficient binary cubic classification at p=3, with exact Z₃ quotient surjectivity and the resulting integer density. The prior unweighted special case is credited, whereas two precise published-preprint statements give the opposite verdict on examples in the supported regime. No exact or stronger covering result was established by the bounded comparison. This is not a claim of historical priority or of novelty of the lifting method.

## value

PASS

The prime dividing the cubic degree is the natural case where unit-cube and lifting behavior changes. The theorem resolves the full binary diagonal classification at this prime and supplies two mathematically decisive boundary counterexamples to the checked non-density claims, as well as the stronger exact local image statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
