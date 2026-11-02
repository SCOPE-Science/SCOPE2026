# Static and adaptive shattering for exact two-literal disjunctions through twelve coordinates

## Finding
For every integer \(n\ge 2\), let \(\mathcal H_n\) be the class of Boolean functions on \(\{0,1\}^n\) of the form \(h_{ij}(x)=x_i\lor x_j\), where \(1\le i<j\le n\). Coordinates are distinct, and queries may be arbitrary Boolean vectors. The complete dimensions for \(2\le n\le12\) are:

| \(n\) | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| \(\operatorname{VCdim}(\mathcal H_n)\) | 0 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 4 | 4 | 5 |
| \(\operatorname{Ldim}(\mathcal H_n)\) | 0 | 1 | 2 | 3 | 3 | 4 | 4 | 4 | 5 | 5 | 5 |

There is also an unrestricted structural statement: a fixed collection of \(d\ge1\) queries is shattered if and only if its \(n\) coordinate-column patterns \(c_1,\ldots,c_n\in\{0,1\}^d\) satisfy
\[
\{c_i\lor c_j:1\le i<j\le n\}=\{0,1\}^d,
\]
where \(\lor\) acts coordinatewise. The minimum possible numbers of coordinates for shattering \(d=1,2,3,4,5\) queries are respectively \(3,4,6,8,12\).

The first strict static/adaptive separation is at \(n=5\). There are further separations at \(n=7,10,11\), but not at \(n=8,9,12\). The cardinality upper bound for Littlestone dimension first fails at \(n=9\), and fails again at \(n=12\): the dimension is respectively \(4<5\) and \(5<6\), even though the numbers of hypotheses are \(36\) and \(66\). No claim is made about dimensions beyond twelve coordinates.

## Assumptions and scope
The ground set has exactly \(n\) labeled coordinates and one hypothesis for each *unordered pair of distinct coordinates*. Every input vector is an admissible query. A shattered static set is a set of distinct query vectors with all binary answer words realized. A complete adaptive tree of depth \(d\) has one query at each internal node, with a separate hypothesis realizing every root-to-leaf answer sequence. The value for a one-hypothesis concept class is dimension zero. The statements concern deterministic, noiseless, exact membership answers, and are not claims about worst-case identification algorithms or average test counts in group testing.

## Proof
**Column characterization.** On \(d\) chosen queries, concatenate the responses of coordinate \(i\) into \(c_i\in\{0,1\}^d\). For hypothesis \(h_{ij}\), the complete response word is precisely \(c_i\lor c_j\). Thus all \(2^d\) words occur exactly when the displayed pairwise-OR equality holds. Conversely, any chosen column patterns define \(d\) queries by using the coordinate patterns as the columns of a Boolean matrix. This proves both directions for all \(d,n\).

**Sharp first five static thresholds.** To express the all-zero word, there must be at least two zero columns. To express each unit word \(e_r\), there must be a column equal to \(e_r\). Hence any basis has two zeros and \(d\) distinct unit columns among its coordinates. These \(d+2\) obligatory columns already express every word of weight at most two, and no higher-weight word. For \(d=1,2\), they suffice. For \(d=3\), a sixth column is necessary and sufficient. For \(d=4\), one extra column yields at most two distinct weight-three words, short of the four required; two extra columns suffice.

For \(d=5\), the five unit columns and two zero columns leave ten weight-three words to realize. Suppose there were at most four additional columns. If all four have weight two, no pairwise OR has weight five, so the all-ones word is absent. Otherwise, let \(a\le3\) of the additional columns have weight two. Each such column can produce at most three of the ten weight-three words by OR with a unit column. Two additional weight-two columns cannot generate a new triple beyond these, since any triple they produce already contains either of the two weight-two supports. Each additional column of weight three can contribute at most its own triple, while columns of weight four or five contribute none. When \(a\le2\), the resulting upper bound is \(3a+(4-a)\le8\). When \(a=3\), the three two-subsets cannot be pairwise disjoint on five coordinates; therefore two share a coordinate and their families of three-containing triples overlap. The three columns cover at most eight distinct triples, and the fourth column contributes at most one: again fewer than ten. Duplicate zero/unit columns cannot help. Hence at least five extra columns, i.e. twelve in total, are necessary. The sharp witnesses for all five thresholds are the column lists recorded in `certificates.json`; `verify.py` independently checks all pairwise OR words.

