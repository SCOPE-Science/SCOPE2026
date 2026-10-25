---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For integer a>=2, N=r+at and y+4z=r+ah with 0<=r<a provide a bijection of every nonnegative representation (x,y,z) to (h,z) with 0<=z<=floor((r+ah)/4) and threshold cost C_{h,z}=r+(a+1)h-3z. For fixed h minimum cost C_h=r+(a+1)h-3floor((r+ah)/4), nondecreasing with h since a+1-3ceil(a/4)>=0. Therefore the second DISTINCT representation is either the second z at h=0 (available iff r>=4, cost C0+3), or the first at h=1 (cost C0+delta); the min yields c_{a,r}. Adding a preserves representations, so each residue's first repeat threshold is exactly T_a(r)=r+a c_{a,r}, with g_1=max T-a and n_1=sum c. For a>=14 (a=4k+d) delta>=3 permits complete four-residue summation and final-residue maximum: displayed g1 and n1 quasipolynomials. At a=13 the g1 extrapolation gives 102 vs exact 89, demonstrating a sharp stability threshold. Independently checked capped generating-function DP for EVERY residue and a=2..29, plus quasipolynomial instances through a=79, all agreeing; infinite proof is the cost comparison and symbolic residue summation.

## originality

PASS

Best-of-knowledge original contribution is the precise Complete first-repeat Apéry thresholds and sharp a>=14 quasipolynomial laws for shifted-square triple (a,a+1,a+4). Prior coverage of general methods/nearby problems is credited; exact statement/implication comparisons and residual risks are detailed below. The unsuccessful Resultary lookup is not treated as proof of novelty.

## value

PASS

The first-repeat two-representation question for the naturally arising first three squares shifted by a is distinct from classical zero-representation Frobenius. The full a-residue Apéry set, explicit small-base cases, sharp simplification onset at a=14 and two quasipolynomials constitute a complete natural family classification. The special d=3 winning residue and sharp a=13 break are meaningful boundary data; general p-Apéry conversion alone does not give them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
