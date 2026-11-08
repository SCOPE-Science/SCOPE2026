---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For integer q≥2,n≥1, root any diameter≤2 anticode at word 0^n via full alphabet/coordinate automorphisms. Other words have weights 1 or 2. Pairwise compatible weight-2 supports must be pairwise intersecting; possible families are empty, exactly one 2-support, a star of ≥2 supports with common nonzero center symbol, or a complete triangle with one symbol prescribed per coordinate. These are disjoint exhaustive cases. Their exact pointed generating function is G=(1+z)^{nr}+C(n,2)((1+z)^{r²}−1)(1+z)^{2r}+nr(1+z)^r[((1+z)^{r(n−1)}−1−(n−1)((1+z)^r−1))]+C(n,3)r³z³. Double counting anchored pairs gives F'=q^n G and the displayed five-term q-ary size polynomial, including n=1,2. Integrating 0..1, first summand supplies q^n 2^{nr+1} and others O_q(q^n n³), with r=q−1. Every non-ball anticode has size at most q² via one-support or triangle case; distinct radius-one balls intersect in at most q words, and at most O_q(n²) ball pairs can intersect. Therefore almost all anticodes lie in a unique radius-one ball, and total-variation size law approaches Binomial(1+nr,1/2), fixed q. Independent direct Hamming graph clique histogram generation checked q=2,n=1..5, q=3,n=1..3, q=4,n=2 and matched exact all coefficients, with binary totals 4,16,81,393,1777, not just maximum. Proof is combinatorial for all q,n, not an inference from these enumerations.

## originality

PASS

Best-of-knowledge original scientific contribution confined to the exact theorem beyond explicitly acknowledged prior partial coverage. Meaningful searched aliases, broader-result implications, primary source materials, and access limits are documented below.

## value

PASS

The full size-enumeration polynomial of diameter-two anticodes is a natural complete combinatorial invariant of the Hamming graph square, strictly richer than the previously known binary aggregate count or maximal anticode size. The all-alphabet exact sharp leading constant, unique ball geometry and binomial typical size make the result useful as a sharp baseline for low-diameter Hamming families rather than an arbitrary tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
