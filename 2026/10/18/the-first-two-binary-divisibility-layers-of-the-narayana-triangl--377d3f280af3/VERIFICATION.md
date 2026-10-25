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

The claimed full-row counts are A0(L)=(5*3^(L-1)-3)/2 for L>=1 and A1(L)=3^(L-1)-3 for L>=2, A1(1)=0. Read proof: Kummer/Legendre binary binomial carry valuations, even/odd Narayana-row split; E(m) and O(m) formulas from trailing-bit/submask constraints yield two geometric 3-power sums for valuation one. These elementary identities are all-length combinatorial arguments, not extrapolations. Independently computed each exact integer Narayana entry via binomial coefficients, all rows n<256, and counted val 0/1 for L=1..8, yielding (1,0),(6,0),(21,6),(66,24),(201,78),(606,240),(1821,726),(5466,2184), exactly the asserted formulas. Limitation to layers 0/1 and dyadic cutoffs explicit; limiting ratio 2/7 among valuation<=1 and 2/5 vs odd follows.

## originality

PASS

Bóna–Sagan full primary paper classifies individual Narayana entries not divisible by a prime, i.e., layer zero; Section 3 discusses beyond-zero valuations but no closed global dyadic layer-one count. Pinheiro/Vascon/Craveiro (2026) full accessible nineteen-page primary paper concerns CENTRAL-column N(2n,n) and necessary/sufficient prime divisibility, not full triangular layer counts. The odd-entry counts are known in OEIS A335965, and numeric 3-power sequences have unrelated OEIS appearances; none implies the layer-one Narayana interpretation and closed count without a nontrivial whole-triangle summation.

## value

PASS

Exact two-adic valuation distribution through the first nonzero layer of the full Narayana triangle is a natural refinement of classical divisibility criteria; an all-L closed form and limiting proportions extract genuine structural information about the triangle, beyond merely listing odd entries or a narrow random slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
