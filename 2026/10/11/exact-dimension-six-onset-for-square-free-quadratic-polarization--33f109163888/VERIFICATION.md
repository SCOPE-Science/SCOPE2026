---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The zero diagonal makes P_A separately affine, so extrema reduce to 2^n sign vertices; B_A is separately affine in both vectors. Conjugating by one sign vector makes the other a U/V cut and cancels cross contributions, B=a−b. Averaging P over opposite signs on one block bounds |q_U+q_V| by M=||P||. If a cut block has ≤2 elements, its quadratic value is negatable; every n≤5 cut, and unbalanced n=6 cuts, obey |a−b|≤M. For n=6 split 3+3, each triple one-flip average is −(its all-ones value)/3, so |a−b/3|≤M and |b−a/3|≤M; subtract to get |a−b|≤3M/2. Opposite-signed complete triangles realize polynomial norm 8 and bilinear norm 12. My independently implemented exact fraction certificate checked all 16+64+256+1024+4096 sign pairs (not a sample over matrices), matching coefficient identities for arbitrary real A and maximal coefficient mass 1 or 3/2 as claimed. These finite dimension computations corroborate the universal coefficient inequalities; the analytic averaging proves the theorem.

## originality

PASS

Best-of-knowledge original square-free dimension-onset threshold; general polynomial polarization works with diagonal terms and does not provide the exact real zero-diagonal 2–6 split. The related Boolean quadratic-form/graph cut formulations were checked at the level of the required numerator/denominator, not by title alone.

## value

PASS

The first dimension at which real square-free quadratic polarization ceases to preserve norm is a natural structural invariant of multi-affine polynomial geometry, not a reparametrization of unrestricted polarization. Proving complete optimal constants through the first failure and identifying a sparse exact extremizer provides useful finite-dimensional boundary data for operator/polynomial norm inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
