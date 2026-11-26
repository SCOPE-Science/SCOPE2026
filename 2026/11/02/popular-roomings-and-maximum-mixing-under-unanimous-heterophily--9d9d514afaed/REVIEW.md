# Independent mathematical audit

## correctness

PASS

For c≤m, reaching H=c forces one minority agent per mixed room. All minority agents there have maximal utility. If the challenger has y_j rooms with j minority agents, its change in the number of majority agents with positive utility is −s∑_{j≥2}(j−1)y_j. The extra majority gains from 1 to more than 1 are at most ∑_{j≥2}(s−j)y_j, while exactly ∑_{j≥2}j y_j minority agents lose. This gives the claimed strictly negative challenger margin unless all y_j for j≥2 vanish, in which case gains and losses balance. In an all-mixed triple partition there are m utility-two agents and no utility-zero agents; a challenger with h mixed rooms has h utility-two agents. Its votes for gains are only promotions to two, and losses include every demotion from two, so it loses by at least m−h or ties exactly if h=m. All-mixed triples are attainable in the stated split. Distinguishing sparse mixed rooms by minority labels and dividing by permutations only among undistinguished rooms gives the first factorial formula; dividing by permutations within each composition of mixed triples gives the second. They agree at the boundaries, and c=0 gives all partitions. The constructions and test for H take linear time in the number of agents.

## originality

PASS

The two-color preference model and room-size-two existence/computation are prior. The supported distinct claim is the deterministic all-partition classification with strict dominance and exact counts for triples and sparse minorities. The strongest inspected results do not imply that package.

## value

PASS

The result identifies a natural domain where deterministic popularity, not just existence of a stable or randomized outcome, can be completely recognized and constructed. It proves a label-independent majority margin, characterizes every popular outcome and makes exact counting possible. The all-triple regime and arbitrary-size sparse-minority regime are both structural, not isolated finite checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
