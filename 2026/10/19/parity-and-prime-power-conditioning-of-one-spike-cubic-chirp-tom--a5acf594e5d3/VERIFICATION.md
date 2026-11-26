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

For k≠0 the cubic phase difference is −3kj²+3k²j−k³. The two impulse cross-terms give the bracket 1+ζ^(−kℓ) in the common phase; at k=0 the delta adds 3 to the identity autocorrelation row. If d divides both the quadratic coefficient and modulus with d their gcd, grouping lifts kills the Gauss sum unless d divides the linear coefficient and otherwise reduces it with factor d. The squared-modulus expansion for the reduced odd unit quadratic has only difference 0 surviving; for a primitive modulus 2^r, r≥2, the two survivors yield 2^r(1+(−1)^b) with reduced linear coefficient b, and modulus 2 gives the opposite parity branch. For p≥5 a surviving Gauss sum has modulus ≥√N; it cannot cancel the impulse terms and, for a≥2, cannot reach the much smaller candidate minimum. On the zero branch only shifts with positive valuation occur. The root nearest −1 is available in the largest possible odd phase order p^(a−1), exactly for valuation one and the displayed two phase residues, each with p frequency lifts. For p=3 unit shifts already permit a vanished Gauss term at unit frequencies, and both nearest-root frequencies are units; nonunit shifts have smaller phase order, and surviving Gauss terms are too large. Direct N=3 evaluation agrees. In the dyadic case a surviving Gauss term is too large to cancel; kℓ=N/2 mod N and a vanished Gauss term are both necessary and sufficient. At odd k the linear coefficient is odd, and at t=v₂(k)≥1 the product congruence fixes v₂(ℓ)=a−t−1, yielding the stated gcd/parity cutoff 2t≥a−1. Each allowed valuation contributes 2^(a−1) zeros; the direct N=2 window has one zero. Weyl conjugations act by distinct orthogonal characters on the Hilbert–Schmidt-normalized Weyl basis, giving singular values √N |A|/(N+3). The frequency sign in the bracket corresponds to M[−ℓ], which is immaterial to the multiset; at fixed k the modulus also agrees under ℓ↦−ℓ since g(−j)=conj(g(j)) and the correlation product is invariant under j↦k−j. Equality in the Cauchy–Schwarz upper bound can hold only for the identity, since any nonzero shift moves the unique modulus-two entry and nontrivial modulation is not constant on the full support. The two condition-number formulas and linear informational-completeness consequences follow.

## originality

PASS

The Weyl spectral reduction and the prime-dimensional nonvanishing component are covered. The distinct contribution of the finding is the cyclic prime-power arithmetic classification: sharp minima and full optimizing index sets on the stated odd branches, and the exact dyadic zero set and rank. The closest exact-margin record supplies a matching p≥5 scalar minimum as a later special case at impulse strength one, not established as prior coverage and not the whole classification.

## value

PASS

The unperturbed cubic phase is a standard chirp whose cyclic prime-power ambiguity degenerates. A one-coordinate repair is a natural minimal modification; computing the worst-case singular direction, its multiplicity and the surviving dyadic nullspace matters for operator reconstruction, beyond showing that some perturbation works. The least gap is controlled by different arithmetic in characteristic three and the other odd primes, and in dyadic dimensions the unit repair leaves an exactly measured rank obstruction. These are useful exact properties of this simple fixed design, not a claim of optimality among windows.

The dated certificate retains the supplied scientific assessment, sources and limitations.
