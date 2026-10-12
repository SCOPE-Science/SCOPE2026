# First coprime-length nonsynchronizing complete binary prefix codes

## Finding

Let \(C\subset\{0,1\}^{+}\) be a **complete binary prefix code**: its finite rooted binary decoding tree is full (each internal node has two ordered children), and no codeword is a proper prefix of another. Call \(C\) *synchronizing* if some finite input word moves the ordinary leaf-reset decoder from **every** internal-tree state to the root. Consider the length-coprime condition
\[
\gcd\{\lvert w\rvert:w\in C\}=1.
\]
Among all such codes with at least two words, the **smallest cardinality admitting failure of synchronization is nine**. Moreover, precisely four labeled nine-codeword codes have coprime word lengths and no synchronizing word. They are:

```
C1 = 00 010 011 100 1010 1011 110 1110 1111
C2 = 000 001 0100 0101 011 10 1100 1101 111
C3 = 000 0010 0011 01 100 1010 1011 110 111
C4 = 0000 0001 001 0100 0101 011 100 101 11
```

These four split into two pairs under global bit complementation: C1 with C4, and C2 with C3. Each has one codeword of length two, four of length three, and four of length four. Completeness here refers to the full tree, not to minimum average encoding length or a particular source distribution.

## Assumptions and scope

A codeword is a nonempty finite binary word. The root is the empty proper prefix \(\epsilon\). The states \(Q\) of the **literal decoder** are all proper prefixes of codewords, including \(\epsilon\). For \(q\in Q\) and \(b\in\{0,1\}\), set
\[
\delta(q,b)=\begin{cases}\epsilon,&qb\in C,\\qb,&qb\notin C.\end{cases}
\]
Completeness ensures exactly one of these situations and that the second case is a proper prefix; this is a complete deterministic finite automaton. Strings are read from left to right. Different labeled tree shapes count separately; no quotient by complement or reversal is used in the count of four. The theorem covers exactly \(2\le\lvert C\rvert\le9\) for its minimality assertion and all nine-word codes for its enumeration assertion.

## Proof

**Why coprimality is a natural boundary.** If every codeword length has a common divisor \(d>1\), every path from the decoder root back to the root has length divisible by \(d\). A reset word of length \(L\) would therefore have \(d\mid L\). At least one proper prefix has length one (indeed a codeword is longer than one), and applying that same word from the corresponding depth-one state would have to complete a concatenation of codewords of total length \(L+1\); this forces \(d\mid L+1\), a contradiction. Hence a synchronizing full binary prefix code must satisfy the gcd-one condition. The issue resolved here is whether that necessary condition is sufficient for small full binary trees.

**Finite search space.** Complete binary prefix codes with \(k\ge2\) codewords correspond bijectively to ordered full binary trees with exactly \(k\) leaves, in which left and right edges carry bits zero and one. The recurrence for their numbers is
\[
T_1=1,\qquad T_k=\sum_{i=1}^{k-1}T_iT_{k-i}.
\]
Consequently \(T_k\) is the Catalan number with index \(k-1\). The first verifier produces this complete family recursively by selecting every root split. The second verifier independently produces it by starting from the two-leaf code and expanding any leaf into its zero and one children; each full tree admits such a leaf-collapse history. Duplicates are removed only in the second algorithm.

**Exact synchronization test.** A deterministic automaton is synchronizing if and only if every pair of distinct states can be merged by some word. For the forward implication apply a reset word. For the reverse implication start with the image of the entire state set and repeatedly apply a word merging any two distinct current states; the image cardinality decreases and can never increase. Eventually the image is a singleton. In a finite full binary decoding tree, any single state can be carried to the root by some nonempty run of zero bits, since following zero-child edges eventually reaches a leaf. Thus a singleton image is equivalent here to a root-resetting word. The first verifier breadth-first searches **all reachable subsets** from the full state set and checks for a singleton; the second instead computes the least collection of **mergeable pairs** closed backwards under either letter. These tests implement different finite decision procedures.

**Exhaustive outcome.** Both procedures return the following complete table. The last column imposes the coprime-length condition.

