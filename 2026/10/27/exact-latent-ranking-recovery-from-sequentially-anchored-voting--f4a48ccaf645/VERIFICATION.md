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

The top-cutoff rule makes each acceptable item better than every unacceptable one. Thus the best displayed item before the first retention is below that retention, each successive retention beats the previous running best, and all other items after the first retention are below the most recent retained record. Conversely, every tree extension is realized: take full acceptability if r_1=1, otherwise take the cutoff immediately above the best item preceding r_1. This leaves all retained records acceptable and first excludes exactly the needed prefix (possibly also excluding later items). A nonfinal retained node's subtree comprises exactly the positions strictly before the next retention. Interleaving extensions of the children gives the tree hook formula; summing subtree size minus one over all nodes gives C=m-1+sum_{h=2}^k(r_h-2), since every incomparable pair admits both orders. Without the log and with arbitrary unknown presentation order, the ballot winner must be the true top; presenting the retained chain from worst to best first, with full acceptability, realizes every ranking satisfying just that top and chain constraint. The no-log counts and example follow. With full acceptability, independent insertion ranks give independent Bernoulli(1/j) indicators; the variance summand is j-5+8/j-4/j^2 for j>=2. In the limit proof each logarithm argument differs from 1 by at most |t|/m; the total quadratic error is O(1/m) and the linear sum converges to the stated integral. This is an unrestricted proof check, not an execution of the supplied finite verifier.

## originality

PASS

On the evidence inspected, credit the exact order-conditional tree fiber and sharp comparison of information with and without order disclosure, not the anchoring mechanism, the tree hook principle, or the record-position probability law. The primary ranked-anchoring theorem concerns invariance of outcomes under presentation, not the inverse set of individual rankings. The strongest surfaced related Resultary claim likewise does not invert that map.

## value

PASS

The rooted tree gives the exact support of the latent preference, not just an upper bound or a win/top rule, and separates pairs whose direction is recoverable from those that can be reversed. The r_h-dependent comparison gives a sharp, observation-specific value of logging presentation order under unknown cutoffs. This answers a specific mechanism-inference question beyond reporting a classical probability limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
