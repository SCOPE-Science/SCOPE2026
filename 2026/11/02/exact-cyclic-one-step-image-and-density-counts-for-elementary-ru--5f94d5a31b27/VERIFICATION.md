---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The exact local truth table forces output ones to be endpoints of length>=2 input zero-runs between input ones; the intervening input ones force a positive separating gap for one alternating pairing. Conversely choosing paired zero arcs and interpair one arcs constructs an exact same-length predecessor. Counting distinguished cyclic one positions by stars-and-bars and correcting overlap yields the binomial formula; the block generating functions B=z^3/(1-z)^2 and C=z^2/(1-z) give the stated log-derivative series, with reciprocal roots establishing lambda and phi coefficients. Distinct rotations are indexed rather than necklace-equivalent; n=1,2 and zero output follow from the local rule. Independent forward enumeration checked all 8190 length-n binary words for n<=12 against classifier and formula; finite enumeration supports, but does not replace, the all-n proof.

## originality

PASS

Same-claim comparison: Finite-block preimage recurrences and necessary forbidden patterns do not logically supply the exact fixed-period ring image criterion or weight count. The stronger-looking dynamics descriptions do not entail these one-update all-ring counts. Existing general finite-state algorithms can compute cases, but do not themselves state the derived formulas. The implication direction from older necessary conditions to this sufficient global cyclic theorem fails; no known broader published identity was found that forces all claims. Historical-priority risks are retained.

## value

PASS

An exact all-length necessary/sufficient image language with explicit same-period preimages, weight enumerator and exponential density for a classical elementary cellular automaton is a motivated natural discrete-dynamical invariant, not merely a generic finite automata routine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
