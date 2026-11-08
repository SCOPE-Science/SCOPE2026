---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Reconstructed actual M^13=I+3B with B rows (91,141,168),(168,259,309),(309,477,568), and residues T_r+1 divisible by 3 precisely r=3,8,10. For each the 3-adic analytic interpolation g_r(z)=(1+e1^T M^r(I+3B)^z v)/3 has isometric difference g_r(a)-g_r(b)=(a-b)*(c_r+3u) with c_r=2 mod3, by the binomial-difference valuation j-v3(j!)>=2 for j>=2. This ensures a unique alpha_r and exact valuation law. Shifted negative-index recurrence T_-3=-1 gives alpha_10=-1. The three permitted mod13 residue supports and two of three lifts at each level imply least period 13*3^t (exclude q/3 and q/13); counting gives density and discrepancy. Independent direct iteration checked levels t=1..4 and least periods. Finite checks are corroborative.

## originality

PASS

Bilu–Luca–Nieuwveld–Ouaknine–Worrell (2022) full paper is on zeros/valuations of unshifted Tribonacci T_n; its 3-adic zero residues do not match the shifted +1 target. Young (2024) shifted results concern prime 47; Antony–Barman (2024) unshifted third-order recurrences. No matching Resultary finding from actual query.

## value

PASS

Exact all-t least periods, residue class counts and natural densities for a shifted classical recurrence are meaningful number-theoretic invariants. The 3-adic root structure and rational densities go beyond experimentally listing divisibilities at a few levels; unshifted valuation results do not trivially substitute for shifted ones.

The dated certificate retains the supplied scientific assessment, sources and limitations.
