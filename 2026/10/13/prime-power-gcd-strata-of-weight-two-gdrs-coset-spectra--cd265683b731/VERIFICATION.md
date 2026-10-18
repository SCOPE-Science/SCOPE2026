---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For M=q−1,k=d−2,gcd(M,k)=p^a>1, the known exact cyclic subset-sum character formula N_{M,k}(λ)=M^(−1)∑_{e|p^a}(−1)^(k+k/e) binom(M/e,k/e)c_e(λ), together with prime-power Ramanujan values, yields the displayed F_s for p-adic valuation strata s=0..a. Differences are p^s(A_s−A_{s+1})/M (1≤s<a) and p^a A_a/M at the top; strict binomial magnitudes ensure no collision, including the exceptional p=2 negative final A_a: for a=1 the last difference p A_1/M is nonzero; for a≥2 one has F_{a−2}<F_a<F_{a−1}. Each leader is unique since d≥5; selecting support, nonzero first symbol and log ratio gives exact class multiplicities. Davydov et al Theorem5.1 turns distinct weight-(d−2) counts into distinct full coset spectra. Independent direct subset enumeration across 41 small (M,k) combinations confirms formulas, including q9,d6 F=(8,10,9); infinite theorem is algebraic.

## originality

PASS

Kosters/Li–Wan already prove the full group-subset-sum character formula, and Davydov et al already prove its application to GDRS coset distributions, including particular prime and index-4 families. The present quantified contribution is strict spectral noncollision and exact numbers of entire cosets for EVERY prime-power gcd p^a; Davydov §4.2 explicitly notes distinctness between different orbits is generally unknown, so that extra universal strictness is not just a change of names for known formulas. Caveat: specialization of known universal formula gives the numbers mechanically, but the no-collision classification requires the new signed binomial separation argument.

## value

PASS

Complete coset spectra and multiplicities are natural code invariants tied in the primary article to MDS cosets and bounded-distance decoding. This establishes the natural p-power gcd layer for all q,d in a motivated open orbit-collision question, including p=2 reordered strata. It is a meaningful exact infinite-family classification beyond a few finite instances, though much formula infrastructure is explicitly credited to known papers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
