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

The stated gcd assumption gives T ≡ q−1 on the subfield and gcd(T,N)=S. Thus H=ker(x↦x^T) has order S, H∩L×=F_q×, and the product H·L× covers K× with constant multiplicity q−1. The congruence on r makes F(uz)=u^r Lcalligraphic(z), so the mth iterate acts separately on the two representatives. A fixed pair up to the overlap has Lcalligraphic^m(z)=λz and u^(r^m−1)=λ^(−1). The cyclic power map has g_m preimages of λ^(−1) exactly for λ^(S/g_m)=1, and the corresponding nonzero eigenspace has q^d−1 vectors. This includes S=1 and r=1, with gcd(0,S)=S. Dividing by q−1 and adding the fixed zero yields the exact count; divisor inversion gives the cycles. For r=1 the L× cosets are invariant copies of the nonzero base action, proving replication and its order/sign consequences. Independently replayed all three displayed cycle inventories in fields of sizes 64, 256 and 729.

## originality

PASS

The supported distinct contribution is the nonenumerative Li-family all-iterate counting formula. The lift and its permutation/inverse theorem, ordinary cycle inversion, and linearized cycle theory are prior. The r=1 replication is an immediate consequence of the known lift formula and the coset factorization, not a separate originality claim.

## value

PASS

This gives a usable cycle invariant for a naturally defined family of generally nonlinear sparse permutations. Computing a single gcd and at most q−1 base-field kernel dimensions per requested iterate avoids enumerating the extension-field elements or their quotient cycles. It covers more than the known inverse and involution problems. The Möbius step and the simple r=1 replication alone would not justify this assessment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
