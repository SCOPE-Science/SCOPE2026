# A two-step majority projection and exact attraction basins on the Heawood graph

## Finding

Let \(H\) be the fourteen-vertex Heawood graph, presented as the point–line incidence graph of the Fano projective plane. In synchronous binary open-neighbor majority dynamics, every vertex adopts the value held by at least two of its three neighbors. For the global update map \(F:\{0,1\}^{14}\to\{0,1\}^{14}\), the exact identity is
\[
F^4=F^2,\qquad F^3\ne F.
\]
Thus the sharp maximum first-periodic-entry time is two. The complete periodic census consists of **58 fixed configurations** and **1,653 primitive temporal two-cycle orbits**; no other periods occur. There are exactly \(28\) nonconstant fixed colorings with six ones, each the indicator of one of the Fano plane's hexagons, and their \(28\) complements, besides the two constant colorings.

The attraction basins have an unusually rigid size distribution:

| Primitive orbit type | Basin size per orbit | Number of orbits |
| --- | ---: | ---: |
| Fixed configuration | 1 | 56 |
| Fixed configuration | 1,296 | 2 |
| Primitive two-cycle | 2 | 1,540 |
| Primitive two-cycle | 72 | 112 |
| Primitive two-cycle | 2,592 | 1 |

Here the basin includes all initial labelled binary states eventually entering that *temporal* orbit. The total is \(2^{14}=16{,}384\) configurations: \(2{,}648\) reach fixed points and \(13{,}736\) reach two-cycles. The exact counts by first periodic entry \(t\) and eventual period \(d\) are:

| \(t\) | \(d=1\) | \(d=2\) |
| ---: | ---: | ---: |
| 0 | 58 | 3,306 |
| 1 | 126 | 1,694 |
| 2 | 2,464 | 8,736 |

## Assumptions and scope

The seven points are the nonzero vectors of \(\mathbf F_2^3\), labelled \(1,\ldots,7\) in binary. The seven lines are the triples \(\{a,b,a\mathbin{\mathrm{xor}}b\}\) for distinct nonzero \(a,b\); duplicate triples represent the same line. They are, in lexicographic order,
\[
\begin{gathered}
123,\ 145,\ 167,\ 246,\ 257,\ 347,\ 356.
\end{gathered}
\]
A point-vertex is adjacent precisely to the line-vertices containing it. This gives a cubic bipartite graph with seven vertices in each shore. States are labelled vertex assignments; temporal rotations are identified in the orbit count, but spatial automorphisms and global color complementation are **not** quotiented out. There are no majority ties and no self-loops.

For a subset \(S\) of points, let \(\Phi(S)\) be the set of lines containing at least two members of \(S\). For a set \(T\) of lines, let \(\Psi(T)\) be the set of points incident with at least two lines in \(T\). The simultaneous dynamics is exactly
\[
F(S,T)=(\Psi(T),\Phi(S)).
\]
A *noncollinear triple* means three Fano points not lying on one Fano line. There are \(\binom73-7=28\) such triples.

## Proof

**1. The two-step projection.** Define \(P=\Psi\circ\Phi\) on point subsets. Elementary Fano incidence gives the following exhaustive cases. The same table applies dually to \(\Phi\circ\Psi\) on line subsets.

| Input subset \(S\) | Number of subsets | \(P(S)\) |
| --- | ---: | --- |
| Empty | 1 | Empty |
| One point | 7 | Empty |
| Two points | 21 | Empty |
| Three points forming a line | 7 | Empty |
| Three noncollinear points | 28 | \(S\) |
| Four points, whose complement is a noncollinear triple | 28 | \(S\) |
| Four points, whose complement is a line | 7 | All seven points |
| Five points | 21 | All seven points |
| Six points | 7 | All seven points |
| All seven points | 1 | All seven points |

