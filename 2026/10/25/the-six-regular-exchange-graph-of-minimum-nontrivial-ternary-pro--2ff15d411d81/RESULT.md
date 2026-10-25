# The six-regular exchange graph of minimum nontrivial ternary projective blocking sets

## Finding

In the projective plane \(\Pi=\operatorname{PG}(2,3)\), a nontrivial blocking set is a point set meeting all lines and containing no entire line. Let \(\mathcal B\) consist of the smallest such sets. On \(\mathcal B\), join \(B\) to \(B'\) exactly when \(|B\setminus B'|=|B'\setminus B|=1\).

**Theorem.** The smallest nontrivial blocking sets have six points, and there are exactly \(234\) of them. They are exactly the six pairwise intersections of four lines with no triple concurrence. Their single-point exchange graph is connected, six-regular, and has \(702\) edges, radius \(6\), and diameter \(6\). From every vertex its distance-layer sizes, from distance zero through six, are
\[
(1,6,24,72,116,12,3).
\]
Every one of the six points of a minimum set has exactly one valid replacement point. When the six-point sets are represented by their uniquely determined four lines of triple incidence, adjacent frames share exactly two lines.

## Assumptions and scope

The point set consists of the thirteen one-dimensional subspaces of \(\mathbb F_3^3\). Normalize each nonzero coordinate vector by scaling its first nonzero entry to \(1\); call the resulting sorted list \(P\). Every line is represented by a nonzero similarly normalized covector \(a\), with its points given by \(a\cdot p=0\) modulo \(3\). This creates precisely thirteen four-point lines. Sets are **labeled** point subsets, not equivalence classes under projectivities. The exchange relation is a single point removal and a single point insertion, not arbitrary projective equivalence or a two-point move. All claims concern this single finite plane; no higher-order extrapolation is made.

## Proof

**Minimum size and shape.** Write \(t_j\) for the number of projective lines meeting a blocking set \(B\) of size \(k\) in precisely \(j\) points. Since the set is nontrivial and blocks every line, \(j\in\{1,2,3\}\). The identities
\[
t_1+t_2+t_3=13,\qquad t_1+2t_2+3t_3=4k,\qquad t_2+3t_3=\binom{k}{2}
\]
give \(t_3=13+\binom{k}{2}-4k\), and \(t_2=\binom{k}{2}-3t_3\). For \(k\le4\), \(t_2<0\). For \(k=5\), the equations require three distinct triple secants on only five selected points. If the three lines are concurrent, their three pairs of off-center points require at least seven selected points; if they are not concurrent, the union of their selected triples has at least six points, with equality only when all their pairwise intersections are among the selected points. Thus \(k\ge6\).

At \(k=6\), the equations give \((t_1,t_2,t_3)=(6,3,4)\). Through each selected point are four lines carrying its five other selected points; at least one must be a triple secant, and at most two can be triple secants. The four triple secants have twelve total incidences with the six selected points. Consequently every selected point belongs to exactly two of the four triple secants. All six pairs of triple secants must therefore intersect at six distinct selected points. The four triple secants form a dual projective frame (no three concurrent), and their six pairwise intersections recover \(B\) uniquely.

**Converse and counting.** Every four-line frame in \(\operatorname{PG}(2,3)\) is projectively equivalent to the frame with covectors \((1,0,0),(0,1,0),(0,0,1),(1,1,1)\). Direct substitution of the thirteen normalized points into the thirteen possible line equations verifies that the six intersections of this reference frame meet every line, and that no line consists entirely of these six points. Projective equivalence gives the assertion for all frames. The projectivity group \(\operatorname{PGL}(3,3)\) has order \(5616\), acts transitively on ordered projective frames, and an unordered four-line frame has stabilizer of order \(4!=24\) (each permutation of its lines induces exactly one projectivity). Thus the number of frames and minimum sets is \(5616/24=234\).

**Degree and exchange structure.** Because the frame stabilizer permutes the six pairwise intersections transitively, it suffices to examine removal of any one intersection in the above reference frame. Only three external points lie on the now-uncovered tangent line; among the three, two give a trivial blocking set containing an entire line, and precisely one produces another nontrivial blocking set. Hence each selected point has exactly one valid replacement, yielding degree six. The exact incidence arithmetic appears in the two reproducible checkers; in the chosen lexicographic normalized labeling, removal of point \(0\) from the canonical reference blocking set \(\{0,1,3,4,6,10\}\) permits the three blocking replacements \(7,8,9\), but only \(9\) remains nontrivial. Examining the resulting four triple secants establishes that adjacent frames have exactly two lines in common (the alternative exhaustive verifier independently checks this for every edge).

**Connectivity and metric.** A breadth-first search on the complete \(234\)-vertex exchange graph from any fixed frame gives the distance layer sizes \((1,6,24,72,116,12,3)\). Since these sum to \(234\), the graph is connected and the fixed frame has eccentricity six. Projectivities preserve blocking sets and one-point exchanges, and they act transitively on frames. The same distance profile and eccentricity therefore hold for every vertex, giving radius and diameter both six. The exhaustive script independently performs breadth-first search from all \(234\) vertices, so the computed metric does not rely solely on the transitivity argument.

## Verification

Run `python3 check_points.py` and `python3 check_frames.py` with Python 3 and no third-party libraries. The first program constructs all \(\sum_{k=1}^{6}\binom{13}{k}\) candidate point sets, filters nontrivial blocking sets, builds every legal one-point exchange, and computes all \(234\) distance profiles. The second program independently generates all four-line frames, reconstructs the associated six intersections, generates the exchanges from five-point overlap, verifies the dual-frame overlap property, and independently computes all \(234\) distance profiles. The plain-text output files record the exact results. Both programs have been executed from their packaged paths. The proofs above use finite arithmetic over \(\mathbb F_3\); no sampling or probabilistic assertion is involved.

## Relationship to prior work

The theory of minimal blocking sets, including field-reduction and cone constructions, is established in Van de Voorde's 2015 work. Coolsaet, Botteldoorn and Fack (2022) classify minimal blocking sets in small Desarguesian projective planes, including the order-three plane. The cardinality and frame representation are treated here as necessary geometry and not asserted to be the novel contribution. The contribution considered for priority is the natural **exchange graph on optimal nontrivial sets**, its unique replacement rule, its connectivity, exact distance profile, and six-regular structure. Classification of individual sets does not by itself supply these transformation-graph invariants. The 2022 full text was not accessible for complete comparison; that is an explicit priority risk. Gill et al.'s Conway moving-counter puzzle also uses \(\operatorname{PG}(2,3)\), but acts by line-induced permutations on a moving position, rather than exchanging one point within a six-point blocking set.

## Limitations

This exact finite result does not claim a uniform theorem for planes of other orders or uniqueness across unindexed literature. The full 2022 classification paper was not materially readable beyond its abstract and bibliography during the comparison; any prior treatment of the same exchange relation in that paper or related literature would supersede the present originality assessment. The independent scientific audit is not performed; computational reproduction here is a self-review of the specified object and algorithms.

## References

- G. Van de Voorde, *Constructing minimal blocking sets using field reduction*, arXiv:1512.04822, first submitted 15 December 2015, https://arxiv.org/abs/1512.04822.
- K. Coolsaet, A. Botteldoorn and V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, Journal of Combinatorial Designs 30 (2022), 561–580, https://doi.org/10.1002/jcd.21842.
- N. Gill, N. I. Gillespie, J. Semeraro and C. E. Praeger, *Conway's groupoid and its relatives*, arXiv:1604.04429, first submitted 15 April 2016, https://arxiv.org/abs/1604.04429.
