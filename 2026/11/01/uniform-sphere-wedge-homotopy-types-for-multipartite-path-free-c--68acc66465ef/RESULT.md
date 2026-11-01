# Uniform sphere-wedge homotopy types for multipartite path-free complexes

## Finding
Let \(r\ge3\), let \(n_1,\ldots,n_r\) be positive integers, let \(N=\sum_i n_i\), and let \(t\ge5\). Define \(G=K_{n_1,\ldots,n_r}\). The simplicial complex \(\operatorname{PF}_t(G)\) consists of vertex subsets whose induced subgraph contains no simple path on \(t\) distinct vertices (the path need not be induced). Put \(s=\lfloor(t-2)/2\rfloor\). Then
\[
\operatorname{PF}_t(G)\simeq\bigvee^{B} S^{t-2},\qquad
B=\binom{N-1}{t-1}-\sum_{i=1}^{r}\sum_{b=0}^{s}\binom{N-n_i}{b}\binom{n_i-1}{t-b-1}.
\]
Every binomial coefficient with an inadmissible lower index is zero, and a zero-fold wedge means a point. Thus all reduced integral homology is free and concentrated in degree \(t-2\), of rank \(B\). In particular, \(\operatorname{PF}_5(K_{4,4,4})\simeq\bigvee^{306}S^3\) and \(\operatorname{PF}_6(K_{4,4,4})\simeq\bigvee^{378}S^4\).

## Assumptions and scope
The parts are labeled nonempty vertex classes and graph edges join precisely distinct parts; the path condition forbids non-induced simple paths on exactly \(t\) vertices, equivalently on at least \(t\) vertices. The theorem covers arbitrary positive part sizes for \(r\ge3\), including \(t>N\), when the complex is a full simplex and \(B=0\). We do not claim a new result for the bipartite cases or for thresholds below five.

## Proof
**1. Longest-path criterion.** Let \(W\) be a nonempty vertex subset with \(k=|W|\), and let \(M\) be its largest intersection size with a part. Its induced complete multipartite graph has a simple path containing exactly
\[
\min\{k,\ 2(k-M)+1\}
\]
vertices. Indeed, any path alternates between members of a largest part and vertices outside it, so it uses at most \(2(k-M)+1\) vertices if that part is overrepresented. This upper bound is attained by alternating every vertex outside that part with one from it; if \(M\le k-M+1\), all \(k\) vertices admit an ordering with adjacent entries in different parts. The latter follows by a short induction on the word length: if the largest part count is at most the ceiling of half the length, remove one element from each of the two most populous distinct parts. The remaining largest count is at most the ceiling of half its new length (a third part cannot have had the former maximum, by summing counts). Arrange the remaining symbols inductively with unequal neighbors, and prepend the two removed symbols in whichever order makes the second differ from the first remaining symbol. The base cases of lengths zero, one and two are immediate. This proves the multiset interleaving criterion without assuming that distinct outside-part vertices can be arbitrarily adjacent. Consequently, every set of size \(k<t\) is a face, and a set \(W\) of size at least \(t\) is a face if and only if \(b=k-M\le s\).

**2. Unique dominant part.** For a face \(W\) of cardinality at least \(t-1\) with \(b=|W\setminus V_i|\le s\), its occupancy in the part \(V_i\) is at least \(t-s-1>s\), whereas every other part contains at most \(s\) vertices. Thus the dominant part \(i\) is unique. This applies to all faces of size at least \(t\) and to their faces obtained by deleting a vertex in the dominant part.

**3. Explicit acyclic matching.** Fix one pivot vertex \(p_i\in V_i\) for every part. For every face \(U\) with \(|U|\ge t\), choose its unique dominant part \(i\). If \(p_i\in U\), pair \(U\setminus\{p_i\}\) with \(U\). If \(p_i\notin U\), pair \(U\) with \(U\cup\{p_i\}\). In either case the two faces are legal: their numbers of vertices outside \(V_i\) agree and do not exceed \(s\). The lower face has size at least \(t-1\), has unique dominant part \(i\), and omits \(p_i\); therefore different pairs cannot overlap. Every face of size at least \(t\) belongs to a pair.