To justify the cases without relying on numerical experiments: two points determine one line, so two or fewer selected points generate at most one selected line; a collinear three-set does the same. A noncollinear triple selects its three pair-joining lines. Each selected point is incident with two of those lines; any unselected point is incident with at most one, because distinct Fano lines meet in exactly one point. For four selected points whose three-point complement is noncollinear, the three excluded pair-joining lines each contain exactly one of the four selected points, and the other four lines are selected; every selected point lies on at least two of these four lines, whereas each excluded point lies on only one. If the three-point complement is itself a line, all six other lines are selected. With at least five selected points, at most one line fails to contain a majority of selected points. In either six-line case every point has at least two incident selected lines. This establishes the entire table.

It follows that \(P^2=P\) and its image/fixed set is
\[
\mathcal R=\{\varnothing,\mathcal P\}\ \cup\
\{S:\lvert S\rvert=3,\ S\text{ noncollinear}\}\ \cup\
\{\mathcal P\setminus S:\lvert S\rvert=3,\ S\text{ noncollinear}\},
\qquad \lvert\mathcal R\rvert=58,
\]
where \(\mathcal P\) is the seven-point set. By point–line duality, \(Q=\Phi\circ\Psi\) is also idempotent with a 58-element fixed set \(\mathcal R^*\). Hence
\[
F^2(S,T)=(P(S),Q(T)),\qquad F^4=F^2,
\]
and the periodic state space is precisely \(\mathcal R\times\mathcal R^*\).

**2. The recurrent swap.** On \(\mathcal R\), the map \(\Phi\) is a bijection onto \(\mathcal R^*\), inverse to \(\Psi\), because \(\Psi\Phi(S)=S\). Every periodic configuration can therefore be uniquely written as \((S,\Phi(U))\) with \(S,U\in\mathcal R\). On this space,
\[
F(S,\Phi(U))=(U,\Phi(S)).
\]
The dynamics is just an interchange of two 58-valued symbols. Consequently there are \(58\) fixed points, \(\binom{58}{2}=1{,}653\) primitive two-cycles, and no other periods. If \(S\) is a noncollinear triple, its three connecting lines together with the three selected points induce a six-cycle in \(H\); the complementary stable configuration is obtained by flipping all bits. Conversely all nonconstant fixed points are of these two forms by the ten-case table. This proves the hexagon assertion.

**3. Complete basin distribution.** The table in step 1 gives the fibers of \(P\) over its 58 fixed subsets:
\[
m(S)=\lvert P^{-1}(S)\rvert=
\begin{cases}
36,&S=\varnothing\text{ or }S=\mathcal P,\\
1,&S\in\mathcal R\setminus\{\varnothing,\mathcal P\}.
\end{cases}
\]
Indeed, exactly \(1+7+21+7=36\) source subsets map to the empty set, and, by complementation, 36 map to the full set. Each of the other 56 images has its one preimage, itself. The dual projection has identical fiber sizes. Thus a fixed orbit \((S,\Phi(S))\) has basin size \(m(S)^2\), while the primitive two-cycle represented by an unordered pair \(\{S,U\}\) with \(S\ne U\) has basin size \(2m(S)m(U)\). Among the \(58\) symbols there are two exceptional ones of weight 36 and 56 ordinary ones of weight one. The five basin classes in the finding follow immediately: fixed \(2\) large and \(56\) isolated; two-cycle \(\binom{56}{2}=1{,}540\) of basin size two, \(2\cdot56=112\) of basin size 72, and one of basin size 2,592.

