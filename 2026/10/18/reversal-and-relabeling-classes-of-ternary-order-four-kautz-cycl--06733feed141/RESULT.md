# Reversal and relabeling classes of ternary order-four Kautz cycles

## Finding
A ternary order-four Kautz cycle is a cyclic word of length \(24\) on \(\{0,1,2\}\) whose \(24\) length-four cyclic factors are exactly the words having unequal adjacent symbols. There are \(384\) such cycles up to rotation, as also follows from the classical Kautz enumeration theorem. Exactly **\(24\)** of these cycles are equivalent to their reversals under rotation. Thus there are exactly **\(204\)** classes under rotation and reversal. Global permutations of the three symbols split the \(384\) cycles into \(64\) classes; adding reversal leaves **\(34\)** classes. Precisely four of the \(64\) symbol-permutation classes are reversal-fixed; each consists of six individually reversal-fixed cycles.

The following four words, considered as cyclic words, are representatives of all reversal-fixed cycles modulo global symbol permutation:

```
010102021021210121201202
010102021210210120121202
010102102021210121202012
010102121020210120201212
```

There is also an all-alphabet obstruction: for every alphabet size \(q\ge3\) and order \(k\ge3\), a maximal Kautz cycle can be rotation-equivalent to its reversal only if \(q\) is odd and \(k\) is even. This necessary condition does not assert existence at every permitted pair.

## Assumptions and scope
A proper length-\(k\) word has unequal neighboring symbols. A maximal Kautz cycle is a cyclic word in which every proper length-\(k\) word occurs as a factor exactly once and no other length-\(k\) factor occurs. Rotation acts on positions, reversal reverses reading order, and global symbol permutation acts simultaneously on all positions. The full exact census concerns \(q=3\), \(k=4\). The parity obstruction concerns every \(q\ge3\) and \(k\ge3\), conditional on existence. Reversal is **not** combined with complementation or symbol exchange unless explicitly stated by the separate relabeling quotient.

## Proof
The Kautz overlap digraph has proper length-three words as its \(12\) vertices and proper length-four words as its \(24\) directed edges. The edge for \(a b c d\) goes from \(a b c\) to \(b c d\). Each vertex has two incoming and two outgoing edges. Kautz cycles up to rotation correspond bijectively to Eulerian circuits in this graph: read the first symbol of each traversed edge. Since the edge `0101` occurs exactly once, fixing it as the first edge removes rotational ambiguity.

Every Eulerian circuit selects a bijection between the two incoming edges and the two outgoing edges at each vertex. There are two local bijections at each of \(12\) vertices, hence \(2^{12}=4096\) complete transition systems. Such a system decomposes the edge set into disjoint directed cycles; it yields an Eulerian circuit precisely when the orbit of edge `0101` uses all \(24\) edges and returns to `0101`. Exhaustively trying the \(4096\) systems and applying this explicit finite predicate gives exactly \(384\) qualifying systems, all with distinct anchored cyclic words.

Independently, depth-first enumeration of unused edges, starting with `0101` and accepting only closed tours after \(24\) edges, produces the **same set of \(384\)** anchored words. This is an independent complete finite search because every Euler tour has a unique unused-edge traversal sequence rooted at that edge. For each generated word \(w\), check all \(24\) cyclic length-four windows. They are exactly the prescribed proper words.

For any cyclic word \(w\), let \(\operatorname{rotmin}(w)\) be the lexicographically least rotation. A cycle is reversal-fixed exactly when \(\operatorname{rotmin}(w)=\operatorname{rotmin}(w^{\mathrm{rev}})\). Applying that exact predicate to the \(384\) exhaustive words yields \(24\) fixed cycles. The remaining \(360\) fall into \(180\) reversal pairs, so Burnside's lemma yields \(24+180=204\) bracelets. For the alphabet-permutation census, calculate the least rotation after each of the six global permutations, optionally also after reversal. Exact set cardinalities are \(64\) without reversal and \(34\) with reversal; the \(24\) reflective cycles occupy exactly the four displayed permutation orbits, each of cardinality six. The self-contained `verify.py` implements both tour enumerations and all these quotient tests using integer arithmetic and complete finite loops.

For the all-alphabet obstruction, suppose reversal followed by some cyclic rotation fixes a maximal Kautz cycle. This reflection induces an involution of its cyclic windows of any fixed length, with at most two fixed positions, irrespective of the window length. If \(k\ge3\) is odd, there are \(q(q-1)^{(k-1)/2}\ge6\) distinct proper palindromic length-\(k\) words. Each appears exactly once. Its unique occurrence is fixed by the reflection, exceeding the two fixed positions: contradiction. If \(k\ge4\) is even and \(q\) is even, there are \(q(q-1)^{(k-2)/2}\ge4\) proper palindromic length-\((k-1)\) words. Each such word has exactly \(q-1\) occurrences, one for each possible right extension to a proper length-\(k\) word. Since \(q-1\) is odd, reflection acts as an involution on an odd set of occurrences and fixes at least one occurrence of **each** of these distinct palindromes. That again requires more than two fixed window positions. Thus reversal symmetry is possible only when \(k\) is even and \(q\) is odd.

## Verification
Run `python3 verify.py` in the directory containing the extracted file; Python standard library suffices. It independently enumerates \(2^{12}\) local edge transition systems and all anchored depth-first Euler tours, confirms the two resulting \(384\)-element sets coincide, checks every proper length-four factor exactly once, tests reflection, enumerates reversal/rotation classes, and enumerates all global alphabet-relabeling orbits. Successful output begins `VERIFY_OK` and contains all six asserted census numbers. The finite exhaustive loops, not timeouts or samples, establish the exact claims.

## Relationship to prior work
Rosenfeld's 2002 *Enumerating Kautz Sequences*, especially Theorem 9, establishes the total count of maximal Kautz cycles and notes that its original enumeration does not identify sequences under reversal. The total \(384\) is therefore **not** claimed as new. Lin, Ward, Jain, and Skiena (2011) study constructions of orthogonal de Bruijn sequences and Kautz-type enumerations, not this reversal and relabeling census. Burris, Motta, and Shipman (2016) investigate an *unoriented de Bruijn* covering objective in which reading both ways covers orientation-classes; that changes the required coverage and does not supply the number of reversal-symmetric complete Kautz cycles. The contribution here is the exact reflection-fixed and multigroup orbit classification, with the general parity obstruction.

## Limitations
The class enumeration is exhaustive only for the ternary order-four case; no complete class counts at higher orders or larger odd alphabets are asserted. The parity theorem supplies only necessary conditions. The literature comparison does not rule out an unindexed equivalent reversal enumeration. The computations are fully reproducible but have not undergone independent external audit. Exact first public **day** of the 2002 foundational paper was not established; its cited publication year is not converted into an invented day.

## References
Rosenfeld, V. R., *Enumerating Kautz Sequences*, Kragujevac J. Math. 24 (2002), 19–41. https://imi.pmf.kg.ac.rs/kjm/pub/12617301003674_3.pdf

Lin, Y.-L., Ward, C., Jain, B., and Skiena, S., *Constructing Orthogonal de Bruijn Sequences*, WADS 2011, LNCS 6844, 595–606. https://doi.org/10.1007/978-3-642-22300-6_50

Burris, C. S., Motta, F. C., and Shipman, P. D., *An Unoriented Variation on de Bruijn Sequences*, arXiv:1608.08480v1 (2016-08-30). https://arxiv.org/abs/1608.08480
