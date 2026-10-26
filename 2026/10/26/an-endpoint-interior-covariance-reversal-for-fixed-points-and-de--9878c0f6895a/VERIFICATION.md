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

# Reproducibility and limits

Run `python3 verify.py` from the directory containing the supplied files. The program uses only Python standard-library integer arithmetic, exact `fractions.Fraction` values, and `itertools.permutations`; no external network access or input data are needed. It exhausts \(n=4,5,6,7,8\) at \(\theta=1/3,1/2,1,2,5\) (25 strata). It verifies the Ewens normalizer, common adjacent descent mean, every local covariance including both endpoints, and covariance aggregated over the fixed-point count.

The analytic argument in RESULT.md supplies the infinite-size justification for all real \(\theta>0\) and integers \(n\ge4\). Exhaustive finite testing does not by itself prove generality, nor does it resolve historical priority.
