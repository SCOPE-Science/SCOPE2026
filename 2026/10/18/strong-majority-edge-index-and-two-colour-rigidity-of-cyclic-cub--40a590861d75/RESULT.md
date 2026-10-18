# Strong-majority edge index and two-colour rigidity of cyclic cubic ladders

## Finding
For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) denote the circular ladder. For every integer \(n\ge2\), let \(M_{2n}\) be the Möbius ladder obtained by adding all \(n\) antipodal chords to the cycle on \(2n\) vertices. A *strong-majority edge-colouring* of a finite simple graph assigns a colour to every edge such that, for each edge \(e\) and each colour \(\alpha\), at most half of the other edges sharing an endpoint with \(e\) have colour \(\alpha\). The least possible number of colours is \(\operatorname{Maj}'(G)\).

**Theorem.** The exact strong-majority edge indices are
\[
\operatorname{Maj}'(P_n)=\begin{cases}2,&n\equiv0\pmod4,\\3,&n\not\equiv0\pmod4,\end{cases}\quad (n\ge3),
\qquad
\operatorname{Maj}'(M_{2n})=\begin{cases}2,&n\equiv2\pmod4,\\3,&n\not\equiv2\pmod4,\end{cases}\quad (n\ge2).
\]
Whenever a two-colour solution exists, **exactly eight** strong-majority edge-colourings use two *named* colours on the indexed graph. Thus the untwisted and twisted cyclic closures select different residue classes modulo four, while the admissible two-colour patterns are rigid.

## Assumptions and scope
All graphs are finite and simple, and colourings need not be proper. The indexing of a prism has vertices \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_i u_{i+1},v_i v_{i+1},u_iv_i\). The indexed Möbius ladder has rim vertices \(0,1,\ldots,2n-1\), edges \(i(i+1)\) with indices modulo \(2n\), and chords \(i(i+n)\) for \(0\le i<n\). The smallest twisted example, \(M_4\), is \(K_4\). A two-colour count treats the two colour labels as distinct and counts indexed edge assignments, not assignments modulo graph automorphisms or interchange of colour names.

Each graph is cubic, so an edge has exactly four adjacent edges. Hence a strong-majority edge-colouring with only two colours is precisely one in which **exactly two** of those four neighbours have each colour. A one-colour strong-majority edge-colouring is impossible because each edge has four neighbours.

## Proof
**1. Uniform system on the infinite ladder strip.** Encode two named colours by the bits \(0,1\). Let \(a_i\) be the colour of the first-rim edge at longitudinal position \(i\), \(b_i\) that of the second-rim edge, and \(c_i\) that of the rung, extending these sequences to all integers. For the untwisted closure, use \(a_{i+n}=a_i\), \(b_{i+n}=b_i\), and \(c_{i+n}=c_i\). For the Möbius closure, use \(a_{i+n}=b_i\), \(b_{i+n}=a_i\), and \(c_{i+n}=c_i\). These identifications exactly describe the edges at the seam: crossing from one rim at its last position switches to the other rim in the twisted case.

The four-neighbour majority condition, expressed for one colour, is equivalent for every integer \(i\) to
\[
\begin{aligned}
a_{i-1}+a_{i+1}+c_i+c_{i+1}&=2,\\
b_{i-1}+b_{i+1}+c_i+c_{i+1}&=2,\\
a_{i-1}+a_i+b_{i-1}+b_i&=2.
\end{aligned}
\tag{1}
\]
The other colour is then automatically balanced, since every edge has four neighbours.

Set \(s_i=a_i+b_i\), \(d_i=a_i-b_i\). Subtracting the first two equations gives \(d_{i+2}=-d_i\), and the third gives \(s_{i-1}+s_i=2\).

Suppose first that \(d_i=0\) for every index. Then \(a_i=b_i\), and the equation for \(s\) forces \(a_{i+1}=1-a_i\). The first equation in (1) reduces to \(c_i+c_{i+1}=2a_i\). If \(a_i=0\), this gives \(c_i=c_{i+1}=0\), but the next equation, where \(a_{i+1}=1\), forces \(c_{i+1}=1\). This contradiction rules out identical rim-colour sequences.

