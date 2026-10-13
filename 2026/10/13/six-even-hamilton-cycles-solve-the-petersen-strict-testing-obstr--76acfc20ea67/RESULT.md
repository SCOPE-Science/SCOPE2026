# Six even Hamilton cycles solve the Petersen strict-testing obstruction

## Finding

For the Petersen graph \(G=KG(5,2)\) with vertices the ten two-element subsets of \([5]\) and edges the fifteen disjoint pairs, the minimum number of nonadaptive *strict* group tests on the candidate graph is exactly six. Equivalently, the complements of its fifteen edges have set-basis number six, or its associated candidate-incidence matrix has zero-cover number six.

Consequently, for every integer \(m\ge5\) and every \(n\le\binom m3+6\), the strict two-stage group-testing number for at most two defectives satisfies
\[
t(n,2,2)\le m+6.
\]
The local six-test result is exact; the two-stage bound is an upper bound, not a claim of global optimality.

## Assumptions and scope

A pool returns positive exactly when it contains a defective element. *Strict* group testing must recover the entire defective set when it has cardinality at most two, and report that there are more than two defectives otherwise. A stage consists of pools tested in parallel; second-stage pools may depend on all first-stage outcomes. The candidate graph has a vertex for each remaining candidate element and an edge for each size-two defective set consistent with the first-stage outcomes.

For a family of second-stage pools \(Q_1,\ldots,Q_r\) to solve a candidate graph strictly, the necessary and sufficient condition is: for each candidate edge \(C\) and each vertex \(w\notin C\), some \(Q_i\) contains \(w\) but avoids \(C\). This criterion is Corollary 5 of the cited work, and also follows by comparing outcomes on \(C\) versus \(C\cup\{w\}\).

## Proof

**1. A six-pool Petersen design.** Identify each Petersen vertex with an edge of \(K_5\). An undirected Hamilton five-cycle of \(K_5\) is called *even* when an orientation of its cyclic order, written as a permutation of \(0,1,2,3,4\), is even. This is well-defined: a rotation or reversal of a five-term cyclic order is even. Exactly six of the twelve undirected Hamilton cycles are even. For each such cycle, make one pool comprising its five \(K_5\) edges.

We show that for any two disjoint \(K_5\) edges \(e,f\) and any third edge \(w\ne e,f\), an even five-cycle contains \(w\) but neither \(e\) nor \(f\). The alternating group \(A_5\) is transitive on unordered pairs of disjoint edges: their fifteen possibilities have a stabilizer of size four. Normalize to \(e=01\) and \(f=23\). The four-element stabilizer has precisely three orbits on the remaining eight edges, represented by \(02\), \(03\), and \(04\) (the first two orbits have size two and the third has size four). For \(w=02\), the even cycle with order \(0,2,1,4,3\) is a witness. For either \(w=03\) or \(w=04\), the even cycle with order \(0,3,1,2,4\) is a witness. Both cycles avoid \(01\) and \(23\). Transport by the stabilizer and then by \(A_5\), which preserves the set of even cycles, to establish the assertion for every \((e,f,w)\). The strict-pool criterion proves that six tests suffice.

**2. Six is the minimum.** Every candidate edge of the Petersen graph gives a binary outcome vector for any fixed family of \(r\) pools. The fifteen such vectors are pairwise incomparable under coordinatewise inclusion: for two different candidate edges \(C,D\), apply the strict-pool criterion to a vertex in \(D\setminus C\), and again with the roles reversed. Sperner's theorem then gives \(15\le\binom r{\lfloor r/2\rfloor}\). The inequality fails for \(r\le5\), because \(\binom52=10\). Therefore \(r\ge6\), establishing exactness.

**3. A strict two-stage construction.** For each three-subset \(T\subseteq[m]\), create one item and include it in exactly the three indexed first-stage pools belonging to \(T\). Add six further items that occur in no first-stage pool (called *zero-incidence items*). Let \(Y\subseteq[m]\) be the set of positive first-stage pool indices. Every defective three-subset item contributes three indices, so \(|Y|\notin\{0,3,4,5,6\}\) implies more than two defectives. The remaining cases have at most six second-stage pools:

