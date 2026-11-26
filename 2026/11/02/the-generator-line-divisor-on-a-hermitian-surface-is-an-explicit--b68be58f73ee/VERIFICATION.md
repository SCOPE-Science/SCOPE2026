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

Expanding F on a geometric line U gives both cross pairings and both self pairings zero (the monomials are distinct even for q=2). Thus U^[q]=U^perp for the ordinary dot product, and applying Frobenius twice gives U^[q²]=U. On a rational generator the q³- and q-power maps agree on a rational basis, so G restricts to zero. Conversely, for any nonrational common zero [x], x and x^[q²] span a line on S: the self pairings vanish, one cross pairing is G(x), and the other is F(x)^q. For rational points the nondegenerate binary Hermitian space P^perp/P has q+1 isotropic directions, by the norm map after diagonalizing; hence all those points also lie on generators. As an independent check of the counts, the number A_n of affine zero sums of n norms satisfies A_1=1 and A_(n+1)=(q+1)q^(2n)−qA_n by the norm fiber sizes. This gives A_4=q^7+q^4−q³ and (A_4−1)/(q²−1)=(q³+1)(q²+1); double counting the incidences gives (q+1)(q³+1) lines. S is smooth and integral (positive-degree hypersurface components in P³ would meet). The gradients of F and G are dependent precisely at projectively F_(q²)-rational points, by nonzero coordinate ratios. Since they are independent at some points of S, F does not divide G. The resulting complete intersection has degree exactly the number of contained distinct lines, so every generic multiplicity is one and there are no other components. Cohen–Macaulayness rules out embedded primes and gives saturation (the irrelevant ideal is not associated). Thus the singular support follows from the rank test, and actual distinct lines give the q+1 tangent directions at each rational point. The standard complete-intersection formulas give the Hilbert series and genus; the generator modulo F has the claimed relative first degree. This is the all-q proof; the frozen q=2,3 enumerations are only finite checks and the uploaded code was not executed.

## originality

PASS

The supported distinct claim is the exact saturated ideal of the full reduced generator union, including the first additional equation modulo F. The Hermitian surface, point and line counts and rational tangent-plane sections are established geometry. The strongest inspected overlap uses the very same Frobenius pairing on degree-three points, but does not supply the geometric zero-divisor identity or its scheme structure. No priority assertion is made.

## value

PASS

The generator union is the intrinsic line arrangement on the smooth Hermitian surface, uniformly in every prime power. Its first equation modulo the surface equation and its scheme-theoretic complete-intersection description answer a natural reconstruction question that a point or line count does not answer. They make the coordinate ring, genus and reduced singular branches accessible without enumerating the generators.

The dated certificate retains the supplied scientific assessment, sources and limitations.
