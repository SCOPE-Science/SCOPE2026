---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Assessment of the delivered corrected RESULT.md: the first-step direction is Fb and the energy minimizer on its span subtracts (b^T F b)^2/(b^T F A F b) from the initial squared error. Scaling F and taking the two active coordinates gives (theta-lambda)^2/[lambda(theta^2+t lambda)] for lambda=1,t^2. Each weighted initial contribution is 1/t; the probabilities give the stated one-step risk. Independently, put a=t-1 and z=theta/t+t/theta. The risk simplifies to (t-2)/(ta)+(z-a)^2/[ta(z^2+a^2/t)]. Here z>2 is strictly increasing in theta>t, and differentiating the variable part gives the sign of z-a since az+a^2/t is positive. This yields the t=3 transition, strict increases for t<=3 including equality at the excluded boundary, and the unique interior root theta_+ for t>3. Subtracting the attained risk from the theta=t value gives the claimed gain. The scaled SPD eigenvalues are 1,theta,theta,t^2, and q_t(t)<0<q_t(t^2) at t>3, so conditioning is unchanged at the optimum. The frozen illustrative example mislabeled 81/605 as the initial risk. The repaired example correctly specifies initial risk 1/5, ordinary one-step risk 81/605, optimized one-step risk 4/45, theta_+=45+5 sqrt(77), and condition number 100. The repair also corrects the minimum-certificate heading and wording about the vanishing square term; the theorem and hypotheses are unchanged.

## originality

PASS

Best of current knowledge: the surviving result is the exact boundary and optimal shared parameter for the balanced two-query Type-I PCG problem, including positive one-step energy gain when no allowed parameter improves the spectral condition number. Neither Type-I preconditioning nor tuning PCG at a finite iteration budget is claimed as new.

## value

PASS

Condition-number tuning and fixed-budget error tuning are meaningful competing objectives for reduced-basis preconditioning. This balanced workload gives a sharp witness: a shared Type-I parameter helps neither on average below the threshold nor in spectral condition number at any t, yet above the threshold it yields a unique strict expected-error improvement. The exact transition, condition-number equality at the optimum, and gain quantify the mismatch rather than asserting typical solver performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
