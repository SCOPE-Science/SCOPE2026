# Independent mathematical audit

## correctness

PASS

Disjoint initial and final symbol supports follow from the length-one condition. Every nonempty code is in an ordered split A versus its complement, as required; multiple representations do not alter the set union. Unequal word endpoints rule out self-borders of lengths one and three, and remove exactly |A||B| period-two words from the raw 16|A||B| candidates. Pairwise compatibility then encodes all remaining overlaps and the distance condition. The maximal-clique equivalence is within a fixed split, which suffices for maxima. Independent replay /workspace/branches/review_replay_5.py used a different exact search: choose at most one word per three-position prefix group (by distance), branch also on skipping the group, and discard a branch only if chosen size plus the surviving group count is strictly below the incumbent. The three splits up to symbol permutations gave (eligible, optimum, ties)=(45,9,72),(60,12,4),(45,9,72). Applying all symbol permutations and deduplicating produced 24 sets and verified the two displayed representatives have disjoint 12-element orbits exhausting them. This is exhaustive for the specified finite domain, not for other alphabet sizes, lengths, or additional constraints.

## originality

PASS

The inspected exact code tables count ordinary non-overlapping codebooks, and the inspected theorem for the combined distance and overlap invariant stops at 16. Related indexed finite enumerations either change parameters or impose added symmetry; none supplies the exact unrestricted 12 and its two symbol orbits by known substitution or reduction.

## value

PASS

This is a small natural test of the interaction between all overlap lengths and single-substitution detection. The exact optimum distinguishes the joint constraint from the general bound 16, and the complete two-orbit classification gives all sharp constructions rather than just one feasible lower bound. Such a baseline lets researchers test sharpness and compare finite constructions without conflating non-overlap alone with the combined invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
