# All maximal intersecting families of rank-two partition flats

## Finding
Let \(N\ge4\), and regard every rank-two flat of the graphic matroid of the complete graph \(K_N\) as a set of unordered vertex pairs (atoms). A rank-two flat is either the three edges of a triangle, or two disjoint edges. A family is intersecting if any two flats share an edge, and **maximal** if it is inclusion-maximal with this property.

**Theorem.** For \(N\ge6\), every maximal intersecting family is exactly one of the following four types:

1. **Star:** every flat containing one fixed edge; size \(\binom{N-1}{2}\).
2. **Three disjoint edges:** for three pairwise vertex-disjoint edges \(e,f,g\), the three two-edge flats \(\{e,f\},\{e,g\},\{f,g\}\); size \(3\).
3. **Triangle and a remote edge:** for a triangle \(T\) and an edge \(g\) vertex-disjoint from \(T\), the four flats comprising \(T\) and \(\{g,h\}\) for each of the three edges \(h\) of \(T\); size \(4\).
4. **Four vertices and a matching:** the four triangle flats on a fixed four-vertex set, together with one of its three two-edge perfect matchings; size \(5\).

Distinct choices give distinct families. The number of maximal intersecting families is therefore
\[
\boxed{\binom{N}{2}+15\binom{N}{6}+10\binom{N}{5}+3\binom{N}{4}}.
\]
More precisely, the four summands count stars and maximal families of sizes \(3\), \(4\), and \(5\), respectively. At \(N=5\), the same classification holds after omitting the three-disjoint-edge type, giving \(10\) stars, \(10\) size-four families, and \(15\) size-five families. At \(N=4\), only the three size-five families are maximal; the three-member stars are extendable. Consequently the smallest size of a maximal intersecting family is \(5\) for \(N=4\), \(4\) for \(N=5\), and \(3\) for every \(N\ge6\).

## Assumptions and scope
All graphs are simple; the ground vertex set has size \(N\ge4\). Flats are closed edge sets in the rank-\(N-1\) graphic matroid of \(K_N\); the intersection condition is nonempty common edge, equivalently rank at least one of the meet. The three-edge triangle is identified with its edge set, not merely with its vertex set. A full star consists of all rank-two flats containing a given edge. Families are not quotiented by vertex relabeling.

## Proof
**Unique two-edge closure.** Any two distinct edges \(e,f\) of \(K_N\) determine exactly one rank-two flat: their three-edge triangle when they meet at a vertex, or the two-edge set \(\{e,f\}\) when vertex-disjoint. Thus two distinct rank-two flats intersect in **at most one** edge.

**A nonstar triple.** Let \(\mathcal F\) be an intersecting family without an edge common to every member. Choose distinct \(A,B\in\mathcal F\), with unique common edge \(e\). Select \(C\in\mathcal F\) not containing \(e\). Write \(f=A\cap C\), \(g=B\cap C\); these are single edges and are distinct from each other and from \(e\), since otherwise two of \(A,B,C\) would have two common edges. The three flats are uniquely determined by the pairs \(\{e,f\}\), \(\{e,g\}\), \(\{f,g\}\). Analyze the three-edge graph \(H=\{e,f,g\}\).

**Case 1: all three edges of \(H\) are disjoint.** Then \(A,B,C\) are the three two-edge flats on \(e,f,g\). Any rank-two flat meeting all three must contain two among \(e,f,g\), hence is one of \(A,B,C\). This is the size-three family.

**Case 2: exactly one pair of edges of \(H\) meets.** Call that pair \(e,f\), with third edge \(g\) disjoint from both. The corresponding three flats are a triangle \(T\) on the endpoints of \(e,f\), and the two matchings \(\{e,g\}\), \(\{f,g\}\). Any additional flat meeting both matchings either contains \(g\), or contains both \(e,f\). In the latter case it equals \(T\); in the former it can meet \(T\) only by pairing \(g\) with one of the three edges of \(T\). Thus exactly one new flat can be adjoined, namely \(\{g,h\}\), where \(h\) is the third triangle edge. This gives the size-four family.

