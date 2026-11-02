# A self-centered, nonregular exchange graph for minimum zero forcing of the four-cube

## Finding

The one-vertex-exchange graph of minimum ordinary zero forcing sets of the four-cube has \(2360\) vertices, \(22848\) edges and is connected. It is nonregular, but every vertex has eccentricity \(8\). Consequently its radius and diameter are both \(8\). Its degree distribution is

\[
384z^{14}+384z^{18}+384z^{19}+432z^{20}+480z^{22}+192z^{23}+104z^{24}.
\]

Its ordered-pair distance polynomial, including the diagonal, is

\[
\begin{aligned}
P(q)={}&2360+45696q+355776q^2+1274880q^3\\
&+2110368q^4+1361280q^5+371184q^6\\
&+45696q^7+2360q^8.
\end{aligned}
\]

Thus the Wiener index, the sum of distances over unordered pairs of distinct configurations, is \(11197808\).

All minimum configurations have feasible complements, and every complementary pair is at distance \(8\). Their exact exchange metric almost agrees with the ambient Johnson metric: for ordered pairs \((S,T)\), the excess \(d_{\mathcal R}(S,T)-[8-|S\cap T|]\) has the multiplicity distribution

| Excess | Number of ordered pairs |
|---:|---:|
| 0 | 5,458,192 |
| 1 | 105,600 |
| 2 | 5,808 |

All ordered pairs, including self-pairs, are included. These multiplicities sum to \(2360^2\). No claim is made that the previously established census of \(2360\) minimum sets or its eleven cube-symmetry orbits is new.

## Assumptions and scope

The simple graph \(Q_4\) has vertices the four-bit words and an edge between words of Hamming distance one. A blue vertex forces a white neighbor if the latter is its unique white neighbor. Any set that eventually colors the graph blue is a zero forcing set. A minimum set is one of smallest cardinality, which is \(8\) for this graph. The reconfiguration graph \(\mathcal R\) has one vertex for each minimum set, and an edge \(ST\) exactly when \(|S\setminus T|=|T\setminus S|=1\). This is a finite theorem only about the four-dimensional cube and ordinary zero forcing. It does not apply to positive semidefinite zero forcing or to arbitrary-dimensional cubes.

## Proof

**Exhaustive reduction with explicitly replayable predicates.** Label cube vertices by integers \(0,\ldots,15\), with vertex \(u\) adjacent to \(u\mathbin{\mathrm{xor}}2^i\), for \(i\in\{0,1,2,3\}\). Encode a blue set by a 16-bit integer. To test it, repeatedly identify every blue vertex with precisely one white neighbor and add the union of its unique white neighbors simultaneously. The process either reaches the full 16-bit mask or stabilizes, and the predicate terminates within 16 rounds. This is exactly the ordinary zero-forcing rule; simultaneous legal forces can be sequentially applied, and a successful sequential forcing sequence can be realized in synchronous closure because forcing is monotone under adding blue vertices.

Enumerate the \(\binom{16}{7}=11440\) seven-subsets and the \(\binom{16}{8}=12870\) eight-subsets. No seven-subset succeeds and precisely \(2360\) eight-subsets succeed. Monotonicity gives minimum cardinality \(8\). (This census independently reproduces previously known finite facts; they are not the novelty claim.) Construct an exchange adjacency by toggling one selected bit and one unselected bit and retaining precisely those neighbors among the successful eight-subsets. The resulting simple undirected graph has \(22848\) edges, and its 2360 degree values yield the displayed polynomial.

For exact all-pairs metrics, the first accompanying implementation enumerates the 384 isometries given by 16 translations and 24 permutations of four coordinates. These preserve forcing and one-vertex exchanges, and partition the 2360 configurations into 11 orbits, with orbit sizes \(8,48,96,96,192,192,192,384,384,384,384\). An ordinary breadth-first search from one representative of each orbit determines its exact distance to every configuration, including reachability. Multiplying each source distance histogram by its orbit size gives every ordered-pair distance multiplicity and proves that all eccentricities equal \(8\). This produces \(P(q)\) and the Wiener index \(\frac12P'(1)\). Since the 11 representative breadth-first searches reach all 2360 states, the exchange graph is connected.

For every ordered pair the same searches compare the actual distance with the Johnson lower bound \(j(S,T)=8-|S\cap T|\); counting the exact differences proves the excess spectrum \(\{0:5458192,1:105600,2:5808\}\). The initial census also verifies that every successful eight-set has a successful complement. Since its Johnson distance from its complement equals \(8\), and the already-proved diameter is \(8\), every complementary pair has exact exchange distance \(8\).

**Independent finite proof replay.** The second implementation independently tests forcing through a sequential legal-move procedure, reconstructs all exchange edges, and performs breadth-first searches from **every** one of the 2360 configurations (not just orbit representatives), computing ordered-pair distance counts and Johnson excess directly. It checks the same 384 cube automorphisms separately. Its independently constructed outputs match all claimed integers. This fully exhaustive, finite, integer-only algorithm constitutes the certificate for the stated graph, not statistical evidence or extrapolation.

## Verification

Run the included Python 3 standard-library program `verify_primary.py` and the independent C++17 program `verify_alt.cpp`:

```sh
python3 verify_primary.py
g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt
./verify_alt
```

Expected final lines are `PRIMARY_CERTIFICATE_PASS` and `INDEPENDENT_CERTIFICATE_PASS`, respectively. The first exhaustively checks 11 symmetry-representative distance balls, while the second checks all 2360 source distance balls. Both verify all claimed integer distributions. The programs are complete and use no external data files.

## Relationship to prior work

The AIM Minimum Rank–Special Graphs Work Group introduced the modern zero-forcing framework, and Peters proved \(Z(Q_d)=2^{d-1}\), which gives the **minimum cardinality** for the cube. Geneson, Haas and Hogben defined and studied reconfiguration graphs of zero-forcing sets under one-vertex exchanges; their general definitions do not give this cube's complete distance census. Brimkov, Cameron and Grubbs examined forts and zero forcing on hypercubes, including differing propagation times of four-cube forcing sets, but not the precise exchange graph distance distribution. Previously available exact counts and cube automorphism classes of its minimum forcing sets are used only as background cross-checks; no numerical counting novelty is asserted for them.

This result adds the entire one-exchange graph's edge/degree statistics, sharp uniform eccentricity, all-pairs distances, Wiener index, and quantitative deviation from ambient Johnson distances. In particular, the general reconfiguration operation itself, the minimum forcing number, the number of minimum forcing sets, and their propagation-time distribution are not claimed as discoveries.

## Limitations

The proof is an exhaustive finite certificate for the stated 16-vertex cube; it does not establish a uniform formula in arbitrary dimension. Each integer is established by the supplied exact predicates and complete breadth-first searches, not by the mere existence of a log. The claim is not independently audited. An equivalent prior classification could exist in unindexed or inaccessible material; a failed literature search is not evidence of uniqueness.

## References

1. AIM Minimum Rank–Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications (2008). DOI: 10.1016/j.laa.2007.10.009.
2. T. Peters, *Positive semidefinite maximum nullity and zero forcing number*, Electronic Journal of Linear Algebra 23 (2012), 815–830. DOI: 10.13001/1081-3810.1559.
3. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets* (2020), arXiv:2009.00220.
4. B. Brimkov, K. Cameron and C. Grubbs, *On the forts and related parameters of the hypercube graph* (2025), arXiv:2507.10826.
