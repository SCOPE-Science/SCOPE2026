---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Original stable μ survives, so pruned hospital-DA ν is perfect and hospitalwise weakly preferred to μ. When n≤2 any distinct perfect ν exchanges both partners and both hospitals strictly improve, so removed original μ pairs cannot block. The displayed three-pair preferences have unique μ=(2,1,3); radius-one around hospital ranks (2,2,3) removes precisely (H3,R1); DA yields ν=(1,2,3), blocked by that removed pair. The safe-direction theorem follows since hospital-optimal full σ dominates μ, survives all below-μ deletions, and any omitted edge cannot block pruned ν, forcing ν=σ. Independent exhaustive 288 small retaining-reference prunings and direct witness confirm boundaries; not an all-n proof.

## originality

PASS

Best-of-knowledge independent statement/implication comparison supports a specific quantitative or structural contribution beyond inspected prior results; this is not an exhaustive novelty certificate. Hospital-proposing DA under symmetric exact-rank prediction windows is exactly the model of McCauley et al.; their Lemma 3.1 already provides qualitative counterexample, but the identified four-pair witness does not itself prove the smaller three-pair minimum. Prior four-pair existence gives no lower bound n≤2 or 1-edge minimality; original DA proposer optimality helps prove those but does not itself give the exhibited exact-window n=3 witness. Resident-proposing stability theorem does not imply hospital-proposing stability.

## value

PASS

The motivating problem already had a qualitative four-pair failure; pinning the minimal market size, minimal removed-edge budget, exact rank-window realization, and a universal safe cut offers a nontrivial sharp boundary for DA implementations with predicted preference lists. This is a meaningful quantitative refinement rather than relabeling generic instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
