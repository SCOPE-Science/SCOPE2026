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

Differentiating the binomial tail telescopes to n·binom(n−1,m−1) z^(m−1)(1−z)^(n−m); the two latent components give opposite derivatives with the same positive factor pq. For 0<h<1, t=h/(1−h) makes the sign that of L(t)=a log(1+t/p)−b log(1+t/q). The numerator of L′ is a−(n−1)p+(a−b)t. With L(0)=0 and growth at infinity of sign a−b, this gives the full strict-sign/one-turn alternatives, also at p=p_c and with either exponent zero. Equal exponents are positive for n≥2 and give the stated comparison with p=1/2; at p=1/2 symmetry gives F=1/2. For n=2,3 the exponents are equal or one is zero, so none can turn. For n=4, m=3, p=4/5 the positive root is t=8/5. Direct integer evaluation of the mixture, using component probabilities 12/13 and 4/13 at the root, gives the claimed endpoint and minimum fractions 512/625, 8704/10985, 4/5. At a positive root the numerator of L′ has already passed its only zero, hence the turning point is nondegenerate. The grid values of the smooth threshold away from ties converge to their hard indicators; the fixed-degree polynomial and two derivatives converge uniformly, preserving a local extremum of the same kind, not necessarily the global phase diagram. Replay: RESULT.md lines 23–81; inspected verify.py lines 86–140 and VERIFICATION.md's frozen 23,097 finite checks, not rerun. Only the group-level response under the stated fixed-size mixture is validated.

## originality

PASS

The exact law of composition, averaged group response, and hard-threshold binomial-tail representation are already in Ribordy et al. The surviving distinction is the finite-size derivative phase diagram for the unconditional adoption probability, including the minimal turning example. The ordinary perturbation argument for smooth local persistence is a consequence of the newly classified nondegenerate turn, not a separate novelty basis.

## value

PASS

The unconditional group adoption fraction is a defined observable in the motivating model, not an arbitrary chosen statistic. Its exact finite-size phase boundary answers when homophily changes from helping to hurting adoption or vice versa, and the minimal four-person witness gives a precise benchmark below both endpoints. These are useful facts about behavioral aggregation without asserting any corresponding epidemic-threshold, prevalence, or policy conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
