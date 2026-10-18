---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Xu–Wang 2025 model (1.2) has independent diffusion components E(σ21+σ22 E), I(σ31+σ32 I). Itô on log P where P=ρ1E+ρ2I gives exact nonnegative subtraction Q=(ρ1²E²(σ21+σ22E)²+ρ2²I²(σ31+σ32I)²)/(2P²). With a=ρ1E/P,b=1−a, quadratic minimization gives δ*=σ21²σ31²/[2(σ21²+σ31²)]. Choosing E=a*ε/ρ1,I=b*ε/ρ2 proves sharpness despite nonlinear terms. Actual Example 5.2 σ21=σ31=.2, σ22=σ32=1 gives .01, contradicting paper’s claimed uniform .25; published exponent −.0651 with only that correction becomes +.1749. Independent ray evaluation at ε=1,.1,.001,10⁻⁶ returned .05241,.012698,.01002528,.0100000253, consistent with the analytic limit. This refutes that lower-bound step and certificate, NOT the theorem’s truth or disease dynamics.

## originality

PASS

Direct primary PDF model (1.2), Section 4 Theorem 4.2, proof and Example 5.2 reveal the exact printed nonlinear diffusion and the invalid σ22,σ32-only damping term. Neither the published text nor prior Han (2020)/Lu (2021) second-order epidemic results state its corrected sharp small-infection infimum or the numeric loss of this specific sufficient certificate. Resultary 2026 entry about a nonnormalizable susceptible boundary density corrects ANOTHER separate flaw in the same Xu–Wang theorem, not this Itô variance correction. Best-of-knowledge O PASS with narrow model-specific priority risk.

## value

PASS

A sharp counterexample to a central state-independent Lyapunov estimate is substantively useful: a reported extinction regime in the motivating model no longer follows from its printed sufficient bound, and quadratic noise cannot act as boundary-uniform damping. Distinguishing analytical-certification loss from true persistence prevents a false dynamical conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
