# Two-dimensional collapse and complete integral homology of ternary and quaternary Hamming neighborhood complexes

## Finding
For every integer \(d\ge1\) and \(q\in\{3,4\}\), let \(G_{d,q}=K_q^{\square d}\) be the Hamming graph whose vertices are the \(d\)-letter words over \(\{0,\ldots,q-1\}\), adjacent when they differ in precisely one position. Write \(X_{d,q}=\mathcal N(G_{d,q})\) for the *ordinary open-neighborhood complex*: a nonempty set of graph vertices is a face when its elements have a common graph neighbor.

**Theorem.** Every \(X_{d,q}\) has an explicit simplicial collapse to a complex of dimension at most two. It is connected, its integral homology vanishes above dimension two, and its complete nonzero integral homology groups are
\[
\begin{aligned}
H_0(X_{d,q};\mathbb Z)&\cong\mathbb Z,\\
H_1(X_{d,3};\mathbb Z)&\cong\mathbb Z^d,\\
H_2(X_{d,3};\mathbb Z)&\cong\mathbb Z^{3^d(d-1)(d-2)+d-1},\\
H_1(X_{d,4};\mathbb Z)&\cong(\mathbb Z/2\mathbb Z)^{d-1},\\
H_2(X_{d,4};\mathbb Z)&\cong\mathbb Z^{4^{d-1}(9d^2-15d+8)-1}.
\end{aligned}
\]
For \(d=1\), the rank-zero conventions apply. The new assertion is the uniform two-dimensional collapse and its integral second-homology consequences. The first-homology formulas are included for completeness and follow from earlier published fundamental-group results.

## Assumptions and scope
Only integer \(d\ge1\), and exactly \(q=3\) or \(q=4\), are claimed. The open neighborhood of a word \(v\) consists of the \(d(q-1)\) words obtained by changing precisely one coordinate of \(v\); the vertex itself is excluded. Write \(k=d(q-1)\). The complex is a union of the full simplices \(F_v=2^{N(v)}\). We use unreduced \(H_0\), and integral coefficients throughout.

## Proof
**1. Intersections and the collapse.** For distinct words \(v,w\), their common-neighbor sets have sizes \(q-2\) if their Hamming distance is one, \(2\) if it is two, and zero if it is at least three. Indeed, at distance one the common neighbor alters the differing position to a third symbol; at distance two it alters one of the two differing positions, and farther apart no word is adjacent to both. Hence for \(q\le4\), any two distinct vertex-neighborhood simplices intersect in dimension at most one.

Fix an arbitrary vertex \(a_v\in N(v)\) for every center \(v\). Every face containing at least three vertices belongs to one and only one \(F_v\). Inside \(F_v\), pair each face \(\sigma\subseteq N(v)\setminus\{a_v\}\) with \(\sigma\cup\{a_v\}\), provided \(|\sigma|\ge3\). Perform these elementary face/coface removals in descending order of \(|\sigma|\). A paired lower face is free at its turn: any other potential coface lies inside the same unique \(F_v\) and was already removed by a larger pair. Distinct neighborhood simplices share no such faces, so the pairs are mutually compatible. Every face of cardinality at least four disappears, and each remaining face has cardinality at most three. For \(k<4\) there is no pair and the complex already has dimension at most two. This gives a genuine finite sequence of elementary simplicial collapses, not merely a chain-homotopy equivalence.

**2. Euler characteristic.** Distinct graph vertices are adjacent in the one-skeleton of \(X_{d,q}\) exactly when their Hamming distance is one or two. Indeed, two words of distance one admit a third-symbol common neighbor since \(q\ge3\); distance-two words have two common neighbors, and farther pairs have none. Thus the number of vertices is \(q^d\), and the number of edges is
\[
f_1=\frac{q^d}{2}\left[d(q-1)+\binom d2(q-1)^2\right].
\]
Any face with at least three vertices occurs in exactly one maximal neighborhood simplex. Its signed contribution, summed over one \((k-1)\)-simplex, equals \(\sum_{j=3}^{k}(-1)^{j-1}\binom kj=1-k+\binom k2\). There are \(q^d\) centers, so
\[
\chi(X_{d,q})=q^d-f_1+q^d\left(1-k+\binom{k}{2}\right).
\]
Substitution and simplification yield
\[
\chi(X_{d,3})=3^d(d-1)(d-2),\qquad
\chi(X_{d,4})=4^{d-1}(9d^2-15d+8).
\]
The formulas also hold for \(d=1\), where higher-face sums are interpreted as empty where appropriate.

