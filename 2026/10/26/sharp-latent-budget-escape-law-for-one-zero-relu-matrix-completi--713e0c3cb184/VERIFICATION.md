---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Exact symbolic checks were executed using `python check_math.py`; the resulting saved output is `verification_output.txt`. The script generated 400 seeded positive rank-one upper-left blocks and positive border vectors, checking 1,600 exact rational determinant identities at four caps per instance. It also recomputed adjugate identities, positivity at sufficiently large cap, the geometric coupling factorization and the leading error coefficient. On the explicit symmetric example, four caps showed convergence of the rescaled constructive loss to \(1/4\).

The global lower bound, genericity and inverse budget/tolerance relation are established algebraically in `RESULT.md`, not inferred from these tests. The file does not constitute independent mathematical validation.
