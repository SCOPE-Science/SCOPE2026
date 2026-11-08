---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Congruence t_j=t_i mod p^a is equivalent to p^a|2ds, d=j-i>=1, s=i+j-1>d, d+s odd. This bijection exactly translates minimizing j to minimizing odd d+s. For odd p, with m=min(v_p(d),v_p(s)), M=max, odd/even parity forces lower bound 2p^m+p^M, optimized at m=floor(a/2). Splitting even and odd a gives minimal sums 3p^k and (p+2)p^k respectively and equality forces unique opposite-parity (d,s), with s>d; for p=2 the even member must be multiple of 2^{a-1}, giving unique minimum (d,s)=(1,2^{a-1}). All boundary conditions a=1 and p=2 hold. Direct independent residue maps confirmed exact first collision and unique predecessor in 66 finite prime powers. The proof is universal; finite tests are supplementary.

## originality

PASS

Z.-W. Sun 2013 proves the least *modulus* among all moduli separating the first n sequence values and gives the 2-power witness in Theorem 2.2(ii), which is thus prior-covered and credited. Its theorem does not fix an arbitrary prime power p^a and determine the exact longest collision-free prefix plus unique predecessor, particularly odd a>=2. Park 2013 treats discriminators of other quadratic polynomials; Sun 2013/2016 related least-modulus sequences differ. O PASS qualified for the complete odd-prime-power parity classification, not for the standard factorization or the 2-power witness.

## value

PASS

A natural local refinement of a canonical quadratic discriminator sequence yields exact first collision horizons for all prime powers, uniqueness and a sharp even/odd exponent transition, relevant to modular injectivity bounds. Beyond the elementary p=2 and a=1 edges, its all-prime-power classification is a motivated exact arithmetic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
