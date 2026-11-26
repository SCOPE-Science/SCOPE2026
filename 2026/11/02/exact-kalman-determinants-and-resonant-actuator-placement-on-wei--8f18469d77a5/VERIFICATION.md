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

The claims hold for the n+1 state combinatorial Laplacian, n≥3 and t>0. In RESULT.md 45–83 the constant and hub-against-path modes have eigenvalues 0 and (n+1)t, and the orthonormal cosine modes on the path have eigenvalues t+λ_k. Substitution at the path endpoints as well as the interior gives the ordinary path eigenvalues, and each nonconstant cosine mode sums to zero. The only collision is the double eigenspace at nt=λ_k. A coordinate vanishes when (2j−1)k≡n mod 2n. For d=gcd(2j−1,n) this gives odd multiples of n/d below n, none if d=1; for two sites, writing D=gcd(n,2j−1,2ℓ−1), simultaneous zeros are odd multiples of n/D below n. For d=1 multiplication by 2j−1 permutes the sign-paired residue classes k≠0,n mod 2n, preserving the product of absolute cosines, equal to √n/2^(n−1). In the normalized eigenbasis the Krylov determinant is the product of the modal coordinates times the Vandermonde. The coordinate product is 1/[(n+1)(2n)^((n−1)/2)], while the path-only Vandermonde is 2^((n−1)/2)n^((n−3)/2), by multiplying |q'_n(λ_k)|=n/[2 sin²(kπ/n)] and taking the square root. The remaining eigenvalue differences give (n+1)t, |q_n(−t)| and |q_n(nt)|, yielding the stated t/n. This accounts for hub invisibility and all singular cases. The count is φ(2n) because the coprime sites correspond to the units mod 2n. At resonance a common zero at the colliding k also defeats the two-dimensional PBH restriction, even if no other mode is invisible. For two path sites the two restrictions are independent iff their cosines differ, giving exactly the two divisibility exclusions in RESULT.md 27–33; the hub coordinate separates the hub mode from the colliding path mode. The endpoint alone works off resonance, and its pair with the hub works even at resonance. The derivative of the simple root gives the claimed positive absolute slope. Independent exact rational replay: python3 /workspace/branches/independent_math_checks.py; 110 determinant and 260 pair-rank checks at 20 (n,t) cases, including rational resonances. This does not check irrational resonances or all n; the analytic proof covers them. The supplied verifier was inspected, not executed.

## originality

PASS

The supported distinct claim is the exact weighted-fan Krylov determinant with its common magnitude across visible sites and the full resonance-specific placement criterion. Bare-path observability, the robust zero-forcing placements, the general join diagonalization and PBH, and simple-root differentiation are not new contributions. No inspected prior statement subsumes the fan-specific determinant and placement classification. This is a best-of-knowledge judgment, not a priority certification.

## value

PASS

A uniformly coupled apex is a natural perturbation of a path consensus model. The exact formula shows both a site-independent Krylov volume at admissible sites and the complete finite set of forced failures; the sharp two-site rule identifies viable replacements rather than only giving a sufficient choice. For example, the two opposite path endpoints at n=4 are individually admissible away from resonance but their pair fails at t=1/2, whereas the hub–endpoint and neighboring-endpoint pairs remain controllable. This is useful for exact parameter and site selection beyond an unevaluated PBH condition. The magnitude is measured in fixed vertex coordinates and is not interpreted as control energy or a Gramian.

The dated certificate retains the supplied scientific assessment, sources and limitations.
