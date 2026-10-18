---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

With the exact sequential opinion-then-action update and exclusions of self-action, z(t+1)=P(t)z(t) is row-stochastic, with every positive entry at least eta=min(phi,1-phi)/n. Each action row of P(t+1)P(t) receives >=eta^2 from every old opinion (through its own intermediate action) and from every old action (through action mixing). Thus if limiting joint diameter D_infty>0, all actions eventually stay a common delta>0 away from both extremes. An opinion interacting with any action thereafter moves permanently into the interior; hence persistent extreme opinions at m and M must be isolated. Their cross-action gaps satisfy [y_b-m]+[M-y_a]=(1+phi)(M-m)>2epsilon, contradicting 2epsilon>=(1+phi)D0. Therefore diameter tends zero. Once D<epsilon every potential confidence link is active and the fixed complete-neighborhood stochastic matrix is primitive, yielding exponential convergence. The two-agent stationary configuration x=(a,a+d), y=(a+(1-phi)d/2,a+(1+phi)d/2) proves sharpness strictly below the boundary. Independent Fraction-based enumeration verified two-step action positivity for all possible directed neighborhood masks and pairs of masks at n=2,3 (16 and 4096 pairs), and the stationary identity.

## originality

PASS

PASS best-of-knowledge for the unconditional sharp uniform population-size threshold and proof of eventual complete-neighborhood stabilization in that domain. The source explicitly leaves graph stabilization unproved in general and does not provide this sharp quantitative sufficient condition.

## value

PASS

Determining when all trajectories of an opinion-action bounded-confidence dynamical system converge is a natural open question posed by the model authors. The sharp confidence-vs-decision-weight boundary and exact polarized obstruction close a meaningful uniform-guarantee gap, not just a numerical simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
