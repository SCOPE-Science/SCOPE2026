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

For every integer 1<=k<ell, the two divisor-sum identities show fixed_divisor(a^ell-a^k) divides every c_{k,ell}(n). Conversely, if p^e divides every coefficient, c_{k,ell}(p^2)=(p^k-p^ell)(1-p^{k+ell}) forces e<=k. For any p-coprime u, multiplying by p^a with ak>=e eliminates the n^k,n^ell terms modulo p^e; multiplicativity and sigma_k(p^a)=1 mod p give sigma_k(u)=sigma_ell(u) mod p^e. Möbius inversion on p-coprime divisors gives u^k=u^ell mod p^e, and p-multiples vanish because e<=k. Hence the two gcds agree exactly. The largest p^e for which all units have t-th power 1 is determined by Carmichael lambda(p^e); taking min with k yields the asserted odd-prime and 2-adic formulas including k=1 and t odd. Independently computed gcd of coefficients n=2..120 for (k,ell)=(1,2),(1,3),(2,5),(3,7),(4,10),(6,9), obtaining 2,6,2,120,504,2; finite sample corroborates, not proves, the universal identity.

## originality

PASS

Craig–van Ittersum–Ono use exactly the same f_{k,ell} polynomial in divisor sums, and Allen–Craig refer to its positive coefficients; equality of notation alone does not imply fixed coefficient content. PNAS 2024 Lemma 12 states primitive/unit-content behavior for particular H_j, with different normalization; no demonstrated implication from it to all c_{k,ell} and exact odd/2-adic exponents. Prime-vanishing and positivity/prime-gap implications of Craig–Ono and Allen–Craig do not imply the sharp coefficientwise modulus. Primary text inspections and Resultary cross-checks found no exact or dominating theorem for the complete claim; this is a best-of-knowledge PASS with the listed explicit literature and accessibility risks, not proof of absolute novelty.

## value

PASS

A complete universal congruence/content classification is a natural invariant of the prime-detecting quasimodular coefficient family: a researcher studying integer normalizations and congruences needs the exact largest common divisor, not simply a first coefficient or the prime-vanishing property. The proof links coefficient content to a classical polynomial fixed-divisor but the global equivalence requires a nontrivial padding and Mobius inversion; the parameter-wide p-adic formula is not a routine restatement of the earlier unit-content result for different distinguished forms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
