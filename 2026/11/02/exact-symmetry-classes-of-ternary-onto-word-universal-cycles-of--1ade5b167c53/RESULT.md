# Exact symmetry classes of ternary onto-word universal cycles of span four

## Finding

Let \(\Sigma=\{0,1,2\}\), and let \(\mathcal S\subset\Sigma^4\) be the 36 four-letter words that contain all three symbols. A *universal cycle* is a circular word \(w\) of length 36 whose 36 indexed cyclic windows of length four are precisely the members of \(\mathcal S\), once each. Rotations are identified, and no shorter period is possible. Then:

- There are exactly **4,800** oriented universal cycles with labeled symbols.
- There are exactly **820** cycles modulo global permutations of the three symbols, retaining orientation.
- There are exactly **410** cycles modulo global symbol permutations and reversal.

For the labeled cycles, every transposition of the alphabet fixes exactly 40 cycles (up to rotation), no three-cycle fixes any, and no composition of reversal with an alphabet permutation fixes any. Thus 120 labeled cycles have a nontrivial symbol-relabeling stabilizer, all of order two, and the other 4,680 have trivial stabilizer.

An explicit labeled witness, read cyclically, is `012001210021012201020112021102210212`.

## Assumptions and scope

Symbols are distinguished except when an explicitly stated group quotient is taken. The permitted windows are *literal ordered words*, not unlabeled set-partition patterns. A rotation preserves orientation; reversal changes it. All assertions concern precisely the three-symbol alphabet and window length four. No claim is made about other alphabet sizes or spans.

## Proof

**1. Reduction to a triangular prism.** Form the directed overlap graph \(D\): an edge labeled \(abcd\in\mathcal S\) runs from the triple \(abc\) to \(bcd\). There are 36 edges and 24 nonisolated vertices. The six vertices with three distinct letters each have indegree and outdegree three. The other 18 vertices, whose triples have exactly two distinct letters, each have indegree and outdegree one.

For distinct \(x,y,z\), each departure from the vertex \(xyz\) has exactly one of the following three forced continuations, written as lists of four-letter edge labels:

\[
\begin{aligned}
P_1(xyz)&=(xyzx), &\text{ending at }yzx,\\
P_2(xyz)&=(xyzy,\ yzyx), &\text{ending at }zyx,\\
P_3(xyz)&=(xyzz,\ yzzx,\ zzxy), &\text{ending at }zxy.
\end{aligned}
\]

These 18 paths are disjoint on edges and together contain all 36 edges of \(D\). Suppressing their 18 internal degree-one vertices gives a six-vertex directed graph \(H\): each permutation triple \(xyz\) has directed arcs to \(yzx\), \(zyx\), and \(zxy\). The arcs are symmetric: the even and odd permutations each form a bidirected triangle, and the reversals \(xyz\leftrightarrow zyx\) form a bidirected matching. Thus the underlying undirected graph is the triangular prism \(K_3\square K_2\). Every Euler tour of \(D\) corresponds bijectively to an Euler tour of \(H\), with the prescribed expansion of the arcs.

**2. Labeled-cycle count.** The undirected prism Laplacian has eigenvalues \(0,2,3,3,5,5\). Its spanning-tree number, by the matrix-tree theorem, is therefore

\[
\tau(H)=\frac{2\cdot3\cdot3\cdot5\cdot5}{6}=75.
\]

Since \(H\) is the bidirected version of this graph, its directed in-arborescence count at any vertex is also 75. By the BEST theorem, Euler circuits beginning with a fixed directed arc out of \(012\) number

\[
75\prod_{v\in V(H)}(3-1)!=75\,(2!)^6=4800.
\]

Take the fixed arc \(012\to120\), which expands to the unique four-factor `0120`. Every universal cycle has this factor exactly once, so rotation uniquely places it at the beginning. Hence there is no extra root or rotation factor. The spanning tree count also proves existence.

**3. Cycles fixed by a transposition.** Let \(\tau\) swap symbols \(0\) and \(1\). On the six vertices of \(H\), it acts freely, with orbit representatives \(012,021,201\). The nine arc orbits give the quotient directed adjacency matrix

\[
A_\tau=\begin{pmatrix}0&1&2\\1&1&1\\2&1&0\end{pmatrix},
\qquad
L_\tau=3I-A_\tau=\begin{pmatrix}3&-1&-2\\-1&2&-1\\-2&-1&3\end{pmatrix}.
\]

The cofactor deleting row and column one is \(\det\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)=5\). To check the cover's monodromy, lift each quotient arc from its displayed representative vertex and mark it \(1\) if the lifted endpoint is the transposition of the chosen endpoint representative. The three rows contribute respectively \(2,3,2\) marks, totaling seven, an odd number. Therefore any Euler circuit in this quotient lifts to a trail from a vertex of \(H\) to its \(\tau\)-image. Following that trail by its \(\tau\)-translate traverses every arc of \(H\) once. Conversely, any \(\tau\)-invariant labeled universal cycle decomposes uniquely in this way: the transposition must act as the half-period shift, since it is nontrivial and the 36 windows are all different. The fixed quotient arc containing `0120` determines the rooting. Another BEST count gives

\[
F_{\tau}=5(2!)^3=40.
\]

All three symbol transpositions are conjugate, hence each fixes 40 cycles.

**4. No three-cycle stabilizers.** Let \(\sigma=(012)\) permute the symbols cyclically. Its vertex action on \(H\) has two orbits, represented by \(012\) and \(021\). The three quotient arcs from \(012\) have endpoint voltages \(1,2,2\) modulo three, and those from \(021\) have voltages \(2,1,1\). Every six-arc quotient Euler circuit therefore has total voltage \(9\equiv0\pmod3\). Its lift closes after one 12-letter block instead of moving to another alphabet sheet. An original universal cycle fixed by \(\sigma\) would require its 12-letter block to move to a different sheet, so that its three symbol-translated blocks cover the 36 distinct windows. This contradiction rules out both nonidentity three-cycles.