**3. Fundamental groups: published input and explicit parity calculation.** Matsushita's theorem identifies the fundamental group of the open neighborhood complex of a connected nonbipartite graph with the even-edge-length subgroup of the graph's \(2\)-fundamental group, obtained by filling its four-edge closed walks [1,2]. The Hamming-graph group calculation of Behal and Chih [3] identifies the latter group as \(\mathbb Z^d\) for ternary factors and \((\mathbb Z/2)^d\) for factors of size four; both descriptions are also obtained by filling coordinate squares and the intrinsic four-cycles in each factor. Each coordinate has an odd triangle loop, hence the even subgroup is the kernel of total coordinate parity. Therefore
\[
\pi_1(X_{d,3})\cong\{(z_i)\in\mathbb Z^d:\sum z_i\equiv0\pmod 2\}\cong\mathbb Z^d,
\]
\[
\pi_1(X_{d,4})\cong\{(\epsilon_i)\in(\mathbb Z/2)^d:\sum\epsilon_i=0\}\cong(\mathbb Z/2)^{d-1}.
\]
These statements, including their abelianizations, are *not* asserted to be novel.

**4. Integral homology.** The one-skeleton contains every original graph edge, so the complex is connected. By step 1, its homology vanishes in degrees exceeding two. Since the collapsed model has no three-cells, its integral second homology is a subgroup of a free abelian two-chain group, therefore is free abelian. By step 3, the first Betti number is \(d\) for \(q=3\) and zero for \(q=4\); the full first homology groups are as displayed. Euler–Poincaré gives \(\operatorname{rank}H_2=\chi-1+\operatorname{rank}H_1\), producing the two asserted ranks. There is no hidden integral torsion in \(H_2\), nor any higher homology.

## Verification
The accompanying standalone `verify_hamming_open.py` enumerates all faces and exact integral triangle relations for seven parameter choices: \((d,q)=(1,3),(2,3),(3,3),(4,3),(1,4),(2,4),(3,4)\). It verifies the neighborhood-intersection bound, Euler characteristics, abelian first homology through unimodular eliminations, and second-homology ranks. The rank checks include \(56\) for \((3,3)\), \(55\) for \((2,4)\), and \(703\) for \((3,4)\). Finite enumeration is supplementary, not a substitute for the all-parameter proof above.

## Relationship to prior work
Matsushita [1,2] gives the fundamental-group relation for ordinary open-neighborhood complexes, and Behal–Chih [3] calculates the relevant Hamming graph groups. Together these already imply the displayed \(H_1\) formulas. They do not themselves supply the *simplicial collapse* or the *complete integral second-homology formula*. Previously calculated particular neighborhood complexes, including the ternary three-cube and the four-by-four rook graph [4,5], agree with the specializations here. Results on intrinsic graph Čech nerves (closed radius-one balls) concern different complexes and are not used as equivalent statements.

## Limitations
The collapse relies on pairwise neighborhood intersections having at most two vertices and is proved here only for three- and four-letter alphabets; for larger alphabets the argument fails. The result determines homology and a two-dimensional model, not the full homotopy type or higher homotopy groups. The novelty assessment is relative to the cited literature and indexed comparisons, and does not constitute exhaustive bibliographic certification. Independent scientific audit has not been performed.

## References
[1] T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first version 10 October 2012. https://arxiv.org/abs/1210.2803

[2] T. Matsushita, *Fundamental groups of neighborhood complexes*, *Journal of Mathematical Sciences, The University of Tokyo* 24 (2017). https://www.ms.u-tokyo.ac.jp/journal/jms240302.pdf

[3] K. Behal and A. Chih, *Fundamental Groups of Hamming Graphs*, arXiv:2308.02938. https://arxiv.org/abs/2308.02938

[4] Indexed earlier calculation, *A perfect discrete-Morse matching for the ternary three-cube neighborhood complex*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-perfect-discrete-morse-matching-for-the-ternary-three-cube-nei--ae99e924c723

[5] Indexed earlier calculation, *Integral homology of the rook-graph neighborhood complex*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homology-of-the-rook-graph-neighborhood-complex--00c7d8853dcb
