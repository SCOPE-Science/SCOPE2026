---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For p=2 direct values beta(3)=2,beta(4)=3,beta(5)=4 rule out both neighbors. For p odd, beta(2p)=p−1 and m=2p+epsilon imply 2 beta(m)=m−c, c=epsilon+2 in {1,3}. Exhaustive factorization for odd m with Omega(m)<=3: prime, square, cube, qr, q^2r are excluded by the displayed exact identities/positivity; qrs with q>=5 or q=3,r>=7 is excluded by the multiplicative ratio bounds >1. Thus q=3,r=5 and 16(s−1)=15s−c, whence s=16−c: only c=3 yields prime s=13, m=195 and p=97. Independent factorization check for all primes p<10000 returned only (97,195), beta(194)=beta(195)=96. The six-case analytic exhaustion, not finite search, proves all primes.

## originality

PASS

Tóth surveys the known unrestricted consecutive collision 194,195 and poses infinitude; OEIS A206368 explicitly lists 194. Those sources do not establish uniqueness under the two natural constraints (even neighbor 2p and odd neighbor Omega<=3). The novel theorem is the uniform low-prime-complexity rigidity, not the already published sample pair. Resultary related restricted divisor-sum findings concern different arithmetic equations; no matching stronger beta classification surfaced.

## value

PASS

The alternating beta collision problem is explicitly open in the original survey. The first nontrivial known 194=2·97,195=3·5·13 example has Omega=3 odd neighbor; proving it is the *only* solution with a twice-prime even neighbor and at most three odd prime factors is a meaningful sharp natural rigidity slice. It is a universal theorem, not a recomputation of the OEIS value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
