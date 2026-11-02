# Five quantifier-rank-four theories of finite odd graphs

## Finding
For every integer \(k\ge1\), let \(O_k\) be the simple graph whose vertices are the \(k\)-subsets of \([2k+1]\), with two vertices adjacent exactly when the subsets are disjoint. These are the classical odd graphs with their customary indices shifted by one: \(O_k\cong\operatorname{KG}(2k+1,k)\).

In first-order logic with equality and one undirected adjacency relation, for all integers \(k,\ell\ge1\),
\[
O_k\equiv_4 O_\ell\quad\Longleftrightarrow\quad
\min(k,5)=\min(\ell,5).
\]
There are exactly five rank-four theories, represented by \(O_1,O_2,O_3,O_4,O_5\), of orders \(3,10,35,126,462\). Every member has a rank-four equivalent representative with at most \(462\) vertices; this is sharp within this family. In particular the odd girth grows without bound along the indistinguishable tail.

## Assumptions and scope
All underlying sets are finite and all vertices are distinct subsets unless a repeated move is explicitly mentioned. The graph language contains equality and adjacency only, without names, counting, a distance relation, or the underlying membership relation. Quantifier rank is the greatest nesting depth of first-order quantifiers; \(G\equiv_4H\) means agreement on every sentence of rank at most four. The definition above begins with \(k=1\) (the triangle). The conventional odd graph of valency \(k+1\) is often denoted \(O_{k+1}\); this notation difference changes no statement.

## Proof
**1. Three previously selected distinct vertices.** Fix \(k\ge3\) and distinct vertices \(X,Y,Z\). Put \(u=|X\cap Y|\), \(v=|X\cap Z|\), and \(w=|Y\cap Z|\). Write \(A\) for intersection zero, \(I\) for intersection in \([1,k-2]\), and \(E\) for intersection \(k-1\). Pairwise graph adjacency means precisely state \(A\).

A fresh fourth vertex adjacent to none of \(X,Y,Z\) always exists. To see this, replace one element of \(X\) by an element outside \(X\): choose the removed element to retain a witness in each of \(Y\cap X\) and \(Z\cap X\), where applicable, and the added element to lie in any of \(Y,Z\) disjoint from \(X\). There are at most two forbidden removals. When both \(Y,Z\) are disjoint from \(X\), their intersection inside the \((k+1)\)-point complement of \(X\) has size at least \(k-1\). For \(k\ge3\) a suitable distinct replacement exists; in the cases with fewer allowed replacements it cannot equal the disjoint selected vertices. Likewise, for each selected vertex (say \(X\)), a fresh fourth vertex disjoint from \(X\) and intersecting the other two exists: the \(k+1\) possible \(k\)-subsets of the complement of \(X\) exclude at most two choices through failure of an intersection and at most two through equality; a set contained in that complement cannot also cause a failed-intersection exclusion, leaving a valid choice. Thus all four adjacency patterns involving zero or exactly one edge from the fourth vertex occur.

A fresh fourth vertex disjoint from both \(X\) and \(Y\) exists only when \(u=k-1\). In that case it is unique, namely \(W=[2k+1]\setminus(X\cup Y)\). If \(Z=W\), the candidate is already selected and does not extend the triple. If \(Z\ne W\) and \(Z\subseteq X\cup Y\), it is adjacent to all three; otherwise it is adjacent exactly to \(X,Y\). The condition \(Z=W\) is equivalent to \(v=w=0\). For three distinct \(k\)-sets, the condition \(Z\subseteq X\cup Y\) with \(u=k-1\) and \(Z\ne X,Y\) is equivalent to \(u=v=w=k-1\) and \(|X\cup Y\cup Z|=k+1\). Call the latter exceptional case **top**. An \(E,E,E\) triple not top is **star**. Both kinds occur for every \(k\ge3\): use three distinct \(k\)-subsets of a fixed \((k+1)\)-set for top, or three \(k\)-subsets containing a common \((k-1)\)-set for star.

Consequently the complete one-quantifier extension type of any ordered triple is determined by the three ordered pair labels from \(\{A,I,E\}\) and, only for \(E,E,E\), the top/star bit. This conclusion includes all fresh-vertex atomic diagrams, and repetitions of already selected vertices are forced by equality.

**2. Which triple labels extend a fixed pair.** Fix distinct \(X,Y\) with \(|X\cap Y|=u\in[0,k-1]\), and ask whether a distinct \(Z\) with prescribed intersection numbers \(v,w\in[0,k-1]\) exists. Partition the ground set into \(X\cap Y\), \(X\setminus Y\), \(Y\setminus X\), and the complement, of respective sizes \(u,k-u,k-u,u+1\). Writing \(t=|X\cap Y\cap Z|\), the four counts of elements of \(Z\) in these regions are
\[
t,\qquad v-t,\qquad w-t,\qquad k-v-w+t.
\]
These can be chosen within their capacities if and only if
\[
|v-w|\le k-u,\qquad k-u-1\le v+w\le k+u.\tag{1}
\]
Indeed the lower endpoint is \(L=\max\{0,u+v-k,u+w-k,v+w-k\}\), and the upper is \(U=\min\{u,v,w,u+v+w-k+1\}\). Under \(0\le u,v,w<k\), the condition \(L\le U\) reduces by comparing each lower candidate with each upper candidate to the three inequalities in (1). All endpoints are integers, so no integrality obstruction remains. Since \(v,w<k\), the resulting \(Z\) is different from \(X,Y\).

