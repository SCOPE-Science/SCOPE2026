# Seven forcing-complement types and a self-centered exchange graph for \(\mathrm{KG}(6,2)\)

## Finding

Let \(G=\mathrm{KG}(6,2)\), whose fifteen vertices are the two-element subsets of \(\{0,1,2,3,4,5\}\), with disjoint pairs adjacent. A zero forcing set is an initially black vertex set from which every white vertex can eventually be turned black, where a black vertex may force its **unique** white neighbour. The known minimum size \(Z(G)=10\) is independently reproduced, but is **not** asserted as new.

There are exactly **1,662 distinct minimum zero forcing sets**, partitioned into **seven** orbits under the natural \(S_6\)-action, of sizes \(360,360,360,360,90,72,60\). Equivalently, consider the five omitted (white) vertices of a minimum zero forcing set as five edges of a six-vertex simple graph \(H\). Then \(H\) is isomorphic to **exactly one** of the following seven representatives; a row is specified by its five unordered edges on \(\{0,1,2,3,4,5\}\):

| Orbit size | Edges of a representative five-edge graph |
|---:|---|
| 360 | 01, 02, 13, 24, 35 |
| 360 | 01, 02, 03, 14, 25 |
| 360 | 01, 02, 03, 12, 34 |
| 360 | 01, 02, 03, 12, 14 |
| 90 | 01, 02, 03, 14, 15 |
| 72 | 01, 02, 13, 24, 34 |
| 60 | 01, 02, 12, 34, 35 |

For example, `01` denotes the unordered edge joining labels 0 and 1, not a two-digit integer.

Build the **minimum-set exchange graph** \(\mathcal Z(G)\) with these 1,662 minimum sets as vertices, joining two if their symmetric difference consists of precisely two original graph vertices (a single token jump). This graph is connected, has **24,270 edges**, and is **self-centered**:

\[
\operatorname{rad}(\mathcal Z(G))=\operatorname{diam}(\mathcal Z(G))=5,
\qquad \operatorname{ecc}(B)=5\quad\text{for every minimum set }B.
\]

The degree distribution of \(\mathcal Z(G)\) is 450 vertices of degree 26, 360 of degree 29, 432 of degree 30, and 420 of degree 32. Its exact unordered-pair distance distribution is:

| Exchange distance | Number of unordered distinct pairs |
|---:|---:|
| 1 | 24,270 |
| 2 | 202,320 |
| 3 | 557,820 |
| 4 | 477,855 |
| 5 | 118,026 |
| **Total** | **1,380,291** |

## Assumptions and scope

All graphs are finite, simple, and undirected. The six underlying labels are distinct; all 1,662 minimum sets are counted as labelled subsets of the fifteen vertices of \(G\). An orbit under relabelling the six ground labels is an isomorphism class of five-edge complement graphs. The exchange distance uses only paths through **minimum** zero forcing sets, not arbitrary black sets. Ordinary (not skew, positive-semidefinite, or probabilistic) zero forcing is used.

## Proof

The following is an exact, finite exhaustive proof with two independently implemented standalone checkers, rather than an argument extrapolating finite data to an infinite family. All loops, termination conditions, and invariants are explicit.

**Forcing decision lemma.** For a black set \(B\) represented by a fifteen-bit mask, let \(N(v)\) be the six neighbours of vertex \(v\) in \(G\). Write \(W=V(G)\setminus B\). If \(v\in B\) and \(|N(v)\cap W|=1\), replace \(B\) by \(B\cup(N(v)\cap W)\). Repeating any available move reaches the all-black state if and only if \(B\) is a zero forcing set. Indeed, adding black vertices can never invalidate the eventual availability of an intended force before its target is black: at worst that force becomes unnecessary because its target was colored earlier. More formally, if a forcing sequence works from \(B\), the sequence can be simulated from any superset of \(B\), omitting steps whose targets are already black. Thus firing all currently legal moves in parallel or selecting any one at a time preserves success/failure. At most fifteen strict additions occur, so the test terminates.

