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

For R=√((x−a)(b−x)), m=4x−a−b and y±=−cx²±xR, direct substitution into the original polynomial vector field yields dot x=xR(4cR±m). The curve f=(y+cx²)²+x²(x−a)(x−b) satisfies dot f=4(−2abc+3c(a+b)x+4y)f (the nontrivial multivariate identity was independently checked by exact symbolic expansion). F=m/(4R) has unique nondegenerate minimum c*=√(hH)/(2(b−a)) at x*=(6ab−a²−b²)/(2(a+b)), hence upper/lower branch velocities have opposite signs below c*. Adding travel times proves quadrature and positive derivative. Lower-branch dt=dx/[4xR²(F−c)]; with F−c=(c*−c)+Fʺ(x*)/2 (x−x*)²+..., dominated rescaling gives sharp coefficient and Cauchy measure, and upper-branch mass becomes negligible. Independent original-time angle quadrature at a=1,b=2 corroborates √(c*−c)T→π/[x*5^(1/4)]≈1.80077968. Source 1966 oval existence is not claimed as new.

## originality

PASS

The 1966 Yablonskii oval and associated parameter range are known. Gasull–Giacomini studies uniqueness/number of limit cycles; Alberich–Ferragut–Llibre identifies Cremona equivalence, which changes time and therefore does not imply this original-physical-time period integral, exact (c*−c)^(-1/2) coefficient or Cauchy normalized time law. The primary older 1966 and 2004 papers were not both inspected in full; their existence and the resulting priority risk are disclosed. Accessible primary texts do not give the new quantitative time observables. This is bounded best-of-knowledge PASS.

## value

PASS

A natural exact dynamical quantity for a classical explicit algebraic limit cycle is its physical-time period and distribution of residence time. The precise arrest exponent/coefficient and universal scaled Cauchy law characterize a striking nonuniform slowdown invisible to shape or limit-cycle-count classifications. The theorem offers reusable local residence asymptotics and a fully normalized example in polynomial dynamics, without claiming a new oval or more general normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
