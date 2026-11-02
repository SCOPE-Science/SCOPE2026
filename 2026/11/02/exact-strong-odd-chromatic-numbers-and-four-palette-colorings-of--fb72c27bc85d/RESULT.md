# Exact strong odd chromatic numbers and four-palette colorings of cycle prisms

## Finding
For every integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the prism graph with two cyclic rims and matched rungs. A strong odd vertex coloring is a proper coloring in which every color present in the open neighborhood of any vertex appears there an odd number of times. The strong odd chromatic number is exactly
\[
\chi_{\mathrm{so}}(P_n)=
\begin{cases}
6,&n=3,\\
2,&n\ge4\text{ even},\\
5,&n\ge5\text{ odd}.
\end{cases}
\]
Here the \(n=3\) equality is already implied by the published strong odd coloring theorem for Cartesian products of complete graphs; the infinite odd-prism equality and the following exact coloring census are the contributions emphasized here.

Fix the named palette \(\{0,1,2,3\}\). Let \(F_4(n)\) denote the number of maps from the **labelled** vertices of \(P_n\) to this palette that give proper strong odd colorings, with no requirement that every palette color is used. Then for all \(n\ge3\),
\[
F_4(n)=12\mathbf1_{2\mid n}+24\mathbf1_{4\mid n}+48\mathbf1_{6\mid n}.
\]
Every such coloring is periodic in the cyclic rung direction with minimal column period \(2\), \(4\), or \(6\). The associated local-state transition has precisely six directed cycles of length two, six of length four, and eight of length six. In particular, no odd prism admits a four-color strong odd coloring, while every odd prism with at least five rungs admits a five-color strong odd coloring.

## Assumptions and scope
The graphs are finite, undirected, simple, and have vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/n\mathbb Z\). Edges are \(u_iu_{i+1}\), \(v_iv_{i+1}\), and \(u_iv_i\). The parameter \(n\) is an integer at least three; for \(n=3\) the rim is a triangle, not a multigraph. A strong odd coloring may use fewer than its available colors. The counting formula uses a fixed set of four **named** colors and preserves the cyclic column labels and the top/bottom labels; it does not quotient by automorphisms or color permutations.

At a degree-three vertex, the strong odd condition says its three neighbor colors are either all equal or all pairwise distinct: a multiset containing one doubled color and one singleton is prohibited. This equivalence will be used throughout.

## Proof
**The four-color transition.** For any four-palette coloring, write the colors on rung \(i\) as \(Q_i=(a_i,b_i)\), top before bottom. Given the preceding rung \(P=(c,d)\) and the current rung \(Q=(a,b)\), properness says \(a\ne b\), \(c\ne d\), \(a\ne c\), and \(b\ne d\). There are \(12\) choices of \(Q\); for each one there are seven choices of \(P\), for a total of \(84\) legal ordered states.

For the successor rung \(R=(x,y)\), the strong odd condition at the current top vertex concerns neighbor colors \((c,b,x)\), while that at the bottom vertex concerns \((d,a,y)\). If \(c=b\), the first triple must be monochromatic, hence \(x=b\). Otherwise \(a,b,c\) are three distinct palette colors and the first triple must have three distinct entries; properness additionally requires \(x\ne a\), so \(x\) is the unique palette color outside \(\{a,b,c\}\). Similarly,
\[
y=\begin{cases}a,&d=a,\\\text{the unique color outside }\{a,b,d\},&d\ne a.\end{cases}
\]
These prescriptions always yield \(x\ne y\): if \(c=b,d=a\) then \(R=(b,a)\); if exactly one equality holds then one coordinate equals \(a\) or \(b\) and the other does not; and if neither holds then \(c,d\) are the two complement colors to \(\{a,b\}\), giving \(R=(d,c)\). Thus the successor is legal and unique. Reversing the same argument determines the predecessor, so the map on the \(84\) ordered states is a permutation.

**Orbit classification, not merely a finite experiment.** Partition the \(84\) states by the relative roles of \(c,d\) against \(a,b\). There are four disjoint types:
\[
\begin{array}{c|c|c}
\text{type}&\text{condition}&\text{number of states}\\\hline
A&c=b,\ d=a&12\\
B&c=b,\ d\notin\{a,b\}&24\\
C&d=a,\ c\notin\{a,b\}&24\\
D&\{c,d\}=\{0,1,2,3\}\setminus\{a,b\}&24.
\end{array}
\]
Color permutations act transitively on states of each type and commute with successor. For type \(A\), the columns alternate between \((a,b)\) and \((b,a)\), so the least period is two. For type \(D\), with the current rung written \((0,1)\) and previous rung \((2,3)\), the cycle in column order is \(((2,3),(0,1),(3,2),(1,0))\), of least period four. For type \(B\), a representative six-column sequence is
\[
((1,2),(0,1),(1,3),(2,1),(1,0),(3,1)),
\]
of least period six; type \(C\) is visited on the same cycles. The recurrence verifies the displayed sequences, and transitivity ensures all states in each type have the stated least periods. Thus the type \(A\) states form six two-cycles, the type \(D\) states form six four-cycles, and the \(48\) type \(B\)/\(C\) states form eight six-cycles. Every cyclic coloring is in bijection with an ordered state fixed by the \(n\)-fold successor map. Counting fixed points yields exactly
\[
F_4(n)=12\mathbf1_{2\mid n}+24\mathbf1_{4\mid n}+48\mathbf1_{6\mid n}.
\]
This also rules out all colorings with three or fewer colors on odd prisms, since they are included among the four-palette assignments.

