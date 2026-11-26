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

The prey equilibrium identities give the displayed concave quadratic; its positive constant and negative leading coefficient give a unique positive root in the stated regime, and x*+y*<K. The prey block has negative diagonal entries and opposite-sign off-diagonal entries, hence it is Hurwitz. Delayed predator birth derivatives in the prey directions vanish at z=0, giving exactly the scalar factor lambda+h-p*exp(-lambda*tau). The modulus comparison excludes the closed right half-plane for p<h; at equality it leaves only zero with derivative 1+h*tau; for p>h strict monotonicity on the positive real axis gives one persistent positive real root. Nonnegative-real-part scalar roots lie in the fixed disk |lambda+h|<=p, ruling out an unstable-root jump from infinity, including as tau tends to zero. The modulus and sign of the imaginary part fix the unique positive frequency and the stated delay phases. The derivative 1+tau*(h+i*omega) is nonzero and implicit differentiation gives real crossing velocity omega^2/[(1+h*tau)^2+(omega*tau)^2]>0; counting relative to tau=0 gives the ladder including the stated counts at crossings. For a small Hopf branch if present, a multiplier from the persistent unstable root remains outside the unit circle by continuity of the retarded variational evolution (one may take a sufficiently large period multiple for compactness). Independently, the integrated predator balance over a period precludes a one-sign nonzero z near E for p>h. If z is identically zero, there is no sufficiently nearby nonconstant prey-only cycle since the endemic prey equilibrium is locally asymptotically stable. The history assumptions preserve positivity of x and y and nonnegativity of z; finite-time logistic, linear prey and delayed predator bounds permit continuation. Eventually x is at most K+eps; starting the scalar comparison after the full delayed history enters that envelope, choose q_eps<h and eta>0 with eta+q_eps*exp(eta*tau)<h. The exponential supersolution proves predator extinction for each finite tau, including tau=0; no converse and no nonlinear p=h conclusion are inferred. Independent bounded replay `python3 /workspace/review_replay.py 5` rechecks equilibrium and thresholds and phase/derivative at three crossings (first tau approximately 4.8675770964). Frozen verifier inspected, not executed.

## originality

PASS

The prey equilibrium and its feasibility, scalar factor and candidate frequency, and general scalar retarded-delay spectral tools are not standalone original here. The supported distinct claim is the model-specific correction of the biological interpretation at the predator-free boundary (no sufficiently near physical predator period orbit at the already unstable crossing) together with an explicit sufficient all-history, all-finite-delay extinction bound for these responses. The exact spectral count makes precise what the source's local Hopf discussion does not say. The close 2019 predecessor remains a named access limitation rather than proof of absence or a reason to defer.

## value

PASS

The result distinguishes three substantively different predictions for this natural model: invasion resistance at endemic prey, future spectral crossings while invasion is already possible, and predator extinction from compatible histories under a stronger intervention bound. The periodic balance is useful because imaginary roots alone are not evidence for feasible small predator cycles. The simple explicit coefficient is meaningful even without a sharp global converse or an explanation of the critical nonlinear case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
