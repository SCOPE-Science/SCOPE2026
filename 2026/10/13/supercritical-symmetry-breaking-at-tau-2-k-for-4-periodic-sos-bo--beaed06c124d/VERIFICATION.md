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

The proof is analytic. Starting from the published 4-periodic equations, introduce \(s=(a+b)/2\), \(d=(a-b)/2\), and \(u=d^2\). At the second shared-root point the equations in \((s,u,\tau)\) have a nonsingular \((s,\tau)\)-Jacobian. The resulting local curve satisfies
\[
\tau(u)=\tau_2(k)+C_k u+O(u^2)
\]
with the positive coefficient displayed in `RESULT.md`. This proves the side of the bifurcation and the square-root amplitude without numerical assumptions.

`verify.py` performs supplementary floating-point checks for \(2\le k\le40\): it isolates the nonunit root \(x_k\), verifies the source shared-root equation to tolerance, checks positivity of the Jacobian and \(C_k\), and substitutes the predicted local branch into the original two equations. It also verifies that the measured exchange amplitude approaches \(2/\sqrt{C_k}\).

The replay does not enumerate all unequal solutions and therefore does not support any global classification. It does not attempt to replace the source's proof that \(\tau_2(k)\) exists uniquely.
