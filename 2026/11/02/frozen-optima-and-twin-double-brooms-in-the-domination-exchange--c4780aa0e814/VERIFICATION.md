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

Neighborhood capacities give the odd lower bound and exclude k tokens on L_{2k}: equality would forbid overlap and endpoint tokens, forcing both second-column vertices to be selected and hence overlap. The alternating odd word and the displayed even words attain the respective bounds. For a minimum word the total excess coverage is 4|S|−e(S)−2n; 00 forces X00X, which consumes four excess incidences and is impossible in the odd case. In the even case those two X columns dominate the whole interval from one column before to one after the block. A token just outside that interval would create overlap, and dominating its column without such a token requires a third X; no such extension is possible. Endpoint selections are also forbidden in this case, leaving precisely 0X00X0 on L₆. Otherwise the empty/occupied count permits at most one X. On even ladders with no X both endpoints are occupied and the single missing internal zero specifies the gap, with independent alternating row phases on its two sides. With one X exactly one endpoint is empty, forcing the adjacent X and the other alternating singletons; these are the four endpoint-double words. For odd n≥5 a sole X would have to dominate both empty endpoints from two distinct columns, so there are just the two alternating words and no slide between them. For even n, moving the gap more than one position changes at least two occupied columns; when it moves one position, the moving token must keep its row, forcing s=r⊕(j mod 2). Rung moves can change a whole alternating block only when its length is one. The only slides to endpoint-double words are the indicated slides out of that endpoint, and two different endpoint-double words are not one move apart for k≥3. These checks give exactly the two B_{k−1} components and the asserted counts, diameter, and isolates. They also apply to the nonexceptional words at k=3. The exceptional word is frozen: every rung target is occupied, a move outward from an X loses one row of the inner empty column, and a move inward loses one row in the outer empty column. Independent finite replay for L₆: enumerate all subsets of the 12 vertices by size through 4, retain those whose closed-neighborhood union is the whole ladder, and test each replacement along a rung or rail. It gives minimum size 4, 17 vertices, 12 edges, component orders 7,7,1,1,1, and each 7-vertex tree has degrees 1⁴,2,3². The uploaded scripts were inspected, not run; the infinite result follows from the word and edge argument.

## originality

PASS

Best-of-knowledge credit is for the uniform, adjacency-constrained double-broom and isolate classification on ordinary even ladders, not for the general γ-graph model, domination number, enumeration of optima, or an unrelated graph on the same optima. The strongest accessible prior ladder graph is a labeled unrestricted-exchange graph with substantial overlap in the word families and candidate exchanges. Its stated parameters and topology are different; the surviving adjacent edges and resulting disconnected components need their own row-compatibility argument. The alternate graph conventions and source access limits below constrain this judgment.

## value

PASS

The ordinary adjacent-swap γ-graph is a pre-existing natural object. For the simplest nontrivial ladder family, the theorem explains exactly which optimal selections are frozen and why the movable ones split into two trees of specified shape. This is a structural answer that the convenient count 4k+4 or the connected unrestricted graph does not provide. The main value is the uniform even-ladder classification and explicit obstruction mechanism; the finite L₆ check alone would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
