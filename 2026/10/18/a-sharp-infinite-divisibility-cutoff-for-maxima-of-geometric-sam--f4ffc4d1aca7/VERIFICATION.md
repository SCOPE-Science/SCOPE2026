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

# Reproducibility and verification

The analytical proof in `RESULT.md` determines the generating functions and coefficients exactly for every admissible integer sample size and real parameter, and contains a full induction for the crucial sign inequality. Run `python verify.py` using Python's standard library. The actual checker was run against the packaged source content and reported `PASS: 1008 exact rational identities and distribution enumerations`.

The diagnostic computations use fractions rather than floating-point sampling, but their parameter grid is finite; they are not a replacement for the general mathematical proof. Publication-priority checks include the parent distribution's aliases, the 2023 discrete-order-statistic theorem, a 2016 broader-family paper, and a 2020 infinite-divisibility characterization for a distinct count family. The original 2013 and 2015 model papers remain partly inaccessible, a limitation of the originality comparison. There has been no independent audit.
