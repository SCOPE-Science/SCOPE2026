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

Run `python3 verify.py` beside `certificate.json`.

The verifier generates a long Tribonacci prefix from \(0\mapsto01\), \(1\mapsto02\), \(2\mapsto0\), then checks occurrence and Parikh-vector differences for the three midpoint witness pairs used in the proof.

Independently of those witnesses, it enumerates all nonzero integer triples \(d\) with
\[
d_0+d_1+d_2=0,
\qquad
|d_i|\le2,
\]
and confirms that there are exactly \(18\), all belonging to the equality or midpoint types. For every weight triple in \(\{0,\ldots,8\}^3\), it checks that the absence of a weighted kernel on those directions is exactly pairwise distinctness plus failure of all three midpoint equations.

As a supplementary stress test, the verifier scans a length-\(120000\) Tribonacci prefix, checks observed factor Parikh vectors through length \(120\), and compares additive and abelian class counts for every weight triple in \(\{0,\ldots,4\}^3\).

The infinite theorem uses the published \(2\)-balance theorem; the finite scan is not treated as its proof.

Independent audit has not been performed.
