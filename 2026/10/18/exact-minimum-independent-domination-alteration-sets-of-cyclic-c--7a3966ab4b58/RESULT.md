# Exact minimum independent-domination alteration sets of cyclic clique expansions

## Finding
For integers \(n\ge 3\) and \(q\ge1\), let \(X_{n,q}=C_n[K_q]\), the lexicographic product of an \(n\)-cycle with a \(q\)-vertex clique. Let \(i(H)\) be the minimum cardinality of a maximal independent set in \(H\), with \(i(\varnothing)=0\). Define the independent-domination alteration threshold by
\[
\tau(H)=\min\{|D|:D\subseteq V(H),\ i(H-D)\ne i(H)\}.
\]
For \(X_{n,q}\), write \(N_-(n,q)\) and \(N_+(n,q)\) for the numbers of deletion sets of cardinality exactly \(\tau(X_{n,q})\) which decrease and increase \(i\), respectively.

**Theorem.** For all \(n\ge3\) and \(q\ge1\),
\[
\tau(X_{n,q})=q\begin{cases}
1,&n\equiv1\pmod3,\\
2,&n\equiv2\pmod3,\\
3,&n\equiv0\pmod3.
\end{cases}
\]
Every minimum altering set consists of whole clique fibers, and is the lift of a unique minimum altering set of \(C_n\). With \(k\ge1\), the complete directional counts are
\[
\begin{array}{c|c|c}
n&N_-(n,q)&N_+(n,q)\\\hline
3k+1&3k+1&0\\
3k+2&\dfrac{(3k+2)(k+1)}2&0\\
3k&\dfrac{k^2(k+1)}2&\dfrac{k^2(k-1)}2.
\end{array}
\]
In particular, \(X_{3k,q}\) has exactly \(k^3\) minimum altering sets, independently of \(q\). All directional changes at the minimum threshold have magnitude one.

More precisely, view the deleted complete fibers as marked vertices on the base cycle. In the class \(n=3k+2\), a marked pair decreases \(i\) precisely when its two intervening runs of unmarked vertices both have length divisible by \(3\). In the class \(n=3k\), a marked triple decreases \(i\) precisely when all three cyclic runs are divisible by \(3\); it increases \(i\) precisely when all three runs are congruent to \(1\pmod3\). Every other marked pair/triple of the relevant size is neutral. For \(n=3k+1\), every one-fiber deletion decreases \(i\).

## Assumptions and scope
All graphs are finite simple undirected labeled graphs. The fibers of \(X_{n,q}\) are the disjoint cliques \(F_j=\{(j,a):1\le a\le q\}\), indexed by \(j\in\mathbb Z/n\mathbb Z\). Distinct vertices in one fiber are adjacent, and every vertex in \(F_j\) is adjacent to every vertex in \(F_{j-1}\) and \(F_{j+1}\). The labels make all deletion sets distinct; no quotient by graph automorphisms is taken. The theorem includes the triangle \(C_3\) and singleton fibers \(q=1\). The empty graph has independent domination number zero.

## Proof
**1. Exact clique-fiber deletion principle.** Consider any finite simple graph \(G\) and the equal clique expansion \(G[K_q]\). For a deleted set \(D\), let \(S(D)\subseteq V(G)\) consist of base vertices whose whole fibers are deleted. In \(G[K_q]-D\), each surviving fiber is a nonempty clique, and two surviving fibers are completely joined exactly when their base vertices are adjacent. Any maximal independent set has exactly one representative from each fiber it meets; its set of base indices is a maximal independent set of \(G-S(D)\). Conversely every maximal independent set of \(G-S(D)\) lifts to a maximal independent set in the surviving expansion by choosing one vertex in each represented fiber. Hence
\[
i(G[K_q]-D)=i(G-S(D)).\tag{1}
\]
If \(t=\tau(G)\), changing the left side requires \(|S(D)|\ge t\). Each member of \(S(D)\) costs \(q\) deleted vertices, so \(|D|\ge qt\). Lifting any minimum altering set of \(G\) by deleting its whole fibers attains \(qt\). Equality forbids any deletion outside those whole fibers, so the correspondence of minimum altering sets is bijective. This proves the transfer and reduces all remaining assertions to the base cycle.

**2. Cycle gap identity.** A path \(P_\ell\) has \(i(P_\ell)=\lceil\ell/3\rceil\) for every integer \(\ell\ge0\): each vertex of an independent dominating set covers at most three consecutive vertices, while choosing every third vertex with a boundary adjustment attains this bound. Independent domination is additive over components. Thus \(i(C_n)=\lceil n/3\rceil\). If \(D=\{d_1,\ldots,d_s\}\) is a nonempty deleted vertex set listed in cyclic order, let \(a_j\ge0\) denote the number of undeleted vertices strictly between consecutive deleted vertices. Then \(\sum_j a_j=n-s\), the remaining graph is the disjoint union of paths of those lengths, and
\[
i(C_n-D)=\sum_{j=1}^s\left\lceil\frac{a_j}{3}\right\rceil.\tag{2}
\]
The formula also holds for consecutive deleted vertices, when a run has length zero, and for deleting all vertices.

**3. Minimum thresholds and gap classes.** If \(n=3k+1\), deleting one vertex leaves \(P_{3k}\), reducing \(i\) from \(k+1\) to \(k\); every one-vertex deletion is equivalent. If \(n=3k+2\), one deletion leaves \(P_{3k+1}\), preserving \(i=k+1\). For two deleted vertices the gap lengths sum to \(3k\), and their residues modulo \(3\) are either \((0,0)\) or \((1,2)\) up to order. Identity (2) gives value \(k\) in the first case and \(k+1\) in the second. Thus only the first case alters \(i\), always downward.

