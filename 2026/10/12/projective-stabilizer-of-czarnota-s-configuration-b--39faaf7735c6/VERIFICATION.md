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
The packaged `verify.py` checks the exact algebra used in the projective-stabilizer proof for
\[
Q_6=x(x-z)(x+z)(y-z)(y+z)(x^2+y^2-z^2).
\]
It verifies that all four diagonal sign changes preserve \(Q_6\) up to nonzero scalar, that \(x=0\) is the unique secant among the five line components while the other four are tangent to the conic, and that
\[
\nu(t)=[2t:1-t^2:1+t^2]
\]
parametrizes the conic with the distinguished parameters \(0,\infty,1,-1\). It also verifies the projective identities inducing \(t\mapsto-t\), \(t\mapsto t^{-1}\), and \(t\mapsto-t^{-1}\), and checks that the remaining scalar condition is \(a^2=1\).

A successful replay prints `VERIFY_OK group_order=4 group=C2xC2 restrictions=t,-t,1/t,-1/t`.

The proof that no additional projective transformations exist is the exact Möbius-pair argument in `RESULT.md`; no numerical sampling or finite-field heuristic is used.