For \(k\ge5\), classify the possible \(v,w\) by \(A=0\), \(I=[1,k-2]\), \(E=k-1\). Applying (1), the three rows of each following matrix indicate the chosen category for \(v\), the columns those for \(w\), in the order \(A,I,E\); a \(1\) means that some such \(Z\) exists:

| \(u\) | row \(A\) | row \(I\) | row \(E\) |
|---|---|---|---|
| \(0\) | 001 | 011 | 110 |
| \(1\) | 011 | 111 | 110 |
| \(2\le u\le k-3\) | 010 | 111 | 010 |
| \(k-2\) | 010 | 111 | 011 |
| \(k-1\) | 110 | 111 | 011 |

For completeness, the table can be verified directly without any numerical cutoff: substitute singleton intervals for categories \(A,E\) and the integer interval \([1,k-2]\) for \(I\) into (1). For each of nine cells, feasibility is the intersection of a rectangle with the three strips in (1). Comparing their integer endpoints gives the displayed rows in each of the five ranges for \(u\). All five ranges are nonempty when \(k\ge5\). Their matrices are pairwise different. The sole extra top/star flag occurs in the \((E,E)\) cell of the final row, with both realizations, as proved in step 1.

The rank-two extension type of an ordered pair (two remaining moves) is determined by its adjacency and the set of one-extension types of its possible ordered triples. Thus the five matrices, together with the uniform top/star refinement, prove that the set of pair rank-two types attained in \(O_k\) is exactly the same for every \(k\ge5\). Vertex transitivity then shows that the rank-three type of a single named vertex is the same for every such graph. The four-round Ehrenfeucht--Fraïssé characterization proves \(O_k\equiv_4O_\ell\) whenever \(k,\ell\ge5\).

**3. Sharpness and small members.** For \(k=3,4\), the same formula (1), with the top/star rule from step 1, gives respectively three and four different rank-two pair types. Their three-row profiles for the \(u\)-values are:

- \(k=3\): `001/011/110`, `011/111/111`, `110/111/011`;
- \(k=4\): `001/011/110`, `011/111/110`, `010/111/011`, `110/111/011`.

For \(k=1\), every distinct pair is adjacent and only one pair type occurs. For \(k=2\), the graph is the Petersen graph: there are both adjacent and nonadjacent distinct pairs, and by its pair transitivity at each intersection size there are exactly two rank-two pair types. Therefore the numbers of different rank-two pair types extending a fixed vertex are respectively \(1,2,3,4,5\) in the five parameter regimes \(k=1,2,3,4,k\ge5\). A rank-four equivalence must preserve this number by the four-round game recursion. Hence no two of the five regimes are rank-four equivalent. The smallest representative of the final regime has \(\binom{11}{5}=462\) vertices, completing the sharpness proof.

## Verification
A standalone exact checker, `verify_odd_graphs.py`, computes the full fourth-point adjacency-pattern signature for each permutation orbit of ordered triples, and recursively computes the two-remaining-move pair signatures. It independently reconstructs the same signatures from direct adjacency bitsets for every \(1\le k\le6\). It confirms the five regimes by orbit enumeration for \(1\le k\le12\) and cross-checks the symbolic interval-profile table for \(5\le k\le60\). The actual output is in `verification_output.txt`. These bounded calculations check the proof and small cases; the unlimited \(k\ge5\) statement is proved by equation (1), the exact fourth-point extension classification, and the interval table, not inferred from finite sampling.

## Relationship to prior work
Pikhurko and Verbitsky (2010, arXiv:1003.4865) establish the general Ehrenfeucht--Fraïssé and finite-graph logical-complexity framework; the inspected survey does not give this odd-graph rank-four classification. Van Dam and Haemers (2010 working-paper version; arXiv:1202.2300 is a later public preprint of the published paper) treat generalized odd graphs using odd girth, eigenvalues, and distance regularity, not bounded-rank first-order equivalence. Standard odd-graph constructions supply the subset model. Existing generic intersection-graph stabilization when the ground-set size is at least four times the vertex-set size does not apply to the near-critical \(2k+1\) ground-set regime here. These are comparisons of statements, not a claim that a negative search proves historical priority.

## Limitations
The classification concerns only ordinary first-order graph logic through quantifier rank four. It does not assert equivalence at rank five, finite-variable logical equivalence with counting, or logical definability of the whole graph family. The source search cannot rule out an implicit equivalent theorem or an unindexed older result. No independent mathematical audit has been performed.

## References
1. O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: a survey*, arXiv:1003.4865 (first public version 2010-03-25), full author-posted text at `https://opikhurko.warwick.ac.uk/E/PikhurkoVerbitsky11cm.pdf`.
2. E. R. van Dam and W. H. Haemers, *An odd characterization of the generalized odd graphs*, CentER Discussion Paper 2010-47 (April 2010); arXiv:1202.2300, full text at `https://arxiv.org/pdf/1202.2300`.
3. N. Biggs, *Some odd graph theory*, Annals of the New York Academy of Sciences 319 (1979), 71–81, doi:10.1111/j.1749-6632.1979.tb32775.x. The full text of this last historical reference was not inspected.
