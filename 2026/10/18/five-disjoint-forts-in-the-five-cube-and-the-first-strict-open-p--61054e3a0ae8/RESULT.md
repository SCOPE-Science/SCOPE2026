# Five disjoint forts in the five-cube and the first strict open-packing separation

## Finding

**Theorem.** In the five-dimensional binary hypercube \(Q_5\), the maximum number of pairwise vertex-disjoint nonempty forts is exactly
\[
\operatorname{ft}(Q_5)=5.
\]
Its open-packing number is \(\rho^{o}(Q_5)=4\). Consequently, \(Q_5\) is the first binary hypercube of dimension \(2\) through \(5\) for which \(\operatorname{ft}(Q_d)>\rho^{o}(Q_d)\). In particular, the previously established interval \(4\le\operatorname{ft}(Q_5)\le6\) is resolved.

## Assumptions and scope

All graphs are finite, simple, and undirected. The vertex set of \(Q_5\) is \(\{0,1\}^{5}\), adjacent when the two binary vectors have Hamming distance one. For an integer-labelled vertex between \(0\) and \(31\), binary XOR with \(1,2,4,8,16\) lists its neighbors. An **open neighborhood** \(N(v)\) is the set of five neighbors of \(v\). A nonempty vertex set \(F\) is a **fort** if every vertex outside \(F\) has either zero or at least two neighbors inside \(F\). The **fort number** \(\operatorname{ft}\) is the maximum number of pairwise disjoint forts, whereas \(\rho^{o}\) is the maximum number of vertices with pairwise disjoint open neighborhoods. Parity refers to Hamming-weight parity.

## Proof

**1. The size-five threshold.** Every fort in \(Q_5\) has at least five vertices, and the five-vertex forts are exactly the 32 open neighborhoods. This is also the dimension-five specialization of Brimkov--Cameron--Grubbs, Corollary 3.10 and Theorem 3.8 [2]. For an independent, self-contained finite verification, the accompanying `verify.py` exhausts all \(242824\) subsets of sizes one through five: there are no forts below size five and precisely 32 of size five, equal to the set of all \(N(v)\). The explicit bitwise predicate in that file is precisely the definition of a fort; this finite exhaustive statement does not depend on numerical tolerances.

**2. At most four disjoint neighborhoods.** Two distinct vertices have intersecting open neighborhoods if and only if their Hamming distance is two. Within one parity class, the only allowed distance between distinct centers of disjoint neighborhoods is therefore four. Any three vertices of a fixed parity cannot all be pairwise distance four: translate the first to zero, leaving two distinct weight-four vectors in five coordinates, whose mutual Hamming distance is two. Thus there are at most two centers of each parity, giving \(\rho^{o}(Q_5)\le4\). The four neighborhoods \(N(0),N(1),N(30),N(31)\) are pairwise disjoint because their centers have mutual distances one, four, or five. Hence \(\rho^{o}(Q_5)=4\).

**3. Five disjoint forts.** Consider the four size-five forts just listed and an eight-element set
\[
F=\{6,7,10,11,20,21,24,25\}.
\]
In the decomposition \(Q_5=Q_4\mathbin{\square}K_2\), this is \(T\times\{0,1\}\), where \(T=\{3,5,10,12\}\) in the four-bit coordinates. Every odd-weight vertex in \(Q_4\) has exactly two neighbors in \(T\), while every even-weight vertex outside \(T\) has none; thus \(F\) is a fort. Its four-bit projections all have weight two. By contrast, the projections of \(N(0)\cup N(1)\) have weights zero or one, and those of \(N(30)\cup N(31)\) have weights three or four. Therefore the five displayed forts are pairwise disjoint, so \(\operatorname{ft}(Q_5)\ge5\).

**4. Structure of six-vertex forts.** Write \(F_0,F_1\) for the even- and odd-parity vertices of a six-element fort \(F\). Its parity profile \((|F_0|,|F_1|)\) must belong to
\[
\{(0,6),(1,5),(5,1),(6,0)\}.
\]
To see this, if \(A\) consists of two vertices of one parity, their five-neighbor sets have intersection of size zero or two. Therefore at least six opposite-parity vertices are adjacent to exactly one vertex of \(A\) and would have to lie in \(F\). Four selected opposite-parity vertices cannot suffice. If \(A\) consists of three same-parity vertices, consider their 15 incident edges to the opposite parity. Each of the three pairs shares zero or two neighbors. If not all three pairs share two, at least seven opposite-parity vertices are adjacent to exactly one member of \(A\); if all three pairs share two, there is one common neighbor of all three, and exactly six opposite-parity vertices have a unique neighbor in \(A\). Again, selecting only three opposite-parity vertices is impossible. Interchanging parities rules out the reverse profiles. If \(|F_0|=1\), its one even vertex \(u\) requires all five odd neighbors in \(F\), so \(F=N(u)\cup\{u\}\). The analogous statement holds for \(|F_1|=1\).

