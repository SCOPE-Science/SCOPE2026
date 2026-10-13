# Minimum zero forcing sets of Möbius ladders
## Finding
Let \(M_{2n}\) be the Möbius ladder on the cyclic vertex set \(\mathbb Z_{2n}\), with each vertex \(i\) adjacent to \(i-1\), \(i+1\), and \(i+n\), where all indices are taken modulo \(2n\). The known zero forcing number is \(Z(M_{2n})=4\) for every \(n\ge 3\).

The minimum zero forcing sets admit the following complete classification. For \(n=3\), one has \(M_6\cong K_{3,3}\), and the minimum zero forcing sets are exactly the complements of one vertex from each bipartition class; hence there are \(9\) of them.

For every \(n\ge4\), a four-vertex set \(S\subseteq \mathbb Z_{2n}\) is zero forcing if and only if there is a vertex \(v\in S\) such that exactly two neighbors of \(v\) lie in \(S\), and, if \(d\) is the unique vertex of \(S\) outside \(\{v\}\cup (N(v)\cap S)\), then
\[
d\in\{v-2,\ v+2,\ v+n-1,\ v+n+1\}.
\]
Equivalently, under the dihedral automorphisms of the cyclic labeling, every minimum set belongs to exactly one of the following five orbits:
\[
\begin{array}{c|c}
\text{representative} & \text{orbit size}\\ \hline
\{0,1,2,3\} & 2n\\
\{0,1,2,n\} & 4n\\
\{0,1,3,n+1\} & 4n\\
\{0,1,n-1,n\} & 2n\\
\{0,1,n,n+1\} & n.
\end{array}
\]
Consequently, for every \(n\ge4\),
\[
z(M_{2n};4)=13n,
\]
where \(z(G;k)\) denotes the number of zero forcing sets of cardinality \(k\).

## Assumptions and scope
Graphs are finite, simple, and undirected. A zero forcing process starts with the vertices of \(S\) blue and all other vertices white; a blue vertex with exactly one white neighbor may force that neighbor blue. The finding concerns the coefficient at the minimum cardinality only. It does not give the full zero forcing polynomial of \(M_{2n}\).

The scalar equality \(Z(M_{2n})=4\) is prior work and is used only to identify the classified four-sets as minimum. The originality-bearing statement is the local if-and-only-if characterization, the five dihedral types for \(n\ge4\), and the exact counts \(9\) at \(n=3\) and \(13n\) for \(n\ge4\).

## Proof
For \(n=3\), the graph is \(K_{3,3}\). A four-set is zero forcing precisely when its two omitted vertices lie in different bipartition classes: then a blue vertex in each class can force the omitted vertex in the opposite class. If both omitted vertices are in the same class, every blue vertex in the other class sees two white neighbors and no force can start. There are \(3\cdot3=9\) minimum sets.

Now assume \(n\ge4\), and let \(S\) be a zero forcing four-set. Consider its first force, say from \(v\). The Möbius ladder is cubic, so \(v\) has exactly two blue neighbors in \(S\) and one white neighbor. Let \(d\) be the fourth member of \(S\), the unique initial blue vertex outside \(\{v\}\cup(N(v)\cap S)\). Immediately after the first force, the blue set is exactly
\[
N[v]\cup\{d\}.
\]
By a cyclic translation take \(v=0\). Then
\[
N[0]=\{-1,0,1,n\}.
\]
The vertices \(-1\), \(1\), and \(n\) respectively have the two potential white-neighbor pairs
\[
\{-2,n-1\},\qquad \{2,n+1\},\qquad \{n-1,n+1\}.
\]
Thus, unless
\[
d\in\{-2,2,n-1,n+1\},
\]
each of those three vertices still has two white neighbors. The vertex \(0\) has no white neighbor. Finally, a direct check from the adjacency rule \(x\sim x\pm1,x+n\) shows that every vertex outside \(N[0]\cup\{-2,2,n-1,n+1\}\) has at most one neighbor in \(N[0]\). Hence such a vertex \(d\) also has at least two white neighbors. The process would therefore be stalled after its first force, contradicting that \(S\) is zero forcing. This proves necessity.

