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

For the printed Poulton–Ellner ODE, at the admitted p=v=0 endpoint A'=-q(t)A with q=beta*alpha(P)*P+w+mu+c(P)>=mu>0. Thus every interior A(0)>0 satisfies 0<A(t)<=A(0)exp(-mu*t)->0 even for R0>1, disproving *full four-variable* uniform persistence. The hyperface A=0 is invariant, and for R0=beta*theta/[lambda*(gamma+mu+phi)]>1 it contains (S,A,I,P)=(1/R0,0,mu*(1-1/R0)/(mu+phi),theta*I/lambda), not disease free. Direct rational substitution with mu=gamma=theta=lambda=1,beta=4,phi=w=p=v=0 gives R0=2 and (1/2,0,1/2,1/2). The essential failure in the primary supplementary S1.5 is the assertion p*gamma*I+v*S>0 at A=0. No claim is made about loss of persistence of I and P.

## originality

PASS

The finding pinpoints a missing endpoint hypothesis in the original all-state persistence claim and an actual additional invariant boundary equilibrium. General Freedman-type persistence results assume the required boundary isolation and thus neither imply a correction nor rescue the printed all-state statement. A relevant Resultary query found qualitatively different epidemic-boundary results, not this exact model-specific contradiction. Search non-detection is not proof of priority; possible later author correction remains a risk.

## value

PASS

A false full-state uniform-persistence theorem changes the global dynamical conclusion and the scope of a proof relying on boundary isolation; the exact p=v=0 admissible boundary is a mathematically motivated counterexample, not an arbitrary trivial test. The disease persistence assertion remains logically separate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
