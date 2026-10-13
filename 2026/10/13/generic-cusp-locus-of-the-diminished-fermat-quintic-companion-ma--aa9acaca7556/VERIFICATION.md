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

`verify.py` uses exact SymPy arithmetic on the six quintics from the source. It checks all nonzero \(3\times3\) Jacobian minors, proves their gcd is \(250abc\), verifies explicit minors ruling out any further torus rank drop, computes the restricted \(2\times2\) minor gcds \(25bc\), \(25ac\), and \(25ab\), and verifies rank \(1\) of the affine Jacobian at the three coordinate vertices.

For each coordinate-line chart it rewrites every normalized target coordinate as a rational expression in \(t,x^2,y\) with \(y=x^3\). It then checks a \(2\times2\) formal Jacobian determinant that is nonzero away from the chart exception \(t^3=-1\), and checks a target coordinate is a unit times \(x^2\). These identities establish the completed image subring \(\mathbb C[[t,x^2,x^3]]\) at a generic coordinate-line point.

Fresh replay output:

`VERIFY_OK nonimmersive=abc=0 vertex_projective_rank=0 generic_cusp=C[[t,x^2,x^3]] exceptions=t^3+1=0 axis_gcds=25*b*c,25*a*c,25*a*b`

Unproved here: the analytic type at coordinate vertices and at the finitely many nonvertex chart exceptions, and any assertion that no other singularities of the global image exist.
