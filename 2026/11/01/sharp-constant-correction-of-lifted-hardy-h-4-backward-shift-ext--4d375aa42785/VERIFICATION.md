---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For Bf=(f-f(0))/z and F=z(I-t)+c with inner I(0)=r=sqrt(phi/2), phi=(1+sqrt5)/2, t=(2phi)^(-1/2), directly reconstruct ||B^2F||_4^4=1-r^4 and ||F||_4^4=D+|c|^4+4q|c|^2+4q Re(conj(c)conj(I'(0))) using Fourier coefficients, where q=t^2,D=(1-r^4)/phi. The only negative-frequency term in z(I-t)|I-t|^2 is q conj(I'(0)). Strict convexity of x^4+4qx^2-4q|I'(0)|x gives unique cubic minimizer; Schwarz-Pick bound |I'(0)|<=1-r^2 is sharp exactly for degree-one Blaschke automorphisms. Independent direct bisection gave delta=0.0941415110017, fourth-power quotient 1.7075217924014 and norm 1.1431193171062>phi^(1/4)=1.1278384855617. This proves the sharp restricted-family quotient and a strict lower bound on global ||B^2||, NOT the global exact norm. Boundary c=0 and singular inner functions covered by bounded boundary expansions.

## originality

PASS

Direct statement-level comparison with relevant original primary research and semantic published-finding records did not identify an equivalent or dominating fully checked result. Known premises are attributed; nontrivial new specific quantitative conclusions assessed at qualified best-of-knowledge level. Inaccessible and incompletely inspected papers remain explicit residual priority risks.

## value

PASS

The recent exact norm for the first Hardy H^4 backward shift left higher-iterate strictness unsettled. The natural complete family of constant-corrected lifts of its known norm-attaining vectors permits a genuinely sharp nontrivial optimization, rigid Blaschke equality cases, and an explicit strict global second-iterate lower bound. This is a mathematically motivated gap, not an arbitrary finite slice; no global ||B²|| determination is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
