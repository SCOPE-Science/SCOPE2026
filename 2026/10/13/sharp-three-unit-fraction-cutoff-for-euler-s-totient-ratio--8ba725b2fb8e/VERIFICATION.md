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

The standalone program `verify_threshold.py` was run directly from the packaged source directory with Python standard-library exact rational arithmetic. It verified 44 bounded unit-fraction triples representing 37 distinct rationals strictly between \(6/7\) and \(1\), and every reduced denominator was divisible by \(2\) or \(3\). It checked the witness \(6/7=1/2+1/3+1/42\) and totient values for every integer through \(300000\). The saved output is `VERIFIER_OUTPUT.txt`.

The exhaustive claim for infinitely many integers and unbounded unit-fraction denominators is proved mathematically in `RESULT.md`. Numerical enumeration alone would not justify those infinite claims. The bound \(z\le41\) for \((x,y)=(2,3)\) and corresponding smaller bounds in the remaining cases are proved using inequalities; the local valuation arguments cover each resulting case. The proof explicitly excludes \(n=1\).
