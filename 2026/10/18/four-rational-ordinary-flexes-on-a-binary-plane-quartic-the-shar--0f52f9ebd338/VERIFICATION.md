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

A smooth plane quartic has no line component (a complementary cubic meets it), and a rational line with three rational flexes would have a fourth rational degree-one factor repeating one root. At that flex the line would then be the tangent and have multiplicity at least three, contradicting degree four. Thus all rational flexes, including hyperflexes, form a cap. Three cap points are a basis over F2, and their sum is the only possible fourth; the three remaining points form a Fano line, giving seven four-caps. An ordinary tangent with residual Q gives the exact normalized restriction F(sP+tQ)=st³, since the sole nonzero scalar is 1. Conversely this restriction on a geometrically smooth form forces its unique tangent and exactly that ordinary flex. An independent restriction-table enumeration with SymPy unit-ideal tests on all three affine charts (python /workspace/branches/independent-reproductions/contact_reproduction.py 5) found 308 candidates and 168 smooth forms. On the fixed cap it found 30 consistent residual assignments, each with two coefficient masks, 44 distinct candidates, and 24 distinct smooth arrow graphs of the required shape; it checked that the rational points on each smooth candidate are precisely its four ordinary flexes. The witness in the frozen coordinates has mask 4418 and arrows 1→2,2→4,4→1,7→4. The cap stabilizer realizes every permutation of the four points by basis change and acts transitively on the labelled three-cycle-plus-tail graphs; a graph stabilizer fixes the tail and its target and then the other cycle vertices. Thus the projective orbit is free and unique. Frozen programs and expected outputs were inspected, not executed; the finite enumeration uses geometric smoothness, not a field-extension sampling cutoff.

## originality

PASS

The exact cap and residual-arrow reconstruction is not given by the inspected earlier literature or indexed companion results. A later indexed census exactly agrees on the maximum, unique extremal class and same representative, so those are not exclusive catalogue content. It does not state the specific directed-graph bijection in the inspected passages. The catalogue is later by the displayed record dates; no stronger claim about historical priority is made.

## value

PASS

Ordinary flexes are canonical tangent divisors for a nonhyperelliptic genus-three curve. The small-field obstruction forces a Fano cap, and directed residual incidence then determines the whole quartic, with no projective stabilizer left. That rigid reconstruction and distinction from hyperflex/contact coverage are meaningful beyond recomputing the count of models. The claim is restricted to rational contacts of smooth binary plane quartics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
