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

The cited v1 stage equations and coefficients, not merely the stability polynomials, give the two forcing samples. On appending time as a component with derivative 1, their offsets are α/(α−e)−1 and that offset plus β/(4ω). The two sample weights agree because m₂ times the first-stage forcing coefficient equals the second-stage forcing coefficient before the common output factor. From the published polynomial order conditions with q=eT₂(ω), preconsistency gives δ=(1−e)/(1+q/e), first order gives δβω=1−q, and the second-order coefficient equation is δβ²/8+eβω=(1+q)/2. Inserting ω²=(1+q/e)/2 yields 3q²+2eq+1−6e=0. The radical root tending to 1 yields positive α,β,ω in the stated neighborhood. The constant and linear forcing moments cancel the t_n² and t_n defect terms; the remaining cubic term has the stated Laurent expansion, independently expanded exactly. With exact starts the final error is h³E times Σ_{j=1}^{N−1}(1−q^j)/(1−q), so the three limits follow from N(1−q) tending to infinity, a positive constant, or zero. In the last case the geometric sums are uniformly asymptotic to j; in the critical case the limit is positive because x−1+e⁻ˣ>0 for x>0. Any sequence for which ε/h fails to diverge has a bounded subsequence, then a further subsequence with a finite limit; both the zero and positive finite cases preclude zero final error. This checks necessity for arbitrary allowed mesh sequences, not just the examples in the frozen checker.

## originality

PASS

The 2023 method, damping/order equations, and abscissae are credited as prior. The distinct result is an exact critical-scale consistency theorem with three mesh-dependent damping regimes for the actual v1 two-stage realization. Neither the inspected v1 method analysis nor the closest indexed switched-energy result supplies this nonautonomous long-horizon theorem.

## value

PASS

A single cubic exact solution with no startup error establishes a sharp practical obstruction to tuning damping with the mesh. It explains what the fixed-damping order and stability results cannot detect: diverging stage times and accumulated forcing errors yield a finite nonzero critical limit and divergence below threshold. This is stronger than numerically displaying an unstable step or checking a single damping value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
