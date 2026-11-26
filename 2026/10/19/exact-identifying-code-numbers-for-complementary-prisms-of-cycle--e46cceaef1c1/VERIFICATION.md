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

The four window tests are the closed-neighborhood domination mask for a cycle vertex and the symmetric differences for cycle distances one and two and complement distance two. Two complement vertices not at distance two have disjoint pairs of excluded complement indices, so their separation is equivalent to at least one not being a defect; defects at distance two violate the fourth test. Cycle vertices farther than two have disjoint neighborhoods; at least four selected complement vertices ensure every complement trace contains at least two complement vertices, separating both layers. In the lifted graph any identifying code gives a path from (q,0,0) to (q,e,n mod 9), e<=1, with cost 9|S|-7n. The fresh replay regenerated the transitions from actual neighborhood masks, verified a feasible integer potential on all 14706 lifted arcs, and computed the minimum over all 256 starting states and both final defect counts. The nine costs are (0,2,-5,6,-1,1,3,5,-2)=9a_r-7r. This is an unrestricted path optimization, not enumeration through a trial length. The nine seeds have their required weights, at least four complement selections, the right defect budgets, and close at state 19. The length-nine seed has no defects; adding copies at the common state preserves every local test and defect budget. This gives equality at all lengths 9k+r with k>=1.

## originality

PASS

The closest inspected primary work establishes 7/9 as the leading coefficient and gives local conditions and constant-error bounds. Its bounds do not determine the exact offsets, even at general multiples of nine. A same-graph indexed result covers n=9 only. The supported distinct claim is the all-length residue classification, not novelty of gamma_ID(P_9)=7, the local characterization, or the leading coefficient.

## value

PASS

The theorem replaces constant-error asymptotic bounds for a natural graph family by exact optimum sizes at every length in scope, including a strictly better upper bound for several residues. The period-nine seed splice and global finite-state lower certificate explain why the small per-residue offsets persist without any trial-length cutoff. It is not merely a computation of the n=9 case or a rederivation of the leading coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
