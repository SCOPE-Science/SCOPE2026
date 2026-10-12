# First finite endpoint departure in the three-class red-blue star family

## Finding
Let \(S_{2,1}\) be the four-vertex red-blue star with a distinguished center, two **ordered** red leaves, and a blue leaf. For a simple \(n\)-vertex graph \(G\), let \(N(G)\) count its injective semi-induced labeled embeddings. Let \(H_{a,b,c}\) have disjoint classes \(A,B,C\) of sizes \(a,b,c\geq 0\): \(A\cup B\) is a clique, \(A\) is complete to \(C\), \(B\) is anticomplete to \(C\), and \(C\) is independent. Write \(n=a+b+c\).

For \(0\leq m\leq\binom n2\), let \(Q_{n,m}\) denote the standard quasi-clique with \(m\) edges, and \(S_{n,m}=\overline{Q_{n,\binom n2-m}}\) its complementary quasi-star. Compare the exact *labeled* semi-induced counts at the same number of vertices and edges.

**Theorem (sharp onset and complete first-order exceptions).** For every \(2\leq n\leq19\) and every nonnegative integer triple \((a,b,c)\) summing to \(n\),
\[
N(H_{a,b,c})\geq\min\{N(Q_{n,m}),N(S_{n,m})\},\qquad m=|E(H_{a,b,c})|.
\]
At \(n=20\), strict inequality in the other direction occurs for exactly two triples \((a,b,c)\), namely \((6,12,2)\) and \((7,11,2)\). Their complete exact comparisons are
\[
\begin{array}{c|c|c|c|c|c}
(a,b,c)&m&N(H_{a,b,c})&N(Q_{20,m})&N(S_{20,m})&\text{gain over best endpoint}\\\hline
(6,12,2)&165&7308&7860&7344&36\\
(7,11,2)&167&6992&7370&7072&80
\end{array}
\]
Uniqueness concerns class-size triples in this specified family, not all graphs on twenty vertices. In particular, the first exact finite realization of a strict endpoint departure **within this three-class family** occurs at order twenty. No general finite-order global extremality claim is made.

## Assumptions and scope
All graphs are finite, simple, undirected and on distinguishable vertex sets. Every \(a,b,c\) is allowed to be zero. A semi-induced embedding requires only the two center-red-leaf edges and center-blue-leaf nonedge; connections among leaves are unconstrained. Consequently the red leaves are ordered, and counts are not divided by graph automorphisms.

Write \(m=\binom t2+s\), where \(t\) is the largest integer satisfying \(\binom t2\leq m\), and \(0\leq s<t\) except when \(m=0\), handled with \(t=1,s=0\). The quasi-clique \(Q_{n,m}\) has a clique on \(t\) vertices plus another vertex adjacent to \(s\) clique vertices if \(s>0\), and all remaining vertices isolated. The definition also covers \(m=\binom n2\), when \(t=n,s=0\). A quasi-star is its edge-complement analogue as above. All endpoints are compared at exactly \(n\) and \(m\), not in an asymptotic limiting-density sense.

## Proof
The labeled embedding count is
\[
N(G)=\sum_{v\in V(G)}d_G(v)(d_G(v)-1)(n-1-d_G(v)).\tag{1}
\]
For each center \(v\), choose the first red leaf in \(d(v)\) ways, the second in \(d(v)-1\) ways, and the blue leaf in \(n-1-d(v)\) ways. This also proves (1) directly, independently of external sources.

The three classes in \(H_{a,b,c}\) have vertex degrees \(n-1\), \(a+b-1\) and \(a\), respectively. Hence
\[
 m=\binom{a+b}{2}+ac,\qquad
N(H_{a,b,c})=b(a+b-1)(a+b-2)c+ca(a-1)(n-1-a).\tag{2}
\]
The first term comes from \(B\); the \(A\) contribution vanishes since its vertices are universal. Formula (2) includes all zero-size boundary cases.