**Minimum and classification.** Enumerate all \(\binom{15}{9}=5,005\) nine-element black subsets and apply the lemma: none succeeds. By monotonicity, no smaller subset can succeed either. Enumerating all \(\binom{15}{10}=3,003\) ten-element subsets yields exactly 1,662 successes, hence \(Z(G)=10\). For the orbit certificate, enumerate all 3,003 five-edge subsets of \(E(K_6)\). The 720 permutations of the six labels partition them into exactly fifteen disjoint full orbits. A forcing decision on one representative of each orbit, and invariance under relabelling, show that exactly seven orbits succeed. Their sizes and explicit five-edge representatives are those displayed above, and their sum is 1,662. The remaining eight orbits do not succeed. `kg62_orbit_check.py` independently implements a recursively branching single-force decision test for every representative; `kg62_direct_check.py` tests every candidate with simultaneous forcing. This provides both a complete negative check and a complete positive list.

**Exchange graph and metrics.** For every successful five-edge complement \(W\), enumerate its five present vertices and the ten absent vertices. Replacing one present vertex of \(W\) by one absent one gives exactly all possible one-token jumps, and retains an exchange edge if and only if the resulting complement also belongs to the independently established set of 1,662 successes. The checkers obtain 48,540 ordered adjacencies, hence 24,270 undirected edges. The direct checker performs breadth-first search from **every** one of the 1,662 states and reaches all states, finding eccentricity exactly five in every case and counting all distinct pairs by distance.

For the independent orbit certificate, the natural relabelling action of \(S_6\) preserves zero forcing and token jumps, and is therefore an automorphism action on \(\mathcal Z(G)\). Thus distance multisets and eccentricity are constant on each of the seven orbits. A separate program constructs the exchange adjacency directly on white complements, performs breadth-first search from one representative of **each of the seven** orbits, and finds 1,662 reachable vertices and eccentricity five at every representative. This proves the universal eccentricity statement without requiring 1,662 separate searches. Multiplying each representative's ordered-distance histogram by its orbit size and dividing by two gives the five exact unordered-pair counts tabulated above. The two programs agree on every numerical quantity, including all distances.

Both programs use exact integers and finite loops. Running either program requires only a standard Python interpreter and no external libraries or data. Their assertions are executable exhaustive certificates for this fixed finite graph.

## Verification

From the unpacked directory, run `python3 kg62_direct_check.py` and `python3 kg62_orbit_check.py`. Both print `DIRECT_PASS` or `ORBIT_PASS` after checking all asserted quantities. The original run executed both successfully. The exact common histogram is \((24270,202320,557820,477855,118026)\) for distances one through five. The first checker uses parallel deterministic closure and all-source breadth-first search; the second uses branching forcing recursion and seven-orbit breadth-first search with \(S_6\) certificates. No floating-point operations occur.

## Relationship to prior work

The AIM Minimum Rank – Special Graphs Work Group (2008) introduced ordinary zero forcing. Brešar, Kos and Torres (2019, Section 5) already state \(\gamma^Z_{\mathrm{gr}}(\mathrm{KG}(6,2))=5\), equivalently \(Z(\mathrm{KG}(6,2))=10\). Hence this scalar value is prior knowledge, not a new component of the claim. Boyer and collaborators (2018) introduced the general zero forcing polynomial, whose coefficient at ten would count the minimum sets; their examined paper does not provide this graph's coefficient or seven-orbit classification. Geneson, Haas and Hogben (2020) introduced the same one-token-jump reconfiguration graph, giving general results and examples but not the particular Kneser-graph census or the uniform eccentricity-five result. The current result supplies the object-specific full enumeration and metric.

## Limitations

This theorem concerns exactly \(\mathrm{KG}(6,2)\), not all Kneser graphs or other zero forcing variants. It is a rigorously finite computational classification supported by two readable exhaustive programs, not a short closed-form infinite-family theorem. Absolute novelty cannot be guaranteed against unpublished, unindexed, or inaccessible computations. The original 2008 primary source's complete text was not accessed during the literature comparison, although its published description and date were checked; the more directly relevant 2018, 2019, and 2020 full texts were examined. An independent third-party scientific audit has not been performed.

## References

1. AIM Minimum Rank – Special Graphs Work Group, *Zero forcing sets and the minimum rank of graphs*, Linear Algebra and its Applications 428 (2008), 1628–1648, doi:10.1016/j.laa.2007.10.009.
2. B. Brešar, T. Kos, and P. D. Torres, *Grundy domination and zero forcing in Kneser graphs*, Ars Mathematica Contemporanea 17 (2019), 419–430, doi:10.26493/1855-3974.1881.384.
3. K. Boyer and collaborators, *The zero forcing polynomial of a graph*, arXiv:1801.08910 (2018), doi:10.1016/j.dam.2018.11.033.
4. J. Geneson, R. Haas, and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020), doi:10.1016/j.dam.2023.01.027.
