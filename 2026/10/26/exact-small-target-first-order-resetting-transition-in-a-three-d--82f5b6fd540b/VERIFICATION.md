---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Independently checked the radial Dirichlet ODE uʺ+2uʹ/x=s u with absorbing boundary transforms u(c)=u(1)=1, exact u=[c sinh(a(1-x))+sinh(a(x-c))]/[x sinh(a(1-c))], a=sqrt(s), and renewal mean M=(1-u)/(s u); zero-rate m=(1-x²-c(1+c)(1/x−1))/6. With delta=c^(1/3), x=z delta, h=x sqrt(s), expansion u=(delta²/z)e^(−h)(1+h delta²/z+O(delta^4)) leads to F(z,h)=z³e^h/h² and delta² correction −z² e^h/h−z²/h². F is uniquely minimized at h=2; crossing with m→1/6 is Z. The exact equality correction, after cancellation, is K=1/3+1/(9e²). Reviewed proof of excluding s→0, bounded positive s, s→∞ with h→0 or ∞; only h≈2 can compete, so the implicit-function coexistence really is global. New independent high-precision nested root solving for c=10^-3,10^-4,10^-5 gave (z−Z)/c^(2/3)=0.36448,0.35556,0.35165 approaching K=0.34837. Numerical convergence is corroboration; rigorous global compactification and uniform expansions are supplied by the pinned proof.

## originality

PASS

The exact asymptotic critical exponents, constants, first correction and two-global-minima coexistence for the specific small-inner-hole transition refine the prior numeric first-order transition in the identical physical model.

## value

PASS

The earlier physical result presents only fitted small-hole critical exponents and amplitudes, which can be misleading outside the asymptotic regime. Deriving Z,K, the −2/3 rate divergence, a global branch-selection theorem and the discontinuous coexistence mechanism answers a motivated unresolved quantitative question in stochastic resetting. The correction term discriminates the fitted exponent from the actual scaling and is not a routine textbook substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