Conversely suppose the displayed condition holds. Reflection about \(v\) reduces the four possible positions of \(d\) to the cases \(d=v+2\) and \(d=v+n+1\). Again set \(v=0\), and write
\[
R_i=\{i,i+n\},\qquad i\in\mathbb Z_n,
\]
for the antipodal rungs. After the first force, the entire rung \(R_0\) is blue. If \(d=n+1\), then \(R_1\) is already blue as well. If \(d=2\), vertex \(1\) has blue neighbors \(0\) and \(2\), so it forces \(n+1\), again making \(R_1\) blue. Once two consecutive rungs \(R_i\) and \(R_{i+1}\) are blue, the two vertices of \(R_{i+1}\) each have exactly one white neighbor in \(R_{i+2}\), so they force all of \(R_{i+2}\). Iterating around the ladder colors every rung. Thus the local condition is sufficient.

It remains to remove the choice of the first forcing vertex. Normalize such a vertex to \(0\). There are three choices for which two of its three neighbors are initially blue and four allowed positions for \(d\), giving twelve rooted local patterns. Translation and reflection collapse these patterns into the five displayed dihedral orbits. Their stabilizers have orders \(2,1,1,2,4\), respectively, in the dihedral group of order \(4n\), so their orbit sizes are \(2n,4n,4n,2n,n\). They are pairwise distinct: the first type has no antipodal pair; the fifth has two; the third induces a path on three vertices plus an isolated vertex; among the remaining two one has its unique antipodal edge at an end of the induced four-vertex path while the other has it as the central edge. Summing the five orbit sizes gives \(13n\).

## Verification
The accompanying script `artifacts/verify.py` independently constructs \(M_{2n}\), simulates the zero forcing rule, tests the local criterion, constructs the five dihedral orbits, checks their disjointness and claimed stabilizer-derived sizes, and compares all three descriptions. It exhausts all four-subsets for \(n=3\) through \(n=12\). The computation is a finite stress test; the all-\(n\) result rests on the proof above.

## Relationship to prior work
The foundational zero forcing paper proves \(Z(M_{2n})=4\) for every \(n\ge3\), exhibiting a four-vertex forcing set and using a \(K_{3,3}\) minor for the lower bound. It does not classify all minimum sets. The later circulant-graph paper revisits the Möbius ladder as \(C_{2n}(1,n)\), again treating the scalar zero forcing number and extending the construction to torus products; its Möbius-ladder discussion does not enumerate all minimum sets. The zero forcing polynomial paper introduces \(z(G;k)\) and the associated counting polynomial, but full-text searches for “Möbius”, “Mobius”, “ladder”, and “circulant” found no treatment of this family.

Targeted searches under the aliases “Möbius ladder”, “Mobius ladder”, and \(C_{2n}(1,n)\), combined with “minimum zero forcing set”, “zero forcing polynomial”, “bases”, and “enumeration”, did not locate a published statement implying the local classification or the coefficient \(z(M_{2n};4)=13n\). This absence is evidence of noncoverage, not a proof of global novelty.

## Limitations
The five-orbit description is stated only for \(n\ge4\); the exceptional graph \(M_6\cong K_{3,3}\) is handled separately. No claim is made about coefficients \(z(M_{2n};k)\) for \(k>4\), propagation-time distributions, or other forcing variants. There remains a residual literature risk from unindexed theses, computational tables, or alternate terminology for minimum forcing bases.

## References
1. AIM Minimum Rank – Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648, doi:10.1016/j.laa.2007.10.009. Proposition 3.9 gives \(Z(M_{2n})=4\).
2. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1; *Discrete Applied Mathematics* 258 (2019), 35–48.
3. L. Duong, B. K. Kroschel, M. Riddell, K. N. Vander Meulen, A. Van Tuyl, “Maximum nullity and zero forcing of circulant graphs,” *Special Matrices* 8 (2020), 221–234, doi:10.1515/spma-2020-0106.
