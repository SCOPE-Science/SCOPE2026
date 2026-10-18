---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For all N>=2, 1<=m<N and J>0, fully connected H=-NJ|u><u|. Uniform survivor b on first m sites evolves with target success probability p(tau)=beta/2[1-cos(NJ tau)], beta=4m(N-m)/N². A failed projective measurement returns a scalar multiple of b, so for iid nonnegative intervals of finite positive mean, successes form IID Bernoulli trials and stopping-time cost Eτ/Ep (if mean success zero, T=inf). Put X=NJ tau; the pointwise ratio g(x)=(1-cos x)/x has unique global maximum sin(x*) at x*=2.33112237041442 (tan(x*/2)=x*) in (pi/2,pi); for x>=pi, g<=2/x<=2/pi<sin x*. Thus E(1-cos X)<=sin(x*) E X, equality only X in {0,x*} with positive mass at x*. The optimum T=2/[beta NJ sin x*] attained by deterministic tau=x*/(NJ) (or zero mixing). Exponential waiting with rate r yields T=2/(beta NJ)[r/(NJ)+(NJ)/r], uniquely best at r=NJ with ratio to optimum 1/(2sin x*)=0.6900250698446504. Independent complex-vector tests for 4 (N,m,J,tau) and 10000 random finite-support trials confirmed examples; global inequality proved analytically.

## originality

PASS

Best-of-knowledge statement-level prior comparison: the exact final claim goes beyond inspected narrower qualitative, lower-bound, upper-bound or Poisson-restricted results. This is not a claim of exhaustive historical priority; see four comparisons and source-specific risks.

## value

PASS

A natural optimization of the complete waiting-time law (not merely Poissonian rate) for the exactly solvable complete-graph target detector, sharpening and quantifying earlier Poisson-protocol optimum by about 31%. Identifies precise deterministic/zero-mass equality laws and the structural role of postfailure ray reset; a useful benchmark for quantum detection scheduling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
