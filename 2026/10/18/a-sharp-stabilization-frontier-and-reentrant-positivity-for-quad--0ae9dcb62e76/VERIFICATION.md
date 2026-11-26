---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For each common eigenmode write d=ell+beta, t=(ell+a)/d, z=hd, s=1-e^(-z), and mu=1-t. The predictor has gain 1-ts; substitution into the published phi_2 corrector yields R=1-ts[1+(1-t)(1-s/z)]. Equivalently R=e^(-z)+(s^2/z)mu+s(1-s/z)mu^2. For -1<=mu<1 this convex quadratic is strictly less than 1: at the endpoints -1 and 1 its values are 1-2s^2/z and 1, and the quadratic coefficient is positive. It is greater than -1 since its linear term is at least -s^2/z and 0<s^2/z<s<1. For mu<-1 the stiff limit mu^2>1 yields finite-step energy growth. The modal weights in the original energy are ell+a>0, giving the exact stabilizer frontier and strict finite-step decrease for nonzero states at equality. For (ell,a)=(1,2), beta=2 gives the exact positive exponential; beta=19/11 at h=11/5 gives 600R=-5+616e^(-6)-11e^(-12)<0, since the terms through order 13 give an exact rational lower bound e^6>400. At beta=1, expanding 4z e^(2z) R(z,3/2) gives coefficient numerators 2^(n-1)(n-6)+3n+6 for n>=1, positive by the first five terms and n>=6; hence there is positivity at every finite positive step. These check a three-parameter reentry witness only, not a phase diagram. For scalar L_0, the worst stiff state gain is the square of max(|beta-a_-|,|beta-a_+|)/(ell+beta), which strictly decreases then strictly increases about their midpoint by differentiating the two branches. The midpoint is feasible, gives the stated value and gives zero for a coincident endpoint. The supplied 3958-check output is frozen finite evidence; verify.py was inspected and not executed. The Jiang reference has a title discrepancy relative to the cited PDF, but the update and proof use Fu–Shen–Yang's exact equations and not the Jiang source.

## originality

PASS

The claimed advance is the exact necessary-and-sufficient commuting quadratic original-energy frontier and the stable sign-loss/recovery witness for the established ETDRK2 scheme. Neither the integrator, the modal reduction, nor the midpoint minimax principle is credited as a new general technique. The known sufficient Lipschitz bound and inspected nonlinear Allen–Cahn/phase-field-crystal results do not imply this result on the stated class. The older scalar ETD2 stability literature remains a real coverage risk, qualified below.

## value

PASS

For a stabilized integrator actually used to enforce energy decrease, the quadratic bound specifies how far one can lower stabilization while preserving unconditional dissipation. The explicit scalar example is a meaningful warning that energy stability and positivity are different: lowering the stabilizer within the stable class can break and then restore all-step positivity. The stiff-step optimum further distinguishes the stable admissible range from good large-step attenuation without implying finite-step or nonlinear optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
