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

Frisch-Waugh-Lovell residualization gives mirror columns u=a+b and v=a-b with u·v=0 and squared norms 2r²(1±rho), proving independent Gaussian coefficient laws. The sign identity |U+V|-|U-V|=2sgn(UV)min(|U|,|V|) gives F_lambda(rho); H(x)=x(2Phi(x)-1)/phi(x) strictly increasing gives derivative negative for 0<rho<1. Isotropic residual Gaussian direction has beta-sphere density; moments E rho²=1/d, E rho⁴=3/[d(d+2)] yield asymptotic A(lambda)/d. Independently checked reported numerical quadratures for d=3,10 and lambda=1,2; these do not establish cross-feature FDR power.

## originality

PASS

The parent Gaussian-mirror construction already normalizes equal residual norms and gives independence of the pair under Gaussian errors. It does not by those facts alone imply the analytic angle dependence, strictly decreasing sign gate, exact sphere mixture or 1/d correction without calculation. Resultary nearest semantic records are the target and different Gaussian mirror variants. Primary full papers were not newly available; equivalent angle analyses under different terminology remain a risk.

## value

PASS

The design-dependent residual angle in low-dimensional Gaussian mirrors is intrinsically tied to sign-based rejection gates. An exact monotone loss and dimension-sensitive mixture quantify a finite-sample power-related cost absent from null-sign symmetry alone; the claim carefully avoids claiming the entire FDR procedure power is determined by that gate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
