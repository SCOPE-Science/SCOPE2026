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

Actual RESULT.md blob b8381dd2c1a8501336475d637374e7a0edb130a7 starts from Merca a(m)=(σ(m)−λ(m))/4 for odd m and a(2^km)=a(m)+(2^(k−1)−1)σ(m) for k≥1. Reconstructed local 2-adic valuations: if λ(m)=0 one p ≡3 (mod8) and exponent 1 (mod4); otherwise σ−λ mod8 isolates p ≡5 (mod8) same exponent, while even exponents yield odd-square Jacobi (2/t). For nonsquare odd m=p^(4h+1)u², p ≡3,5 (mod8), PNT in the two residue classes and sum of reciprocal odd squares π²/8 give F(Y)~π²Y/(16 logY), dyadic summation doubles constant; square branch is O(sqrt X). Independently enumerated direct signed representation/parity for n<=1799. Checks test low n; global proof additionally assumes the published Merca coefficient/dyadic identities and classical PNT AP.

## originality

PASS

Merca published the full coefficient formula and subsequent dyadic identity; these stronger formulae are explicitly prior, so parity is algebraically derivable, but the complete exact mod2 support and prime-density asymptotic are not stated in the inspected original primary full article. OEIS A192717 covers the p≡3 subsequence and is acknowledged. Second dyadic article was found at abstract but full-text retrieval failed through authorized Oxford VPN; relevant coverage remains a specific risk rather than automatically failing originality.

## value

PASS

The arithmetic support of a natural signed partition function is sparse at prime rather than square scale; a sharp positive leading constant and all dyadic parity flips are meaningful information not conveyed by an unevaluated divisor-sum formula. The result is a natural global density theorem, not just rewriting a congruence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
