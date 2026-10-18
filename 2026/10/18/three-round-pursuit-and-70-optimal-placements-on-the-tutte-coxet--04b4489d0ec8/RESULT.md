# Three-round pursuit and 70 optimal placements on the Tutte–Coxeter graph

## Finding
Consider the standard visible-robber game on the Tutte–Coxeter graph \(T\). Cops choose their starting vertices (repetitions allowed), the robber then chooses a starting vertex, and in each round all cops may simultaneously stay or move one edge, after which the surviving robber may stay or move one edge. Capture is immediate when a cop occupies the robber's vertex. The cop number is \(c(T)=3\) and its capture time with three cops is exactly \(\operatorname{capt}_3(T)=3\) rounds.

Among the \(\binom{32}{3}=4960\) unordered initial multisets of three cops, precisely \(70\) guarantee capture within three rounds. Every such multiset has three distinct vertices, all in one of the two bipartition classes. The exact geometric classification is:

1. **Thirty-five point triples:** every projective line in \(\mathrm{PG}(3,2)\), represented by the nonzero vectors \(\{a,b,a+b\}\) for distinct nonzero \(a,b\in\mathbb F_2^4\).
2. **Fifteen concurrent line triples:** the three isotropic lines incident with a chosen point of the generalized quadrangle.
3. **Twenty regulus triples:** three pairwise disjoint isotropic lines admitting exactly three other isotropic lines that each meet all three; together the two triples form a \(3\times3\) grid subconfiguration.

No mixed point–line configuration and no repeated-location configuration is optimal. These counts are for indistinguishable starting cops; all corresponding permutations give equivalent placements for labeled cops.

## Assumptions and scope
Let \(V=\mathbb F_2^4\), using coordinates \(a=(a_0,a_1,a_2,a_3)\). Define the alternating nondegenerate bilinear form
\[
B(a,b)=a_0b_2+a_2b_0+a_1b_3+a_3b_1\pmod2.
\]
The point class of \(T\) contains the \(15\) nonzero vectors. The other class contains the \(15\) two-dimensional totally \(B\)-isotropic subspaces, each written as a three-element set of nonzero vectors. Incidence is vector containment. This is the classical incidence graph of \(W(2,2)\), hence the \(30\)-vertex, \(45\)-edge Tutte–Coxeter graph. All moves take place on the incidence graph, **not** on its point graph.

All strategies are deterministic perfect-information strategies, with cops and robber permitted to remain stationary. A round starts with the cops' move, and a robber already on a cop is immediately captured. The optimal-start classification applies to precisely three cops; no assertion is made about other pursuit variants.

