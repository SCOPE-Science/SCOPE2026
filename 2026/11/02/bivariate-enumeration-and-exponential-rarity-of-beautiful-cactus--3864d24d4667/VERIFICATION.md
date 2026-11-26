---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Wunderlich's Theorem 1.1 has the stated finite-graph scope and exact forbidden list. A cactus has no diamond, eliminating gem and watch; its cycles are induced. External neighbors of different vertices of a triangle must lie in disjoint branches and be mutually nonadjacent, since a path between two branches would produce a second cycle sharing a triangle edge. Thus an induced net exists at precisely a triangle with no degree-two corner. In a branch whose root already meets a parent block, a child triangle needs one of its nonroot corners bare, so its contribution is s(T^2-(T-x)^2)/2; rooted edges contribute T and each long even cycle contributes tT^{2k-1}/2 by reversal. SET of child blocks gives the implicit T equation. At a free root the only missed case is a lone triangle with both other corners nonbare, giving sx(T-x)^2/2. These cases are disjoint and cover the singleton too. For the singularity, the nonnegative equation in U=T-x is analytic when x+U<1 and has positive second U-derivative; rooted trees yield consecutive positive coefficients, giving aperiodicity. The critical ordinate y_c(x) solves y(1+x+B'(y))=1 for B=y^5/[2(1-y^2)]: the left side increases from 0 to infinity. On the interval up to the unique x=y_c(x), h(x)=log(x/y_c)+F(x,y_c) increases strictly since h'=1/x+y_c-x; h starts negative and ends positive. The smaller root T lies between x and y_c before this first contact. The smooth implicit-function theorem and transfer therefore apply. The rooted square-root coefficient is -(1+rho(tau-rho))kappa, and division by n yields n^-5/2 for the unrooted EGF coefficients. Independent numerical solving gave rho=0.27382690559655265, tau=0.5719059969810869, A=0.1629352693913701, rho0=0.23874014368511712 and A0=0.12014981250116957, hence base 0.8718651776201598 and prefactor 1.3561009043587482. As an exact check at n=6, the unrestricted triangle-and-bridge tally 3996 loses 120 labeled nets and gains 60 six-cycles, giving 3936. Symbolic decomposition, not this finite check or the reported verifier run, proves the infinite claim.

## originality

PASS

The protected triangle condition is an elementary specialization of a prior forbidden-subgraph characterization, and unrestricted cactus enumeration is not claimed as new. The supported distinct claims are the coupled two-marked labeled enumeration and the sharp density consequence. The nearest sources examined do not supply their constrained rooting decomposition or ratio. This is a bounded originality assessment, with the access limitation below.

## value

PASS

The exact enumeration removes a genuine incidence obstruction that standard independent block products miss. The two marks separate triangles subject to that obstruction from allowed long even cycles. The asymptotic compares the hereditary class to a natural ambient labeled family and quantifies how restrictive the condition is, beyond merely listing small-order counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