**4. First-entry clock.** By direct incidence classification, \(\Phi\) takes exactly 72 distinct values: one empty line set, seven singleton-line sets, 28 triangle line sets, 28 four-line complements of triangles, seven six-line sets, and one full line set. The dual map \(\Psi\) likewise takes exactly 72 values. Therefore
\[
\lvert\operatorname{im}F\rvert=72^2=5{,}184,\qquad
\lvert\operatorname{im}F^2\rvert=58^2=3{,}364.
\]
All states of \(\operatorname{im}F^2\) are periodic, all states of \(\operatorname{im}F\setminus\operatorname{im}F^2\) first enter after one further update, and all other states first enter after two updates. The corresponding totals are \(3{,}364,1{,}820,11{,}200\). The exact period-refined table is obtained by counting the preimages of the fixed states: the two constant fixed configurations have 64 immediate predecessors each; the other 56 have one each. Thus the first-entry-one fixed count is \(2(64-1)=126\), and the first-entry-two fixed count is \(2(1{,}296-64)=2{,}464\). Subtraction from the total entry layers gives the two-cycle figures. Finally, the state with just points 1 and 2 occupied and all line-vertices resting follows the trajectory \(\{1,2\}\to\{\text{line }123\}\to\varnothing\), establishing that two updates are necessary for some initial states and that \(F^3\ne F\).

## Verification

The full-state checker `check_heawood.cpp` independently builds the fourteen-vertex graph from the seven explicitly listed lines, enumerates all \(2^{14}\) binary configurations, constructs the functional digraph, extracts primitive orbits and exact basins by indegree peeling, and checks the identity and all entry-time counts. Compile with `g++ -std=c++17 -O2 -Wall -Wextra check_heawood.cpp -o check_heawood` and execute `./check_heawood`. Its output is preserved in `check_heawood_output.txt`.

Separately, `check_fano.py` constructs the seven Fano lines from nonzero binary triples, verifies the ten-case projection classification, the two-point and two-line maps, exact fibers, hexagon correspondence, and then also performs an independent full-state path-following census. Execute `python3 check_fano.py`; its output is in `check_fano_output.txt`. Both programs contain assertions that fail if any stated identity or count disagrees. They were executed on the packaged source files, with all assertions passing. The mathematical proof above does not depend on an unbounded numerical extrapolation.

## Relationship to prior work

The period-at-most-two conclusion for finite synchronous symmetric threshold networks is classical, especially the theorem of Goles and Olivos (1980), and is *not* claimed as new. Tamuz and Tessler (first submitted 2013) prove information-retention and general convergence results for majority dynamics on various graphs, and Benjamini, Chan, O'Donnell, Tamuz and Tan (first submitted 2014) study convergence and unanimity on unimodular and random graphs. Their inspected full text discusses the general two-period restriction and bounds but does not give the Fano-incidence projection, this 58-symbol swap, the exact basins, or the two-step cutoff. Agur, Fraenkel and Klein (1988) exactly enumerate fixed points for the **different** self-inclusive majority rule on cyclic binary strings, with a Fibonacci-like count; their entire eight-page article concerns that one-dimensional rule, not the Heawood graph. The Fano-incidence geometry and its 28 six-cycles are standard facts; the novel content assessed here is their complete dynamical consequence under the specified strict-neighbor rule.

## Limitations

The theorem is an exact finite result for the labelled Heawood graph only. It does not assert the same projection identity, counts, convergence cutoff, or basin patterns on larger projective-plane incidence graphs or other cubic graphs. The synchronous open-neighbor update must not be confused with self-inclusive majority (which is a different rule on other graphs), noisy voter models, or asynchronous majority. A numerical search cannot establish absolute historical priority; equivalent unpublished computations or differently indexed treatments could exist. Independent external audit has not been performed.

## References

1. O. Tamuz and R. J. Tessler, *Majority Dynamics and the Retention of Information*, arXiv:1307.4035, first posted 2013-07-15, https://arxiv.org/abs/1307.4035 ; full HTML https://arxiv.org/html/1307.4035v2 .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486, first posted 2014-05-11, https://arxiv.org/abs/1405.2486 .
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
4. Z. Agur, A. S. Fraenkel and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics 70 (1988), 295–302, https://doi.org/10.1016/0012-365X(88)90005-2 ; lawful open full text https://www.imbm.org/wp-content/uploads/2020/01/AFK88.pdf .
5. SageMath Graph Theory documentation, *HeawoodGraph*, https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/graph_generators.html (graph geometry, not a dynamical enumeration).