## Proof
**Finite state-space recurrence.** For \(k\in\{1,2,3\}\), let \(\mathcal C_k\) be all multisets of \(k\) vertices and let \(M(C)\) comprise all multisets reachable by one simultaneous move, allowing each cop to stay. Write \(S(C)\) for the support of multiset \(C\), \(N[r]\) for a robber's closed neighborhood, and \(F_t(C)\) for the set of robber locations from which the cops can force capture in at most \(t\) cop turns, starting at \(C\) with the cops to move. Then
\[
F_0(C)=S(C),
\]
\[
F_{t+1}(C)=S(C)\cup\bigcup_{C'\in M(C)}\left(S(C')\cup\{r:N[r]\subseteq F_t(C')\}\right).
\]
This formula is an exact backward induction: the cops choose \(C'\) after seeing \(r\); occupying \(r\) ends the game immediately, while otherwise every legal robber response must leave a winning position with one fewer cop turn. Thus it computes the full set of optimal-play game states without a probabilistic or strategic heuristic.

The script `verify_game.py` builds the graph from the displayed alternating form, constructs every cop multiset and legal simultaneous move, and evaluates this recurrence by integer bitsets over all thirty robber positions. For one cop, the total numbers of winning \((C,r)\) states at times \(t=0,1,2\) are \(30,120,120\); the last two *sets* coincide, proving that a single cop cannot force capture. For two cops they are \(900,3420,3420\), again with equality of the last two sets, proving that two cops cannot force capture. For three cops the counts at \(t=0,1,2,3\) are \(13950,50520,55080,75360\). Exactly \(70\) of the \(4960\) three-cop multisets have \(F_3(C)=V(T)\), while none have \(F_2(C)=V(T)\). Thus \(c(T)=3\) and \(\operatorname{capt}_3(T)=3\).

**Conceptual lower bound on rounds.** Each vertex of \(T\) has precisely \(10\) vertices within distance two; this follows from degree three and girth eight. Every two such balls intersect, since the graph has diameter four and a shortest path between their centers contains a vertex at distance at most two from both. Therefore the union of any three radius-two balls has fewer than \(30\) vertices. The robber can initially choose a vertex at distance at least three from every cop and stay stationary through the first two cop moves. Hence no three-cop initial configuration can capture every robber within two rounds, independently of the exhaustive computation.

**Classification of optimal starts.** The same recurrence tests all cop multisets. Restricting the \(70\) successful multisets to point vertices produces exactly the \(35\) triples \(\{a,b,a+b\}\), one for each two-dimensional subspace of \(\mathbb F_2^4\). Restricting to line vertices produces exactly the \(15\) point pencils and the \(20\) pairwise disjoint triples with three common transversals. The verifier tests these descriptions directly against all \(\binom{15}{3}=455\) subsets of each type; no other multiset succeeds. The file `optimal_starts.csv` gives the complete ordered census using point labels \(0\) through \(14\) for vectors \(1\) through \(15\), and line labels \(15\) through \(29\) for the lexicographically sorted isotropic triples generated by the code.

## Verification
The package includes two standalone Python 3 programs requiring only the standard library. Run `python3 verify_game.py` and `python3 verify_dual.py` from this directory. Both report `VERIFY_OK`. The first computes the cop-winning backward recurrence; the second independently implements the complementary robber-survival recurrence, directly taking intersections over cop responses and unions over evasive robber moves. For three cops, the complementary recursion gives exactly \(134850,98280,93720,73440\) losing \((C,r)\) states at horizons zero through three; these counts complement the first program's winning counts in the \(148800\) states. Both recover exactly the same \(70\) optimal positions and their \(35+15+20\) geometry. The ordered census has SHA-256 `422e6ea22043c57643838985dc011c76221708a837c123f32282bb65c4d9353d`.

The first program also constructs the graph, verifies its degree, girth and diameter, and checks the radius-two-ball lower bound for every possible starting multiset. The accompanying `.out` files record actual executions. The proof is a complete finite-state exhaustive proof for this thirty-vertex graph; none of these finite tests is extrapolated to a family of graphs.

## Relationship to prior work
Bonato and Burgess, *Cops and Robbers on Graphs Based on Designs* (first online 17 October 2012), establish cop-number methods for several design-derived graphs; their reported work includes generalized quadrangle **point graphs**, whereas the present theorem concerns the **incidence graph** and a complete three-round start classification. The article's accessible abstract and indexed text do not state these \(70\) optimal configurations. However, its complete publisher-hosted text was unavailable during this comparison, so undiscovered overlap within that article remains a genuine risk.

Bonato, Golovach, Hahn and Kratochvíl initiated systematic graph capture-time study; their general fixed-cop polynomial-time computability is not an exact result for \(T\). Bonato, Kinnersley, Gordinowicz and Prałat (2013) analyze hypercube capture times for a different graph family and provide the standard move and timing definitions. Neither the general algorithmic framework nor the hypercube bounds imply this particular optimal-placement geometry. Other published mathematical records concerning the Tutte–Coxeter graph's topology or distance-complexes concern distinct invariants.

## Limitations
The classification is exact only for the standard three-cop visible-robber game on \(T\), with pass moves allowed. It gives no formula for arbitrary generalized quadrangles or other cages, and makes no claim about invisible robbers or simultaneous adversarial moves. The explicit search over a finite state space is a mathematical proof for this instance, not a noncomputational proof of the \(70\)-placement characterization. Possible unindexed enumerations and the inaccessible full text of the Bonato–Burgess article are residual prior-art uncertainties.

## References
1. A. Bonato and A. Burgess, *Cops and Robbers on Graphs Based on Designs*, Journal of Combinatorial Designs 21 (2013), 404–418; first published online 2012-10-17, DOI `10.1002/jcd.21331`.
2. A. Bonato, W. B. Kinnersley, P. Gordinowicz and P. Prałat, *The capture time of the hypercube*, arXiv `1308.3354` (first submission 2013-08-15).
3. A. Bonato, P. Golovach, G. Hahn and J. Kratochvíl, *The capture time of a graph*, Discrete Mathematics 309 (2009), 5588–5595, DOI `10.1016/j.disc.2008.04.004`.
4. M. Aigner and M. Fromme, *A game of cops and robbers*, Discrete Applied Mathematics 8 (1984), 1–12.