**5. Relabeling and reversal orbits.** Burnside's lemma now gives

\[
\#(\mathcal U/S_3)=\frac{4800+3\cdot40+2\cdot0}{6}=820.
\]

No cycle can be fixed by pure reversal: each of the six palindromic triples \(aba\) with \(a\ne b\) occurs exactly once, because its overlap vertex has outdegree one. A reflection of 36 cyclic positions fixes at most two starting positions of length-three windows, whereas all six of these uniquely occurring palindrome windows would have to be fixed.

Nor can a reversal composed with a transposition fix a cycle. For the swap \(0\leftrightarrow1\), exactly four allowed length-four words satisfy \(u=\tau(\operatorname{rev}u)\), namely `0221`, `1220`, `2012`, and `2102`. All four occur exactly once and hence would need four fixed positions under the induced reflection of window starts; every reflection has at most two. Finally, a reversal composed with a three-cycle cannot fix a cycle, since its square would be a forbidden nonidentity three-cycle symmetry. Thus reversal acts freely on the 820 relabeling classes, and

\[
\#(\mathcal U/(S_3\times C_2))=820/2=410.
\]

The 120 cycles stabilized by transpositions are pairwise distinct across the three transpositions because their intersection would force a three-cycle stabilizer; all other cycles have trivial alphabet stabilizer.

## Verification

The included standard-library-only `verify.py` reconstructs all 36 words and 24 overlap vertices; checks the 18 forced paths and the triangular-prism reduction; obtains 75 spanning trees by both a Laplacian cofactor and exhaustive five-edge tree subsets; checks the transposition quotient cofactor and odd monodromy; checks zero three-cycle monodromy; and independently enumerates every Euler circuit of the original 36-edge graph rooted at `0120`. It verifies 4,800 distinct cycles and exact fixed-point counts under all twelve alphabet/reversal operations, obtaining 820 and 410 orbits. Run `python3 verify.py`; successful output starts with `VERIFY_OK`.

A witness is supplied separately in `witness.txt`. The script checks all 36 cyclic windows directly. The finite exhaustive computation is a cross-check; the preceding graph and group arguments establish the count without assuming the computation.

## Relationship to prior work

Burstein and Kitaev, *On unavoidable sets of word patterns* (arXiv:math/0311399, posted 2003-11-23), study the full graph of normalized word patterns and prove that their pattern-overlap graph has a Hamiltonian circuit (Theorem 3.8), which supplies existence for all patterns. Their Sections 3.1–3.2, including the complete Hamiltonicity proof, contain no count of Euler circuits in the different graph induced by the 36 length-four ternary words using every symbol, and no alphabet/reversal fixed-point enumeration. Existence in their broader pattern setting is therefore distinct from the exact cycle counts here.

Blanca and Godbole, *On Universal Cycles for new Classes of Combinatorial Structures* (arXiv:1008.2251, first publicly posted 2010-08-13), Theorem 11, already proves existence of universal cycles for words required to contain all specified letters. Our 36-word family is a direct instance of that theorem: existence is **not** claimed as new. Their statement and inspected Section 5 give neither the exact 4,800 count nor symbol/reversal orbit counts.

Gardner and Godbole, *Universal Cycles of Restricted Words* (arXiv:1711.07029, publicly posted 2017-11-19), survey onto-word existence in Theorem 2 and prove new existence statements for augmented onto words. Their inspected introduction and Section 2.6 do not give the present enumeration or symmetry classification.

Chen and Kitaev, *On universal partial words for word-patterns and set partitions* (DOI:10.1051/ita/2020004, online first 2020-01-28, MSC 68R15), study single-wildcard universal partial words for surjective word-patterns and set partitions. Their inspected full-text definitions and main results concern a different, wildcard-enabled optimization problem, not counting the ordinary 36-edge labeled universal cycles. This motivates treating the exact ordinary count and its symmetry reduction as a separate question.

The BEST and directed matrix-tree theorems are classical ingredients. The contribution here is the explicit forced-path prism reduction and the completed stabilizer and orbit enumeration for the first nonbinary onto-word span beyond its alphabet size.

## Limitations

The result is confined to alphabet size three and span four. It does not yield an all-alphabet or all-span formula, and does not assert any new existence theorem. Although source-specific comparisons and multiple descriptive searches found no equivalent enumeration, unindexed literature may contain it. The checks do not constitute independent peer review.

## References

1. A. Burstein and S. Kitaev, *On unavoidable sets of word patterns*, SIAM J. Discrete Math. 19 (2005), 371–381, arXiv:math/0311399 (2003), https://arxiv.org/abs/math/0311399 .
2. A. Blanca and A. P. Godbole, *On Universal Cycles for new Classes of Combinatorial Structures*, arXiv:1008.2251 (2010), https://arxiv.org/abs/1008.2251 .
3. K. B. Gardner and A. P. Godbole, *Universal Cycles of Restricted Words*, arXiv:1711.07029 (2017), https://arxiv.org/abs/1711.07029 .
4. H. Z. Q. Chen and S. Kitaev, *On universal partial words for word-patterns and set partitions*, RAIRO Theoretical Informatics and Applications 54 (2020), article 5, https://doi.org/10.1051/ita/2020004 ; full text https://spider-v.science.strath.ac.uk/sergey.kitaev/Papers/upwords.pdf .
5. The BEST theorem on Euler-tour counts and the directed matrix-tree theorem (standard graph-theoretic results).
