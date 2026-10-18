---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For odd p, the source invokes Sanna 2016 Cor.1.6: v_p(U_n)=e_p+v_p(n/z_p) when z_p|n, else zero, including ramified rank z_p=p. Expanding A_p(n)=p^v_p(U_n) as a locally finite sum of divisibility indicators gives D_p(z_p)=p^e−1 and D_p(z_p p^j)=p^(e+j−1)(p−1), with D_p(1)=1, others zero. For p=2 and even P, U_odd is odd, V_odd has v2(P)=s, V_even has v2=1; U_{2m}=U_m V_m proves v2(U_{2^t m})=s+t−1 for odd m. Thus the binary tower coefficients follow by Möbius inversion and are nonnegative. At supported indices, the first odd-prime coefficient and n=z_pp constrain the least repair z_p/gcd(z_p,p−1), including z_p=p if ramified; binary support n=2 forces repair 2. Unramified ratio-of-roots order z_p divides p−1 in split and p+1 in nonsplit case, never 1 or 2 for nonsplit; yields iff Legendre(P²+4/p)=+1 for Dold, and densities 1/2 split with finite ramified exceptions. Independent integer recurrence/Möbius recomputation tested 4,500 (P,p,n) values with P2,4,6,8,12 and primes 2..23 and n≤100. Infinite theorem relies on valuation, 2-adic doubling, group order and density proofs, not numeric finite checks.

## originality

PASS

Sanna provides the exact odd-prime valuation input and classical splitting explains the rank condition; both are credited. The recent 2026 local-Dold analysis is centered on Fibonacci P=1 and companion Lucas sequences. The submitted single explicit uniform even-P family, binary/ramified obstructions, least repairs and density quadruple are not located as an implication-equivalent published classification. Novelty is the complete natural parity-family assembly, not the imported valuation formula.

## value

PASS

The even-P first-kind Lucas family is a natural complementary parity class to recent Fibonacci local Dold work. Exact supported Möbius transforms, minimal repair factors including ramified primes and a precise split-prime density law resolve a motivated familywide realizability problem; the result is a complete arithmetic classification, not arbitrary small-parameter enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
