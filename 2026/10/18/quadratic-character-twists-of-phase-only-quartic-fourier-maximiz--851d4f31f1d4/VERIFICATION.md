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

The standalone `artifacts/verify.py` uses only the Python 3 standard library. Invoke it from this package root with `python3 artifacts/verify.py` and compare the standard output with `artifacts/verification_output.txt`.

The program enumerates every unordered and ordered quartic-graph two-sum fiber over the nineteen-element field, confirms all 36 nontrivial collisions and two disjoint 18-relation dilation orbits, and checks each quadratic-character product. It constructs the displayed 17-by-17 integer relation minor explicitly from the first seed and computes its determinant with exact-divisibility Bareiss elimination; its absolute value is 722. It also recomputes the 991 fourth moment and checks nonconstancy of all 360 nonzero additive parameter pairs.

The mathematical proof interprets determinant 722 as a full-rank index in a 17-dimensional degree-zero lattice, which bounds all projective phase patterns. The explicit family gives exactly the same number of solutions. This finite exhaustive certificate applies to \(\mathbb F_{19}\) only, and provides no infinite-prime or unrestricted-amplitude assertion. The fourth-moment numerical value is already derivable from prior additive-energy literature. Independent audit and external scientific certification have not been performed.
