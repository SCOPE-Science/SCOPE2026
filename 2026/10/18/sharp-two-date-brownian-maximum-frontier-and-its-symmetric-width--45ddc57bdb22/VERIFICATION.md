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

A two-date rule is exactly a continuation event A in the time-a filtration of mass 1-q, modulo null sets. Reversing Brownian increments on [0,a] and applying reflection gives a half-normal law for D=M_a-B_a; independent increments and reflection give an independent future maximum S_h with half-normal scale sqrt(h). Thus the objective is C_a+E[1_A G_h(D)] with G_h(d)=E[(S_h-d)_+] and G_h'(d)=-erfc(d/sqrt(2h))<0. Subtract the threshold gain before comparing two equal-mass events: the difference then has constant sign, strict off the quantile level, proving both extrema and uniqueness. Differentiation of H combines the two Gaussian-prefactor terms into 2 sqrt(h/a)/pi times exp(-bz^2/(2ah)), with the remaining term -z f_a(z) erfc(z/sqrt(2h)); hence H'=f_a G_h, H(0)=C_a and H(infinity)=C_b. Quantile windows of fixed mass slide continuously between extreme events, yielding all intermediate values without extra randomness. Inverse quantile differentiation gives U'=-G_h(u_q), L'=-G_h(v_q), with U''<0<L''; the endpoints extend continuously to q=0,1, and the positive interior width is symmetric and strictly concave, uniquely widest at 1/2. Replay: python3 /workspace/reproduction/frozen_checks.py 2, using layer-cake integration in the future-maximum variable rather than integrating the closed gain. At (a,b,q)=(1,2,1/2), it gives U=1.06233964388872721, L=0.86392408400965072, W=0.1984155598790764898. The original checker was inspected but not executed; finite quadrature supports the explicit formula only.

## originality

PASS

Known coverage includes the maximizing drawdown-barrier principle for the binary law, and the complementary relation of the two optimization problems is elementary for two dates. Credit is limited to the evaluated two-sided frontier, constructive nonrandomized full-interval attainment and the sharp width as a function of the binary mass, not a new general barrier theorem. No earlier equivalent evaluation was identified in the inspected evidence.

## value

PASS

Two deterministic dates give the first nontrivial atomic target law in a natural Brownian optimization problem. The explicit endpoints and nonrandomized interpolation calibrate every feasible expected maximum, not just an optimal stopping event. The widest attainable range at equal stopping masses holds for every date pair and supplies a quantitative benchmark not available from a barrier existence theorem alone. No atomless or multi-date extension is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
