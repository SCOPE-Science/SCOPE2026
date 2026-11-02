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

Run `python3 verify_monotone_cv.py` in the directory containing the file. The script uses the Python standard library, fixed random seed, 300 finite positive mixtures, and 24 target-in-interval parameter settings. It independently evaluates the coefficient-of-variation derivative and the two-copy kernel and checks a central finite-difference approximation. The scientific argument's infinite density-class coverage instead rests on the analytically proved inequality for the kernel.

Observed results: 300 mixture cases passed. The largest normalized discrepancy between the differentiated analytic expression and the independently evaluated pair kernel was 4.58e-16. All 300 analytic derivatives were negative. All 24 interval-target cases were negative. For a centered uniform reset interval in scale-one units, the squared coefficient of variation was approximately 4.412797376 at dimensionless inverse length 0.5, 2.484071215 at 1, 1.601542839 at 2, and 1.007812016 at 128.

The program checks algebraic consistency and representative floating-point behavior; it does not certify every continuous parameter, settle novelty, or provide an independent scientific audit. Mathematical assumptions, the exact kernel identity, and the endpoint proof are given in RESULT.md.
