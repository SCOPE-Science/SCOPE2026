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

The frozen existential statement 'on every connected graph with at most four vertices' literally includes K1, for which there is neither a two-vertex seed nor a neighbor to copy. The complete repaired RESULT.md explicitly restricts the model to order at least two and the lower-bound claim to orders 2–4. The mathematical threshold and calculations are unchanged. In the repaired domain, a cut-edge copying sequence gives absorption at fixed r>0 and nonsingularity of the transient system. The direct transitions aggregated by the two mutant counts give the four displayed nonself probabilities and ten transient states. The independently written independent_check.py under /workspace/branches/2281794c-9ac0-4eb0-a52f-32c1fdce89b3/ reconstructs the quotient from full configurations, confirms identical aggregate rows for all configurations within each orbit, and reproduces all three fixation rational functions and all three differences. Positive denominators and positive gap numerators exclude L for every r>0. The H−S gap is −P/[60(r+1)Q(r)]; P has one sign change, P(1)=−4500 and P(3)=259464, so there is exactly one positive root in (1,3) and one change of maximizing orbit. The decimal near 2.05144026631733432 is informational. The same replay enumerates all connected labelled edge sets through order four and canonicalizes under vertex permutations, yielding 1,2,6 classes at orders 2,3,4. Solving their full configuration chains gives common optima as listed and coefficient sign certificates on r=1+z for each nonzero gap, for all z>0. K2's only seed already fills the graph. The independent_check.log records completion of both exact checks.

## originality

PASS

The supported distinct finding is the sharp minimum graph order for an advantageous-bias optimizing two-seed switch. Existence of a crossover on the witness graph follows from prior work and is not credited as new. The exact five-vertex formula and orbit ranking are also explicitly recorded in the later indexed comparison, whose theorem is specific to K2,3 and does not cover the exclusion of smaller graphs. No inspected primary result already gives that sharp lower bound. The tightened domain excludes only a graph with no feasible seed; the same comparison applies to the surviving theorem.

## value

PASS

This gives the smallest graph size at which changing a positive fitness advantage forces a different optimizing pair in the stated death–birth model. The cutoff concerns optimizer stability rather than just an example of two intersecting curves, and the exactly solved witness demonstrates both sides and a unique tie. Excluding the infeasible singleton does not weaken that boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
