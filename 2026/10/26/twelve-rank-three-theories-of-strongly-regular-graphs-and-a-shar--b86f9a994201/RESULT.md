# Twelve rank-three theories of strongly regular graphs and a sharp ten-vertex kernel

## Finding
Let \(G\) be a finite simple undirected graph. Write \(G\equiv_q H\) when \(G\) and \(H\) satisfy the same first-order sentences of quantifier rank at most \(q\) in the adjacency/equality language.

**Theorem.** Among all nontrivial strongly regular graphs, including the disconnected and complete-multipartite examples, there is one \(\equiv_2\)-class and exactly twelve \(\equiv_3\)-classes. For a graph with parameters \((n,k,\lambda,\mu)\), put
\[
\sigma(G)=\left(
[\lambda>0],\ [k-1-\lambda>0],\ [n-2k+\lambda>0],\
[\mu>0],\ [k-\mu>0],\ [n-2-2k+\mu>0]
\right).
\]
Then \(G\equiv_3 H\) if and only if \(\sigma(G)=\sigma(H)\). Every class contains a representative of at most ten vertices, and no smaller bound works.

The complete list of representatives and their signatures is:

| Representative | Order | Signature \(\sigma\) |
|---|---:|---|
| \(2K_2\) | 4 | `001010` |
| \(3K_2\) | 6 | `001011` |
| \(2K_3\) | 6 | `101010` |
| \(3K_3\) | 9 | `101011` |
| \(K_{2,2}\) | 4 | `010100` |
| \(K_{3,3}\) | 6 | `010101` |
| \(K_{2,2,2}\) | 6 | `110100` |
| \(K_{3,3,3}\) | 9 | `110101` |
| \(C_5\) | 5 | `011110` |
| Petersen graph | 10 | `011111` |
| Complement of the Petersen graph | 10 | `111110` |
| \(3\times3\) rook graph | 9 | `111111` |

## Assumptions and scope
A nontrivial strongly regular graph has order \(n\), degree \(k\), exactly \(\lambda\) common neighbors for each adjacent pair, and exactly \(\mu\) common neighbors for each distinct nonadjacent pair, with \(0<k<n-1\). We do not assume connectivity or vertex transitivity. A complete multipartite graph has at least two equal parts, each of size at least two; the disjoint clique graphs similarly have at least two equal components, each of size at least two. No counting quantifiers, named vertex colors, or external order relations occur.

## Proof
**1. Two-round equivalence.** Every vertex of every graph in scope has both a neighbor and a distinct nonneighbor. In a two-round Ehrenfeucht–Fraïssé game, after the first arbitrary pair of matched vertices, the second response can match equality and either adjacency or nonadjacency. Hence all graphs in scope are \(\equiv_2\)-equivalent.

**2. Exact three-round invariant.** Fix distinct vertices \(u,v\). If \(u\sim v\), the four counts of vertices \(w\notin\{u,v\}\), according to whether \(w\) is adjacent to both, to \(u\) alone, to \(v\) alone, or to neither, respectively, are
\[
\lambda,\quad k-1-\lambda,\quad k-1-\lambda,\quad n-2k+\lambda.
\]
If \(u\not\sim v\), the four analogous counts are
\[
\mu,\quad k-\mu,\quad k-\mu,\quad n-2-2k+\mu.
\]
A third move can detect whether any one of these classes is empty, but not its positive cardinality. Conversely, if the six zero/nonzero statuses match, Duplicator matches the first move arbitrarily, the second by equality/adjacency status, and the third by the appropriate third-vertex class (including repeated vertices). This is a winning three-round strategy. Every one of the six positivity bits is independently visible by a rank-three existential sentence specifying two distinct adjacent or nonadjacent vertices and a distinct third vertex with the designated adjacency pattern. Because every graph in scope has both edges and nonedges, differing bits give a distinguishing sentence. Thus the invariant is necessary and sufficient.

**3. Exactly twelve realizable signatures.** Count edges from the neighborhood of a fixed vertex to its nonneighbors to obtain
\[
(n-k-1)\mu=k(k-1-\lambda).
\]
If \(\mu=0\), then \(k-1-\lambda=0\) and the graph is a union of \(t\ge2\) cliques of common size \(s=k+1\ge2\). Its signature depends only on whether \(s=2\) or \(s\ge3\), and whether \(t=2\) or \(t\ge3\): four cases, realized by the first four representatives.

If \(\mu=k\), any nonadjacent pair has identical open neighborhoods, so nonadjacency together with equality is an equivalence relation. The graph is complete multipartite with \(t\ge2\) equal parts of size \(s\ge2\). Its signature depends only on whether \(t=2\) or \(t\ge3\), and whether \(s=2\) or \(s\ge3\): four further cases.

