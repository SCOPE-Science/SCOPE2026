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

For 0<c<1 project any optimizer to the two-dimensional ray span, then align the phases to increase one expectation while preserving the other. Write G_p(theta)=(cos^(2p)(theta)+cos^(2p)(gamma-theta))/2, gamma=arccos c, theta in [0,gamma]. On 0<theta<gamma/2 derivative sign equals sign(F(theta)-(2p-1)) where F is the positive log ratio of sines to cosines. The ratio is a strictly decreasing weighted mean of cot(s)cot(gamma-s), from +infinity to (1+c)/(1-c), hence the exact one/two-ray threshold c=1-1/p and uniqueness of off-center stationary solution. At c=0 and p=1 all rays in the projector span maximize, at c=0,p>1 only two projector rays, c=1 only common ray. Independent symbolic differentiation confirms the p=2 rational branches agree C1 but have second derivatives 19/2 versus 1/2 at c=1/2; finite grid source checks are not a continuum proof.

## originality

PASS

Published SCOPE Resultary's p=2 rank-one-pair Euclidean special case (57c3a3b603ff) already covers the entire Euclidean two-branch numerical formula and c=1/2 symmetry-breaking, so that subcase is explicitly NOT original. The actual claim nevertheless quantifies over every real p>=1 and proves a new sharp variable-p threshold 1-1/p and a unique monotone angle equation; the available p=2 theorem and general joint-radius bounds do not imply this varying exponent result. The most relevant 2026 AIMS article body was not fully accessible; risk recorded; originality PASS for proper all-p extension, not for p=2 subclaim.

## value

PASS

The least noncommuting pair of positive projections exhibits a nontrivial exponent-controlled two-to-one optimizer bifurcation and exact all-p maximizing geometry. This supplies a parameter-sharp model for joint numerical radii and nontrivial structural information beyond the known isolated p=2 benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
