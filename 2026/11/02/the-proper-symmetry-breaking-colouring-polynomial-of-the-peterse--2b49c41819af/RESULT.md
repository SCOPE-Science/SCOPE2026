# The proper symmetry-breaking colouring polynomial of the Petersen graph

## Finding

Let \(P=KG(5,2)\), the Petersen graph whose ten vertices are the two-element subsets of \(\{0,1,2,3,4\}\), adjacent exactly when disjoint. For every integer \(q\geq0\), let \(D_P(q)\) count *proper distinguishing* vertex colourings \(c:V(P)\to\{1,\ldots,q\}\): adjacent vertices have different colours, and the only automorphism preserving every named colour is the identity. Colours need not all appear.

Then the complete symmetry-breaking colouring polynomial is

\[
\boxed{D_P(q)=q(q-1)(q-2)(q-3)(q^6-9q^5+40q^4-120q^3+229q^2-277q+164).}
\]

Equivalently, with \((q)_{\underline{k}}=q(q-1)\cdots(q-k+1)\),

\[
D_P(q)=160(q)_{\underline4}+1844(q)_{\underline5}+2745(q)_{\underline6}+1425(q)_{\underline7}+315(q)_{\underline8}+30(q)_{\underline9}+(q)_{\underline{10}}.
\]

The coefficients count proper partitions of the ten graph vertices into exactly \(k\) nonempty independent colour classes having no nonidentity automorphism preserving each class.

In particular, \(D_P(3)=0\), \(D_P(4)=3840\), and \(D_P(5)=240480\). There are exactly \(12960\) proper colourings from four named colours, so precisely \(8/27\) of these are distinguishing. Among the \(520\) proper partitions into exactly four nonempty colour classes, exactly \(160\) are distinguishing. They form precisely two orbits of the natural \(S_5\) action on *unlabelled colour classes*: one orbit of \(40\) partitions with class-size pattern \((4,2,2,2)\), and one of \(120\) partitions with pattern \((3,3,2,2)\).

If a proper \(q\)-colouring is selected uniformly at random, the probability that it has a nontrivial colour-preserving automorphism satisfies

\[
1-\frac{D_P(q)}{\chi_P(q)}=\frac{10}{q^3}+O(q^{-4})\qquad(q\to\infty),
\]

where \(\chi_P(q)\) is the ordinary chromatic polynomial. The coefficient \(10\) comes from the ten transpositions of the underlying five symbols.

## Assumptions and scope

All vertices and all available palette colours are distinguished labels. A colour-preserving graph automorphism fixes every named colour, not merely the *set* of colour classes. The graph is the specific ten-vertex \(KG(5,2)\), not an arbitrary Kneser graph or a generalized Petersen family. The polynomial counts all proper colourings with palette \(\{1,\ldots,q\}\), including ones using fewer than \(q\) colours. The two orbit types above refer to partitions into exactly four nonempty classes, with colour names forgotten; each such partition yields \(4!\) proper colourings using all four colours.

## Proof

**Automorphism group.** An independent set in \(KG(5,2)\) is a family of pairwise-intersecting two-element subsets of a five-set. If an intersecting family of pairs has no common symbol, then it contains a triangle of pairs, and no further pair can intersect all three. Hence every independent set of size four is a star \(I_a=\{\{a,b\}:b\ne a\}\). There are exactly five such sets. Every automorphism permutes the five stars, and the vertex \(\{a,b\}\) is their unique common member \(I_a\cap I_b\). Thus the automorphism acts faithfully on the stars, giving an injection into \(S_5\). Conversely, all \(120\) permutations of the five symbols act as automorphisms. Hence \(\operatorname{Aut}(P)\cong S_5\).

**Colour-class reduction.** A proper colouring using exactly \(k\) colours determines an unordered partition of the vertex set into \(k\) nonempty independent sets. Conversely, every such partition gives \((q)_{\underline{k}}\) named \(q\)-palette colourings by choosing distinct colours for its blocks. An automorphism preserves the colouring if and only if it fixes each block setwise. Let \(a_k\) be the number of these partitions whose common setwise stabilizer in \(S_5\) is trivial. It follows *for every integer* \(q\ge0\) that \(D_P(q)=\sum_{k=0}^{10}a_k(q)_{\underline{k}}\).

**Exhaustive coefficient certificate.** The following finite recursion is complete and duplicate-free. Write subsets of the ten vertices as ten-bit masks. Given a nonempty mask \(U\) of unassigned vertices, take its least-indexed vertex \(v\). For each independent nonempty mask \(B\subseteq U\) containing \(v\), create block \(B\) and recurse on \(U\setminus B\). At \(U=\varnothing\), test all \(120\) permutations of the underlying five symbols and count those fixing every recorded block. Every partition has a *unique* block containing \(v\), so every proper partition appears exactly once. Exhaustive output is the following stabilizer-size table; its entries sum to \(7430\).

| Number \(k\) of blocks | Stabilizer order 1 | Stabilizer order 2 | Stabilizer order 6 | Total |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 0 | 0 | 20 | 20 |
| 4 | 160 | 350 | 10 | 520 |
| 5 | 1844 | 400 | 0 | 2244 |
| 6 | 2745 | 120 | 0 | 2865 |
| 7 | 1425 | 10 | 0 | 1435 |
| 8 | 315 | 0 | 0 | 315 |
| 9 | 30 | 0 | 0 | 30 |
| 10 | 1 | 0 | 0 | 1 |

There are no proper partitions with fewer than three blocks. Summing the stabilizer-one column gives the falling-factorial formula in the Finding, and elementary polynomial multiplication gives its displayed factorization.

