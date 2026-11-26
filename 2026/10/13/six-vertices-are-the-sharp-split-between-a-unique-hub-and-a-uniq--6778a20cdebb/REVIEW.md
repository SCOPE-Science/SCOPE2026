# Independent mathematical audit

## correctness

PASS

Independent edge-mask orbit census and exact distance layers reproduce connected labeled counts (1,1,4,38,728,26704), set differences (0,0,0,0,400,18480), and distinct unique choices (0,0,0,0,0,720). The two displayed witnesses have the stated degree, eccentricity and farness vectors, and their disjoint relabeling orbits each have size 360 and exhaust the conflicts. Structurally, in a conflict the hub cannot be universal or have degree n−2 (in the latter case its sole nonneighbor is at distance 2, making the hub a center). Maximum degree at most 2 gives a path or cycle, with no conflicting unique choices. Thus through five vertices conflict is impossible; at six the hub must have degree 3. A vertex at distance at least 3 from it can only attach through its other nonneighbor, which has at most one further neighbor because all nonhub degrees are at most 2. This forces the length-three pendant path off the hub; the only optional edge joins its other two neighbors. This gives precisely the two shapes. In both the distinct hub and center minimize farness jointly. Replay: python /workspace/replay_frozen_graphs.py 4, output /workspace/replay_4.log.

## originality

PASS

The verified distinct contribution is the unique degree versus minimax center boundary, two first-layer isomorphism classes, and the farness-tie refinement. The same-day 720/26704 centrality comparison in the catalogue is a close numerical match but has a different objective and a disjoint conflict class. The classical definitions and broad qualitative diversity of centralities are not novel.

## value

PASS

A high-degree hub is a natural local placement heuristic; the graph center is the exact minimax placement rule. The first order at which these unambiguous choices split is a useful benchmark distinct from the first set-level difference. The two complete onset shapes isolate a short pendant path as the obstruction, and mean-distance closeness failing to break the tie distinguishes all three notions in a concrete way.

The dated certificate retains the supplied scientific assessment, sources and limitations.