For endpoints, construct the exact degree multiset of \(Q_{n,m}\) by assigning degree \(t-1\) to each clique vertex, then incrementing \(s\) of those degrees by one and assigning degree \(s\) to the additional vertex. If \(s=0\), no additional nonisolated vertex is used. For \(S_{n,m}\), complement every degree in \(Q_{n,\binom n2-m}\), replacing \(d\) with \(n-1-d\). Substitution into (1) gives both endpoint scores exactly.

The remaining assertion is a bounded arithmetic theorem, certified by the complete integer enumeration in the attached `verify.py`. For each integer \(n\) from \(2\) through \(20\), it visits \(a=0,\ldots,n\), \(b=0,\ldots,n-a\), and the *unique* admissible \(c=n-a-b\), computes (2), computes the two endpoint degree lists from the explicit formulas, and tests the strict inequality. These loops visit **every** nonnegative triple for the specified orders, without random sampling, pruning, numerical approximation, graph-isomorphism assumptions, or timeouts. The number of visited triples is
\[
\sum_{n=2}^{20}\binom{n+2}{2}=1767.
\]
The exact computed result is zero strict improvements for every order through nineteen, and at order twenty precisely the two records printed in the theorem. The loops and assertions constitute the complete finite exhaustion certificate; they can be independently inspected and rerun with a standard Python interpreter. Finally, explicit edge sets for both twenty-vertex examples are generated and each ordered red-red-blue triple is directly counted, reproducing the two values independently of the degree formula. The certificate additionally compares direct counts for every profile through order eight. This proves the theorem. The finite certificate makes no assertion about arbitrary orders greater than twenty.

## Verification
Execute `python3 verify.py` in the directory containing this document and the script. The included `verification_output.txt` records all nineteenth earlier orders with zero improvements, both exact twenty-vertex exceptions, and the final check summary. Only standard-library exact integer arithmetic is used. The exhaustive loop source and assertions, rather than the printed log alone, establish the finite claim. For the two twenty-vertex witnesses, explicit adjacency sets and four-vertex embedding loops verify \(N=7308\) and \(N=6992\) without using formula (1).

## Relationship to prior work
Deng and Hou (2026, arXiv:2606.23351, especially Introduction, Theorem 1.6 and Section 4) introduced the same three-class complement-split construction and proved the **asymptotic fixed-density minimum profile**, including a strict departure from an endpoint-only formula at limiting density \(9/10\). The construction and generic count identity are **prior work**. The present theorem concerns the smallest *finite integer order* at which this exact finite construction beats both finite quasi-endpoints, and gives the complete list of first-order class-size exceptions. No implication from an asymptotic strict inequality fixes that least finite order or its discrete edge counts. Balogh, Lidický, Mubayi, Pfender and Volec (2026, arXiv:2601.03433) formulated the earlier endpoint-profile context and considered star constructions; their asymptotic statements likewise do not classify the twenty-vertex finite triple census.

## Limitations
The theorem does **not** assert that either witness globally minimizes \(N(G)\) among all graphs with fixed \(n,m\); it proves comparison only against the two specified endpoints. It does not claim that twenty vertices is the first such failure among arbitrary graphs or other graph families. All assertions are exact for \(n\leq20\) within the three-class construction. The enumeration is small and exhaustive but is not an analytic classification for every \(n\). Literature may contain an unindexed equivalent finite enumeration.

## References
1. Jinghua Deng and Jianfeng Hou, *Fixed-density profiles for the semi-induced 4-vertex star*, arXiv:2606.23351v1 (first public June 22, 2026), particularly Introduction and Theorem 1.6. https://arxiv.org/abs/2606.23351
2. József Balogh, Bernard Lidický, Dhruv Mubayi, Florian Pfender and Jan Volec, *Semi-Inducibility of some small graphs*, arXiv:2601.03433v1 (January 6, 2026), especially Section 7. https://arxiv.org/abs/2601.03433
