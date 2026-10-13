# Locating-dominating coalition numbers of complete bipartite graphs
## Finding
Let \(K_{m,n}\) be a finite complete bipartite graph with shores \(X\) and \(Y\), where \(|X|=m\), \(|Y|=n\), and \(m,n\ge1\). The graph \(K_{1,1}=K_2\) has no locating-dominating coalition partition. For every \(m+n\ge3\),
\[
C_L(K_{m,n})=
\begin{cases}
4,&(m,n)=(2,2),\\
3,&\text{otherwise.}
\end{cases}
\]
In particular, \(K_{2,2}\) is the unique complete bipartite graph with locating-domination coalition number greater than three.

## Assumptions and scope
A locating-dominating set (LD-set) \(D\) is a dominating set such that distinct vertices outside \(D\) have distinct open-neighborhood traces on \(D\). Two disjoint sets form an LD-coalition when neither set is an LD-set but their union is an LD-set. An LDC-partition is a vertex partition in which every block is not an LD-set and has another block as an LD-coalition partner. The number \(C_L(G)\) is the largest number of blocks in such a partition, when one exists.

For \(m,n\ge2\), a set \(D\subseteq V(K_{m,n})\) is an LD-set exactly when it omits at most one vertex from each shore. Indeed, two omitted vertices in the same shore are twins relative to \(D\), while if at most one vertex is omitted from each shore then every omitted vertex is dominated and the two possible outside traces lie on opposite shores. Consequently,
\[
\gamma_L(K_{m,n})=m+n-2\qquad(m,n\ge2).
\]
For a star \(K_{1,n}\) with \(n\ge2\), the standard value is \(\gamma_L(K_{1,n})=n\).

## Proof
First suppose \(m=1\) and \(n\ge2\). Choose two leaves \(y_1,y_2\) when \(n\ge3\), put \(A=V(K_{1,n})\setminus\{y_1,y_2\}\), and take the three blocks \(A,\{y_1\},\{y_2\}\). The block \(A\) is not locating-dominating because the two omitted leaves have the same trace, while \(A\cup\{y_i\}\) is an LD-set for each \(i\). The singleton leaves are not dominating. Thus \(C_L(K_{1,n})\ge3\). The same conclusion for \(K_{1,2}=P_3\) follows from the all-singleton partition. Since \(\gamma_L(K_{1,n})=n\), Proposition 2.8 of the initiating paper gives
\[
C_L(K_{1,n})\le (n+1)-n+2=3,
\]
so every star of order at least three has value three.

Now suppose \(m,n\ge2\). If \(\max\{m,n\}\ge3\), choose two vertices \(y_1,y_2\) from a shore containing at least three vertices and again take
\[
\Pi=\{V(K_{m,n})\setminus\{y_1,y_2\},\{y_1\},\{y_2\}\}.
\]
The large block is not an LD-set because it omits two vertices in the same shore, while adjoining either singleton leaves only one omitted vertex and hence gives an LD-set. Therefore \(C_L(K_{m,n})\ge3\). For \(K_{2,2}\), the four singleton blocks form an LDC-partition: every singleton has any opposite-shore singleton as a partner. Hence \(C_L(K_{2,2})=4\) once the upper bound below is noted.

For \(m,n\ge2\), the exact LD-set characterization gives \(\gamma_L(K_{m,n})=m+n-2\), so Proposition 2.8 yields \(C_L(K_{m,n})\le4\). It remains to show that a four-block LDC-partition forces \(m=n=2\). Suppose \(\{A,B,C,D\}\) is an LDC-partition and \(A\cup B\) is an LD-set. Its complement \(C\cup D\) omits at most one vertex from each shore. Since \(C\) and \(D\) are nonempty, they are singleton blocks on opposite shores; write \(C=\{x\}\subset X\) and \(D=\{y\}\subset Y\).

The block \(C\) must have a partner. If its partner is \(D\), then \(\{x,y\}\) itself is an LD-set, which requires \(m=n=2\). Otherwise, by symmetry, let \(C\) partner \(A\). Then the complement of \(A\cup C\), namely \(B\cup D\), must omit at most one vertex from each shore. Since \(D\) already contains one vertex of \(Y\), the nonempty block \(B\) can contain no vertex of \(Y\) and at most one vertex of \(X\); hence \(B\) is a singleton in \(X\). Finally, \(D\) cannot partner \(A\), because the complement would contain the two distinct \(X\)-singletons \(B\) and \(C\). If \(D\) partners either \(B\) or \(C\), their two-vertex union contains one vertex from each shore and is locating-dominating only when \(m=n=2\). Thus no four-block LDC-partition exists outside \(K_{2,2}\).

Finally, \(K_{1,1}=K_2\) has no LDC-partition because either singleton is already an LD-set, exactly as noted in the initiating paper.

## Verification
The proof above is analytic and covers every pair of positive integers \((m,n)\). The accompanying `verify.py` independently checks the LD-set predicate and exhaustively enumerates every set partition for all complete bipartite graphs with \(1\le m\le n\) and \(m+n\le9\). It also checks the explicit three-block and four-block constructions through shore size forty. These finite checks are corroborative and are not used as an infinite proof.

## Relationship to prior work
Chellali, Dobrynin, Foucaud, Golmohammadi, and Valenzuela-Tripodoro introduced locating-dominating coalitions in 2026. Their paper proves the general upper bound \(C_L(G)\le |V(G)|-\gamma_L(G)+2\), determines paths and cycles, characterizes all connected graphs with \(C_L(G)=|V(G)|\), and characterizes trees with \(C_L(T)=|V(T)|-1\). Its full text contains no occurrence of “bipartite” or “complete bipartite”. Proposition 4.1 includes the boundary cases \(P_3=K_{1,2}\) and \(C_4=K_{2,2}\) only as members of the complete \(C_L(G)=|V(G)|\) classification; it does not imply the values for larger bicliques.

The present classification therefore extends the initiating theory to the full canonical biclique family. The general upper bound alone leaves the nonstar case at \(C_L(K_{m,n})\le4\); the four-block obstruction above is the additional step that forces the uniform value three outside \(K_{2,2}\).

## Limitations
This result concerns ordinary locating-dominating coalitions, not locating-total, self-locating, solid-locating, identifying-code, or other location-domination variants. It does not classify complete multipartite graphs with three or more partite classes. The originality search cannot exclude a poorly indexed or very recent equivalent result under different terminology, although exact invariant-name, notation, biclique, star, and complete-bipartite searches were performed.

## References
1. M. Chellali, A. A. Dobrynin, F. Foucaud, H. Golmohammadi, J. C. Valenzuela-Tripodoro, “Locating-dominating coalitions in graphs”, arXiv:2602.18760v2, 2026. The first public arXiv version was posted 2026-02-21.
