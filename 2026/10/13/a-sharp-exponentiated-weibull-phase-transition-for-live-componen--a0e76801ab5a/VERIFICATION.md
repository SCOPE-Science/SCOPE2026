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

Conditional on system failure before t and at least one survivor, survivor count R_t is asymptotically exactly one: P(R_t=1|event)=1-O(S(t)), as failure rank K is independent of IID order statistics. Conditional survivor maximum survival lies between Q_t=S(t+y)/S(t) and (1+O(S(t)))Q_t uniformly in y, preserving the squared-survival integral. Uniform exponentiated-Weibull tail S(x)=alpha exp[-(x/lambda)^beta](1+O(exp[-(t/lambda)^beta])) for x>=t and incomplete-gamma Laplace endpoint show integral Q_t^2 ~ lambda^beta*t^(1-beta)/(2beta). Multiplication by -1/2 proves the three regimes. Conditional event has positive probability for stated signature; n,alpha,s_i affect only lower terms.

## originality

PASS

The initiating 2026 article treats live-component CRJ and exponentiated-Weibull examples including beta=1.5 with a vanishing limiting CRJ, and gives fixed-y limits under IHR. It does not in the inspected text give a first-order all-beta phase transition or signature-independent coefficient for the conditional maximum; those require the survivor-count concentration step. General extreme-value excess scaling is credited. Best-of-knowledge novelty is restricted to this coherent-conditioning asymptotic.

## value

PASS

Determines a natural reliability uncertainty functional and exact shape-class boundary, including vanishing, finite and diverging regimes. The conditional architecture independence is a substantive observation beyond merely evaluating the component tail, and permits coherent systems with different signatures to share a universal leading law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
