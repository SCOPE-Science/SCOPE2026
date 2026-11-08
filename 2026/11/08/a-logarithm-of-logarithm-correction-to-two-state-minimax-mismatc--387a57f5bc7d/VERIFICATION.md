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

# Verification instructions and limits

Run `python3 verify.py` using Python 3 with the standard-library `decimal` module. The script computes both channel transition probabilities from \(e^{tQ}\), evaluates conditional entropy using two algebraically different expressions (entropy chain rule and four joint probabilities), checks the positive-variance formula responsible for strict concavity, solves the unique stationarity equation by bisection at selected small positive times, and cross-checks the symmetric case.

On a successful run the first line reports `PASS 135 deterministic exact-formula and high-precision checks`; subsequent lines display sample optimizer and remainder values. The program uses 145-digit Decimal arithmetic and checks the sign of the derivative at endpoint cutoffs. Test cases include unequal rates \((a,b)=(3,1),(5,2),(11,10)\) and equal rates \(1/4,1,7\), with several short-time orders of magnitude. It is not an exact symbolic proof or a certification of asymptotic limits; these are established by the inequalities and Taylor remainders in RESULT.md. Published-priority searches and independent mathematical examination cannot be automated by this verifier.
