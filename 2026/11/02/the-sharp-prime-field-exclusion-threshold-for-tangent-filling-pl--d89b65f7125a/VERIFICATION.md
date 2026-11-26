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

Coverage by rational tangents dualizes to a blocking set. For a geometrically integral cubic in p>3, its irreducible dual has degree at most six by intersecting with a general dual line and pulling back to a polar conic. It cannot be a line: concurrency of the tangents would make the quadratic directional derivative toward that point vanish identically on the cubic and hence as a polynomial, which in p>3 would make the cubic independent of one variable and geometrically reducible. Thus p+1>6 excludes a full dual line. Blokhuis gives 3(p+1)/2, while distinct smooth points have distinct tangents by Bézout. For p=11,13, Hasse forces exactly 18,21 points respectively. A geometrically integral singular cubic has at most p+2 rational points by its genus-zero normalization and unique possible singular point; a ground-field irreducible geometrically reducible cubic has no smooth rational point because its three lines are Frobenius-conjugate. The published prime-field bound covers p≥17. For the remaining smooth cubics, an origin exists by Hasse, and the short-Weierstrass classification exhausts pointed curves. Any rational degree-three embedding arises from O_E(2O+T), modulo translation by a rational point (hence modulo 3E(F_p)) and projective basis change. For T=(r,s), s≠0, Y=(y+s)/(x−r) has simple poles at T and O and is regular at −T, so 1,x,Y form a basis of L(2O+T); substitution yields the stated cubic. Independent exact finite-field computations confirmed both single scaling orbits; the listed cosets have sizes 6,6,6 and 7,7,7 and exhaust the underlying groups. The six (points, tangents, coverage) triples are (18,18,114), (18,18,112) twice; (21,21,145), (21,21,156) twice, strictly below 133 and 183. The F_7 witness covers all 57 points by twelve tangents, and the gradient argument excludes common nonzero zeros even over the algebraic closure.

## originality

PASS

The distinct claim is exclusion of cubic tangent filling at both 11 and 13, completing the threshold theorem. The general bound, dual blocking-set reduction and characteristic-seven existence are prior and are not credited as new. No inspected relevant claim implies the two residual primes. This is a bounded literature assessment, not an assertion of global priority.

## value

PASS

This resolves the sharp prime-field transition for a natural geometric covering question. The residual primes are forced by general bounds, rather than an arbitrary computational slice. Exhaustion of all degree-three embedding classes rather than just elliptic curves is the key step that makes this finite calculation a complete exclusion theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
