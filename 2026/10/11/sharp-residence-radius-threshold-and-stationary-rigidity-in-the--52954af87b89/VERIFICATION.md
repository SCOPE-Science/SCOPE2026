---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

For a!=0, all real b, direct cancellation in H=z+x/a gives Hdot=1-b*z. When b=0, on radius R the bound |H|<=R*sqrt(1+a^-2) and Hdot=1 give T<=2R*sqrt(1+a^-2). For b!=0 equilibrium E_b=(-b^-2,0,b^-1) has radius sqrt(b^-4+b^-2). If a length-T trajectory resides below this radius, time averages give |zbar-1/b|<=2K/(|b|T) and |zbar^2-b^-2|<=4K(1+K)/(b^2 T) for T>=1, while ydot=x+z^2 and Jensen imply xbar<=-b^-2+(C+2R)/T; a second Jensen bound yields R^2>=b^-4+b^-2-(2LD+C)/T once T>=2D/L. Thus all below-radius residence times admit uniform upper bounds, whereas equilibrium yields unbounded length at or above radius. Invariant measures have E[z|H]=1/b via arbitrary smooth test functions, E[x]=-b^-2-Var(z), Cov(x,z)=-a Var(z) and exact radial expectation L^2+L+(2L+1)v+v^2+Var(x)+E y^2. If v=0 invariance enforces the unique equilibrium; any other state straddles its z-height. Independent SymPy check Hdot identity and radius substitution; checked numerical bounds algebra. This is about trajectory *segments*, not all escaping solutions.

## originality

PASS

Best-of-knowledge comparison against the same primary mathematical object, stronger theorems, equivalent reductions, exact tables and indexed related results finds no previously established result implying the full final statement. Searches alone are not novelty proof. Most relevant full primary texts were read where accessible; restricted sources and mathematical priority uncertainties are named below.

## value

PASS

An origin-centered exact radius necessary and sufficient for arbitrarily long residence is a natural dynamical invariant of the canonical Sprott N flow. The explicit uniform time bound distinguishes prolonged chaotic-looking transients from possible compact recurrence; the height-conditioned stationarity and strict radial defect add meaningful infinite-time statistics beyond a trivial equilibrium existence calculation. The parameter b=0 boundary is separately sharp. No broader attractor classification is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
