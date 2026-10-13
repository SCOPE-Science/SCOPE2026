# The generic digraph's bimorphism orbit preorder is a product of three-state forks

## Finding
Let \(D\) be the generic loopless digraph without 2-cycles: the unique countable homogeneous digraph whose age is all finite loopless digraphs with no 2-cycles. Let \(B=\operatorname{Bi}(D)\) act componentwise on ordered tuples, and quotient the forward-orbit preorder by mutual reachability, equivalently by strong orbits.

Fix an equality partition \(\pi\) of \([n]\) with \(k\) blocks. Label the blocks by the least coordinate they contain. For each unordered pair of distinct blocks record one of three states: \(0\) if there is no arc between the corresponding vertices, \(+\) if the arc goes from the lower-labelled block to the higher-labelled block, and \(-\) if it goes in the reverse direction. Put the fork order \(0<+\) and \(0<-\), with \(+\) and \(-\) incomparable. Then the forward-orbit quotient on this equality stratum is exactly
\[
V^{\binom{k}{2}},\qquad V=\{0,+,-\}.
\]
Different equality partitions are incomparable because bimorphisms are bijections.

Hence, writing \({n\brace k}\) for a Stirling number of the second kind, the number of strong orbits is
\[
s_n=\sum_{k=1}^{n}{n\brace k}3^{\binom{k}{2}},
\]
the rank enumerator is
\[
R_n(q)=\sum_{k=1}^{n}{n\brace k}(1+2q)^{\binom{k}{2}},
\]
the number of ordered comparable pairs of strong orbits is
\[
c_n=\sum_{k=1}^{n}{n\brace k}5^{\binom{k}{2}},
\]
and the number of directed covers is
\[
e_n=\sum_{k=2}^{n}{n\brace k}\,2\binom{k}{2}3^{\binom{k}{2}-1}.
\]
For every comparable pair \(x\le y\),
\[
\mu(x,y)=(-1)^{r(y)-r(x)}.
\]
On injective \(n\)-tuples the quotient is simply \(V^{\binom n2}\).

## Assumptions and scope
A bimorphism is a bijective endomorphism. Forward reachability means that \(y\) is reachable from \(x\) if some bimorphism sends the ordered tuple \(x\) to \(y\). Strong orbit means mutual forward reachability. The source theorem used here is that \(D\) is MB-homogeneous: every monomorphism between finite induced substructures extends to a bimorphism. The argument is for every integer \(n\ge1\) and allows repeated tuple coordinates.

The primary literature also proves the general fact that, in an appropriate homomorphism-homogeneous structure, two tuples are in the same strong orbit exactly when a finite partial isomorphism carries one to the other. Here the stronger statement is the complete forward-reachability order between those strong orbits.

## Proof
Fix two ordered \(n\)-tuples \(a\) and \(b\) having the same equality partition \(\pi\). A bimorphism is injective, so any bimorphism sending \(a\) to \(b\) induces a bijection between the distinct vertices occurring in the two tuples. Because it is a homomorphism, every arc present among the vertices of \(a\) must remain an arc with the same orientation among the corresponding vertices of \(b\). Since \(D\) has no 2-cycles, a pair in state \(+\) can only remain \(+\), and a pair in state \(-\) can only remain \(-\). A pair in state \(0\) may remain \(0\) or acquire either orientation. Therefore forward reachability implies coordinatewise comparison in the fork \(V\).

Conversely, suppose the state vector of \(a\) is coordinatewise below that of \(b\). The coordinate correspondence from the distinct vertices of \(a\) to the corresponding distinct vertices of \(b\) is then an injective homomorphism between the induced finite substructures: every source arc occurs with the same orientation in the target. By MB-homogeneity this finite monomorphism extends to a bimorphism of \(D\), so \(b\) is forward-reachable from \(a\). This proves the product-poset description.

Mutual reachability holds precisely when every fork coordinate agrees, so the strong-orbit classes are the individual state vectors. Equivalently, each strong orbit is already an automorphism orbit because identical finite oriented patterns give a partial isomorphism, and homogeneity extends it to an automorphism.

For a stratum with \(k\) distinct vertices, there are \(N=\binom{k}{2}\) independent fork coordinates. Thus it has \(3^N\) strong orbits. Its rank polynomial is \((1+2q)^N\): at each coordinate there is one rank-zero state and two rank-one states. A single fork has exactly five ordered comparable pairs, namely \((0,0),(0,+),(0,-),(+,+),(-,-)\), so the stratum has \(5^N\) ordered comparable pairs. A cover changes exactly one coordinate from \(0\) to one of its two upper states, giving \(2N3^{N-1}\) directed covers. Finally, every interval in a product of forks is a Boolean lattice on the coordinates that actually change, hence its Möbius value is \((-1)^d\), where \(d\) is the rank difference. Summing each stratum over the \({n\brace k}\) equality partitions gives the displayed formulas.

## Verification
The included checker exhaustively constructs the fork-product order for \(k\le4\), verifies antisymmetry of the quotient, the rank coefficients, the number of ordered comparable pairs, the directed-cover count, and the Möbius formula on every comparable interval in those products. It separately verifies the Stirling-transform formulas and the first seven values
\[
(s_n)_{n=1}^{7}=1,4,37,913,67060,15284551,10770210577,
\]
\[
(c_n)_{n=1}^{7}=1,6,141,16411,9925076,30665089531,477479400037941,
\]
and
\[
(e_n)_{n=1}^{7}=0,2,60,3254,424200,149588432,149514364692.
\]
The checker tests only the finite combinatorics. The extension from a finite monomorphism to a global bimorphism is supplied by the published MB-homogeneity theorem, not by finite computation.

## Relationship to prior work
Coleman proves that the generic digraph without 2-cycles is MB-homogeneous and explicitly identifies it as the unique countable homogeneous structure whose age is all finite digraphs without 2-cycles. Coleman, Evans, and Gray develop forward and strong orbits for transformation monoids and prove that strong orbits in homomorphism-homogeneous settings are controlled by finite partial isomorphisms. Those results imply the ingredients used here, but the inspected sources do not state the forward-orbit quotient as a product of three-state forks, nor the resulting rank, comparability, cover, and Möbius formulas.

Targeted searches for the generic digraph together with bimorphism reachability, forward orbits, and three-state product orders found the underlying MB-homogeneity papers and adjacent orbit-count results, but no equivalent formulation. Exact searches for the initial numerical profile also found no matching database entry. The closest adjacent work concerns automorphism-orbit profiles of random bipartite or random-poset reducts, which does not determine this transformation-monoid reachability order.

## Limitations
The originality claim is limited to the explicit forward-orbit quotient and its enumerative consequences. The proof is short once MB-homogeneity is combined with the three possible pair states, so uncatalogued folklore remains a realistic residual risk. The result concerns the generic digraph without 2-cycles; allowing 2-cycles changes the local state poset and is not covered here.

## References
1. T. D. H. Coleman, *Two Fraïssé-style theorems for homomorphism-homogeneous relational structures*, Discrete Mathematics 343 (2020), 111674; arXiv:1812.01934. In particular, Example 5.11 identifies the generic digraph without 2-cycles and records its MB-homogeneity.
2. T. D. H. Coleman, D. M. Evans, R. D. Gray, *Permutation monoids and MB-homogeneity for graphs and relational structures*, European Journal of Combinatorics 78 (2019), 163–189; arXiv:1802.04166. Section 1 defines forward and strong orbits and Proposition 1.6 relates strong orbits to finite partial isomorphisms.
