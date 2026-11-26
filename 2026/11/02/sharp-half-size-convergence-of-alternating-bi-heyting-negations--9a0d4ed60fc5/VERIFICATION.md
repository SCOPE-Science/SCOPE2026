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

On upsets, composing the ordinary Heyting pseudocomplement with the co-Heyting supplement gives F(U)=up(down(U)). A point belongs after one step exactly if it shares a lower bound with some point in U. Thus reflexive common-lower-bound graph expansion gives F^j, and its components agree with the comparability graph (each graph edge is a comparability walk of length at most two; comparables are adjacent). Closure fills exactly the reached components, and the fixed sets are precisely the upsets with upset complements. If k>0 is the last strict growth index in the sense of k steps, a shortest length-k path from U has k distinct nonminimal vertices before its last vertex: starting at a minimal vertex would make the next vertex also belong to U, and an internal minimal vertex would supply a shortcut. Choose a minimal lower bound for each edge; finiteness makes such a choice possible and minimality among common lower bounds implies minimality in the poset. Repetition of a chosen bound would again shortcut the path. These k new distinct vertices prove n>=2k. As an independent graph check, any shortest comparability path from U must first descend (an ascending step stays in U) and alternate directions (two successive steps in one direction shortcut by transitivity). Grouping descending-ascending pairs, with a solo last descending edge if needed, shows that distance from U in the common-lower-bound graph is the ceiling of half the comparability distance: the reverse inequality is immediate by expanding each common-lower-bound edge into at most two comparability edges. In the height-two fence the comparability graph is a path of 2k vertices from b_0 to a_(k-1), hence that endpoint takes k steps. An added isolated vertex does not alter the reached component; n=1 and U empty are fixed from the start.

## originality

PASS

The supported distinct claim is the sharp number of iterations for this particular composite on finite posets, with start-dependent graph distances and a matching fence at each size. The bi-Heyting operations, their up/down-set expression, comparability components and the eventual least updownset are established ingredients, not the basis of the pass.

## value

PASS

The existing component description says where closure ends but not how many mixed-negation layers are needed to get there. The theorem gives that cost from the start set and a sharp worst case using only carrier size, with no saving from restricting to height two. In particular a fence misses its terminal minimum before the predicted step, giving an explicit minimal-size obstruction to faster uniform convergence. This is a bound on the specified iteration, not a claim about the expressive depth of all possible formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
