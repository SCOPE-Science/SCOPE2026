---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-11.md",
      "INDEPENDENT_AUDIT_2026-10-11.json"
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

Using the original boundary family expansion f_epsilon=-epsilon conjugate(zeta)+(1-epsilon²)sum_{k>=0}epsilon^k zeta^{2k+1}, Poisson multiplication and the Haar-preserving change w=zeta² reduce ||P_r f||_4^4/r^4 to ||H||_4^4 for analytic H=-epsilon+(1-epsilon²)w/(1-epsilon r²w). Parseval on H² yields the displayed rational expression. Independently expanded it with SymPy in x=epsilon²,s=r² and proved the exact cleared-polynomial identity (1-xs²)^3(1-||H||_4^4)=x(1-x)(1-s)P(s,x), symbolic remainder zero. Inspected the supplied exact polynomial verifier and Bernstein b_ij table (degrees 5 and 3); each of 24 coefficients nonnegative and some strictly positive. All Bernstein basis factors are positive for 0<x,s<1, yielding strict endpoint deficit at every finite radius. This is an all-parameter polynomial identity and analytic positivity, not a finite-sample numerical test.

## originality

PASS

Kovalev's 2026 actual full 13-page primary paper was read from complete primary text; its Proposition 4.4 (page12) presents this exact canonical family only to prove the p>4 obstruction in the small-r limit, with an asymptotic expansion, and its Conjecture5.1 explicitly leaves the p=4 all-function endpoint open. It does not present the all-r exact factorization or Bernstein positivity for this family in the materially read sections. The prior Riesz-projection p=4 results concern infinitesimal/other operators, not finite-r family deficit. Best-of-knowledge original as this exact positive rational certificate for the canonical example, with temporarily unavailable published-finding semantic search an explicit residual risk.

## value

PASS

The endpoint p=4 is conjecturally sharp and technically unresolved for complex-valued Poisson Schwarz contraction. This natural explicit one-parameter family is precisely the standard supercritical obstruction; an exact strict finite-radius certificate for the borderline exponent is a meaningful boundary case, not an arbitrary numeric slice. It does not claim to prove the general endpoint conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
