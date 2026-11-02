# Six agents are necessary and sufficient for cycling in two-coalition cutoff hedonic games

## Finding
For the happy-in-isolation (HIS) cutoff-cost hedonic game on the real line, with at most two unlabeled nonempty coalitions and strictly improving unilateral jumps, the **minimum population admitting an improvement cycle is exactly six**. More strongly, for at most five agents no symmetric binary enemy relation can yield such a cycle, even without a line embedding. At six agents, positions \(0,9,18,26,27,28\) and cutoff \(\lambda=10\) yield the eight-jump cycle certified below.

## Assumptions and scope
Let \(N=\{1,\ldots,n\}\), and let each player \(i\) have position \(x_i\in\mathbb R\). Declare \(j\) an enemy of \(i\) when \(|x_i-x_j|>\lambda\), for a common \(\lambda>0\); equality is friendship. For a non-singleton coalition \(S\ni i\), cost is \(c_i(S)=|\{j\in S\setminus\{i\}:|x_i-x_j|>\lambda\}|/(|S|-1)\). Singleton cost is \(c_i(\{i\})=0\). An allocation is a partition into at most two nonempty unlabeled coalitions. A unilateral jump moves one player into an existing other coalition and is improving precisely if their cost strictly decreases. Any move from the lone coalition of a one-coalition partition has no destination, so one-coalition states have no outgoing jumps. A move from a singleton coalition into the other cannot be strictly improving, as the original cost was zero. Consequently, every directed improvement cycle is confined to partitions into two nonempty coalitions with no singleton departures.

## Proof
**Finite universal lower bound.** Represent any symmetric enemy relation by an undirected simple graph on \(n\) labeled vertices. Every such graph is enumerated by its \(\binom n2\) edge bits. For a two-coalition partition \(S\mid T\), with player \(i\in S\) and \(|S|\ge2\), let \(a=|E(i)\cap S|\), \(b=|E(i)\cap T|\), \(p=|S|\), and \(q=|T|\). The jump from \(S\) into \(T\) is profitable if and only if
\[
\frac a{p-1}>\frac bq\quad\Longleftrightarrow\quad aq>b(p-1).
\]
This integer inequality is tested exhaustively, not approximated. Every unordered nontrivial bipartition has exactly one representative with the last vertex in \(T\), giving \(2^{n-1}-1\) vertices in the state graph. Exhaustively constructing its directed improving-jump edges and running depth-first cycle detection on every labeled enemy graph for \(n=2,3,4,5\) finds no directed cycle. There are exactly \(2+8+64+1024=1098\) graphs, \(15834\) graph-partition combinations, and \(28108\) profitable directed edges checked. This is a finite exhaustive proof for all symmetric enemy relations through five players and therefore for their one-dimensional cutoff subfamily. For \(n=1\), no intercoalition jump is possible.

**Six-person construction.** Choose \(x=(0,9,18,26,27,28)\), \(\lambda=10\), and write each partition by the six-bit integer mask of its first coalition, with bit \(i-1\) indicating membership of player \(i\). The second coalition is the complement. The sequence of masks is
\[
30\to31\to27\to25\to17\to16\to20\to22\to30.
\]
The corresponding moving agents are \(1,3,2,4,1,3,2,4\). Direct substitution into the cost formula yields old-to-new costs
\[
1\to3/4,\quad 1/4\to0,\quad 2/3\to1/2,\quad 1/2\to1/3
\]
and then repeats those four strict decreases. Each transition toggles exactly the corresponding mover's membership, its source is not a singleton, and the destination is nonempty. The final mask equals the initial mask, establishing a directed strict-improvement cycle. Combined with the universal lower bound, this proves sharp minimality \(n=6\).

## Verification
Run `python3 check.py` with Python 3.8 or later. It generates every labeled enemy graph up to five vertices, constructs all unordered bipartitions, enumerates all admissible moves using exact integer cross-products, and detects directed cycles; it independently builds the six-agent enemy graph from the real positions and checks all eight steps with `fractions.Fraction`. Expected terminal lines are `LOWER_OK graphs=1098 states=15834 profitable_edges=28108`, followed by `WITNESS_OK` and `VERIFY_OK`. The finite exhaustive algorithm is part of the proof of the bounded-size exclusion. The displayed witness is verified directly with exact fractions. No heuristic sampling, floating-point assumptions, or open-ended computational search is used in either argument.

## Relationship to prior work
De la Haye, Lenzner, Soheil, and Wunderlich study cutoff hedonic games on a line and present an improvement cycle in their 2026 paper *Metric Hedonic Games on the Line*, Theorem 3.3 and its tabulated example. The result here is the exact **minimum** population: a six-agent construction and a rigorous all-graphs impossibility result through five. An existence example at a larger size does not imply the sharp cutoff. Milchtaich and Winter (2002) examine group formation with average-distance-type incentives; that difference in utility prevents a direct implication for the cutoff fraction-of-enemies game. The two-coalition and HIS convention are essential scope conditions.

## Limitations
Minimality is for at most two coalitions, uniform common cutoff, symmetric distance-based enemy relations, happy-in-isolation singleton costs, and strict unilateral jumps into an existing coalition. The universal five-agent lower bound is stronger than required but does not imply absence of cycles with more coalitions or other update rules. Literature checks cannot exclude every unpublished or unindexed equivalence. The status is a self-review, not independent validation.

## References
1. M. de la Haye, P. Lenzner, F. Soheil, and M. Wunderlich, *Metric Hedonic Games on the Line*, arXiv:2602.05888v1 (first submitted February 5, 2026), especially model definitions and Theorem 3.3.
2. I. Milchtaich and E. Winter, *Stability and Segregation in Group Formation*, Games and Economic Behavior (2002), doi:10.1006/game.2001.0878; a related but distinct average-distance incentive model.
