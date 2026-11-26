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

The uniform step bounds imply a uniform contraction bound q<1 on |1−λh(x)| and positive uniform variance bounds. The second-moment drift and everywhere-positive transition density give an irreducible, aperiodic chain with small compact sets, a unique invariant law and full support; fourth-moment drift follows by absorbing the quadratic cross term into a coefficient strictly below one on x^4. Reflection of the transition kernel proves symmetry by uniqueness. The conditional second-moment balance is E[hY²]−(λ/2)E[h²Y²]=vH. Recenter h=H+(h−H): E[(h−H)Y²]=−Δ and E[(h−H)²Y²]=S, giving exactly the two-defect formula; the positive denominator and fixed-step AR(1) variance are as stated. Independent copies and radial monotonicity give Δ≥0; continuity and full support give S>0 if h is nonconstant, including at H=1/λ. For hε the moment drifts are uniform for small ε and the transition kernels converge on compact sets to the h0 kernel. Tightness, passing stationarity against bounded continuous functions, and uniqueness show convergence to N(0,V0); the fourth-moment bound gives uniform integrability for the quadratic terms. The Gaussian exponential tilt gives Δε/ε→2kV0²/(1+2kV0)^(3/2)>0 and Sε=O(ε²). This proves the coefficient, with strict negative sign at each fixed h0>1/λ for sufficiently small ε. The comparison is against its own Hε, not h0. It is existential above the boundary, not a universal upper bound there. Even to target any prescribed H strictly above the boundary, vary h0 in [H−ε,H]: the invariant law and mean step are continuous by the same compact-kernel argument, and the endpoint mean steps bracket H. The sign proof still applies along h0→H. These are mesh-point variances; an invariant physical-time law would be a different comparator.

## originality

PASS

Neither the equivalent adaptive Euler kernel, the continuous-time residence-time correction, nor the classical fixed-step OU variance is distinct here. The supported distinct result is the finite-step sign comparison to a fixed step set at the adaptive chain's own invariant mean step, with a sharp universal domain and opposite-sign witnesses beyond it. The inspected adaptive invariant-law and time-change results do not supply that comparison.

## value

PASS

Matching the invariant average step makes the variance comparison meaningful per Markov update. The identity quantifies two competing sources of stationary bias and identifies a sharp point where radial shrinking ceases to be universally worse than a fixed step. It answers a concrete sampling-design question without inferring improved autocorrelation, physical-time sampling, or runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
