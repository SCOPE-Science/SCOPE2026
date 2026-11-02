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

Run `python3 check_multipartite.py` using Python 3 and only its standard library. The program constructs a zero-sum basis and exact rational powered-distance forms for prescribed rational values of \(t=1-2^{-p}\). Exact Gaussian elimination verifies the endpoint radical for the 32 tied-maximum profiles of total order at most ten. Rational positive-definiteness and violation witnesses are checked on both sides of the computed threshold for 119 distinct noncomplete multipartite profiles. The example \(K_{3,2,1}\) checks \(9t^2-11t+3=0\) and its smaller root.

A passing run prints `PASS 119 ... exact endpoint ranks 32 ... strict-inside tests 119 ... irrational example 1`. Numerical bisection only locates trial parameters; exact arithmetic certifies the finite checks. A finite list of profiles does not establish the universal statement; its proof uses the equality-exact reduction and monotonicity in RESULT.md. Source-comparison incompleteness and lack of independent review are recorded in REVIEW.md and AUDIT.json.
