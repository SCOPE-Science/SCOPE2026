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

The cubic t³+at²+bt+1 has no zero root; in odd characteristic the sextic in x has a repeated root exactly when this cubic does. Its usual discriminant reduces to the stated Δ modulo 7. In the Cartier formula the off-diagonal x^(7i−j) exponents are odd and vanish, while the x⁶ and x¹² coefficients are b³+6ab+3 and a³+6ab+3. Each nonzero semilinear diagonal summand remains invertible under every iterate over the algebraic closure; rank and stable rank coincide. Thus the nullity is the a-number and stable rank is the geometric p-rank. The three smooth common zeros have a-number two, the superspecial criterion for the geometric Jacobian. The H_a graph has a≠0 and b=(a³+3)/a; putting z=a³, multiplication of the restricted discriminant by z gives −3(z+1)³. The three excluded a values are already rational; the swapped graph has the same form. Off the origin, each line of a³−b³=0 is the only member of that union through its intersection point, so the multiplicities are exactly the multiplicities of the restricted polynomial b³−ζb²+3. For ζ=1,2,4 it has respectively simple roots 2,4,1 and double roots 3,6,5. The simple pairs have Δ=4 and the double pairs have a³=−1, hence Δ=0. At a simple root the line derivative is nonzero and gives transversality; at a double root the local intersection ring has length two before localization to U. For every finite extension, a geometrically repeated root of a cubic is unique, hence Frobenius-fixed; the constant term forces s≠0 and the remaining root to be −s⁻². The coefficient formula is injective in s, so the singular count is q−1. Each graph has q−4 smooth points, with three common points, proving the three rank counts, also for q=7 where there are no rank-one coefficient pairs. Replay: RESULT.md Cartier, substitution and repeated-root proof; VERIFICATION.md and verify_symbolic.py/verify_fields.py were inspected, not run. The recorded two-field census does not establish the all-extension count.

## originality

PASS

The normal form, general bielliptic geometry and Cartier method are established. The distinct result is the full marked characteristic-seven Hasse intersection, including three simple smooth points and three doubled singular-boundary points, with closed marked counts over all finite extensions. The closest published moduli/count results and indexed analogous Hasse schemes are on genuinely different objects or do not yield these local lengths and counts.

## value

PASS

This exact stratification of a standard bielliptic family determines where its two Hasse factors coincide, and separates the actual superspecial fibers from points and multiplicities contributed by the singular boundary. The uniform counts make the marked family usable for finite-field comparisons and explain why an isolated finite census or unmarked moduli count answers a different question. There is no claim about isomorphism-class counts or stable reduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
