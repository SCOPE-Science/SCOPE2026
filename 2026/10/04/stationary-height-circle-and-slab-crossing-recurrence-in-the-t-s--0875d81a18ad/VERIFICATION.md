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

The package-level verification replays the critical algebra for the normalized T-system using exact symbolic expressions. Running `python verify.py` must print `VERIFY_OK`; the captured output is included in `verification_output.txt`.

Verified identities are
\[
Ligl(y^2+z^2-2mzigr)=-2nz(z-m),
\]
\[
L(x^2)=2x(y-x),
\qquad
Lz=xy-nz.
\]
The checker also verifies the equilibrium substitutions and the derivative of \(xy\) on \(z=m\), used in the endpoint-rigidity proof.

The measure-theoretic passage uses the standard invariance identity \(\int L\phi\,d\mu=0\) on compact support. The conditional law follows by testing functions of \(z\); no numerical simulation is used as proof. The sign argument for \(q(z)=z(z-m)\) is exact. Independent audit has not been performed.
