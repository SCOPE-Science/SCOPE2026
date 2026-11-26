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

In odd characteristic the sextic is squarefree exactly for t≠0,1. The two quotient maps give elliptic curves and their differential pullbacks are 2x dx/y and 2 dx/y, a basis. Thus the quotient maps induce a separable isogeny to the product, so the Newton polygons are assembled from the two elliptic factors. Cartier is diagonal because the off-diagonal exponents are odd; at each geometric parameter the nonzero diagonal entries persist under semilinear iteration, giving stable rank equal to rank and a-number equal to 2 minus rank. An independent multinomial expansion gives the two diagonal factors exactly, their monic gcd t²−t+1 at 17 and gcd 1 at 3,5,7,11,13. Thus the common Hasse zero gives a-number 2 and superspeciality; precisely one diagonal zero occurs at 5,7,11,14. For the quotient j formulas, applying the cubic invariants to E1 gives 64(3t+1)³/[t(t−1)²]; inversion u↦1/u in the quartic model gives a twist of E1 at 1/t and the stated E2 invariant. Modulo the common quadratic the denominators are units and both invariants are 8. The quadratic discriminant 14 is nonsquare in F17, and subtracting the excluded and exceptional parameters gives (0,4,11) and (2,4,281). These are marked counts; inversion of the original x gives the geometric t↔1/t identification. The first-prime result is for this pencil and odd primes only. Independent certificate: /workspace/branches/430c75c1-717f-4000-b335-ce3931326929/record4_poly_check.py, with adjacent record4_poly_check.txt; frozen script and snapshot were inspected, not executed. The certificate checks finite-field algebra, not the general Cartier or isogeny facts.

## originality

PASS

The distinct claim supported by the comparison is the full marked rank stratification and prime boundary in this reciprocal one-parameter pencil, not discovery of an unmarked superspecial curve type. Classical bielliptic normal forms, the prior polynomial criteria for superspeciality, and prior superspecial counts by unmarked automorphism group materially cover background and the class containing the rank-zero pair. The compared sources do not give the common-zero and rank-one slices together in the marked coordinate or the smallest prime for this pencil.

## value

PASS

The model fixes an opposite branch pair and arranges the other four branch values as the roots of x⁴−t. Its natural reciprocal symmetry exchanges the elliptic quotient j maps, so the problem asks whether and where their supersingular conditions actually meet in one coefficient. The split between a quadratic common locus, four rational parameters with exactly one supersingular factor, and the remaining ordinary parameters is an explicit benchmark for rank stratification in a geometrically motivated slice. The first odd prime and field-of-definition distinction give useful boundaries. The contribution is not a re-count of unmarked superspecial curves or a new general test for superspeciality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
