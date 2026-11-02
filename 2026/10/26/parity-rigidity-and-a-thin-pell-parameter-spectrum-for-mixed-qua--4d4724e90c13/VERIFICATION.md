---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For positive x,y, gcd=1 and x odd convert the divisibilities to xy|(x²+2y²+1). The quotient k≥3. The 2-adic valuation of x²+1 separates odd y (k≡4 mod8) from y≡2 mod4 (odd k). Integral positive Vieta conjugations in the odd chamber strictly descend according to sign of x²−2y², terminating uniquely at (1,1) and k=4. Completing squares gives u²−2y²=−1 and x=2y±u. The even chamber is exactly s²−(k²−8)t²=−1, y=2t and x=kt±s, with all parity and positivity converses checked; k=3 yields only (3,2), solvable odd k≥5 infinite by units. For primes p≡7 mod8, the two roots k²≡8 mod p are impossible because −1 is nonsquare. CRT over p≤√log X, the product bound and the Mertens progression estimate yield ≪X/√loglogX. Independently counted 15 pairs in 1≤x,y≤350 and parameters {3,4,5,7,9,11}; this is corroboration, not the infinite proof.

## originality

PASS

Best-of-knowledge priority comparison for Parity rigidity and thin Pell-parameter spectrum for x|2y²+1, y|x²+1: actual mathematical claims and implications, not title-only comparisons, evaluated against the listed primary sources and Resultary. Relevant prior methods are credited; no decisive stronger covering result was demonstrated within accessible readings. Residual priority risks remain explicit.

## value

PASS

The asymmetric 1:2 quadratic divisibility pair is a natural test of whether integral Vieta conics retain classification under nonmonic coefficients. The exact parity split, exceptional parameter, Pell fibers, and density-zero parameter set jointly answer a structural question; not merely a generic Pell rewrite or a trivial congruence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