**Even prisms.** When \(n\ge4\) is even, color the two rims alternately with colors zero and one in opposite parity along the rungs. This is a proper two-coloring of the cubic bipartite prism; all three neighbors of a vertex have the other color, an odd multiplicity. An edge precludes a one-color proper coloring, so the optimum is two.

**Odd prisms of at least five rungs.** Here are explicit cyclic rung-color sequences over the palette \(\{0,1,2,3,4\}\):
\[
\begin{aligned}
B_4&=((2,3),(1,0),(3,2),(0,1)),\\
B_5&=((2,3),(1,4),(3,0),(4,2),(0,1)),\\
B_7&=((2,3),(1,0),(3,2),(0,4),(1,3),(4,2),(0,1)).
\end{aligned}
\]
Directly checking the two neighbor triples at every column (with wraparound) proves each block valid. All three blocks start with \((2,3)\) and end with \((0,1)\), so concatenating any two preserves the neighbor triples at their joining vertices. Every odd \(n\ge5\) has the form \(5+4t\) or \(7+4t\) for an integer \(t\ge0\); use \(t\) copies of \(B_4\), followed by \(B_5\) or \(B_7\). The coloring uses at most five colors, and four colors are impossible by the exact census, proving equality five.

**The triangular prism.** For \(n=3\), the rim is \(K_3\), and \(P_3=K_3\square K_2\). The exact value six follows from the published complete-graph Cartesian-product theorem, which states \(\chi_{\mathrm{so}}(K_p\square K_q)=pq\). Equivalently, the square of the triangular prism is complete on six vertices: any two distinct vertices are at distance at most two, and each pair of neighbors of a vertex has to be differently colored because two of its three neighbors receiving the same color would leave a forbidden two-plus-one neighbor-color pattern unless all three shared a color. For the triangular prism, the published product theorem is the definitive cited justification; six pairwise distinct colors visibly suffice.

## Verification
The companion standard-library Python verifier independently constructs all labelled prism neighbor triples and checks properness and odd multiplicities. It tests every four-palette pair-of-rungs state, its unique successor and the complete cycle partition \(6\times2+6\times4+8\times6=84\). It independently enumerates all cyclic four-palette colorings for \(n=3,4,5,6\), checking the census; checks explicit blocks and concatenations for every odd \(n\le121\); and tests all \(5^6=15625\) five-palette assignments for the triangular prism. These finite checks corroborate, but do not replace, the universal transition proof and constructions.

To reproduce: run `python3 verify.py` in a clean environment using Python 3.9 or later; the verifier has no third-party dependencies.

## Relationship to prior work
The motivating manuscript by Pradhan, Sharma and Verma (2026) studies computational complexity, parameterized algorithms and strong odd colorability; its publicly accessible abstract and excerpt do not assert the present prism family classification. The foundational paper of Caro, Petruševski, Škrekovski and Tuza (2024) studies Cartesian products and proves \(\chi_{\mathrm{so}}(G\square H)\le\chi_{\mathrm{so}}(G)\chi_{\mathrm{so}}(H)\), as well as the exact complete-graph product formula. The latter **already determines** the \(n=3\) boundary here. For \(n\ge5\) odd, product submultiplicativity yields only a generally nonsharp upper bound from the factors; it does not imply the sharp five-color classification or the four-palette count. The earlier strong odd coloring work of Kwon and Park gives sparse-graph estimates rather than an exact circular-prism census. No claim of uniqueness or exhaustive bibliographic coverage is made.

## Limitations
The theorem covers the ordinary strong odd coloring convention for the simple cycle prism with \(n\ge3\), not arbitrary ladders, Möbius ladders, higher-dimensional Cartesian products or the weaker odd-coloring notion. The four-palette formula counts named color assignments, not equivalence classes under graph or color symmetries. Historical priority is provisional: some potentially relevant complete recent manuscripts were not accessible for full-text inspection. A mathematical audit independent of the present self-review has not been performed.

## References
1. D. Pradhan, V. Sharma and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441v1 (first public 2026-10-01), https://arxiv.org/abs/2610.01441.
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336v1 (2024-10-03), especially Section 4, Theorems 4.2 and 4.4, https://arxiv.org/html/2410.02336v1.
3. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (2024), https://arxiv.org/abs/2401.11653.
