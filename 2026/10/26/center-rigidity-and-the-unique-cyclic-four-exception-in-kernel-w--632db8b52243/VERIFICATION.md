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

The product character is a homomorphism because the top is abelian and translations permute the factors; every base tuple determines exactly one top coordinate in the kernel. The balanced base projects onto each factor by using a second coordinate to cancel the character, and every top element has a lift. A central element moving the coordinates cannot fix a singleton supported in ker chi; if chi is injective and |T|>2, it cannot fix an opposite pair supported at x,y with the moved x outside {x,y}. Coordinate surjectivity then forces a central base tuple to have entries in Z(R), and top surjectivity forces them to agree. Conversely, each such diagonal is in the kernel since chi(c)^|T|=1 and it commutes with the full wreath product. In the remaining case an element with base (a,1) and top a squares to the nonidentity diagonal, hence generates the order-four kernel. Since the group order changes by |R| to |R|^|T| at each step, an exceptional step can occur only initially. The A4×C5 seeds and p=3,5 towers are as in Damele and give center C5 and order 60^(p^m). The argument is uniform, not an extrapolation from nine finite examples; the uploaded checker was inspected, not run.

## originality

PASS

The distinct claim is the uniform center classification with uniqueness of the exception, and hence the center invariant in the towers. Do not credit the construction, tower existence, or the exceptional identification G≅C4 in isolation: the latter is explicit in the September 18 Resultary record for the same kernel. The classification is supported by the comparisons below, not a claim of absolute priority.

## value

PASS

An exact multiplicative-group center is useful for distinguishing the invariants of growing simple skew braces from their additive-group structure. The classification settles all allowed quotient choices at once, including uniqueness of the only possible enlargement, and reads off a persistent C5 in both natural A5 towers without enumerating their elements. The prior C4 computation alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
