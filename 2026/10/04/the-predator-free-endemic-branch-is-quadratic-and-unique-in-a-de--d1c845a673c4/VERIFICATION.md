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

At predator-free y>0,z=0, infected-prey stationarity yields x=nu(alpha+y)/beta. Substituting into susceptible-prey equation yields exact quadratic F(y)=r(alpha+y)[beta K-alpha nu-(beta+nu)y]-beta^2 K y. If beta K<=alpha nu, F<0 for y>0. If A=beta K-alpha nu>0, leading coefficient negative, F(0)>0, hence one positive root (the positive and negative roots of the sign-changed quadratic have opposite signs). This proves threshold iff beta K/(alpha nu)>1 and uniqueness. Independent exact substitutions verify printed-proposition counterexample (r,alpha,nu,beta,K)=(1,1,1,2,2/5), F=-(15y^2+24y+1)/5, and feasible K=1 giving F=1-6y-3y^2. No predator-interior/delay bifurcation conclusion claimed.

## originality

PASS

The full open-access Sarwardi–Mollah–Raezah–Al Basir 2024 model equations give a cubic Eq (4), multiple-root sign table and Proposition 1 feasibility beta>nu alpha, inconsistent with exact predator-zero elimination. The corrected necessary-and-sufficient ratio, unique quadratic branch, and explicit original-proposition counterexample are new source-specific correction. Naji–Hasan has mass-action/recovery; Mortoja–Panja–Mondal is related but not shown to imply this saturated-incidence correction.

## value

PASS

A mathematical error in the number and feasibility of biologically meaningful endemic boundary equilibria materially affects equilibrium classification and downstream bifurcation interpretation of a published eco-epidemic model. Exact threshold plus counterexample is substantively useful, not a routine isolated toy negative parameter test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