For \(d=6\), the two zero columns and six units provide just \(1+6+\binom62=22\) words. With at most four further columns, each can form at most seven words by OR with the eight obligatory columns (zero yields one and the six units at most six), and the pairs of further columns contribute at most \(\binom42=6\) more words. Thus there are at most \(22+4\cdot7+6=56<64\) words. Hence six queries cannot be shattered with twelve coordinates. These thresholds, together with monotonicity under adding unused coordinates, yield the VC row of the table.

**Adaptive lower bounds.** `certificates.json` gives complete query trees at \((n,d)=(3,1),(4,2),(5,3),(7,4),(10,5)\). Each internal node specifies the queried pool of coordinates. Each of the respectively \(2,4,8,16,32\) leaf paths names a different unordered pair of defective coordinates, and direct evaluation of the associated disjunction agrees with every answer bit on the path. The supplied verifier checks all 62 paths independently against the node queries. Inserting unused coordinates embeds \(\mathcal H_m\) into \(\mathcal H_n\) for \(n\ge m\), giving the lower bounds throughout the table.

**Adaptive upper bounds.** There are exactly \(\binom n2\) distinct hypotheses, hence \(\operatorname{Ldim}(\mathcal H_n)\le\lfloor\log_2\binom n2\rfloor\). This matches the claimed upper bounds except at \(n=9,12\). If a pool leaves \(t\) coordinates unqueried, then exactly \(\binom t2\) hypotheses answer zero and \(\binom n2-\binom t2\) answer one. At depth \(d\) both children of the root must contain at least \(2^{d-1}\) hypotheses. At \(n=9,d=5\) this requires \(16\le\binom t2\le20\), impossible since consecutive nearby triangular numbers are \(15,21\). At \(n=12,d=6\), it requires \(32\le\binom t2\le34\), impossible since consecutive nearby triangular numbers are \(28,36\). These obstructions complete the exact Littlestone row without extrapolation.

## Verification
Run `python3 verify.py certificates.json` in a directory containing the two named files. The checker validates every static column-basis construction, separately exhausts all \(17{,}902\) sets of at most four nontrivial extra columns for the five-query exclusion, validates every node and leaf of all five adaptive trees, tests the root-branch and cardinality upper bounds, and independently recomputes the exact adaptive dimensions through twelve coordinates by a memoized recurrence over concept subsets. Its expected output is included as `checks.txt`. The proof above, not the computer experiment, establishes the unrestricted column criterion and the stated finite upper bounds.

## Relationship to prior work
Exact two-literal disjunctions are also the *exactly-two-defective* noiseless pooled-testing hypotheses: a query is positive when its pool intersects the unknown defective pair. General group-testing bounds and identification strategies are not equivalent to complete adaptive shattering, which requires every binary root-to-leaf transcript of a fixed depth to remain realizable. The survey of Aldridge, Johnson and Scarlett (2019) treats the former and supplies context for pool testing. Guingona, Kolesnikov, Nierwinski and Soucy (2021) establish equality of VC and Littlestone dimensions for the full zero-set family of nonzero linear combinations, not this restricted, nonlinear exact-two-OR family. Cambie, Girão and Kang (2018) study bounds on set families under repeated unions, rather than the fixed pairwise-OR completeness threshold of arbitrary coordinate columns. Chase, Freitag and Reyzin (2023) develop broad Littlestone-based query-learning/compression theorems, not these exact finite dimensions.

## Limitations
All exact numerical dimensions are restricted to \(2\le n\le12\). The reduction to pairwise-OR bases is valid for every \(n,d\), but the minimal basis sizes are established only through \(d=5\). The finite certificates were checked computationally and in the accompanying proof; no independent external audit has occurred. Earlier terminology from combinatorial group testing, Boolean OR-bases, thicket dimension, or sparse-disjunction learning may conceal unlocated priority. A general zero-error group-testing identification algorithm must not be confused with a shattered complete answer tree.

## References
1. Guingona, Kolesnikov, Nierwinski, Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, originally submitted 2021-09-10. https://arxiv.org/abs/2109.04805
2. Aldridge, Johnson, Scarlett, *Group Testing: An Information Theory Perspective*, arXiv:1902.06002, first submitted 2019-02-15. https://arxiv.org/abs/1902.06002
3. Cambie, Girão, Kang, *VC dimension and a union theorem for set systems*, arXiv:1808.02352, first submitted 2018-08-07. https://arxiv.org/abs/1808.02352
4. Chase, Freitag, Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812, first submitted 2023-10-07. https://arxiv.org/abs/2310.04812
