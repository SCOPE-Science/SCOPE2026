# Independent mathematical audit

## correctness

PASS

In the duad–syntheme incidence graph, every perfect matching chooses a distinct incident syntheme for every duad. Exact cover on all 30 vertices independently enumerated 288 matchings, and applying all 720 symbol permutations produced two orbits of 144. For a representative m of each orbit, a subset A forces exactly when no n distinct from m agrees on every selected duad. The original superset sum counts all matching extensions including m once. The independent direct-containment computation checked all 32768 subsets per representative and agreed in degrees 5–15: (240,1380,3360,4745,4420,2887,1355,455,105,15,1) and (240,1355,3310,4710,4410,2886,1355,455,105,15,1), with every lower coefficient zero. Relabelling preserves containment, so multiplying their sum by 144 gives the aggregate in the Finding. This counts all forcing subsets, not only inclusion-minimal ones; the ordinary minimum-based polynomial is 288 t^5. Independent replay and output: /workspace/branches/replay/independent_tutte_census.py and r3_tutte.out in that directory. No frozen verifier was run.

## originality

PASS

The supported distinct claim is the complete orbit-refined forcing-subset census on this graph. A closely related earlier record already gives the 288-matchings split into the same two 144-element complementary cycle-type classes. That overlap is material and is not counted as novelty. The inspected corresponding statements do not supply forcing-subset counts for those classes.

## value

PASS

On the canonical cubic eight-cage, the refined invariant answers a natural edge-identification question: how many partial edge sets uniquely identify each perfect matching at each budget. Neither the known two-factor split alone nor the uniform forcing-number minimum exposes the difference 1380 versus 1355 at budget six. Having the complete orbit-refined data makes this a useful exact benchmark, even without a general cage theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
