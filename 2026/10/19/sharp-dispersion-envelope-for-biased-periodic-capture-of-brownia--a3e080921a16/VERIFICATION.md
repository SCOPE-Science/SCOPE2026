---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Exponential-time Brownian motion has characteristic function r/(r+D k^2), giving the printed Laplace law. Index j or higher occurs at displacement at least L(j-1+theta); the mirrored left threshold gives the opposite tail. Summing tails with weights 1 and 2j-1 gives m and b. For Z=LK-vT, E Z=0 at v=rLm. To justify variance convergence rather than just a CLT, stop the sum of the iid centered rewards at the first event after t. This is a stopping index of mean rt+1; the L2 martingale isometry gives second moment (rt+1) E Z^2. Removing the crossing cycle, adding the unfinished Brownian displacement and subtracting the residual drift changes the sum by a uniformly L2-bounded term: age is bounded in law by Exp(r), overshoot is independent Exp(r), and capture rounding changes free displacement by at most L. Thus the limiting centered variance is r E Z^2 per unit time. Differentiating the exponential mixture yields E(TK)=m/r-partial_r m; expansion gives b+z m partial_z m and the factor z^2/2. In a=z/2, w=|theta-1/2|z, the normalized w derivative is C/cosh(w)+w coth(2w)+1/2-h(a), with h(s)=s coth s. Since h'(s)<tanh(s), h(a)-h(w)<=C/cosh(w)-1. The remaining lower bound 1/2-w/sinh(2w) is strictly positive at w>0, including w=a. Endpoint substitution, symmetry and strictness give all equality cases; the small-z expansion is uniform on the compact gate interval and the positive interior gaps give the claimed exponential large-z decay. At directed endpoints m is constant and the large-z limit instead grows as z^2/4. The frozen checker was inspected, not executed; its recorded finite checks do not establish the continuous order.

## originality

PASS

Qualified pass for the strict all-rate sharp order in the gate offset, including the two kinds of endpoints. The exact interior formula and covariance correction demonstrably overlap a later-dated indexed result; neither that overlap nor an already known drift or symmetric endpoint is credited as a separate new contribution in this verdict.

## value

PASS

At fixed material and clock parameters, changing capture bias is a natural design variable that changes drift and spreading. The sharp strict order determines the full range and unique symmetry classes of the endpoints, including a singular distinction at rapid capture between the strictly interior gates and a directed endpoint. That control information does not follow from the known symmetric value, current, or weak-rate coefficient alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
