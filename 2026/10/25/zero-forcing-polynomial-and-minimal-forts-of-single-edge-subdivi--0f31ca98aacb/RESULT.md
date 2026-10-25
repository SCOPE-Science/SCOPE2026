# Zero-forcing polynomial and minimal forts of single-edge-subdivided complete bipartite graphs

## Finding
For integers \(p,q\ge3\), construct \(H_{p,q}\) by subdividing one edge of \(K_{p,q}\) exactly once. Write \(\mathcal Z(G;z)=\sum_{S\text{ zero forcing}}z^{|S|}\). Then
\[
\boxed{\mathcal Z(H_{p,q};z)=z^{p+q-2}\bigl((3pq-p-q)+(pq+2p+2q-2)z+(p+q+1)z^2+z^3\bigr).}
\]
Moreover, the inclusion-minimal forts of \(H_{p,q}\) are completely classified below. The zero-forcing number is \(p+q-2\); the number of minimum zero-forcing sets is \(3pq-p-q\). This is an exact description at all cardinalities, not just a numerical minimum.

## Assumptions and scope
Let the original bipartition be \(A=\{a_0,\ldots,a_{p-1}\}\), \(B=\{b_0,\ldots,b_{q-1}\}\). Replace the original edge \(a_0b_0\) with \(a_0s\) and \(sb_0\), where \(s\) is a new vertex. All other original cross edges remain. Put \(A'=A\setminus\{a_0\}\) and \(B'=B\setminus\{b_0\}\). The graph is simple and has \(N=p+q+1\) vertices. Since \(p,q\ge3\), each of \(A'\) and \(B'\) contains at least two false twins.

A zero-forcing process begins with a blue set \(S\); a blue vertex having exactly one white neighbor may color that neighbor blue. Success means all vertices eventually become blue. A *fort* is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A blue set is zero forcing exactly when its white complement contains no fort: failure leaves a nonempty terminal white fort, and any initially white fort cannot lose its first vertex by a force.

## Proof
**Necessity and forbidden white configurations.** Since vertices of \(A'\) have identical open neighborhoods, any two of them form a fort; the same holds for \(B'\). Therefore the white set \(W\) of a zero-forcing configuration contains at most one vertex from each of \(A'\) and \(B'\).

