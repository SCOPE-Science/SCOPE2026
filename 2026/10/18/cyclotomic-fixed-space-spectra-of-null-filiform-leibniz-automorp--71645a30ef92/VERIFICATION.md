---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The bracket recursion makes the first column determine the automorphism; any column with first entry a≠0 gives a triangular map with diagonal a,a²,…,aⁿ and preserves all zero brackets. On k[t]/(tⁿ) this map is aU(t)σ_a. In the conjugacy equation U(t)W(at)=H(t^ℓ)W(t), the degree-j coefficient of the new gauge term is aʲ−1, so a choice can be made at every degree, with only multiples of ℓ retained in H. The cyclic norm is conjugacy invariant and equals H^ℓ; raising to ℓ is bijective on the abelian principal-unit p-group, giving uniqueness. The centralizing gauges are the units supported at multiples of ℓ, so all normal forms have the stated equal-size fibers. Only the exponent residue ℓ−1 can support fixed vectors. With m=⌊n/ℓ⌋ this block is multiplication by H−1 on k[z]/(z^m), giving dimension min(m,ord(H−1)) or zero for m=0. Uniform coefficients of H give the displayed multiplicities; ℓ=1 and m=1 obey the same count, and the ℓ>n case gives the fixed-point-free criterion by cyclicity of k×. Burnside accounts for ordered tuples and the one-tuple count follows also by making the leading coordinate an i-th power orbit and removing all higher coefficients by principal units. Fresh exhaustive elimination for (q,n)=(2,4),(3,4),(5,5),(7,4) agreed with all histograms, including a fixed-point-free sector, and an explicit nonconstant ℓ=2 conjugacy over F₅ preserved the computed fixed rank.

## originality

PASS

The all-automorphism fixed-space polynomial in the natural n-dimensional representation is the supported distinct claim. The triangular parametrization and group structure are established. The strongest same-family catalogue comparator contains the same norm-based normal form and equal fibers, and another gives the one-tuple orbit count; neither is credited here as an independent originality gain. The same-family element-order and abstract conjugacy counts do not count the individual fixed-block ranks, which require resolving the full first nonzero resonant coefficient rather than just thresholds for its p-power order.

## value

PASS

The fixed-space polynomial is a natural invariant of the actual automorphism action, rather than an abstract group order. It distinguishes nonsemisimple operators within a scalar order, gives exact probabilities of each fixed dimension, and by Burnside supplies all tuple-orbit counts rather than merely the one-vector marginal. Those uses justify the precise census even after crediting the known normalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