| Number of leaves | Full ordered trees | Nonsynchronizing trees | Nonsynchronizing and coprime |
| ---: | ---: | ---: | ---: |
| 2 | 1 | 0 | 0 |
| 3 | 2 | 0 | 0 |
| 4 | 5 | 1 | 0 |
| 5 | 14 | 0 | 0 |
| 6 | 42 | 0 | 0 |
| 7 | 132 | 4 | 0 |
| 8 | 429 | 1 | 0 |
| 9 | 1430 | 4 | 4 |

Every tree with fewer than nine leaves therefore fails either the nonsynchronization or the coprime-length requirement. All four nonsynchronizing nine-leaf trees meet the length-gcd requirement and have the displayed codeword lists. This establishes both the first occurrence and the complete classification.

**Independent finite witnesses for nonmergability.** The auxiliary `expansion_results.json` lists, for each exceptional code, two distinct decoder states and an explicit finite set of unordered **distinct** state pairs containing that pair and closed under the actions of both input bits. Because its elements are never diagonal and both letters preserve the set, no word can merge the exhibited pair. For C1, for example, the initial pair is \((\epsilon,0)\), and the closed set of pairs is
\[
\{(\epsilon,0),(\epsilon,10),(\epsilon,11),(1,01),(1,101),(1,111)\}.
\]
The supplied `verify_certificates.py` checks every transition of all four such witness sets from the codewords themselves. This furnishes explicit finite obstructions independent of an unexamined negative search outcome.

## Verification

Run `python3 enumerate_trees.py`, `python3 enumerate_expansions.py`, and `python3 verify_certificates.py` with the Python standard library; they print JSON with fields `counts` and `nine_word_exceptions`. The latter also outputs all `certificates`. The embedded `tree_results.json` and `expansion_results.json` are their exact outputs. Compare the first two fields across the programs; they agree for every size. Additionally check each exceptional certificate by reconstructing proper-prefix states, applying both letters to each pair in `closed_pairs`, and confirming that both successor pairs belong to the same set and are unequal. This independent transition check was performed for all four sets. No randomness or approximate floating-point computation is involved.

## Relationship to prior work

Freiling, Jungreis, Théberge and Zeger (2003) formalize the same leaf-reset decoder and show that asymptotically almost all complete binary prefix codes synchronize; their explicit nonsynchronizing examples have an even-length obstruction. Ryzhikov and Szykuła (2018) analyze finding shortest synchronizing words for prefix-code decoders, rather than enumerating the first coprime-length exceptions. Gusev and Pribavkina (2019) state a particularly relevant two-distinct-length theorem: complete finite prefix codes with two different codeword lengths synchronize when those two lengths are coprime. Perrin’s 2019 presentation records synchronization for every prefix code of cardinality two, three, five or six, but does not give a nine-codeword census. The present examples have **three** distinct lengths, so do not contradict that theorem, and the nine-leaf count is not implied by it. The question here is the first **coprime-length nonsynchronizing full binary code** and all labeled optimizers at that first size, not the older asymptotic frequency or shortest-reset algorithms.

## Limitations

The exhaustive lower bound holds only up to nine leaves; it neither classifies larger full prefix codes nor bounds their shortest reset words. This is a finite exact classification, not an infinite-family assertion. The 2019 length-criterion paper was available only as abstract and metadata; its inaccessible full text is a residual bibliographic uncertainty, as are earlier unindexed catalogues. These uncertainties do not change the independently checkable finite mathematical proof, but they limit the strength of historical novelty assertions. 

## References

1. C. F. Freiling, D. S. Jungreis, F. Théberge, and K. Zeger, *Almost All Complete Binary Prefix Codes Have a Self-Synchronizing String*, IEEE Transactions on Information Theory 49(9) (2003), 2219–2225. DOI: 10.1109/TIT.2003.815803. https://doi.org/10.1109/TIT.2003.815803
2. A. Ryzhikov and M. Szykuła, *Finding Short Synchronizing Words for Prefix Codes* (2018). arXiv:1806.06299. https://arxiv.org/abs/1806.06299
3. V. V. Gusev and E. V. Pribavkina, *On Codeword Lengths Guaranteeing Synchronization*, Combinatorics on Words, LNCS 11682 (2019), 207–216. DOI: 10.1007/978-3-030-28796-2_16. https://doi.org/10.1007/978-3-030-28796-2_16
4. D. Perrin, *Decomposition and Synchronization of Finite Codes*, presentation (June 10, 2019). https://www.sandgal19.cremona.polimi.it/wp-content/uploads/2019/06/Perrin.pdf
