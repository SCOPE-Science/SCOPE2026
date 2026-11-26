---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The adjacent-difference isometry identifies the quotient norm with the infinity norm and intertwines Q with B=[[-(u+v),w],[v,-(w+z)]]. The exponential is positive for t>0, so its norm is its maximal row sum and the linear potential attains it. Squaring B+sI gives delta²I and hence the stated row formulas, time-independent ordering, and the two-exponential profile. Its derivative at zero gives necessity of the contractivity criterion; sufficiency follows from B1<=0 and positivity. In the increasing case k>s/delta>1, the derivative of the two-exponential profile has exactly the stated positive root and turns negative. For an independent check of the delicate conductance sign, write x=u+v, y=w+z and E=exp(tB). The ratio R=E21/E22 starts at zero and satisfies R'=v+(y-x)R-wR². At R=beta*pi1, where beta=1/pi1+1/pi2, one has y=w*beta*pi1, so R'=v-x*beta*pi1<0. Thus the ratio stays strictly below beta*pi1, making the Duhamel integrand for the c2 derivative of row 2 strictly negative. Reflection gives the c1 derivative of row 1. Setting the relevant conductance to zero gives the triangular limiting row and the recorded strict bound. For sharpness with c1=1,c2=epsilon² and t=1/epsilon, Duhamel in the Markov sup norm bounds the perturbation from c2=0 by a constant times t*epsilon², which vanishes while the fast edge equilibrates. Reflection covers the other branch. The uniform and overall envelopes and nonattainment follow as stated. The support script was inspected, not run; its finite comparisons test neither universal strictness nor the limiting quantifiers by themselves.

## originality

PASS

The supported contribution is the sharp fixed-stationary-law positive-conductance envelope, together with pointwise strict conductance monotonicity and endpoint bounds, not the usual fixed-generator Wasserstein contractivity criterion. A later-dated indexed theorem exactly generalizes the envelope and credits the earlier three-state special case; this is real overlap but not evidence of prior coverage by that indexed theorem. No inspected earlier theorem gives the full optimization or the parameter derivative.

## value

PASS

The invariant law is a natural constraint when comparing dynamics used to smooth toward the same equilibrium. The sharp pointwise bounds explain how transient Lipschitz amplification can occur despite equilibrium convergence and why the maximum possible loss requires one weak edge. The result is strictly more informative than the state-space diameter bound and the local contractivity test, and distinguishes edge-wise rate dependence from the global supremum. Its claim remains restricted to the unit-edge three-state model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
