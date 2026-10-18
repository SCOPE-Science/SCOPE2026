# Independent mathematical audit

## correctness

PASS

The 120-bit signature is by definition the set of nonempty length<=4 scattered subsequences. The precise append recurrence S(wa)=S(w) union {a} union {ua: u in S(w), |u|<=3} is an equality both ways. Because each of 3 possible append transitions is evaluated for EVERY reached state, a BFS that exhausts its queue visits the entire finite quotient, and first distance is the minimal representative length. I independently reimplemented the 120-bit automaton transition, BFS, and symmetry actions rather than relying on the package's expected histogram; obtained exactly 334202 states and 1002606 transitions with maximum depth 18, 18 extremals and disjoint six-state orbits covering them. Depth histogram independently matched every one of 19 levels. Independent position-combination oracle and published ranker criterion in checked package provide separate witness checks. Exhaustion is genuine transition closure, not incomplete search.

## originality

PASS

Previously published total quotient index 334202 and generic shortlex normal-form algorithms are credited; they do not determine the maximum minimum representative length or the three extremal symmetry types. Full-text Pach and Fleischer-Kufleitner comparisons did not disclose the precise length/orbit census. Potential earlier specialized level-four normal-form conference paper could contain it and was not fully inspected.

## value

PASS

The maximum shortest representative length is the sharp intrinsic normal-form cutoff for the first nonbinary alphabet at level four. This complete sharp finite invariant and all maximum symmetry types could inform exact algorithms and finite witness bounds; the known total class count does not mechanically determine radius or orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
