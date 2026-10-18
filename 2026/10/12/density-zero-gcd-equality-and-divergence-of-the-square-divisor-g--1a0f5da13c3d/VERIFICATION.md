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

For each fixed p=1 mod3 and fixed B, Hensel lifting produces unit r mod p^B with r²+r+1=0. Dirichlet reciprocal-prime divergence for primes q≡r (mod p^B) plus CRT on the pairwise coprime q² cylinders gives density-one existence of q||m. Multiplicativity then forces p^B|sigma(m²) on density-one m. For any fixed T>=1 choose finite sets of p≡1 mod3 with p>T and B=2. Apart from a density-zero exceptional union, any p||m implies p|R(m), so R(m)<=T forces avoiding all those p||m; exact CRT upper-density <=product_p(1-1/p+1/p²). Let finite P exhaust p≡1 mod3; divergent reciprocal prime sum drives product to 0. Every quantifier is fixed before its limit. This proves bounded R has zero natural density and the R=1 equality conjecture. Independent exact prefix counts m<=1000 matched 10,99,974, roots mod49 are 18,30 and CRT avoidance q=7,13 is 6751/8281; no finite search used as the limit proof.

## originality

PASS

Dris 2022 explicitly states zero density as Conjecture 5.1 after a bound below one; Meyerowitz 2020 gives the primitive-root mechanism with a heuristic infinite Euler product but leaves inter-prime justification. Finite CRT cylinder products with rigorously ordered limiting arguments establish it and also prove stronger divergence in density. Resultary prior supplies an asymptotically density-zero subfamily lower bound, logically compatible and not dominating.

## value

PASS

Resolves a concrete named number-theoretic density-zero conjecture and proves the stronger divergence-in-density for the natural gcd ratio. The proof converts a suggested but unrigorous infinite-event argument into finite CRT bounds and a justified prime-set limit. It has unrestricted scope and an independently motivated arithmetic invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