- If \(|Y|=0\) or \(3\), individually test the six zero-incidence items. In the latter case the unique three-subset item with incidence \(Y\) is known defective.
- If \(|Y|=4\), there are four eligible three-subset items. Test each individually in four pools, including *all six zero-incidence items in each pool*. Every candidate of at most two defectives consists of two of the four three-subset items; their singleton signatures distinguish them, while any additional defective item is detected.
- If \(|Y|=5\), the ten eligible three-subset items correspond to the two-subsets \(e=Y\setminus T\). Exactly the pairs of disjoint \(e,f\) are candidates of cardinality two: their candidate graph is \(KG(5,2)\). Use the six even five-cycle pools of part 1 and include all six zero-incidence items in every pool. The strict-pool criterion covers every eligible three-subset item outside each candidate pair. It also covers each zero-incidence item because, for every candidate pair, some cycle avoids both edges (for example by applying the criterion to any of the eight other eligible items). Thus all candidate pairs can be identified and all larger defective sets rejected.
- If \(|Y|=6\), the twenty eligible three-subset items split into ten complementary pairs. The ten possible candidate pairs are exactly these complementary pairs. Assign them the ten distinct binary strings of length five and weight two; give both items in a complementary pair the corresponding column, and include all six zero-incidence items in every test. An eligible third item has a different weight-two column, possessing a one in some position where a given candidate-pair column has zero. Each zero-incidence item also has such a one. Thus five tests satisfy the strict-pool criterion.

For \(|Y|\ge7\), strict rejection needs no second-stage test because two three-subset items cannot activate more than six indices. The construction therefore uses at most \(m+6\) tests. Deleting any subset of items from a strict design preserves strict identification on the remaining items, proving the bound for every smaller \(n\).

## Verification

Run `python3 verify.py` with Python 3 and its standard library. The verifier enumerates the six even Hamilton cycles, checks all \(15\cdot8=120\) Petersen separation triples, and independently executes a complete exhaustive two-stage decoding check over all \(2^{16}=65,536\) defective sets at \(m=5\). It also checks all \(17,902\) defective sets of weight at most four at \(m=6\), including every size-zero, -one and -two case. Expected final line: `VERIFY_OK petersen_min=6 two_stage_m5=65536 two_stage_m6_weight_le4`.

These finite tests corroborate the proof; the arbitrary-\(m\) conclusion rests on the preceding combinatorial argument and does not rely on an extrapolation of a finite experiment.

## Relationship to prior work

Damaschke, Sheikh Muhammad and Wiener established the strict candidate-hypergraph criterion (their Theorem 1 and Corollary 5), and used the Petersen candidate graph in Proposition 16 to prove \(t(n,2,2)\le m+7\) for \(n\le\binom m3+7\). Their Lemma 17 supplies seven pools for this graph via a five-edge matching. Here the *same* Petersen obstruction is solved exactly with six different pools, built from even Hamilton cycles; this tight local result reduces their number of second-stage tests by one while retaining six zero-incidence items. The original seven-pool construction and its broader framework remain prior art.

## Limitations

The theorem does not assert \(t(n,2,2)=m+6\) or determine its optimum for each \(n\); it proves a local optimum and a general construction-based bound. It does not classify every six-pool strict Petersen design. A search cannot rule out an unindexed earlier equivalent design; any such priority question requires continued independent bibliographic checking.

## References

P. Damaschke, A. Sheikh Muhammad and G. Wiener, *Strict group testing and the set basis problem*, Journal of Combinatorial Theory, Series A **126** (2014), 70–91. DOI: `10.1016/j.jcta.2014.04.005`. Open original full text: https://research.chalmers.se/publication/198643/file/198643_Fulltext.pdf. Available online May 8, 2014.