To prove acyclicity, orient unmatched Hasse edges downwards and matched ones upwards. In an alternating path, after traversing a matched edge from \(L\) to \(U=L\cup\{p_i\}\), any different downward deletion \(U\setminus\{v\}\), where \(v\ne p_i\), still contains \(p_i\), still has at least \(t-1\) vertices, and still has unique dominant part \(i\) with outsider count at most \(s\). But every lower member of a matched pair of size at least \(t-1\) necessarily omits the pivot of its unique dominant part. Hence this descending face cannot begin another matched edge. No nontrivial alternating path, and therefore no directed matching cycle, exists. Forman's discrete Morse theorem yields a CW model of dimension at most \(t-2\).

**4. Homotopy type.** All subsets of at most \(t-1\) vertices occur in the complex, so it contains the full \((t-2)\)-skeleton of the \((N-1)\)-simplex. If \(t\le N\), this skeleton is \((t-3)\)-connected; adding higher-dimensional simplices preserves this connectivity. Thus the Morse CW model is \((t-3)\)-connected and has dimension at most \(t-2\). As \(t\ge5\), the Hurewicz theorem and the simply connected homology Whitehead theorem show that it is homotopy equivalent to a wedge of \((t-2)\)-spheres. If \(t>N\), the complex is a simplex and is contractible.

**5. Exact sphere number.** The contribution of faces of sizes at most \(t-1\) to reduced Euler characteristic is \((-1)^{t-2}\binom{N-1}{t-1}\). A larger face has a unique dominant part \(i\); writing \(b\) for the number of outsiders and \(a\) for the number of vertices chosen inside \(V_i\), its signed contribution summed over \(a\ge t-b\) is
\[
\sum_{a=t-b}^{n_i}(-1)^{a+b-1}\binom{n_i}{a}\binom{N-n_i}{b}
=(-1)^{t-1}\binom{N-n_i}{b}\binom{n_i-1}{t-b-1}.
\]
The identity remains valid when the summation range is empty with the stated binomial convention. Sum over unique parts and \(0\le b\le s\). Since the wedge has reduced Euler characteristic \((-1)^{t-2}B\), the displayed formula follows. This also proves \(B\) is a nonnegative integer.

## Verification
Run `python verify.py` with Python 3.10 or newer; it uses only the standard library. It exhaustively constructs multiple complete multipartite examples, verifies face membership independently by exact simple-path dynamic programming when \(N\le9\), reconstructs every explicit matching pair, checks all codimension-one incidences, topologically sorts the reversed-matching Hasse directed acyclic graph, checks mod-two homology by independent exact boundary elimination for small cases, and compares reduced Euler characteristics against the closed formula. Representative output includes `parts=(4, 4, 4) threshold=5 ... B=306` and `parts=(4, 4, 4) threshold=6 ... B=378`. These finite tests corroborate but do not substitute for the preceding universal proof.

## Relationship to prior work
Deshpande, Goyal and Sawant (first public version 2026-07-06) establish structural decompositions and exact vertex-decomposability thresholds for path-free complexes of complete multipartite graphs and state a complete sphere-wedge homotopy classification for the *bipartite* subfamily. Their accessible abstract does not assert the uniform homotopy classification or the exact top Betti formula above for \(r\ge3\); the new proof does not use any result of that paper. The full 19-page primary text was not accessible for complete implication checking, so related unpublished or unindexed calculations remain a source of originality uncertainty. Prior four-path-free calculations concern the excluded threshold \(t=4\) and are not a proof of the present all-threshold result.

## Limitations
The theorem requires a complete multipartite graph, integer \(t\ge5\) and at least three nonempty parts. It does not classify arbitrary graphs, maps induced by graph automorphisms, or homotopy equivalences natural in edge modifications. The literature comparison is based on accessible primary abstracts and available indexed sources, not a complete reading of the nearest 19-page preprint. No independent mathematical audit is claimed.

## References
1. P. Deshpande, S. Goyal and R. Sawant, *On a complete characterization of path-free complexes associated with complete multipartite graphs*, arXiv:2607.05358v1 (first posted 2026-07-06), https://arxiv.org/abs/2607.05358 .
2. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145 (discrete Morse theorem).
3. Standard Hurewicz and Whitehead theorems for simply connected CW complexes.
