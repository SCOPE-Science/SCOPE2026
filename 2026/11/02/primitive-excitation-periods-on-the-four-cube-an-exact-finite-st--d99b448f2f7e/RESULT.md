# Primitive excitation periods on the four-cube: an exact finite-state census

## Finding

For synchronous three-state threshold-one Greenberg–Hastings dynamics on the hypercube graphs \(Q_d\) of dimensions \(1\le d\le4\), the exact number of primitive temporal orbits of each least period is:

| Dimension | Number of configurations | Primitive orbit counts (period : orbits) |
|---:|---:|---|
| 1 | 9 | 1 : 1 |
| 2 | 81 | 1 : 1; 4 : 2 |
| 3 | 6,561 | 1 : 1; 3 : 84; 4 : 48 |
| 4 | 43,046,721 | 1 : 1; 3 : 292,616; 4 : 13,190; 10 : 1,344 |

All other primitive period counts are exactly zero in these four dimensions. In particular the four-dimensional cube is the smallest hypercube among these dimensions supporting a primitive ten-cycle, and it supports exactly \(1,344\) distinct such cycles. The four-cube is isomorphic to the nearest-neighbor, periodic four-by-four square grid \(C_4\square C_4\).

For \(Q_4\), the exact total number of configurations attracted to each eventual period is \(592641\) (period one), \(16535592\) (period three), \(25166232\) (period four), and \(752256\) (period ten). These numbers sum to \(43046721\). The maximum number of updates before an orbit is entered is exactly \(11\). The lone fixed point is the all-zero configuration.

## Assumptions and scope

Let \(1\le d\le4\). The vertices of \(Q_d\) are integers \(v\in\{0,\ldots,2^d-1\}\), interpreted as length-\(d\) binary strings. Vertices \(v,w\) are adjacent if \(w=v\mathbin{\operatorname{xor}}2^j\) for some \(0\le j<d\). There are no loops. All vertex colors update simultaneously and deterministically by the map \(F_d\):

\[
(F_d(x))_v = \begin{cases}
2,&x_v=1,\\
0,&x_v=2,\\
1,&x_v=0\text{ and some neighbor of }v\text{ has color }1,\\
0,&\text{otherwise}.
\end{cases}
\]

The **primitive period** of a periodic state \(x\) is the smallest positive integer \(p\) such that \(F_d^p(x)=x\). A primitive temporal orbit is the set of the \(p\) distinct states in that cycle. The **first-entry time** of an initial configuration is the least nonnegative \(t\) for which \(F_d^t(x)\) is periodic, and the basin of a period class consists of initial states whose eventual least period has that value. Orbit counts do not identify states modulo graph automorphisms: all \(2^d\) vertices are labelled.

## Proof

This is a finite-range theorem with a complete finite certificate, rather than an inductive extrapolation. Let \(n=2^d\) and encode every configuration uniquely by
\[
s(x)=\sum_{v=0}^{n-1}x_v3^v,\qquad 0\le s<3^n.
\]
The source programs `tools/census.cpp`, `tools/independent.cpp`, and `tools/basins.cpp` implement exactly the stated transition. The first implements the equivalent bit-set update: if \(A=\{v:x_v=1\}\) and \(B=\{v:x_v=2\}\), then the next color-2 set is \(A\), while the next color-1 set is
\[
N(A)\setminus(A\cup B),
\]
where \(N(A)=\bigcup_{u\in A}N(u)\) is the **open** vertex neighborhood of \(A\). These two sets are disjoint, so the radix-three successor is exactly the sum of their digit weights, with coefficient two on the former set. For every \(d\le4\), \(3^{2^d}\le43046721\) and the whole state space is explicitly represented.

For each state \(s\in\{0,\ldots,3^n-1\}\) in increasing order, a three-color depth-first functional-digraph traversal follows the unique successor until it reaches either (i) a state already grey in the current walk or (ii) a previously completed black state. In case (i), the segment from the repeated state to the end of the walk is one previously uncounted directed cycle, whose exact number of distinct vertices is its primitive period. In case (ii), the walk reaches an already counted component and introduces no new cycle. All visited grey states are then marked black. Since every vertex of the finite functional digraph is either visited by the outer scan or already reached, this process examines **every one** of the \(3^n\) configurations; each periodic orbit is counted exactly once and there is no possible unexamined period. Applying this exhaustive procedure gives precisely the four period-count rows in the Finding table.

