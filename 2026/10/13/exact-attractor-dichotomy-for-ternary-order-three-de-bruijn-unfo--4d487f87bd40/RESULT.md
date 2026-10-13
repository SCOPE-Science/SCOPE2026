# Exact attractor dichotomy for ternary order-three de Bruijn unfoldings

## Finding
Let \(\Sigma=\{0,1,2\}\). A cyclic de Bruijn word of order three is a cyclic word of length \(27\) containing each member of \(\Sigma^3\) exactly once as a cyclic factor. For each such cycle \(b\) and a cut \(r\in\{0,\ldots,26\}\), write \(T_{b,r}\) for the resulting length-\(29\) word obtained by repeating the first two letters after the rotated length-\(27\) word. Denote by \(\gamma^*(T)\) the minimum size of a full string attractor (a marked position set intersecting at least one occurrence of every nonempty factor).

**Exact classification.** There are \(373248\) cycles up to rotation and \(10077696\) (cycle,cut) pairs. Exactly \(8274096\) have \(\gamma^*(T)=9\); the other \(1803600\) have \(\gamma^*(T)=10\). The number of cycles having exactly \(0\), \(9\), \(18\), or \(27\) nine-optimal cuts is respectively
\[
(1632,\ 19968,\ 155568,\ 196080).
\]
In particular, \(1632\) cycles fail to have a nine-optimal cut at **any** rotation. One such cycle (with canonical cut immediately before its first displayed zero) is `000100212012101112221102022`; this unfolding has a ten-position attractor at zero-based positions `0,3,5,8,11,14,17,20,23,26`.

## Assumptions and scope
The alphabet is fixed to three labeled letters; the cyclic order is three and no repetitions of an order-three factor are allowed. Cycles are identified under cyclic rotation, but **not** under letter permutations or reversal. All \(27\) cuts of each cycle are counted separately. A linear unfolding appends the first two symbols. Marked positions use zero-based indices from \(0\) to \(28\). A full attractor must hit every distinct nonempty substring at some occurrence, not merely every length-three substring.

## Proof
**Reduction.** The unfolding has exactly one occurrence of each of the \(27\) ternary length-three words, with starts \(0,\ldots,26\). A marked position belongs to at most three such windows. Hence every attractor has at least nine positions. At size nine, all marked positions must lie inside exactly three windows and their covered triple-window sets must partition \(0,\ldots,26\); the first mark must be at index \(2\), after which the next is forced to be three positions later. Therefore the only possible size-nine set is
\[
P_9=\{2,5,8,11,14,17,20,23,26\}.
\]
For a size-ten set hitting every triple, its sorted positions \(p_0<\cdots<p_9\) necessarily and sufficiently satisfy \(p_0\le2\), \(p_{j+1}-p_j\le3\), and \(p_9\ge26\). Direct generation of these inequalities yields exactly \(275\) candidates. Moreover, if all \(27\) triple windows are hit, every factor occurrence of length at least three is also hit (it contains a hit triple window). Thus such a candidate is a **full** attractor exactly when its marked positions additionally cover all three one-letter factors and all nine two-letter factors. These factors exist in every de Bruijn unfolding, and the checker verifies their coverage using two finite bit sets.

**Complete enumeration.** Each cycle corresponds to a length-\(27\) directed Euler circuit using every edge once in the ternary de Bruijn graph whose vertices are the nine length-two words and whose edges are the \(27\) length-three words. The edge `000` occurs once, so fixing it as first edge chooses exactly one representative of every cyclic word. Starting at vertex `00`, the embedded `verify.cpp` explores every unused outgoing edge in depth-first order, accepts exactly the closed tours, and computes each word from the first letter of each chosen edge. This enumerates every cycle once. An independent count check is
\[
\frac{(3!)^{3^2}}{3^3}=373248,
\]
the standard de Bruijn cycle formula (also reproduced by the complete generator).

For each generated cycle, the checker first tests the forced size-nine marking against letter/digram coverage for each of the three cut residue classes. It then examines all \(27\) rotations: a rotation passes at rank nine precisely when its forced residue class passes. For every failed rank-nine rotation, it exhaustively tests all \(275\) ten-position triple-hitting candidates against the missing letter/digram constraints. The computation returns:

```
cycles=373248 candidate10=275
optimal9classes_0=1632
optimal9classes_1=19968
optimal9classes_2=155568
optimal9classes_3=196080
cut9=8274096 cut10=1803600 cut_over10=0 cycles_without_9=1632
VERIFY_OK
```

Because every possible cycle and cut is covered, each failed size-nine cut has a verified ten-position witness, and there is no further case. Thus the full minimum is exactly nine or ten with the stated multiplicities. The class sizes correspond to \(9\) cuts per successful residue class, so the two levels of the census agree arithmetically.

## Verification
Compile and run the included standalone source with `g++ -O3 -std=c++17 -Wall -Wextra -pedantic verify.cpp -o verify && ./verify`. A nonzero exit indicates a mismatch. The checker reconstructs all cycles and tests every relevant rotation; it does not load any prerecorded table. The explicit bad-cycle example was also directly checked against factors of every length from one to \(29\), and the stated ten-position set passed.

## Relationship to prior work
Mantaci, Restivo, Romana, Rosone and Sciortino establish general lower/upper bounds for de Bruijn attractors and examples, not a classification of every ternary order-three cycle and cut. Whittington explicitly distinguishes sharp versus full attractors, gives a ternary order-three cut that fails to be nine-optimal, proves a nine-attractor for one Lyndon-generated cycle at a suitable cut, and asks whether every de Bruijn cycle admits some optimally unfolded cut. The present complete census shows the answer to that last **universal-cycle** question is negative: precisely \(1632\) ternary order-three cycles have no nine-optimal cut. It does not refute Whittington's separate existence conjecture asserting that some favorable cycle exists for every alphabet and order.

## Limitations
The result is an exact finite theorem for three letters and order three; it is not an infinite-order classification. The finite certificate is essential for the exhaustive multiplicities. The proof does not infer exhaustive counts from sampled experiments. An unindexed prior exhaustive census may exist despite the primary-literature comparisons. No optimal coding, online-attractor, or higher-order claim is made.

## References
1. S. Mantaci, A. Restivo, G. Romana, G. Rosone, and M. Sciortino, *String Attractors and Combinatorics on Words*, arXiv:1907.04660 (first public July 10, 2019), especially de Bruijn section; https://arxiv.org/abs/1907.04660 .
2. P. Whittington, *Online String Attractors*, arXiv:2407.15599v1 (first public July 22, 2024), Section 5, Theorem 29 and surrounding open questions; https://arxiv.org/html/2407.15599v1 .
3. D. Kempa, A. Policriti, N. Prezza, and E. Rotenberg, *String Attractors: Verification and Optimization*, arXiv:1803.01695 (background on attractor verification); https://arxiv.org/abs/1803.01695 .
