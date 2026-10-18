---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed the 2×2 infected Jacobian at B0=(Λ/μ,0,0,0). Its characteristic polynomial is r²+(ω+τ+2μ)r+(ω+μ)(τ+μ)−nΛω/μ; other eigenvalues −μ. For R*<1 all eigenvalues lie in the open left half plane, and for R*>1 a real positive eigenvalue occurs. The sample (μ,ω,τ,n,Λ)=(1,2,3,1,4) gives R*=2/3 and Rsrc=4/3 exactly. For R*>1 the endemic positive equilibrium has cubic coefficients A=μ+c+a+b, B=(μ+c)(a+b), C=abc, a=ω+μ,b=τ+μ,c=nI*>0. Direct symbolic determinant reconstruction confirms these and AB>C, giving Hurwitz stability and the Caputo angle condition for every 0<α≤1. At R*=1 linearization is nonhyperbolic; no global result follows.

## originality

PASS

The original source already supplies the infected block and a quadratic eigenvalue expression, but misidentifies its zero-eigenvalue parameter threshold. Standard next-generation and fractional stability methods give general tools, while the source-specific reversed classification and endemic Hurwitz verification were not found in checked related results.

## value

PASS

A wrong epidemic threshold literally reverses whether infection invades for an explicit positive-parameter regime; identifying exact corrected condition plus feasible endemic local stability is a substantive model diagnosis beyond a typographical substitution. The finding is deliberately limited to a concrete published specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
