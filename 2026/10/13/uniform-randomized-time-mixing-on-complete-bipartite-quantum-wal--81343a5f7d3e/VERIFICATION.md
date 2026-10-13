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
# Verification of the mathematical finding

The complete mathematical proof appears in `RESULT.md`. It uses a cubic matrix relation to compute the entire adjacency-walk propagator and then two moments of a bounded cosine random variable. No finite enumeration is invoked to infer a statement for all orders or for all probability laws.

## Reproduction

Run `python3 verify.py` with Python 3 and no third-party packages. The program checks exactly the cubic adjacency identity, the mixing formulas, seven cosine specializations and unit row sums for each ordered pair of sizes from one through fifteen; the specified uniform averages for the three positive bicliques with rational cosine values; and a separate symbolic squared-sine check for the single-edge case. It also checks the four-leaf error bound for 1445 explicit rational two-point laws. It prints:

`VERIFY_OK block_cubic_and_rows=225 uniform_witnesses=4 K14_gap=2/45 rational_two_point_laws=1445`

A separate numerical comparison against direct complex matrix exponentials for seven graph types at five times each agreed within numerical error; this numerical comparison is supplementary and not a component of the standalone standard-library verifier.

## Limits

The script is a finite cross-check of identities and examples. It does not exhaust all probability measures, all graph sizes, or all possible equivalent published formulations. The unrestricted necessity rests on the bounds \(1-X^2\leq1\), \(X\geq-1\) and \(\mathbb E(1+X)^2\geq0\). The publisher version-of-record body was not inspected; originality therefore retains a literature-access risk. Independent audit has not been performed.
