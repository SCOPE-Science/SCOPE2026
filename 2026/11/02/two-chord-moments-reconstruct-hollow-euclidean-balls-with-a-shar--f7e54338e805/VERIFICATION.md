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

# Verification of the inverse hollow-ball chord moment theorem

Run `python3 verify.py` in the directory containing this file. It uses only Python's standard library. Observed output: `VERIFY_OK 2122 exact_rational_and_independent_sample_checks`; relative errors from six seeded Euclidean point-pair experiments did not exceed \(0.0041\) in the six second-moment and fourth-moment comparisons.

The verifier tests exact moment-ratio order at rational radius ratios for dimensions \(2\) through \(25\), sharp interval bounds, endpoint coefficients, exact consecutive-dimension overlap identities through dimension \(59\), inverse bisection, radius-scale recovery and independently sampled uniform hollow-ball pairs (270,000 pairs). The random generator seed is fixed in the code. No finite enumeration establishes universal monotonicity, higher-dimensional coverage, or historical originality; the mathematical argument is in `RESULT.md`.

The exact proof uses the moment identities, strict convexity of \(x\coth x\), an algebraic interval calculation, and endpoint expansions. There is no external audit or independent certification.
