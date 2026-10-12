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

The package contains the standalone script `verification/verify.py`. Run it with `python verification/verify.py` in a Python installation with SymPy. It prints `VERIFY_OK` only when the following checks succeed.

The script reconstructs the linear-chain Jacobian from the five nonlinear equations and confirms, symbolically, the identity
\[
\tau\det(\lambda I-J_4)=(\lambda^2+A\lambda+C)(\lambda+b)(1+\tau\lambda)+D.
\]
It reconstructs the **exact** Hurwitz determinants
\[
\Delta_2=(A+b)+(A+b)^2\tau+A(Ab+C+b^2)\tau^2>0,
\]
\[
\Delta_3=A(Ab+C+b^2)(1+b\tau)(1+A\tau+C\tau^2)-D[1+(A+b)\tau]^2,
\]
and the derivative sign factor \(H(\tau)\) controlling the unique minimizer of the threshold \(K\).

For the rational parameter witness it verifies **all five equilibrium equations**, the positive epidemiological threshold \(\mathcal R_0=20/3\), and the values \((A,b,C,D)=(1,1,1,5/2)\). The third Hurwitz determinant is checked to equal
\[
\tfrac12(6\tau^3-8\tau^2-8\tau+1).
\]
Using exact rational arithmetic, opposite signs are checked at the endpoints of
\[
(0.11326,0.11327),\qquad(1.96785,1.96786).
\]
The analytic uniqueness-of-minimum proof in `RESULT.md` shows that these are the **only** positive roots; the finite sign checks merely isolate them.

Finally, the signs at \(\tau=0,1,3\) certify a stable–unstable–stable witness by the quartic/cubic Hurwitz theorems, not by numerical trajectory simulations. The general theorem is analytic; the checker independently verifies each algebraic premise and its concrete rational witness.
