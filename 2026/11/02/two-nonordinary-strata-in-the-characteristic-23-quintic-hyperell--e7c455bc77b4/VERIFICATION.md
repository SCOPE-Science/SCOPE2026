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

Eliminating a common root of x⁵+x+t and 5x⁴+1 gives t⁴=1 exactly in characteristic 23. For the Frobenius convention one can use the Čech classes y/x and y/x²: the coefficient in output row i, input column j is [x^(23j−i)](x⁵+x+t)^11. Independent expansion by occupied factor positions confirmed all four entries and det=2t⁴(t⁴+2). On t⁴=−2 the Frobenius matrix Mᵀ has image the first coordinate line and restricts there to the nonzero semilinear map z↦−5t z^23. Its stable rank is therefore exactly one, not an inference from one-step rank alone. With column vectors the two-step matrix is H H^(23); both orders of these two factors have the same image and nonzero eigenvalue 13 here. The zero and invertible matrices give stable ranks zero and two respectively. One-step ranks give the stated a-numbers, and a=2 is superspecial in dimension two. The determinant has order four at zero and all four other smooth roots are simple. Those roots lie in F529 by the multiplicative-order calculation and are not F23-rational since −2 is a nonsquare; the independent field replay confirmed all four. Under x=s²X, y=s⁵Y with s⁸=1 the parameter multiplies by s^(−2), acting transitively on the four roots; distinct p-rank separates their geometric curve from the center.

## originality

PASS

Credit only the complete mixed geometric p-rank stratification of this characteristic-23 pencil and its nonzero exceptional isomorphism class. Zhu's coefficient formula covers the determinant and one-step ranks by substitution, and the central superspecial curve is classical. Neither the generic-ordinarity theorem nor the sources on the central curve supply the exceptional stable Frobenius rank and the full pencil-orbit classification. No matching characteristic-23 statement was identified in the bounded primary and catalogue comparisons.

## value

PASS

For the standard sparse hyperelliptic pencil, understanding where ordinary fibers degenerate and distinguishing stable ranks there is a natural classification problem, not just a coefficient evaluation. An independent smaller-odd-prime screen supports the relevance of 23: at 3, 11, 17 and 19 the center is ordinary; at 5 and 7 the determinant vanishes identically; at 13 it is a nonzero multiple of t⁴, giving no second nonordinary parameter. At 23 a superspecial center coexists with both an ordinary generic fiber and a separate rank-one exceptional class. The four-to-one relation between nonzero parameter presentations and the single geometric class and the divisor multiplicities are useful exact data about that transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