Write \(x=a_0\), \(y=b_0\), \(t=s\), and represent the possible white vertices from the two twin classes by \(u\in A'\), \(v\in B'\). These labels represent actual selected vertices whenever present, not formal vertices replacing the classes. The following sets are forts, as a direct check of their neighborhoods shows:
\[
\{x,t,u\},\qquad \{y,t,v\},\qquad \{x,y,u,v\}.
\]
For instance, outside \(\{x,t,u\}\), the vertex \(y\) sees exactly \(t,u\), each \(b_j\in B'\) sees exactly \(x,u\), and other vertices see none or two; the symmetric statement holds for \(\{y,t,v\}\). Outside \(\{x,y,u,v\}\), the vertex \(t\) sees \(x,y\), every other vertex in \(A'\) sees \(y,v\), and every other vertex in \(B'\) sees \(x,u\). Thus a successful \(W\) contains none of those three patterns.

**Sufficiency.** Conversely suppose \(W\) contains at most one member of each twin class and avoids these three forbidden patterns. Any four of the five possible representatives \(x,y,t,u,v\) contain a forbidden pattern: omitting \(t\) leaves \(\{x,y,u,v\}\), while each other choice of the omitted representative leaves either \(\{x,t,u\}\) or \(\{y,t,v\}\). Therefore \(|W|\le3\).

When \(|W|=3\), the eight possible admissible types are precisely
\[
\{x,y,t\},\quad\{x,y,u\},\quad\{x,y,v\},\quad\{x,t,v\},\quad
\{y,t,u\},\quad\{x,u,v\},\quad\{y,u,v\},\quad\{t,u,v\}.
\]
All eight are zero forcing. Here is a concrete forcing schedule for each, in the same order. An arrow \(a\to b\) denotes a valid blue-to-white force; use an initially blue \(a^*\in A'\setminus\{u\}\) or \(b^*\in B'\setminus\{v\}\) whenever an alternative is needed:

| Initially white | Valid force sequence |
| --- | --- |
| \(\{x,y,t\}\) | \(a^*\to y,\ b^*\to x,\ x\to t\) |
| \(\{x,y,u\}\) | \(a^*\to y,\ t\to x,\ b^*\to u\) |
| \(\{x,y,v\}\) | \(b^*\to x,\ t\to y,\ a^*\to v\) |
| \(\{x,t,v\}\) | \(a^*\to v,\ y\to t,\ t\to x\) |
| \(\{y,t,u\}\) | \(b^*\to u,\ x\to t,\ t\to y\) |
| \(\{x,u,v\}\) | \(y\to u,\ t\to x,\ a^*\to v\) |
| \(\{y,u,v\}\) | \(x\to v,\ t\to y,\ b^*\to u\) |
| \(\{t,u,v\}\) | \(a^*\to v,\ b^*\to u,\ x\to t\) |

For the second, third, and other lines where \(u\) or \(v\) is absent, the designated \(a^*\) or \(b^*\) can be any initially blue member of the corresponding class. Such choices exist because each class has at least two vertices. If \(|W|\le2\), the white set is a subset of one of the eight admissible triples: there are three possible completions of a fixed pair among five representatives, and at most two prohibited triples. Zero forcing remains possible when fewer vertices are initially white. This proves the exact characterization for every \(S\).

**Minimal forts.** The forbidden families are precisely
\[
\binom{A'}2,\quad \binom{B'}2,\quad
\{\{x,t,u\}:u\in A'\},\quad
\{\{y,t,v\}:v\in B'\},\quad
\{\{x,y,u,v\}:u\in A',\ v\in B'\}.
\]
Each listed set is a fort. They are pairwise inclusion-incomparable. Every nonforcing white set contains a listed fort by the characterization just proved, so these are *all* inclusion-minimal forts. Their total number is
\[
\binom{p-1}{2}+\binom{q-1}{2}+(p-1)+(q-1)+(p-1)(q-1).
\]

**Enumeration.** The permitted initial white sets have sizes at most three. There is one empty set and \(N=p+q+1\) singletons. Among the \(\binom N2\) pairs, only the \(\binom{p-1}{2}+\binom{q-1}{2}\) twin pairs are forbidden, leaving \(pq+2p+2q-2\) admissible pairs. For three whites, tally the eight types above, using \(p-1\) choices of \(u\) and \(q-1\) choices of \(v\). The count is
\[
1+2(p-1)+2(q-1)+3(p-1)(q-1)=3pq-p-q.
\]
A forcing set with \(k\) white vertices has \(N-k\) blue vertices. Substituting these four counts proves the polynomial and its minimum exponent.

## Verification
The standalone script `verify_subdivision.py` independently constructs the original graph adjacency, applies the zero-forcing color-change rule to every vertex subset, and compares the resulting coefficients with the closed polynomial and the proposed fort-avoidance criterion. It checks twelve rectangular parameter choices with \(p,q\ge3\), a total of \(22{,}656\) subsets. On four small parameter pairs, it additionally computes every fort from its original neighborhood definition and compares the inclusion-minimal families. The package includes `verification_output.txt`, recorded from running this exact script. All tests pass. Exhaustive tests on finitely many graphs are corroboration; the preceding argument proves the assertions for the full infinite family.

## Relationship to prior work
Boyer and collaborators introduced the zero-forcing polynomial and proved the established formula
\[
\mathcal Z(K_{p,q};z)=pqz^{p+q-2}+(p+q)z^{p+q-1}+z^{p+q}
\]
for the original complete bipartite graph. The same minimum cardinality, \(p+q-2\), persists after subdivision, but its number of minimizers changes from \(pq\) to \(3pq-p-q\). The coefficient changes cannot be deduced by applying that complete-multipartite result to the subdivided graph, which is not complete multipartite. Its original even four-cycles through the chosen edge become odd five-cycles.

Menon and Singh study bounds on zero-forcing-set counts under several graph operations, but their inspected results do not state this all-coefficient one-edge-subdivision identity or its fort classification. A published exact theorem for chain graphs with no singleton twin classes also does not cover the present graphs, which are nonbipartite. A separate published classification for all-edge subdivisions of complete graphs concerns a different operation and a different family. No inspected source directly entails the displayed polynomial or the five-type minimal-fort classification. This is a targeted priority comparison, not a proof of global novelty.

## Limitations
The assertions assume \(p,q\ge3\). When one original part has size two, some required blue alternative vertices may not exist and the formula is not asserted. Only one chosen edge is subdivided once; this is not a formula for arbitrary partial subdivisions, subdivisions of all edges, or noncomplete bipartite bases. Publication searches may miss differently named families or unindexed theses. Verification is independent of the stated fort criterion at the implementation level but is finite; an independent mathematical audit has not been performed.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1 (26 January 2018), Proposition 4 and Section 4, https://arxiv.org/pdf/1801.08910 .
2. K. Menon and A. Singh, “Exploring the Influence of Graph Operations on Zero Forcing Sets,” arXiv:2405.01423v1 (2 May 2024), Sections 1–3, https://arxiv.org/pdf/2405.01423 .
