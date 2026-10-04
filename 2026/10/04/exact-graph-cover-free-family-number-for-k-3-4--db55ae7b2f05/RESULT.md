# Exact graph cover-free-family number for \(K_{3,4}\)
## Finding
For the graph cover-free-family number introduced by Parida and Moura,
\[
t(K_{3,4})=6.
\]
Moreover, among complete bipartite graphs \(K_{a,b}\) with \(2\le a\le b\), this is a minimum-order instance for which the coloring-construction bound
\[
t(K_{a,b})\le t(1,a)+t(1,b)
\]
is strict.  For \(K_{3,4}\), that published bound is \(7\), while the exact value is \(6\).

## Assumptions and scope
A \(G\)-CFF on a ground set \(X\) assigns a distinct block \(B_v\subseteq X\) to each vertex \(v\in V(G)\).  For every edge \(uv\), the blocks \(B_u\) and \(B_v\) are incomparable, and \(B_u\cup B_v\) contains no block \(B_w\) with \(w\notin\{u,v\}\).  The parameter \(t(G)\) is the minimum possible \(\lvert X\rvert\).  The claim concerns only complete bipartite graphs with both parts of size at least two; it does not assert a general formula for \(t(K_{a,b})\).

## Proof
Let the three vertices in one part of \(K_{3,4}\) receive the blocks
\[
\{5,6\},\quad \{1,3\},\quad \{2,4\},
\]
and let the four vertices in the other part receive
\[
\{3,4,6\},\quad \{1,2,6\},\quad \{1,4,5\},\quad \{2,3,5\}.
\]
A direct check shows that every cross-part pair is incomparable and that the union of every cross-part pair contains none of the other five blocks.  Hence \(t(K_{3,4})\le6\).

For the lower bound, suppose the ground set had at most five points.  Write the incidence matrix with one column for each of the seven vertices.  For every edge \(uv\), incomparability requires a row with \(u=1,v=0\) and a row with \(v=1,u=0\).  For each third vertex \(w\notin\{u,v\}\), the condition \(B_w\not\subseteq B_u\cup B_v\) requires a row with \(w=1,u=v=0\).  Conversely, these row witnesses are sufficient for the \(G\)-CFF conditions.  For \(K_{3,4}\) there are exactly \(84\) such requirements.

The accompanying verifier enumerates all \(2^7=128\) binary row patterns and solves this finite covering problem by complete branching with exact integer bitsets.  Strictly dominated row patterns are discarded only when every requirement they witness is also witnessed by one dominating pattern; replacement therefore cannot destroy a cover.  The search exhausts all covers by at most five rows and finds none, while it finds and directly rechecks a six-row cover.  Thus \(t(K_{3,4})\ge6\), proving equality.

For the minimum-order statement, the same exact search gives
\[
t(K_{2,2})=4,\quad t(K_{2,3})=5,\quad t(K_{2,4})=6,\quad t(K_{3,3})=6.
\]
These are precisely the complete bipartite graphs with both parts at least two and fewer than seven vertices, and each value equals \(t(1,a)+t(1,b)\).  Hence no smaller-order complete bipartite graph makes the published coloring bound strict.

## Verification
Run `python3 verify.py`.  The verifier uses only the Python standard library.  It reconstructs the necessary-and-sufficient row-witness system, proves nonexistence at five rows by exhaustive branching, rechecks a six-point construction directly from its blocks, and repeats the exact calculation for all smaller complete bipartite graphs relevant to the minimum-order statement.  The archived output is in `verify_output.txt`.

## Relationship to prior work
Parida and Moura introduced graph cover-free families and proved the general complete-bipartite construction \(t(K_{n_1,n_2})\le t(1,n_1)+t(1,n_2)\).  Their full September 2026 revision lists exact values for paths, cycles, wheels, and complete graphs, but not for non-star complete bipartite graphs; it also identifies exact values or bounds for additional graph classes as a further direction.  The present value \(t(K_{3,4})=6\) strictly improves their bound \(7\) on this natural test graph.  published-finding corpus searches for the exact graph, the \(G\)-CFF terminology, the equivalent \(G\)-disjunct-matrix formulation, and complete-bipartite exact values found no prior item covering this statement.  The closest published-finding corpus record concerns exact small values for paths, cycles, and wheels, which does not imply the complete-bipartite result.

## Limitations
The lower bound is an exact finite exhaustive proof, not a structural formula for arbitrary complete bipartite graphs.  No claim is made about \(t(K_{a,b})\) beyond the values explicitly stated.  Public searches cannot rule out unpublished work; the originality assessment is therefore relative to the inspected public literature and published-finding corpus records.

## References
1. P. Parida and L. Moura, *Cover-free families on graphs*, arXiv:2605.12634, first public version 12 May 2026; revised 24 September 2026.  In particular, Definition 4.1 and Corollary 4.7 give the graph-CFF/disjunct formulation and the complete-bipartite coloring upper bound.