Therefore \(d_j\ne0\) for some index \(j\). Since the bits lie in \(\{0,1\}\), we have \(s_j=1\). The recurrence \(s_{i-1}+s_i=2\), in both integer directions, forces \(s_i=1\) for every \(i\). Consequently \(b_i=1-a_i\). The recurrence \(d_{i+2}=-d_i\) now becomes
\[
a_{i+2}=1-a_i.\tag{2}
\]
In particular \(a_{i-1}+a_{i+1}=1\); equation (1) yields
\[
c_i+c_{i+1}=1.\tag{3}
\]
Conversely, (2), (3), and \(b_i=1-a_i\) imply every equation in (1). Thus these conditions classify all two-colour solutions on the infinite strip.

**2. Period and seam constraints.** Equation (2) yields \(a_{i+4}=a_i\) and \(a_{i+2}\ne a_i\) for every index. The *minimal* positive period of \(a\) is therefore four: period one or two is excluded, and period three would also imply period one because the sequence already has period four. Equation (3) makes \(c\) alternate with period two. For the untwisted closure we require \(a_{i+n}=a_i\), which is possible exactly when \(4\mid n\); this also ensures the required closure for \(b,c\). For the Möbius closure we require \(a_{i+n}=b_i=1-a_i\), equivalent by (2) to \(n\equiv2\pmod4\); the same condition ensures \(b_{i+n}=a_i\) and the rung closure \(c_{i+n}=c_i\).

In either permitted case every solution is determined by three independent bits \(a_0,a_1,c_0\); the equations recover all other edge bits uniquely. Conversely each of the \(2^3=8\) choices gives a valid colouring and each is distinct on the indexed edge set. If the seam congruence fails, there is no two-colour colouring.

**3. Three colours always suffice.** Every proper three-edge-colouring of a cubic graph is strong-majority: at either endpoint of an edge, the other two incident edges have the two colours different from that edge, so among its four adjacent edges each of those colours appears exactly twice and its own colour appears zero times.

For \(P_n\), choose any proper three-edge-colouring of the cycle \(C_n\), use it identically on both rims, and colour rung \(u_iv_i\) by the unique third colour missing at cycle vertex \(i\). This is a proper three-edge-colouring of the whole prism. Such a cycle colouring exists for every \(n\ge3\), using two alternating colours for even \(n\) or the three colours for odd \(n\). For \(M_{2n}\), alternately colour the \(2n\)-cycle edges by the first two colours and colour every antipodal chord by the third. All three incident edges at each vertex have different colours. In view of the excluded one-colour case and the exhaustive two-colour classification, the asserted indices follow. \(\square\)

## Verification
The attached standalone `verify.py` independently builds each graph by unordered endpoint pairs and recomputes each edge's four neighbours. It compares exhaustive two-colour counts with the theorem for nine small instances, solves 157 separate binary integer-feasibility problems without using the recurrence in the proof, and checks 477 explicitly constructed two- and three-colour instances. Exact two-colour brute-force tests examine every bit assignment, not a sample. Reproduce by installing the versions recorded in `requirements.txt` and running `python verify.py`; the output is embedded in `verification_output.txt`. These finite checks corroborate the theorem but do not replace its unrestricted proof.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak (2026) introduced the strong-majority edge index, proved general bounds, and obtained the cycle residue-class result. Antoniuk, Prorok and Salia (2026) improved universal bounds, while Pękała and Przybyło (2026) obtained a three-colour theorem for graphs of minimum degree at least five and discussed necessary conditions for two-colour solutions. The present cubic families have minimum degree three. The general inequalities alone do not imply either sharp residue-class obstruction or the enumeration of the eight two-colour assignments. The smallest positive circular-ladder case, \(P_4\), is isomorphic to the three-dimensional cube \(Q_3\); this isolated special case is not asserted as previously unknown. A circular ladder has two independent cyclic rims; a Möbius ladder glues them with a twist, forcing the distinct congruences displayed above.

## Limitations
The result concerns only the two specified graph families, not all cubic graphs or generalized Petersen graphs. The count eight is for two named colours and fixed graph indexing, without quotienting by graph automorphisms; it is not a count of three-colour optimal assignments. Prior-art comparison found no theorem with the same cyclic and twisted exact classification, but an uncatalogued equivalence via strong-majority vertex colouring of line graphs or a more general transfer argument cannot be excluded. Independent mathematical validation has not been performed.

## References
1. R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs* (2026), arXiv:2605.23828v1, https://arxiv.org/abs/2605.23828.
2. S. Antoniuk, M. Prorok, N. Salia, *Strong Majority Edge-Coloring* (2026), arXiv:2607.00212v1, https://arxiv.org/abs/2607.00212.
3. P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours* (2026), arXiv:2608.04122v1, https://arxiv.org/abs/2608.04122.
