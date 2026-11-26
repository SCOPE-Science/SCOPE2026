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

Independent proof reconstruction for primes p≥5: conjugation sends each Weyl input to a distinct output character times its ambiguity coefficient. The input Hilbert–Schmidt norm is p^(3/2), the output character norm p^3, so singleton intersections give singular value sqrt(p). For a nonzero curve difference the first coordinate is the nonzero parameter increment and the second uniquely fixes the base parameter; this yields precisely p(p−1) nonzero shifts, with one term at every frequency on those shifts and no terms at other nonzero shifts. At zero shift the multiplicity polynomial has degree at most p−1, and a primitive pth-root zero forces it to be 1+X+…+X^(p−1). Hence cancellation is exactly permutation. Nonconstant linear phases permute; genuine quadratic phases have a reflection collision. After depression of a cubic to t^3+ut, any u≠0 gives a distinct-input collision: for c=−4u the number of solutions of 3s²+v²=c is p−χ(−3)>2, and at most two have v=0. The character-sum identity follows by factoring (s−b)(s+b)=a≠0. For u=0, the cube map permutes exactly for p≡2 mod 3. Counting yields the stated two ranks, the full complementary Weyl basis, and precisely p^4(p−1) supported nonzero-shift singular directions, without claiming this is the total multiplicity of sqrt(p). Applies to the full complex-linear map, not pure-state injectivity. The frozen finite verification was inspected, not re-executed; it is not the arbitrary-prime evidence.

## originality

PASS

The Weyl diagonalization, prime-root permutation criterion, and cubic permutation facts are not the novelty. The closest indexed exact-rank result has a different ambient space, shift geometry, and permutation family. None of the inspected statements gives or mechanically specializes to the cubic moment-curve rank, kernel and supported nonzero-shift band together. This is a scoped judgment from the evidence, not a priority guarantee.

## value

PASS

The standard cubic moment curve is a natural sparse window with maximal uniqueness of its ordered nonzero differences. Exact tomography rank and a full operator nullspace determine the recoverable linear directions; the supported nonzero shifts also have a fixed singular scale. The arithmetic deficit at zero shift distinguishes the two prime classes in a way a difference-set count or generic Gabor theorem alone does not. This is a narrow structural invariant, not a claim of phase retrieval or general stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
