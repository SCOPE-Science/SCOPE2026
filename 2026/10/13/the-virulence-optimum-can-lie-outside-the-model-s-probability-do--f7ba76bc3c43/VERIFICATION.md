---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The source's discrete-time progression parameter gamma is a probability (0<gamma<1); Section 5's equation q*gamma=pc*((beta1+p*beta2)/(1+p))^2 consequently imposes beta1+p*beta2<B=(1+p)*sqrt(q/(pc)). With beta1<B the strictly feasible beta2 interval is (0,(B-beta1)/p). Substitution into R0a=beta1/delta + p*beta2/gamma gives derivative q(1+p)^2*(beta1-p*beta2)/(c*(beta1+p*beta2)^3), so beta2*=beta1/p is feasible iff 2*beta1<B. For B/2<beta1<B the entire nonempty feasible domain is increasing and has only a boundary supremum. Exact rational witness p=q=1/2,c=1,beta1=1,delta=1/2 has 0<beta2<1, source optimum beta2=2 would demand gamma=16/9, and supremum R0a=5/2. The independent checker re-derived all identities symbolically; the proof handles all positive parameters and the equality 2*beta1=B excludes the strict boundary optimum.

## originality

PASS

The 2023 Ripoll-Font paper is the named source of the probability-stage model and its unconstrained optimizer. The specific omitted feasibility inequality, its sharp partition into interior-versus-boundary cases, and an admissible counter-regime have not been identified in the inspected source or related virulence-tradeoff literature. The general evolutionary possibility of intermediate virulence, illustrated by Shirreff et al., predates this result and is not claimed. This is a source-specific error/boundary correction rather than independent invention of optimum calculus; priority remains best of knowledge.

## value

PASS

The probability-domain restriction changes the source's unrestricted evolutionary assertion: an open and physically valid parameter regime has no lawful interior virulence optimum even though the printed derivative has one. It changes admissible model interpretation and mathematically distinguishes strict-probability supremum from an attained unconstrained optimum. The original Figure 3 parameter set lies in the feasible regime, so that particular figure is not overturned. This is more than a cheap sign check because it locates and characterizes a consequential parameter-domain failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
