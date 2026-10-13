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
# Verification and reproducibility

Execute `python3 verify.py` in the directory containing this document. This file is executed with only the Python standard library and consumes no external data. The actual run output is stored in `verify_output.txt`; the final line must be `ALL CHECKS PASSED`.

The code constructs the exact sets of distinct domination polynomials of trivially perfect graphs using disjoint unions and universal-vertex extensions, exhausts all nondecreasing component-size partitions through order 15, and checks every coefficient inequality exactly. There are 230337 distinct polynomials at order 15 and 230337 connected polynomial images at order 16; the latter contain exactly one log-concavity failure, \(d_2^2-d_1d_3=-5\).

Independently, the code enumerates every labeled graph through order five and recognizes trivially perfect graphs using the forbidden induced four-vertex path and four-cycle. It counts dominating sets directly and checks exact equality of polynomial-image sets. It also examines all 65536 vertex subsets of the 16-vertex windmill and compares the direct count with the polynomial arising from the closed-form formula.

The disconnected order-16 part uses the standard theorem that convolution preserves log-concavity for nonnegative sequences without internal zeros, with both hypotheses verified for domination-polynomial coefficients. The finite verifier cannot prove new claims about arbitrary higher graph orders; the explicit three-blade family threshold is instead proved analytically from its first three coefficients. No independent external audit has been conducted.
