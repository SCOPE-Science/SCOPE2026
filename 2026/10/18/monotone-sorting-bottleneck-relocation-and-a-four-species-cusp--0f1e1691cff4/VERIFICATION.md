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

# Reproduction and limits

Run `python3 verify.py` using Python 3 and only the standard library. The script uses exact rational operations for three symbolic evaluations at \(a=1\), an exact middle-gap stationarity identity, and two 22-step derivative-sign bisections. For each rational trial point, it applies the strong-convexity lower bound \(\mu_m=32/(v_m-v_{m-1})^3\) to bracket the true minimum. The exact inequalities prove that the unique bottleneck switch lies between \(467/500\) and \(187/200\).

Expected certificate output is `PASS: exact rational endpoint inequalities and identities`; the printed decimal intervals illustrate the exact underlying rational comparisons. The tests were run successfully for the bundled program and do not require scientific Python packages.

The existence, uniqueness, no-reentrance ordering and cusp are proved analytically in `RESULT.md`. Finite exact computations do not prove the infinite-particle sorting-time limit; that limit is an explicitly cited established input. The new result does not establish priority relative to inaccessible or previously undiscovered papers.
