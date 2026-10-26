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

# Reproduction

Run `python checks/verify_exhaustive.py > out1.json` and `python checks/verify_lifts.py > out2.json` from a directory containing the embedded `checks` folder. SymPy is required; Python's standard library supplies the other dependencies. Compare the two outputs to `checks/exhaustive_output.json` and `checks/lift_output.json`. In particular, compare their `all_net_mask_sets` arrays verbatim.

The exhaustive program loops over all 1023 nonzero forms. Its three projective-chart Gröbner basis computations determine geometric smoothness exactly over the algebraic closure. It checks rational gradients and all seven rational points, constructs all admissible two- and three-dimensional subspaces, enumerates all 168 projective transformations, and checks rational flexes by tangent-line restrictions. The independent program enumerates 512 graph splittings of the 3-dimensional evaluation kernel, without using the first program's data, and tests all seven nonzero forms of each graph.

The coefficient integer uses bit order `X^3,X^2Y,X^2Z,XY^2,XYZ,XZ^2,Y^3,Y^2Z,YZ^2,Z^3`. Thus the sample basis masks `100,421,523` correspond to the displayed three equations. Their XOR-closure is one of the eight seven-member sets in both outputs.

The standalone checker tests actual equations, not archived logs. Finite-field point incidence alone would not establish geometric smoothness; the chart ideals supply that missing algebraic implication. The independent 512-case check by itself covers only nets with linear evaluation; the complete 1023-form checker separately establishes that every qualifying net lies in this subfamily. The maximality deduction excludes dimensions four and above because a binary four-space has fifteen distinct three-spaces, while only eight admissible three-spaces exist globally.

No claim is made about independent human validation or smoothness of every nonrational member after field extension.
