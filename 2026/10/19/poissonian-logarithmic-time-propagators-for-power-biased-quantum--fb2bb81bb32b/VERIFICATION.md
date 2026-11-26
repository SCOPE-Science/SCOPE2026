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

In the energy matrix units the history equation is diagonal. Multiplying the scalar equation by t^b and differentiating gives t f''+(b+λt)f'+biωf=0, with f(0)=1 and f'(0)=−iω. Its regular Kummer solution solves the original equation by integration back from t=0. For ω≠0, Re a and Re(b−a) are positive. In Euler's integral for the Kummer solution, expand (1−x)^(b−a−1)=1+(a+1−b)x+O(x²) near x=0, with the rest exponentially suppressed because Re λ>0. Integrating against e^(−λtx)x^(a−1) gives the nonzero leading C=Γ(b)λ^(−a)/Γ(b−a) and the stated coefficient c=a(a+1−b)/λ. It is nonzero since both a and a+1−b=(λ−br)/λ are nonzero for ω≠0. Zero modes are identically one. The finite set of nonzero scalar asymptotics gives eventual invertibility; taking ratios gives a uniform expansion e^(−au)[1+c(e^(−u)−1)/t+O(t^−2)] for u in [0,U]. The diamond norm of a difference of Schur multipliers is bounded by the sum of the absolute coefficient differences, using the individual left/right coordinate projections, and the limiting multiplier equals the compound-Poisson exponential of the rate-r exponential-time averaging channel. In dimension two the exact norm is the magnitude of the off-diagonal scalar: rotation by a diagonal unitary reduces to a nonnegative factor times (Id−Ad Z)/2, and a superposition input attains it. In Hilbert–Schmidt norm the active gaps contribute in quadrature, preventing phase cancellation. The least active gap gives the slow exponent bΔ²/(r²+Δ²), strictly positive leading modulus and the claimed integrability trichotomy. No active gaps means an identically zero integrand. The finite-time normalized ratio is not assumed to be CP. Inspected RESULT.md lines 35–100, VERIFICATION.md, requirements.txt and verify.py; did not execute the frozen verifier. Its finite scalar checks do not substitute for the ancilla norm proof or the infinite-time estimate.

## originality

PASS

Credit the classical power-kernel Kummer solution and its leading exponent, and the uniform-bias quantum channel. The coherence threshold follows readily from that decay and is not the main originality basis. The supported distinct claim is the compact-log-time normalized quantum channel asymptotic with a CPTP compound-Poisson limit, a uniform diamond error bound, and the exact nonzero sharp qubit coefficient for b>1. No inspected prior statement establishes that combination or the sharp channel-level term.

## value

PASS

Normalization compares widely separated times without losing the decaying coherence modes. Identifying its limit as a physical exponential-time compound-Poisson channel, with a uniform operational norm estimate and a nonzero sharp error in the simplest nontrivial system, gives information beyond a scalar decay exponent or the long-time pinching channel. The scope is finite dimension, fixed parameters and compact logarithmic-time windows; it implies neither finite-time CP-divisibility nor independent increments of the historical clock.

The dated certificate retains the supplied scientific assessment, sources and limitations.