**Exactly four classes.** To obtain the complete orbit certificate, transform every four-block partition by all \(120\) symbol permutations, sort the resulting block masks, and mark the resulting orbit. The full orbit table, grouped by (block-size pattern, orbit size, colour-preserving stabilizer order), is:

| Block sizes | Orbit size | Stabilizer order | Number of such orbits |
| --- | ---: | ---: | ---: |
| \((3,3,2,2)\) | 30 | 2 | 1 |
| \((3,3,2,2)\) | 60 | 2 | 2 |
| \((3,3,2,2)\) | 120 | 1 | 1 |
| \((3,3,3,1)\) | 10 | 6 | 1 |
| \((3,3,3,1)\) | 20 | 2 | 1 |
| \((3,3,3,1)\) | 60 | 2 | 1 |
| \((4,2,2,2)\) | 40 | 1 | 1 |
| \((4,3,2,1)\) | 60 | 2 | 2 |

Thus there are ten orbits comprising all \(520\) four-block partitions. Exactly the \(40\)- and \(120\)-member orbits have trivial *individual colour-class* stabilizers. Note that the 40-member orbit has an unlabelled-partition stabilizer of order three which cyclically permutes colour classes; this does *not* preserve their named colours and is not a contradiction.

**High-palette asymptotic.** The ordinary Petersen chromatic polynomial is

\[
\chi_P(q)=q(q-1)(q-2)(q^7-12q^6+67q^5-230q^4+529q^3-814q^2+775q-352).
\]

Subtracting the verified exact \(D_P(q)\) gives

\[
\chi_P(q)-D_P(q)=10q(q-1)(q-2)(q^4-6q^3+15q^2-22q+14).
\]

Since the leading degrees are \(10\) and \(7\), respectively, the asserted failure probability follows. Structurally, among the \(119\) nonidentity permutations of the five base symbols, exactly the ten transpositions have seven vertex-orbits on the ten pairs; every other permutation has at most six. A colouring fixed by a transposition has at most seven freely chosen orbit colours, giving the leading degree, and simultaneous invariance under two distinct transpositions imposes at least four independent equalities. This independently identifies the leading coefficient as ten.

## Verification

The package includes two complete executable standard-library Python verifiers. Run from the containing directory with `python3 verify/independent_blocks.py` and `python3 verify/restricted_growth.py`.

The first enumerates all independent vertex masks, uses the least-unassigned-vertex recursion above, computes the stabilizer order of every proper partition, and independently builds the ten four-class symmetry orbits. The second generates canonical restricted-growth colour words with adjacency pruning, checks every automorphism for every completed word, and *separately* enumerates all proper assignments from four named colours without canonicalization. It also reconstructs both the ordinary chromatic polynomial and the new symmetry-breaking polynomial by integer polynomial arithmetic, and checks every possible symbol permutation's cycle-orbit count. Both execute without external libraries or input data.

These are exhaustive enumerations: each recursion covers all of its explicitly specified finite domain. The argument makes no claim about arbitrary-order Kneser graphs or other palette-counting problems.

## Relationship to prior work

Collins and Trenk (2006, Theorem 2.5) proved \(\chi_D(P)=4\), including a symmetry-breaking four-colouring and the obstruction for three colours. Their theorem is *not* a new result here; it follows as a covered corollary of the coefficient table. Weigand and Jacobson (2008), and Lal and Bhattacharjya (2009), investigated distinguishing chromatic numbers of generalized Petersen graphs, principally identifying thresholds and constructions. Arvind, Cheng, and Devanur (2008) developed general counting methods for distinguishing vertex labellings without the proper-colouring restriction. The ordinary Petersen chromatic polynomial is classical and is an independent consistency check, not a new claim.

The added information is the *complete proper distinguishing counting polynomial*, every exact colour-class stabilizer count, the two distinguished four-block symmetry types, and the asymptotic failure probability. Previously published orbit or recolouring counts for proper four-colourings do not alone specify the colour-preserving stabilizers for all numbers of classes, and do not yield the full variable-palette polynomial without the present class-by-class analysis.

## Limitations

This is a specific finite graph theorem with an exhaustive, reproducible counting proof and a short group-theoretic reduction; it is not a general formula for the generalized Petersen family. Although the most closely related available full texts were inspected, no bibliographic search can exclude every unindexed historical table or unpublished computation of the same polynomial. No independent external validation has been performed.

## References

- K. L. Collins and A. N. Trenk, *The Distinguishing Chromatic Number*, Electronic Journal of Combinatorics 13 (2006), R16, Theorem 2.5. DOI: 10.37236/1042. Publicly published February 15, 2006.
- J. Weigand and M. S. Jacobson, *Distinguishing and Distinguishing Chromatic Numbers of Generalized Petersen Graphs*, AKCE International Journal of Graphs and Combinatorics 5 (2008), 199–211. DOI: 10.1080/09728600.2008.12088865.
- A. K. Lal and B. Bhattacharjya, *Breaking the Symmetries of the Book Graph and the Generalized Petersen Graph*, SIAM Journal on Discrete Mathematics 23 (2009), 1200–1216. DOI: 10.1137/080728640.
- V. Arvind, C. T. Cheng and N. R. Devanur, *On Computing the Distinguishing Numbers of Planar Graphs and Beyond: A Counting Approach*, SIAM Journal on Discrete Mathematics 22 (2008), 1297–1324. arXiv:math/0703927.
- P. J. Cameron, *Counting colourings of graphs*, April 12, 2012, for the classical Petersen chromatic polynomial: https://cameroncounts.wordpress.com/2012/04/12/counting-colourings-of-graphs/.