The separate `tools/independent.cpp` reconstructs each color from trits and applies the local rule vertex-by-vertex rather than the neighborhood bit-set identity, and independently traverses the entire functional graph. It reproduces the same period counts. This separate implementation supports the critical transition/cycle-count computation; it does not replace the exhaustive argument.

For basins and entry times, `tools/basins.cpp` again constructs the successor vertex-by-vertex, records periodic cycles as entry time zero, then propagates period and entry time one step backward along each explored finite path. Following a path into a previously classified component propagates the correct eventual period and increases entry time by one; a newly detected cycle has entry time zero. These are all cases because outdegree is exactly one. The resulting complete \(Q_4\) first-entry profile is `data/entry_profile.txt`; summing its columns gives the four basin counts above. The entry-time profile contains positive entries at time \(11\) and none afterward, proving the sharp value \(11\).

An explicit period-ten orbit is recorded in `data/period10_witness.txt`, with all sixteen trits in increasing vertex-label order. Each successive row satisfies the local update, all ten rows are distinct, and the eleventh equals the first. Since the ten displayed states are distinct and the next state returns to the start, the trace itself directly verifies least period ten.

Finally, the independent program `tools/circulation.cpp` checks the extinction basins by the circulation criterion of Gravner–Lyu–Sivakoff. On each oriented edge \(u\to v\), assign increment \(+1\) for colors \(0\to1\), \(-1\) for \(1\to0\), and zero otherwise, then sum around every square face. The square faces generate the integral cycle space of the hypercube graph. The reduced increment agrees on all closed walks with the usual one-third winding of the three-color increment, because on any closed color walk the net \(0\to1\), \(1\to2\), and \(2\to0\) transition counts are equal by conservation at each color. By the cited convergence criterion, an initial coloring reaches zero exactly when these sums all vanish. Independently counting such colorings yields \(9,57,1485,592641\) for \(d=1,2,3,4\), agreeing exactly with the computed extinction basins. This external theorem is used only for the additional check; the direct exhaustive functional-graph proof does not require it.

## Verification

Compile with a standard C++17 compiler, for example `c++ -O3 -std=c++17 tools/census.cpp -o census`, and similarly compile `independent.cpp`, `basins.cpp`, and `circulation.cpp`. Execute each program for dimensions \(1\), \(2\), \(3\), and \(4\). The expected counts and the complete basin profile are included in `data/observed_counts.txt` and `data/entry_profile.txt`, with full captured outputs of all four standalone programs in `data/reproduction_output.txt`. All four programs were compiled and executed successfully at all four dimensions. The two orbit-enumeration algorithms, independently coded, agree on every primitive period count, and the circulation computation agrees on all extinction basins.

The four-cube has \(43,046,721\) configurations, so complete enumeration is substantial but finite; no sample-based inference is used to establish the listed cycle counts. The explicit witness trace supplies a concise independent positive certificate for a primitive ten-cycle.

## Relationship to prior work

Durrett and Steif (1991) study long-time Greenberg–Hastings dynamics on periodic square lattices and asymptotic, random-initial-state regimes. Their results do not give the complete primitive-orbit counts for the fixed four-by-four toroidal grid. Gravner, Lyu, and Sivakoff (2016), Theorem 3, characterize persistence using a graph-theoretic edge-circulation invariant; this implies extinction versus nonextinction for each configuration but does not itself give this primitive-period census or the \(1,344\) count. Doba (2018) analyzes activity rates on finite graphs and explicitly reports a ten-step orbit on another graph; thus period ten is **not** claimed new across all finite graphs. The present finding is restricted to the precise four-cube classification and sharp lower-dimension comparison.

## Limitations

No primitive-period bound or orbit-count formula for \(Q_d\) with \(d\ge5\) is asserted. The classification is for the exact threshold-one, three-state, synchronous, loopless rule and labelled hypercube vertices. A complete finite computation certifies the stated finite cases but does not establish an infinite-dimensional pattern. No claim of independent peer review, external certification, or exhaustive historical priority is made. The literature comparison remains vulnerable to unindexed or unavailable exact tables and equivalent formulations of this finite problem.

## References

- R. Durrett and J. E. Steif, *Some Rigorous Results for the Greenberg–Hastings Model*, Journal of Theoretical Probability **4** (1991), 669–690. DOI: `10.1007/BF01259549`.
- J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, first arXiv version posted 2016-10-24, `arXiv:1610.07320v1`.
- N. Doba, *The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph*, Complex Systems **27** (2018), 101–128. DOI: `10.25088/ComplexSystems.27.2.101`.
