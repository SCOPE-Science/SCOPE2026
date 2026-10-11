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
The proof was checked in exact arithmetic. For \(t=1/3\), the function defining \(\gamma_{X_H}(t)\) is convex on the product of the hexagonal unit ball with itself, so it is enough to evaluate the six-by-six vertex pairs. The exact maximum is \(25/18\), attained for example by \((1,1)\) and \((1,0)\). Multiplication by the independently reconstructed factor \(9/10\) gives \(5/4\).

A second check uses \(u=(1,1/2)\) and \(v=(0,1/2)\). Exactly, \(N(u+v)=N(u-v)=1\), \(N(u+2v)=3/2\), and \(N(2u+v)=2\), so the defining quotient of \(\Omega'\) is \(5/4\).

The bundled `verify.py` uses rational arithmetic only. It enumerates all \(36\) vertex pairs, checks the profile maximum, checks the conversion factor, and checks the direct attaining pair. The calculation is finite and exhaustive for this polygonal norm; it does not verify any claim about other norms.