**5. Six disjoint forts are impossible.** Suppose six disjoint forts exist. Every fort has size at least five. There must be at least four five-vertex forts: otherwise the total number of selected vertices would be at least \(3\cdot5+3\cdot6=33>32\). By step 1, these are neighborhoods. Step 2 rules out five or more such neighborhoods, so exactly four of the six forts have size five. The remaining two have size exactly six, and all 32 vertices are covered.

Let the four neighborhood centers be \(a,b\) of even parity and \(p,q\) of odd parity. Step 2 forces the distance between \(a,b\), and also between \(p,q\), to be four. Their neighborhoods cover ten vertices of each parity, leaving a residual set \(R\) of precisely six even and six odd vertices. Any fort of size six inside \(R\) of mixed parity would, by step 4, contain a full neighborhood \(N(u)\), which would be disjoint from the four existing neighborhoods. This contradicts step 2. Thus a residual six-fort would have to be **all six remaining vertices of one parity**.

That is impossible as well. For the six remaining even vertices, take an odd vertex \(z\) differing from \(p\) in exactly two of the four coordinates on which \(p\) and \(q\) differ. Then \(z\) has distance two from each of \(p,q\). Therefore \(N(z)\) meets each of \(N(p)\), \(N(q)\) in exactly two even vertices; these four neighbors are distinct because \(N(p)\) and \(N(q)\) are disjoint. Of the five even neighbors of \(z\), exactly one lies in the six remaining even vertices. So these six do not form a fort. Exchanging parity and using \(a,b\) rules out the remaining six odd vertices. Hence no six-fort partition exists, giving \(\operatorname{ft}(Q_5)\le5\), as required.

For \(d=2,4\), equality between fort and open-packing numbers is Theorem 3.13 / Corollary 3.14 of [2]. For \(d=3\), the minimum fort size is three, so at most two disjoint forts fit into eight vertices; two opposite neighborhoods attain two. This establishes the asserted first strict separation.

## Verification

Run `python3 verify.py` using only the Python standard library. It checks all \(242824\) subsets of sizes one through five, all size-six subsets to classify their parity profiles, the five explicitly displayed forts, and all choices of open-packing centers through cardinality five. The expected final line is `VERIFY_OK`; complete captured output is included in `verification_output.txt`. The upper bound for fort packings is the proof above and is not inferred merely from testing a restricted family of packings.

## Relationship to prior work

Cameron, Hogben, Kenter, Mojallal and Schuerger [1] introduced the fort-number framework and established \(\operatorname{Z}^{*}(Q_d)=2^d/d\), but not \(\operatorname{ft}(Q_5)\). Brimkov, Cameron and Grubbs [2] classified minimum forts in hypercubes (Theorem 3.8) and proved general fort-number bounds (Corollary 3.12), which give exactly \(4\le\operatorname{ft}(Q_5)\le6\); their exact theorem concerns powers-of-two dimensions. The present result selects the middle value, explains the obstruction to six forts, and separates fort packings from open-neighborhood packings. No claim of first discovery of the definition, the minimum-fort classification, or the power-of-two theorem is made.

## Limitations

This theorem concerns exactly the five-dimensional binary hypercube and makes no assertion about the fort number in larger non-power-of-two dimensions. Searches of the specified primary sources and accessible indexed records did not identify an earlier exact value, but cannot rule out unindexed equivalent work.

## References

[1] T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904, first publicly posted 2023-10-27; https://arxiv.org/abs/2310.17904 . Full accessible manuscript v3 examined, especially Proposition 3.15 and the summary of known parameters.

[2] B. Brimkov, T. R. Cameron, and O. Grubbs, *On the forts and related parameters of the hypercube graph*, arXiv:2507.10826v1 (2025-07-14), Theorem 3.8, Corollaries 3.10 and 3.12, and Theorem 3.13; https://arxiv.org/html/2507.10826v1 .
