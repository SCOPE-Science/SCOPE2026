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
The proof was replayed from the standalone artifact `artifacts/verify.py`.

Checks performed:
- exact integer norm and orthogonality identities for the Bloch vector numerator \((-1,-2,-1)\) and rotation-axis numerator \((2,1,-4)\);
- exact cross-product identity giving \((-3,2,-1)/\sqrt{14}\);
- exact imaginary-time pool velocities \(v_Y=0\) and \(v_Z=-1\);
- exact Gram value \(J^{\mathsf T}J=5/14\) and positive right-hand side \(J^{\mathsf T}v=1/\sqrt{14}\);
- the symbolic directional derivative \(s_E=1/(5+14\lambda)>0\) for every \(\lambda\ge0\);
- exact target imaginary-time rate \(-2\operatorname{Var}(H)=-1\).

The finite sample values of \(\lambda\) in the checker only test the implementation. The all-\(\lambda\) statement follows from the displayed positive rational function, and the one-term minimality statement is proved symbolically in `RESULT.md` rather than by enumeration.
