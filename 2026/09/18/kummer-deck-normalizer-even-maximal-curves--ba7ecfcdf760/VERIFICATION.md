---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

I reconstructed the cover and the lifts. The valuation 1 at u=0 proves degree m by Eisenstein, and k contains the m-th roots of unity. The simple roots of (u^(q²)−u)/(u^q−u) are precisely F_(q²) outside F_q; deg f=q^n gives the infinity label 1 modulo m. If d divides r and m, then q^(n−1)=1 and q^n=−1 modulo d, so q=−1 and the odd-length geometric sum r is 1 modulo d; hence d=1. For n≥4 the two exponents 1 and r are distinct modulo m. A normalizer preserves the fixed field and must send z to h(u)z^t by the deck eigenspaces, with t a unit mod m. Taking valuations of f(M(u))=h(u)^m f(u)^t shows that t permutes the labels. A swap would exchange classes of unequal sizes q+1 and q²−q (also unequal at q=2), so t=1 and the classes are preserved. The stabilizer of P¹(F_q) is PGL₂(q), by the action on three distinct points. Independently, for matrices over F_q, M(u)^(q^i)−M(u)=det(M)(u^(q^i)−u)/(γu+δ)^(q^i+1), for i=1,2, giving f(M(u))/f(u)=det(M)/(γu+δ)^m. The norm from k to F_(q^n) supplies all determinant roots λ. The kernel is exactly the m deck transformations; they commute with every lift. The quotient PGL₂(q) has trivial center: a central element must preserve the unique fixed point of each point stabilizer and so fixes all points. This proves the stated center and order. The same label argument works after base change, and all lifts are already defined over k. For n=2 the labels coincide; the proof requires even n≥4 and does not determine the full even-n automorphism group.

## originality

PASS

Credit Ma–Wang with the model, ramification and every explicit lift, and older cyclic-cover theory with the branch-label method. The supported addition is the exact stabilizer of the distinguished Kummer structure in this even-n family and its consequences, not the existence or order of the candidate subgroup in isolation or a new general normalizer principle. The strongest inspected comparisons do not establish this even-n identification.

## value

PASS

The result closes the natural quotient-preserving portion of the even-family automorphism problem. In particular, the known subgroup is maximal among automorphisms preserving the specified Kummer structure, and any extra automorphism must move the deck group. This eliminates a plausible source of extra automorphisms, including at small q, without conflating the stabilizer with the full group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
