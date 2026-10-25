---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For the specified irreducible countable-state birth/death/hopping/local-clearing CTMC, the total-population Foster–Lyapunov drift is LS=2a-(d+r)S and a negative quadratic bound for LS^2 guarantees unique stationary law and finite second moments. Generator balances for m=E[Ni], U=E[Ni(Ni-1)], W=E[N1N2] are (d+r)m=a, (2d+2h+r)U-2hW=2am and -2hU+2(d+h+r)W=2am. Solving gives U=2a^2(d+r+2h)/((d+r)Delta), W=a^2(2d+r+4h)/((d+r)Delta), Delta=r^2+3(d+h)r+2d^2+4dh. Direct independent symbolic simplification confirms V=m+a^2*r*(d+r+h)/((d+r)^2 Delta), C=a^2*h*r/((d+r)^2 Delta)>0, and ratio C/(V-m)=h/(d+r+h). Derivative C_r has numerator P(r)=2d^3+4d^2h-(2d^2+4dh)r-(7d+6h)r^2-3r^3 with P_prime<0, P(0)>0 and P(d)<0: exactly one global optimum r* in (0,d). C_h>0 and stated limits follow from rational expression. Linear affine conditional-mean drift matrix exponentiates to the exact stationary cross-lag covariance, avoiding any unwarranted Gaussian assumption. The code’s finite-state truncations are corroborative and do not prove infinite-state moments; our proof uses Foster–Lyapunov and exact balances.

## originality

PASS

Existing literature includes site resetting in extensive zero-range networks and one-type immigration/death with catastrophes or stochastic queue networks; no consulted source states this two-site joint signed covariance, its a-independent overdispersion ratio, and the unique optimal independent site clearing rate. Generator moment closure is standard and is not asserted to be invented here; the sharp covariance and global one-optimum classification is the candidate original content. Broad queueing factorial-moment frameworks could algebraically subsume it, an explicit residual implication risk rather than an automatic rejection.

## value

PASS

Independent local clears nonetheless generate strictly positive stationary synchrony between symmetrically hopping sites; the sign is nontrivial because immigration and clearing clocks are independent. An exact local-reset rate below death rate maximizing that dependence, plus an injection-independent correlation-to-excess-variance identity and lag formula, is a natural complete finite-network fluctuation classification. It answers precise parameter-selection and covariance questions for reset transport models, not a trivial consequence of the process being symmetric.

The dated certificate retains the supplied scientific assessment, sources and limitations.
