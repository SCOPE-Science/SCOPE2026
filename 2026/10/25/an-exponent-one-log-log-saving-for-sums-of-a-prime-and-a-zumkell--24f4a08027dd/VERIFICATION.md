---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: The minimally abundant consecutive-prime block B crosses 2 by its last prime, and C=product(1-p^-2)=1+O(1/P), giving phi(A)/A=C/B=1/2+O(1/P) from below. The Zumkeller divisor partition implies sigma(z)>=2z and phi(z)sigma(z)/z^2<1, proving the per-seed strict bound. Prime Mertens gives Q asymptotic P^2; iterated disjoint blocks have sum 1/P_j finite and log z_j<=exp(D*2^j), producing K*2^-r failure product. Linnik primes in the appropriate reduced residue classes force representation outside size O(z_j^(2L)), and CRT contributes X*2^-r plus the essential O(Z_r) endpoint error. Choosing 2^r comparable to log log X makes Z_r and thresholds X^o(1); separate even-seed Linnik step bounds odd exceptional integers by a power saving. Independently checked four rational prime blocks and three full-period CRT families; finite checks do not prove the global asymptotic.

## originality

PASS

PASS, qualified: Li 2026 Theorem 1.2 gives the weaker exponent A=log2(2*pi^2/(2*pi^2-3)) about .2378 and uses essentially the same prime blocks. Its proof takes phi(A)/A>3/(2*pi^2) instead of the sharp asymptotic 1/2 and does not state the exponent-one claim. The other block-existence input is published; local per-seed density is an evaluated sharpening, not a proof of global optimality.

## value

PASS

PASS: A quantitative exponent-one strengthening of an explicit new analytic exceptional-set problem is nontrivial, using a sharp local Euler-product obstruction plus a correct finite-interval CRT remainder; it yields an exact mechanism with meaningful scope and does not rely solely on finite samples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
