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

The theorem is proved analytically in `RESULT.md`. The checker verifies exact algebraic consequences only; it is not used to infer the universal separable-state claim from finite data.

Run:

`python3 verify.py`

Expected terminal line: `VERIFY_OK`.

The checker uses only the Python standard library and exact rational arithmetic. It reconstructs the displayed maximizing state's augmented Bloch matrix, confirms that its Gram matrix has nonzero eigenvalues \(1/2,1/2\), and confirms normalized geometric discord \(1/4\). It also rewrites the scalar singular-value bound with \(s_3=\sqrt2\,w\), checks that the only equality root in \(0\le w\le1/3\) is \(w=0\), and checks the other interval endpoint gives \(4/9<1/2\).

The equality-to-rank argument is mathematical rather than computational: a polar partial-isometry norming functional forces every augmented pure-state Bloch vector into one two-dimensional initial space, whose intersection with the fixed-coordinate sphere contains at most two points. Gharibian's previously proved rank-two equality classification is then invoked. No independent audit has been performed.