If \(n=3k\), one deletion leaves \(P_{3k-1}\) and preserves \(i=k\). With two deletions the gap lengths sum to \(3k-2\); their residues are \((0,1)\) or \((2,2)\) up to order, both yielding \(i=k\) by (2). For three deleted vertices the gap lengths sum to \(3k-3\). Their residue multisets modulo \(3\) are exactly \((0,0,0)\), \((1,1,1)\), \((2,2,2)\), and \((0,1,2)\). Substitution in (2) gives respectively \(k-1\), \(k+1\), \(k\), and \(k\). The first and second cases are exactly the decreasing and increasing minimum sets.

**4. Labeled enumeration.** For \(n=3k+2\), choose a starting deleted vertex in \(n\) ways and let the next deleted vertex follow a run of \(3b\) surviving vertices. Since the complementary run also must be divisible by \(3\), \(b\) can be any integer in \(\{0,\ldots,k\}\). This gives \(n(k+1)\) oriented pairs, each unordered pair counted twice, proving \(N_-=n(k+1)/2\).

For \(n=3k\), a decreasing triple has run lengths \(a_j=3b_j\), with \(b_j\ge0\) and \(b_1+b_2+b_3=k-1\). The number of ordered nonnegative triples is \(\binom{k+1}{2}\). Choose a starting marked vertex in \(n\) ways; divide by three because every unordered marked triple has three choices of start. The decreasing count is
\[
\frac{n}{3}\binom{k+1}{2}=\frac{k^2(k+1)}2.
\]
An increasing triple has run lengths \(a_j=3b_j+1\), with \(\sum b_j=k-2\). For \(k\ge2\), there are \(\binom{k}{2}\) ordered compositions, giving
\[
\frac{n}{3}\binom{k}{2}=\frac{k^2(k-1)}2.
\]
For \(k=1\) this class is impossible and the same formula gives zero. Summing the two counts yields \(k^3\). In \(n=3k+1\), all \(n\) singleton deletions decrease the value. Finally, (1) lifts the exact classifications and counts to every \(q\ge1\). This completes the proof.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library. It independently checks all base-cycle gap classifications and counts for \(3\le n\le30\), direct independent-dominating-set enumeration of the cycle deletions for \(3\le n\le11\), the fiber transfer on all labeled base graphs through order four with \(q=2\) (16,932 base-graph/deletion combinations), and direct clique-cycle deletion enumeration for six \((n,q)\) pairs. It reports `VERIFY_OK`. These finite checks test implementation and small boundaries; the infinite statement rests on the proof above, not on extrapolation.

## Relationship to prior work
Jahari and Alikhani proved a lexicographic-product identity for the independent domination polynomial, \(D_i(G[H],z)=D_i(G,D_i(H,z))\) (Theorem 2.3 of arXiv:1808.07369). This implies the already-known identity \(i(G[K_q])=i(G)\), but it does not itself enumerate the deletion sets that first change this value. Wu and collaborators investigated single-vertex independent-domination stability of unicyclic graphs. Alikhani, Mehraban, Zakharov, and Golmohammadi determined the cycle alteration thresholds \(1,2,3\) by residue class (Proposition 2.8 of arXiv:2311.01733); the numerical thresholds on the **base cycle** are therefore prior work, not the contribution here.

The contribution is the complete labeled classification, directional split, cubic total, and exact count of **all minimum alteration sets**, with a full-fiber lifting principle for clique expansions. Corollary 4.4 of arXiv:2311.01733 states a general stability formula for lexicographic products. Applied literally to \(C_5[K_2]\), it would predict threshold \(2\), whereas identity (1) and a direct exhaustive check give \(4\): changing \(i\) requires deleting both full neighboring two-vertex fibers. Thus that general formula cannot supply a covering implication for this result. This explicit conflict is recorded to distinguish mathematical statements, not to resolve the status of the earlier publication.

## Limitations
All counts are for individually labeled vertex-deletion sets, not orbits under cycle symmetries. Only minimum-cardinality altering sets are enumerated; this theorem makes no claim about the full distribution of deletion responses at larger deletion sizes. The result concerns equal **clique** substitutions; replacing each fiber by an arbitrary graph generally invalidates the simple projection identity. Literature coverage is limited to the specifically inspected sources and searches; unindexed equivalent formulations may exist. The previous lexicographic-product stability corollary noted above is an unresolved literature-level inconsistency, not a dependency of the self-contained proof.

## References
1. S. Jahari and S. Alikhani, *On the independent domination polynomial of a graph*, arXiv:1808.07369 (first posted 21 August 2018), especially Theorem 2.3 and the clique-expansion discussion. https://arxiv.org/pdf/1808.07369
2. P. Wu, H. Jiang, S. Nazari-Moghaddam, S. M. Sheikholeslami, Z. Shao, and L. Volkmann, *Independent Domination Stable Trees and Unicyclic Graphs*, Mathematics **7** (2019), article 820, published 5 September 2019, doi:10.3390/math7090820. https://www.mdpi.com/2227-7390/7/9/820
3. S. Alikhani, M. Mehraban, A. Zakharov, and H. R. Golmohammadi, *Independent domination stability in graphs*, arXiv:2311.01733 (first posted 3 November 2023), especially Proposition 2.8 and Theorem 4.3/Corollary 4.4. https://arxiv.org/pdf/2311.01733
