# Two hexagonal faces in minimum-genus embeddings of \(K_{4,n}\)

## Finding
For every odd integer \(n\ge 5\), the complete bipartite graph \(K_{4,n}\) has an orientable cellular embedding of minimum genus with exactly two hexagonal faces and all remaining faces quadrilateral. Equivalently, the face-length multiset is \(\{6^2,4^{2n-3}\}\), and the genus is \(g=(n-1)/2\).

## Assumptions and scope
An embedding is cellular when every complementary region is an open disk. Face lengths count edge occurrences along the facial boundary walk, including multiplicity. The graph is simple and bipartite, so every facial boundary has even length at least four. The claim is an existence theorem for odd \(n\ge5\); it does not assert that every minimum-genus embedding has this face distribution or classify all other distributions.

## Proof
Write the four-vertex part as \(A=\{a_0,a_1,a_2,a_3\}\), and the other part as \(B=\{b_0,\ldots,b_{n-1}\}\). A rotation system lists the cyclic order of neighbours at every vertex; its face permutation sends a directed edge \(u\to v\) to \(v\to w\), where \(w\) is the successor of \(u\) in the rotation at \(v\).

**Base case.** For \(K_{4,5}\), use the following rotations (each list is cyclic):

- \(a_0:(b_0,b_1,b_2,b_3,b_4)\)
- \(a_1:(b_0,b_4,b_2,b_1,b_3)\)
- \(a_2:(b_0,b_3,b_4,b_2,b_1)\)
- \(a_3:(b_0,b_2,b_4,b_3,b_1)\)
- \(b_0:(a_0,a_1,a_2,a_3)\)
- \(b_1:(a_0,a_3,a_1,a_2)\)
- \(b_2:(a_0,a_2,a_3,a_1)\)
- \(b_3:(a_0,a_2,a_1,a_3)\)
- \(b_4:(a_0,a_3,a_2,a_1)\)

Face tracing gives the following nine boundary walks:

1. \(a_0b_0a_1b_4\)
2. \(b_0a_0b_1a_3\)
3. \(b_1a_0b_2a_2\)
4. \(b_2a_0b_3a_2b_4a_1\)
5. \(b_3a_0b_4a_3\)
6. \(a_1b_0a_2b_3\)
7. \(a_1b_1a_2b_0a_3b_2\)
8. \(b_1a_1b_3a_3\)
9. \(a_2b_2a_3b_4\).

Thus there are seven quadrilaterals and two hexagons. Here \(V=9\), \(E=20\), and \(F=9\), so \(V-E+F=-2=2-2g\) gives \(g=2\), equal to Ringel's genus \(\lceil(4-2)(5-2)/4\rceil=2\).

**Two-vertex extension.** Suppose a rotation system for \(K_{4,n}\) has \(b_0\)-rotation \((a_0,a_1,a_2,a_3)\). Add new vertices \(x,y\) to the second part. At \(a_0,a_2\), insert \((x,y)\) immediately before \(b_0\); at \(a_1,a_3\), insert \((y,x)\) immediately after \(b_0\). Give \(x\) rotation \((a_0,a_1,a_2,a_3)\) and \(y\) rotation \((a_0,a_3,a_2,a_1)\); leave all other rotations unchanged. Direct tracing of the face permutation shows that the old face-length multiset is preserved and four additional quadrilateral faces appear, with boundaries
\(a_0b_0a_1ya_0\), \(a_2b_0a_3ya_2\), \(xa_0ya_3x\), and \(a_1xa_2ya_1\).
The local face-permutation switch changes only the two opposite corners at \(b_0\); tracing the reconnected boundary walks shows that the old face-length multiset is unchanged. The new rotation system therefore embeds \(K_{4,n+2}\) with the same nonquadrilateral face lengths and four more quadrilaterals. Since \(V\) increases by two, \(E\) by eight, and \(F\) by four, Euler characteristic drops by two and the orientable genus increases by one.

Starting from the base case and iterating this operation proves the required face distribution for every odd \(n\ge5\). Finally, Ringel's formula gives \(g(K_{4,n})=\lceil(2(n-2))/4\rceil=(n-1)/2\) for odd \(n\); the constructed genus has exactly this value. The embeddings are therefore minimum-genus.

## Verification
The base rotation system was traced explicitly above. A standalone checker included with this record reconstructs the face permutation, verifies the nine base faces and checks the first several inductive extensions. Those finite checks are consistency checks only; the all-odd conclusion rests on the local extension argument, not on extrapolating a finite enumeration.

## Relationship to prior work
Ringel's genus formula gives the minimum orientable genus of \(K_{m,n}\). Grannell and Knor enumerate minimum-genus orientable embeddings for complete bipartite graphs with both part sizes at most seven, including the two-hexagon pattern for \(K_{4,5}\) and \(K_{4,7}\). Their enumeration is finite and does not state the uniform odd-parameter extension proved here. The contribution is the explicit local rotation-system operation that propagates this face distribution through the entire odd family.

## Limitations
The theorem proves existence of one face distribution, not that it is unique. It does not classify the other possible face-size multisets for odd \(n\), and it makes no claim about nonorientable embeddings. The local insertion is specific to the four-vertex part and should not be assumed to extend unchanged to \(K_{m,n}\) for \(m\ne4\).

## References
- G. Ringel, “Das Geschlecht des vollständigen paaren Graphen,” *Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg* 28 (1965), 139–150.
- M. J. Grannell and M. Knor, “An enumeration of minimum genus orientable embeddings of some complete bipartite graphs” (preprint dated 2010-01-08; published 2010). The nine-page preprint contains the genus/excess formula and the finite enumeration through part sizes seven.
