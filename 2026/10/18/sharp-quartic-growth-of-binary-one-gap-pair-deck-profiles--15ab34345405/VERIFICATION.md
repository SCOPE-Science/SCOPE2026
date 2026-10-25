---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For any binary word of length n, the number of ones K, constant-run count R, first bit e and ordinary scattered 01 count T determine all four one-gap ordered pair counts by subtraction of adjacent pairs, hence Q(n)≤2n(n+1)(⌊n²/4⌋+1). For n≥100 with m=⌊n/100⌋, the explicit word 0^(H0+a)1^(8m)0^(4m−a)(10)^s1^d0^(8m+1)1^(h+4m−d) has length n and positive exponents for s in [m,2m], h in [m,10m], a,d in [1,4m−1]. The observed K and G11 recover s,h, while fixed s,h give T=T0+8ma−(8m+1)d. Coprime coefficients and |a−a'|,|d−d-prime|<4m force injectivity; this gives (m+1)(9m+1)(4m−1)^2 distinct observations, hence Θ(n⁴). The noiseless zero-error code capacity follows by one representative per profile. Independent literal enumeration reconstructed Q(n) for n≤12, including Q(12)=1296, and disjoint witness counts 180,2793,13552 at n=100,200,300. No asymptotic claim rests solely on these samples.

## originality

PASS

Rigo–Stipulanti–Whiteland’s 2023 full paper gives a useful binary gapped-binomial equivalence characterization, but it studies complexity of factors of selected infinite words and does not state the exact aggregate Θ(n⁴) count for all binary words. Golm et al.’s gapped k-deck paper focuses on collision/reconstruction thresholds. Golafshan 2026 explains ungapped 2-binomial classes via 3D hyperplane arrangements with cubic count, a different observation. A separate published Resultary adjacent-pair multispectrum theorem yields Θ(n²) and excludes nonadjacent ordered pairs. The four-parameter coprime construction establishes the new matching lower exponent. Risk: a broader equivalence characterization might imply n⁴ through an unstated easy count or older literature.

## value

PASS

Counting how many distinct exact observations a gapped length-two deck can carry is a natural reconstruction-code information invariant. The sharp degree four distinguishes gapped pair decks from both adjacent-pair multispectra and ordinary 2-binomial decks. A complete asymptotic exponent, with an explicit unambiguous four-parameter witness family, is independently useful even though the exact leading constant and Q(n) formula are unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
