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
# Verification

The standalone `verify.py` requires standard Python 3 only. Execute `python3 verify.py` and compare its output with `verification_output.txt`. The program constructs exactly the classified near-perfect two-prime families for \(1\le e\le9\) by complete loops over exponent and redundant-divisor parameters. Every primality assertion uses integer trial division to the integer square root; for each generated integer the exact divisor-sum and proper redundant-divisor identity are checked. Every candidate is compared against each base \(3,5,7,9\) and each length \(3\le\ell\le19\), with all possible digits decided by an exact quotient test.

The symbolic LTE and growth arguments in `RESULT.md` prove that **no** case outside those finite ranges can satisfy the hypotheses. Computation is used only for the finite sieve; the output of an arbitrary fixed search cutoff would not prove the theorem. The known foundational family theorem is cited, not treated as a computational certificate. This verification is not an independent audit.
