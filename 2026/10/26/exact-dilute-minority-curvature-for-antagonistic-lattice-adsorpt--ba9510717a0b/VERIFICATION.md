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

Checked the Poisson expansion at fixed volume independently, with A-rate 1 and B-rate ε=p/(1−p). The root-only probability is ε/(5+ε). Conditional on the A clocks, truncate at M=max of all first A clocks. If at most two B attempts have occurred by M, every vacant vertex at M has an A neighbor: an adjacent B is needed to have blocked its own first A; among the other three neighbors the second B cannot protect the two opposite neighbors simultaneously unless located at the vacant vertex itself. A neighbor unprotected by the two B particles must have accepted A on its first clock. Thus no subsequent B can change the result in these histories. The probability of three or more B attempts through M is bounded by (L²ε)^3 E[M³]/6; the root-only comparison obeys the same truncation logic. In the difference, histories with at most two attempts contribute only an off-root attempt at u followed by the root attempt at s. For overlap m the gain on the success event at u has first-A survival e^(−5u−(5−m)s), minus the no-cooperation e^(−5s−(5−m)u). Conditional on the A clocks the exact Poisson weight includes e^(−L²εM); replacing it by 1 at this order is controlled by another finite moment of M. Both configurations contributing to the increment require s<M (a nonoverlap root clock exceeds s). Integration gives 1/60 for each of eight m=2 offsets and 1/180 for each of four m=1 offsets, and zero otherwise. Consequently the ε² coefficient is −1/25+7/45=26/225, giving 71/225 in p; the arithmetic difference from 493/1800 is 1/24. Same-type retries after failure can never help, but a B attempt after an A attempt was blocked is not a same-type retry. For example, in an adjacent two-B history one can have u<T_root<s; this contributes at quadratic order. The error bound is fixed-L only. No uploaded code was executed; the frozen checker was inspected and its local identities agree with the derivation.

## originality

PASS

The repeated-attempt square-lattice model and leading coefficient are prior. The supported distinct claim is the exact fixed-volume quadratic term with a controlled remainder. MDZ's 493/1800 is a tentative estimate for the same scientific observable, not an exact theorem; the comparison is to their two-B calculation, not a claim that their actual process uses one attempt per site. The fixed-volume result alone does not settle an interchange of dilute and infinite-volume limits.

## value

PASS

A motivated exact second-order coefficient for an established competitive deposition process replaces a widely usable numerical/tentative benchmark at fixed volume, with a geometric bound that makes the perturbation rigorous. It identifies when post-rejection deposition matters without revising unrelated threshold estimates or asserting a thermodynamic remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
