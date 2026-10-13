# All two-uniform representations of complete bipartite graphs
## Finding
Fix a labeled complete bipartite graph \(K_{m,n}\) with nonempty labeled parts \(X\) and \(Y\), where \(|X|=m\) and \(|Y|=n\).

Every \(2\)-uniform word representing \(K_{m,n}\) has, after a cyclic rotation, the form
\[
A\,B\,A^R\,B^R,
\]
where \(A\) is a permutation of \(X\), \(B\) is a permutation of \(Y\), and \(R\) denotes reversal.

Consequently the number of linear \(2\)-uniform word-representations is exactly
\[
(m+n)m!n!.
\]

If \(m+n\ge3\), then \(K_{m,n}\) is not complete, while the displayed form gives a \(2\)-uniform representation. Hence its representation number is exactly \(2\). The published square-freeness theorem for representation-number-uniform words then implies that every one of these \((m+n)m!n!\) words is square-free.

For \(m+n\ge3\), the number of these representations modulo cyclic rotation is
\[
\frac{m!n!}{2}.
\]

The exceptional graph \(K_{1,1}=K_2\) still has exactly two \(2\)-uniform representations, but its representation number is \(1\), and those two words are the squares \(\mathtt{abab}\) and \(\mathtt{baba}\).

## Assumptions and scope
A word represents a graph when two distinct letters alternate in the word if and only if their corresponding vertices are adjacent. A word is \(2\)-uniform when every vertex letter occurs exactly twice.

The bipartition \(X\sqcup Y\) is fixed and labeled. Counts are for linear words on those labels; only the explicitly stated cyclic count identifies rotations.

The square-free conclusion uses the published result that for a connected word-representable graph of representation number \(k\), every \(k\)-uniform representant is square-free. Complete bipartite graphs with both parts nonempty are connected.

## Proof
Take any \(2\)-uniform representant \(w\), choose \(x_0\in X\), and cyclically rotate \(w\) so that
\[
w=x_0\,U\,x_0\,V.
\]
Every letter of \(Y\) must alternate with \(x_0\), so it occurs exactly once in \(U\) and exactly once in \(V\). Every other letter of \(X\) is nonadjacent to \(x_0\), so its two occurrences lie together in \(U\) or together in \(V\).

Consider a letter \(x\in X\setminus\{x_0\}\) whose two occurrences lie in \(U\). Since \(x\) must alternate with every \(y\in Y\), the unique occurrence of every \(y\) in \(U\) must lie strictly between the two occurrences of \(x\). Thus the occurrence intervals of all such \(X\)-letters contain the complete \(Y\)-block in \(U\). Because two \(X\)-letters must not alternate, these intervals are nested. Therefore
\[
U=P\,B\,P^R
\]
for some permutation \(P\) of the \(X\)-letters assigned to \(U\), with \(B\) a permutation of \(Y\). The identical argument gives
\[
V=Q\,C\,Q^R
\]
for a permutation \(Q\) of the remaining \(X\)-letters and a permutation \(C\) of \(Y\).

Now take two distinct letters \(y_i,y_j\in Y\). If their relative order were the same in \(B\) and \(C\), their two occurrences would alternate, creating an edge inside \(Y\). Hence every pair has reversed relative order, so
\[
C=B^R.
\]
Thus
\[
w=x_0PBP^R x_0QB^RQ^R.
\]
Rotate this word to start with \(Q^R\). Setting
\[
A=Q^R x_0P
\]
gives exactly
\[
A\,B\,A^R\,B^R.
\]

Conversely, every word of this displayed form represents \(K_{m,n}\). Two letters in the same part occur in opposite relative orders in the first and second copies of that part, so they do not alternate. A letter of \(X\) and a letter of \(Y\) occur in the cyclic order \(x,y,x,y\), so they do alternate.

It remains to count. There are \(m!n!\) ordered choices of \((A,B)\). For \(m+n\ge3\), the only duplication at the cyclic level is
\[
(A,B)\sim(A^R,B^R),
\]
obtained by rotating by \(m+n\) positions. These parameter pairs are distinct because at least one of \(A,B\) has length greater than one. Hence there are \(m!n!/2\) cyclic classes.

Each such cyclic word has all \(2(m+n)\) rotations distinct. Indeed, a shorter period would have to be \(m+n\), because every letter occurs exactly twice. That would force the first and second halves to agree, hence \(A=A^R\) and \(B=B^R\), which is impossible when \(m+n\ge3\). Therefore the number of linear words is
\[
2(m+n)\frac{m!n!}{2}=(m+n)m!n!.
\]

Finally, when \(m+n\ge3\), a \(1\)-uniform word represents a complete graph, whereas \(K_{m,n}\) is not complete. The explicit \(2\)-uniform form proves representation number \(2\). The published representation-number theorem therefore makes every counted word square-free.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier uses two independent finite engines for every positive \(m,n\) with \(m+n\le5\). One enumerates every double-occurrence word directly and tests the alternation graph. The other generates all rotations of the structural form \(ABA^RB^R\). The two sets agree exactly in every tested case.

It also checks the linear formula, the cyclic formula for \(m+n\ge3\), and square-freeness of every generated representant through this exhaustive range. The \(K_{1,1}\) exception is tested separately.

## Relationship to prior work
Das and Hariharasubramanian prove that every connected graph whose representation number is \(k\) has every \(k\)-uniform representant square-free. They then ask to count square-free words representing graphs and obtain the exact total \(n\,n!\) for the complete graph \(K_n\). For non-complete connected graphs they instead establish the existence of infinitely many square-free representants of larger uniformities.

The present result isolates and completely counts the representation-number layer for the fundamental non-complete family \(K_{m,n}\). It is stronger than merely observing that complete bipartite graphs are circle graphs: it classifies every double-occurrence representant and gives exact linear and cyclic counts.

The standard equivalence between circle graphs and \(2\)-word-representable graphs identifies the same objects with chord diagrams or double-occurrence words. Searches using all three languages—word-representations, double-occurrence words, and chord diagrams/interlacement graphs—located general circle-graph literature and explicit complete-bipartite examples, but no enumeration or structural classification equivalent to the theorem above.

## Limitations
The classification is specific to complete bipartite graphs and to the \(2\)-uniform representation-number layer. Non-complete connected word-representable graphs can have infinitely many square-free representations at higher uniformities, so the formula is not a count of all square-free representants of \(K_{m,n}\).

The theorem does not classify \(2\)-uniform representants of arbitrary bipartite circle graphs or complete multipartite graphs.

An older or unindexed chord-diagram enumeration may contain an equivalent count even though the inspected word-representation and interlacement literature did not expose one.

## References
1. B. Das and R. Hariharasubramanian, “Square-free Word-representation of Word-representable Graphs,” arXiv:2402.14426v1, first public version 2024-02-22; Graphs and Combinatorics 42 (2026), Article 12, DOI 10.1007/s00373-025-03000-w.
2. M. M. Halldórsson, S. Kitaev, and A. Pyatkin, “Semi-Transitive Orientations and Word-Representable Graphs,” Discrete Applied Mathematics 201 (2016), 164–171, DOI 10.1016/j.dam.2015.07.033.
3. R. Brijder and H. J. Hoogeboom, “Splitting cubic circle graphs,” arXiv:1504.01143v1, 2015.
