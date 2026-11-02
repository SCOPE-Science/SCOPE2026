# Mathematical review: sharp quadratic travel-distance moment on theta networks

## Correctness (PASS)
The claim quantifies over precisely three internally disjoint positive-length paths, sorted by length, with independent uniform-arclength samples and intrinsic shortest-path distance. The six-region integration is exhaustive: same-arm paths either follow the segment or pass through the shortest alternative arm; different-arm paths have exactly four simple route types. The elementary integrals give the displayed quartic exactly. Substitution of length gaps produces two polynomial certificates with nonnegative coefficients, establishing the unique sharp lower minimizer and strict upper inequality. The upper constant is approached in the two-short-arms limit, but never attained for positive lengths. Independently integrating the four-route minimum numerically and checking rational polynomial certificates provides supplementary verification, not an infinite proof. The CDF crossing uses explicit small-threshold pair-area calculations and continuity in the three lengths.

## Originality (PASS, historically provisional)
Earlier work by Doyle and Graver, Garijo–Márquez–Silveira, and Baptista–Kennedy–Mugnolo addresses first moments of intrinsic network distances. Exact first-moment theta optimization is not claimed. The 2012 Hosoya-polynomial reference studies discrete graph distance moments, which are not continuous arclength-pair moments on metric edges. The comparisons distinguish these objects and quantifiers from the exact squared-moment quartic and its *sharp three-arm* bounds. Relevant full open text was inspected for the modern first-moment papers. Full text of Doyle–Graver (1982) was not accessible, leaving a genuine historical-priority risk; this prevents claiming proven novelty in the absolute sense, but no decisive coverage by a stronger published statement was found.

## Mathematical value (PASS)
The squared-distance cost is a natural quadratic travel-inefficiency and second metric moment, complementary to—not a notation change of—the existing linear mean-distance extremum. A complete exact shape formula and two optimal constants solve the fixed-length quadratic optimization problem. The equilateral network minimizes this cost, but the explicit CDF comparison shows it does not order all pairwise travel distances stochastically; this explains why the quadratic inequality needs its own argument. Degeneration to a circle supplies a sharp geometric boundary. No claim is made about broader graph families or resilience to empirical noise.

## Scientific limitations
The result is restricted to three parallel arms with positive lengths. The upper bound is strict and only asymptotically reached. Checks are finite, and full text of the oldest closely related historical source was not inspectable. Any historical priority assertion is provisional.

Self-review: passed. Independent audit: not yet performed.
