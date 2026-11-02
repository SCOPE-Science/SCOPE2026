# Independent mathematical audit

## correctness

PASS

For Q4 vertices encoded as 16 bits, the identifying property requires all 16 closed-ball intersections with code C to be nonempty and distinct. Independent code enumerated every 7-subset (11,440 candidates), checked all 6-subsets (8,008 candidates, no identifying code), and found exactly 960 minimum codes. By monotonicity of coverage/separation, no smaller codes exist. One-word swaps correspond to shared 6-element cores. An independently constructed 960-state graph has degree 9 everywhere, 4320 edges, 12 triangles per vertex, hence 3840 triangles. Independent BFS from ALL 960 states (not merely orbit representatives) found exactly the same distance shells (1,9,35,132,300,338,130,15), so radius=diameter=7 and connected. Source scripts/check_mask.py blob b2615f2ddc9b9fa4cace7665dfa158b97bb2e7d6, scripts/check_sets.py blob eb7547fcc6189f540f67e976b1367126e9775493 inspected. Source scripts enumerate all 384 cube isometries and yield orbit sizes 384,384,192; orbit sizes not independently recomputed here, though the algorithms and group order were inspected. Full finite census is exhaustive at the stipulated dimension, not extrapolation to higher cubes.

## originality

PASS

The optimum M(4)=7 is explicitly known in Herva-Laihonen-Lehtilä 2024 Table 1; early Karpovsky 1998 reports a six-code value under a potentially different separating-versus-dominating convention. Package and independent check establish that weak pairwise-distinct-only six-sets exist (192) but do not dominate, clarifying normalization. The 960-state one-exchange graph, common complete distance-shell distribution, triangle regularity, and three natural symmetry orbits were not located in inspected primary work. Charon et al 2010 local code replacement discussions are not complete exchange-graph classification.

## value

PASS

The graph of all minimum identifying codes and their allowed one-codeword swaps is a canonical finite reconfiguration object. Its full orbit, metric and local triangle census reveals a self-centered graph across multiple symmetry orbits, useful for exact local-search and code-design structure. The result does not assert a general hypercube family law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