**Case 3: exactly two pairs of edges of \(H\) meet.** Then their union is a path with four vertices, say \(ab,bc,cd\). Its three pair-generated flats are the triangles \(abc\), \(bcd\), and the two-edge flat \(\{ab,cd\}\). Every flat meeting all three is one of these or one of the triangles \(abd\) and \(acd\): it must use \(ab\) or \(cd\) to meet the matching, and the other triangle forces its remaining edge. These five flats intersect pairwise and constitute the size-five type.

**Case 4: all three pairs of edges of \(H\) meet.** The edges cannot form a triangle: every pair would determine the same flat, contradicting the distinctness of \(A,B,C\). Hence they form a three-edge star on four vertices. The initial flats are three of the four triangular flats on those vertices. A flat meeting all three must be either their fourth triangle, or one of the three perfect-matching flats on those four vertices. The three matchings are mutually nonintersecting as edge sets; the fourth triangle intersects each. Therefore every maximal extension is exactly the four triangles plus one matching, the size-five type.

Every nonstar intersecting family is a subset of one of these maximal configurations; each listed configuration is itself intersecting and inclusion-maximal (as shown by the exhaustive possible-extension descriptions). This proves the classification of nonstar maximal families for every admissible \(N\).

**Stars and small boundaries.** A full star at edge \(e\) has \(N-2\) triangle flats and \(\binom{N-2}{2}\) two-edge matching flats, totaling \(\binom{N-1}{2}\). At \(N\ge5\), its size is at least six, whereas the preceding classification bounds every nonstar intersecting family by five; hence a full star is maximal. At \(N=4\), a three-member full star is contained in one of the displayed size-five families, and is not maximal. This completes the boundary classification.

**Counting.** Stars: \(\binom N2\). Three disjoint edges: \(15\binom N6\), since there are fifteen perfect matchings of six chosen vertices. Triangle and a remote edge: \(\binom N3\binom{N-3}2=10\binom N5\). Four vertices with one perfect matching: \(3\binom N4\). Their supports and displayed structures distinguish all choices, completing the count. \(\square\)

## Verification
The included standalone standard-library program `verify.py` constructs flats independently as triangles and disjoint edge pairs, forms their intersection graph, and uses bitset maximal-clique enumeration to check **all** maximal families for \(N=4,5,6,7\). It checks the predicted distributions exactly, and separately verifies that every pair of distinct edges lies in precisely one rank-two flat. Run `python verify.py`; the final line is `VERIFY_OK`. Finite enumeration is corroboration, not a substitute for the case-complete proof above.

## Relationship to prior work
Cao, Liao and Zhang (arXiv:2608.05951, first posted 2026-08-06) study Erdős–Ko–Rado and Hilton–Milner extremal cardinalities of intersecting families in the partition lattice, including strong large-ground-set results. A secondary review describes a rank-two lemma bounding nonstar intersecting families by five; that bound alone does not enumerate or classify **all inclusion-maximal** families, including smaller sizes three and four. The present statement is precisely the entire maximal-family size distribution and total count, rather than just an extremal-size bound. The arXiv abstract and bibliographic metadata were available; full primary text could not be retrieved. Consequently, earlier containment in a stronger full-text classification remains a material historical-priority risk.

## Limitations
The result is specific to rank-two flats in the graphic matroid of the complete graph and pairwise rank-one intersections. It does not address higher flat ranks or higher intersection thresholds. Publication priority has not been independently established; a relevant 2026 primary manuscript was not fully accessible. No independent mathematical audit has been performed.

## References
Cao, Mengyu; Liao, Jiaqi; Zhang, Haixiang. *Erdős--Ko--Rado and Hilton--Milner Theorems in the Partition Lattice*. arXiv:2608.05951, first posted 2026-08-06. https://arxiv.org/abs/2608.05951

Secondary literature overview: https://www.themoonlight.io/en/review/erds-ko-rado-and-hilton-milner-theorems-in-the-partition-lattice (consulted only to identify possible overlap, not as a substitute for the primary proof).
