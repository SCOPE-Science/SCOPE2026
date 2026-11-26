---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For two iid product laws the four signed atom differences, divided by the difference of the single-site means, are -(2-t), 1-t, 1-t, t; hence homogeneous TV is d(1+|1-t|)/2. If d=0 the bound is vacuous and both homogenized laws agree. Otherwise common complementation and exchange of laws give t >= 1 and differences a+b=d>0. Opposite signs give a marginal TV at least d. For a,b >= 0 set h=max(a,b)/d and u,v the pooled coordinate means. The marginal TV bounds give TV/d >= h; the event 11 yields (va+ub)/d = 1-((1-v)a+(1-u)b)/d >= 1-(2-t)h. Their maximum is at least 1/(3-t), including all allowed boundaries. Undo complementation and use (2-w)(1+w)=9/4-(w-1/2)^2 at w=|1-t| to obtain the chain through 8/9. In the cited epsilon family the atom differences are epsilon, epsilon, 0, -2 epsilon, so the ratio is 8/(9-3 epsilon) and its limit proves sharpness. The new exact replay `python3 /workspace/branches/frozen_math_checks.py` checked 1,296 quadruples on a distinct 1/5 mesh plus an extra limiting-family example. The replay is supplementary, not a continuum proof. No claim of pointwise optimality at each pooled mean is made.

## originality

PASS

The new content is the matching universal two-site lower bound for the known 8/9 obstruction and the stronger pooled-mean inequality. Primary statements supply the obstruction, conjecture and weaker broader bounds, not these lower bounds. The closest inspected Resultary statements concern a single sum approximation or rare-event asymptotics, not the pair of labeled products. This is a bounded coverage judgment, not a priority guarantee.

## value

PASS

Two coordinates are the first nontrivial dimension and already contain the known upper obstruction to a named sharp-constant conjecture. Proving no two-site pair can do worse is a natural structural boundary. The proof gives a useful parameter-sensitive certificate from marginal and joint-success events, rather than a numerical optimization of selected parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
