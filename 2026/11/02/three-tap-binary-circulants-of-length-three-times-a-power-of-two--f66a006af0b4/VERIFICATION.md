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

For P=x^(3m)−1=(x+1)^m g^m with g=1+x+x², a three-monomial f has f(1)=1. For a root ω of g the only nonzero binary relation on 1,ω,ω² uses all three, so divisibility by g for three taps occurs exactly with one tap in each residue modulo 3. For a singular support remove its least-exponent monomial and take the largest common dyadic divisor d of the two exponent differences. This is ≤m since the two positive differences are distinct and both <3m (they cannot both be multiples of 2m). In the residual trinomial the two exponent differences are not both even and are distinct modulo 3; its derivative at ω is consequently nonzero, whether it has one odd term or two. Frobenius and the gcd kernel formula give exactly g^d and the asserted ideal. CRT counts the supports agreeing modulo 2^t by 2^t(m/2^t)^3; adjacent differences give the census, including k=0 and the deepest stratum. Divisor monotonicity gives the actual nested ideals. The generator factors as (1+x^d) times the geometric sum at spacing 3d; the degree <2d multipliers give arbitrary independent even triples in one block, each repeated r times. This proves the ordinary Hamming weight enumerator (its binary complete enumerator is just its homogenization). For generalized weights, projections of a j-dimensional subcode have dimensions 0,1,2 with total ≥j and exact support costs 0,2r,3r; pairing one-dimensional projections reduces cost and filling dimension-two blocks first attains the bound by a direct sum. Independently, binary matrix elimination on all 19,561 supports for k=0,…,4 matched the census and checked the claimed block basis as the actual kernel of every singular matrix. Exhaustive shortened-code ranks over all coordinate subsets confirmed the full generalized weight hierarchy for n=3,6,12. A separate gcd replay also checked the rank strata through k=5 and the enumerators through k=3.

## originality

PASS

The general rank/gcd and cyclic-ideal kernel principles are prior. The distinct content is the exact census conditioned on three distinct taps in this mixed repeated-root length family, with the actual kernel attached to each stratum and its full support hierarchy. The closest inspected exact table and trinomial result change length, counted objects or invariants; the unrestricted rank counts cannot supply this fixed-sparsity census.

## value

PASS

This is a fixed-sparsity census in the first length family with one linear and one quadratic factor of arbitrarily high repeated multiplicity. It characterizes not only rank probabilities over all three-tap choices but the same labelled null-space code for each nullity and the minimum coordinate exposure of every subcode dimension. This links sparse convolution singularity to concrete coding invariants and goes beyond applying a generic invertibility test to a single trinomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
