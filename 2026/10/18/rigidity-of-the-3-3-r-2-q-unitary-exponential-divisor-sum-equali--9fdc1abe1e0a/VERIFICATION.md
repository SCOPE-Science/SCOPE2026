---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For pairwise distinct primes 3,r,q, multiplicativity and the exact prime-power divisor definitions yield 28(r²+1)(q+1)=30(r²+r)q; solving gives q=14-210(r-1)/(r²+15r-14), so 0<q<14. Excluding q=3 and requiring primality restricts q to 2,5,7,11,13. The quadratic in r has discriminant Δ(q)=281q²-728q-784. Direct exact recomputation found Δ=-1116,2601,7889,25209,37241 respectively; only 2601=51² is a nonnegative square, and q=5 factorization 9r²-75r+84=3(3r-4)(r-7) forces prime r=7. At r=7,q=5, both divisor sums equal 8400 for 3³7²5=6615. This is a complete infinite-prime-pair proof by a bounded q inequality and integer discriminants; numerical prime searches are not used as proof.

## originality

PASS

Compared mathematical implications against primary literature, Resultary semantic findings, aliases and broader formulations. Best-of-knowledge priority only. Neither existing equality example nor a finite exponent-layer classification logically eliminates hypothetical solutions with a distinct large prime r. The q<14 algebra plus complete discriminant test does so.

## value

PASS

Trudgian explicitly identified 6615 as an early equality of two distinct multiplicative divisor sums and raised the distribution problem. Classifying the entire natural exponent-signature family (3,2,1) anchored at the cubic prime 3 turns that isolated known example into a rigorous infinitude-of-candidates rigidity statement. This is a narrow elementary result rather than a solution of the global equality problem; the exact uniqueness is not supplied by the cited example list or a finite search, and can be useful as a fixed-support benchmark. Its modest scope and inexpensive arithmetic are stated without inflated significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
