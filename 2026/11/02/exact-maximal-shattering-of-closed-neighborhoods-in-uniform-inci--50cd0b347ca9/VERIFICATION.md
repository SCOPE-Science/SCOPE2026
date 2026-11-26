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

For all-point closed supports a point center supplies any singleton and (outside the support) the empty trace. The full trace bounds size by k and the required two-point traces force size at most n-k+2. These bounds suffice since a block can fill with points outside the support. A mixed support cannot contain >=2 vertices of each type, and if one side has size >=3 the unique center for a trace including the singleton-side vertex and >=2 opposite vertices precludes shattering. A block-only support of size s>=3 requires distinct point witnesses for all nonsingleton incidence signatures, giving k>=2^(s-1)-1 and n-k>=2^(s-1)-s. Both are strict relative to the size-d thresholds for s>=4. At k=2 the pair types give C(n,2), 2C(n,2), and n C(n-1,2); there is an empty witness even at n=3. At d=3 the mixed types are an included point pair in a block, or a common selected point in two blocks with intersection size >=2. A block triple requires precisely the three pair-only regions and the triple region to be nonempty. At k=3 those four regions exhaust the capacity of all blocks and give four triples per four ground points; at k=n-1 all block triples qualify. This recovers the exceptional coefficients, including agreement at (4,3). For rank two, a block root has only three positive hypotheses, and the positive branch of a point root has no split with both children of size >=4. This rules out depth four. At a point root the positive branch splits at an incident block into two distinguishable sides when n>=4, and the negative branch restricted to the remaining incidence graph contains its VC-two class; at n=3 only six hypotheses exist. For the repaired open comparison, the two bounds for point supports are s<=k and k-1<=n-s (the smallest nonempty trace is a singleton); block supports require 2^(s-1) points inside and 2^(s-1)-1 points outside each selected block. These are sufficient for the claimed upper bound, which the point supports attain. Independent literal-set trace checks in branches/independent-replays/incidence.py verified the corrected open dimensions and closed extremal counts at all 15 ranks/orders through n=7, and nonexistence of larger closed supports through n=6; the symbolic proof gives all orders. The frozen script checks only closed neighborhoods, so its recorded output did not validate the original open comparison.

## originality

PASS

The distinct supported claim is the two-sided inclusive closed-neighborhood dimension and exact extremal support structure and census, together with the rank-two online law. The repaired open-neighborhood calculation is elementary and not claimed new. No verified inspected statement covers the central result; priority remains bounded by the evidence.

## value

PASS

The graph is canonical, but including both point and block centers changes the extremal trace problem. The exact exceptional censuses and the fact that block vertices disappear from all maximum supports at dimensions at least four identify a structural threshold, not merely one small graph computation. The rank-two online gap holds uniformly on a natural infinite subdivision family. These features survive the repair of the open-neighborhood comparison and are useful as exact examples for neighborhood learning and incidence-trace enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