The remaining case \(0<\mu<k\) is primitive: both \(G\) and its complement are connected. For the complement, the degree is \(n-k-1\) and the nonadjacent-pair common-neighbor number is \(n-2k+\lambda\). Thus \(k-1-\lambda\), \(n-2k+\lambda\), \(\mu\), and \(k-\mu\) are all strictly positive. The remaining independent binary possibilities are \(\lambda=0\) or \(>0\), and \(\lambda'=n-2-2k+\mu=0\) or \(>0\), yielding at most four cases. Each exists: \(C_5\) has both zero, the Petersen graph has \(\lambda=0\) and \(\lambda'>0\), its complement has the reverse, and the \(3\times3\) rook graph has both positive. This gives exactly \(4+4+4=12\) distinct signatures, all listed above.

**4. Sharp ten-vertex bound.** The table supplies representatives of order at most ten. To prove sharpness, consider the Petersen signature: \(G\) must be primitive, triangle-free, and have \(\lambda'>0\). A triangle-free \(k\)-regular graph has \(k\le n/2\) by Mantel's bound. For \(n<10\), this gives \(k\le4\). Degree \(k=1\) produces disjoint edges; degree \(k=2\), under strong regularity and connectedness, gives \(C_4\) or \(C_5\), neither with the needed primitive signature. For \(k=3\), the parameter equation forces \(n=4+6/\mu\); the possibilities are \((n,\mu)=(10,1),(7,2),(6,3)\). The first has order ten, the second violates evenness of \(nk\), and the third is complete bipartite. For \(k=4\), similarly \(n=5+12/\mu\), giving \((17,1),(11,2),(9,3),(8,4)\). The last is complete bipartite; parameters \((9,4,0,3)\) cannot occur: on the eight-dimensional orthogonal complement of the all-ones vector, the adjacency eigenvalues are the two roots of \(z^2+3z-1\). Since that polynomial is irreducible over \(\mathbb Q\), each root would have multiplicity four, giving adjacency trace \(4+4(-3)=-8\), contradicting the zero diagonal. Hence no graph of order below ten has the Petersen signature. The Petersen graph realizes it on ten vertices. Complementation gives the same minimum for the complement-Petersen signature.

## Verification
The standalone script `srg_rank3_verify.py` constructs twelve representatives and six additional strongly regular examples, checks their parameters directly from adjacency sets, and independently computes rank-three types via the recursive *atomic type plus set of one-vertex-extension types* rule. All twelve representative types are distinct; every tested pair agrees at rank three if and only if its six positivity bits agree. The script also confirms common rank-two type across all representatives and confirms that the \(3\times3\) and \(4\times4\) rook graphs and the Shrikhande graph share the same rank-three type. Execute `python3 srg_rank3_verify.py`; recorded output is `srg_rank3_verify_output.txt`. The unbounded theorem uses the symbolic proof above, not extrapolation from these finite checks.

## Relationship to prior work
Verbitsky's 2004 preprint studies quantifier rank via graph Ehrenfeucht games and separator-dependent definability, not a strongly-regular graph rank-three census. Libkin's finite-model-theory treatment supplies the game/type correspondence, not an enumeration over this class. The literature on strongly regular graphs provides the parameter identities, primitive/imprimitive dichotomy, and small examples used here. An exact twelve-class low-rank logical classification and the ten-vertex cutoff were not found in the examined material; the comparison is not an independent literature-certification claim. Existing logical classifications of rook and Johnson subfamilies do not imply the universal twelve-class result without the present intersection-support analysis and realizability argument.

## Limitations
Only ordinary first-order graph sentences of rank at most three are classified; no claim is made at rank four or with counting quantifiers. The graph class excludes edgeless and complete graphs. This is a self-review, not independent verification. A logically equivalent reformulation may occur in unindexed sources or mathematical folklore, particularly because the proof uses standard strongly regular graph identities and a classical three-move game argument.

## References
1. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361v1, publicly posted 26 January 2004. https://arxiv.org/abs/math/0401361
2. L. Libkin, *Elements of Finite Model Theory*, Chapter 3 (especially §§3.3–3.5). https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf
3. C. Godsil and K. Meagher, *Erdős–Ko–Rado Theorems: Algebraic Approaches*, Chapter 5: Strongly regular graphs, Cambridge University Press, 2015. https://www.cambridge.org/core/books/abs/erdoskorado-theorems-algebraic-approaches/strongly-regular-graphs/14AD9F996417DD9B1355527326873E81
4. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, monograph (2021), Chapter 1, §§1.1.1, 1.1.4, 1.1.17. https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf
