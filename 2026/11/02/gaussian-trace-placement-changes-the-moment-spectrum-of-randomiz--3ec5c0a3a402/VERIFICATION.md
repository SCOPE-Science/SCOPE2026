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

# Verification summary

The proof derives two analytic tail equivalents for every dimension and probe count under the displayed fixed-smoother hypotheses. The samplewise fixed-norm result is an exact identity and inequality. In the explicit case \(n=2\), \(m=3\), and \(H=I_2/2\), the direct Gaussian denominator is \(\chi_6^2/6\) and the subtraction denominator is \(2-\chi_6^2/6\); the expected direct score and both asymptotic tail constants are exact.

Run the provided Python standard-library script using `python verify.py`. A successful run prints `VERIFY_OK 836 exact rational and asymptotic spot checks`. It tests rational Rademacher trace identity, inverse chi-square moments, an exact scalar-smoother witness, density-derived tail coefficients, and a nonscalar trace difference identity. Finite checks cannot verify the universal Gaussian small-ball asymptotic or infinite-moment conclusions; those rest on the proof in RESULT.md. No external independent audit has been performed.
