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

For ω(n)=4 and 4|n, set n=2^a u v w with a>=2 and odd increasing prime powers u=p^b,v=q^c,w=r^d. Unit sum σ*(n)=∏(1+p_i^e_i), and equal-sum partition requires σ*(n)>=2n because one half contains n. Thus 2<=(1+2^-a)(1+u^-1)(1+v^-1)(1+w^-1). For a>=4 maximal ratio at 2^4*3*5*7 is 68/35<2. For a=3 ratio forces u=3,v=5,w=7, hence n=840. For a=2 ratio forces u=3 and (1+v^-1)(1+w^-1)>=6/5; either v=5 with exponent one and w=r^d any prime r>5, yielding 60r^d, or v=7 and w in {11,13,17,19}, yielding 924,1092,1428,1596. All larger odd prime powers violate this inequality. For 60R, σ*=120(1+R), and {60R,60} exactly halves the sum; the proper unitary subset {3R,12R,15R,60} sums to (σ*-60R)/2. For 84r r=11,13,17,19, the offsets 80-4r are respectively 36=1+7+28,28,12,4, all unitary, and displayed proper-unitary half-witnesses for those r and 840 verify sufficiency. Independently enumerated all 1644 eligible n<=35000 by exact factorization, unitary subset-sum bitsets: exactly 115 are Zumkeller and 115 half-Zumkeller, all predicted by formula. This exhaustive finite range is corroboration only; multiplicative inequality and symbolic witnesses prove unbounded exponents.

## originality

PASS

Best-of-knowledge PASS for complete four-support ν2>=2 classification and a partial proof of the unitary half-Zumkeller conjecture. Das 2024 provides necessary abundance, general constructions, and poses the conjecture; an existing published three-prime-support classification concerns a disjoint domain. OEIS example lists do not imply this infinite arithmetic iff theorem. Inaccessible or unindexed equivalent classifications remain priority risk.

## value

PASS

The four-distinct-prime support stratum with 4|n is naturally selected by unitary-abundance constraints and the unsettled even-half conjecture. A complete infinite classification, sharp 2-adic cutoff, five isolated exceptions and explicit both full/proper partitions is a substantively useful arithmetic theorem beyond known small lists or previous three-support treatment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
