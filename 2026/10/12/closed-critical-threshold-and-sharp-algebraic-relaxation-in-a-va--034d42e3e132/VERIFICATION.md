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

At A1=0 and theta(0)S0=mu1, differentiate L=S-S0+S0 log(S0/S)+E: Ldot=-mu0(S-S0)^2/S-S0 E(theta(0)-theta(I))<=0. Positive bounded invariant region and LaSalle exclude a persistent E>0 on the zero-derivative set. The I equation is a stable filter, so the full disease-free equilibrium attracts globally; L and linear I response give stability. For E(0)>0, E never vanishes, d log E/dt ->0; the linear ratio equations give I/E -> alpha/mu2 and (S0-S)/E -> mu1/mu0 even if the susceptible displacement starts negative. Differentiability theta(I)=theta0+theta1 I+o(I) then yields (1/E)dot -> K=theta0 mu1/mu0-S0 theta1 alpha/mu2>0, hence t(E,I,S0-S)->(1,h,d)/K and integrated E~log(t)/K. I independently integrated the literal model with theta(I)=1/(1+I/2) at mu0=2,mu1=4,mu2=3,alpha=1,S0=4; at t=100000, (tE,tI,t(S0-S))=(.37498,.12499,.74996), agreeing with (3/8,1/8,3/4). Numeric replay is corroborative, not proof.

## originality

PASS

The motivating same-model 2023 primary paper proves global extinction only for strict R0<1, and its endemic-equilibrium theorem only says A1=0,R0>1 for positive endemic equilibrium; it does not give the critical t^-1 vector profile. Earlier SEIS/SEIR equality-threshold and critical-slowing results show that threshold closure itself is old, so the surviving comparison is the explicit model-specific K combining vaccination and theta prime, not global stability alone. Searches of published findings found positive-importation comparative statics and separate epidemic critical models, no implication of this exact coefficient. Best-of-knowledge with residual equivalent-notation risk.

## value

PASS

Explicit coefficient and full compartment ratios at a nonhyperbolic threshold are independently useful: the strict disease-free theorem fails to give convergence speed or cumulative critical infection. Here the precise vaccination and nonlinear-contact derivative sensitivities decide that speed; logarithmic cumulative incidence is a substantive boundary phenomenon, not a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
