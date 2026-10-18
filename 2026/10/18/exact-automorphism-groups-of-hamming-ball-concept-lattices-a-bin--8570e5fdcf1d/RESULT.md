# Exact automorphism groups of Hamming-ball concept lattices: a binary extra-coordinate symmetry

## Finding
For integers \(d,q\ge2\), form the formal context \(\mathcal K_{d,q}\) with both object and attribute sets equal to \([q]^d\) and incidence \(xIy\) precisely when their Hamming distance is at most one. Let \(\mathcal L_{d,q}\) be its ordinary formal-concept lattice. Its complete **order-preserving lattice automorphism group** is
\[
\operatorname{Aut}(\mathcal L_{d,q})\cong
\begin{cases}
(\mathfrak S_q)^d\rtimes\mathfrak S_d,&q\ge3,\\
V_{d+1}^{\mathrm{even}}\rtimes\mathfrak S_{d+1},&q=2,
\end{cases}
\]
where \(V_{d+1}^{\mathrm{even}}=\{v\in\mathbb F_2^{d+1}:\sum_i v_i=0\}\), and the indicated symmetric group acts by permuting coordinates. In particular the orders are \((q!)^d d!\) and \(2^d(d+1)!\), respectively. For \(q\ge3\), every concept-lattice symmetry comes from a Hamming-graph isometry. In the binary case, the natural Hamming-graph automorphism subgroup has **exact index \(d+1\)**, and that extra symmetry occurs in every dimension \(d\ge2\). For example, the lattice for \(d=2,q=2\) is the sixteen-element Boolean lattice, with automorphism group \(\mathfrak S_4\) instead of the square graph's dihedral group of order eight.

## Assumptions and scope
Take \([q]=\{0,1,\ldots,q-1\}\) as a set of symbols, not necessarily a field; no prime-power assumption is made. Objects and attributes are **distinct sorts**, even though both are indexed by the same words. The relation is reflexive as a relation on the word labels, so it is the closed one-neighborhood incidence, not open adjacency or distance-two incidence. Automorphisms preserve the lattice order (not order dualities); under the dual closed-intent presentation, this is the group of permutations respecting set inclusion. The theorem applies to all integral parameters \(d,q\ge2\); degenerate \(d=1\) and \(q=1\) are excluded.

## Proof
**1. Closed intents and rigidity reduction.** Write \(V=[q]^d\) and \(B_x=\{y\in V:d_H(x,y)\le1\}\). The intent closure of \(A\subseteq V\) is exactly the intersection of all \(B_x\) containing \(A\). The closed intents, ordered by inclusion (the order-dual of the usual extent-ordered concept lattice), are therefore all intersections of this ball family. For distinct \(x,z\), direct coordinate comparison gives
\[
 B_x\cap B_z=\begin{cases}
\text{the coordinate line through }x,z,&d_H(x,z)=1,\\
\text{the two intermediate words},&d_H(x,z)=2,\\
\varnothing,&d_H(x,z)>2.
\end{cases}
\]
Every intersection of three or more balls is consequently either a previously occurring line or pair, a singleton, or empty: intersecting an off-line ball with a coordinate line yields at most one point, unless its center lies on that line; intersecting a two-element set cannot create any other type. Every singleton \(\{y\}\) is closed, since for centers \(y\) and two neighbors obtained by changing two distinct coordinate positions, the intersection of those three balls is exactly \(\{y\}\). All \(B_x\) are distinct and are maximal proper closed sets: every other proper closed set is contained in one, while \(V\) itself is closed by convention (intersection of no sets). Every nonempty closed intent is a union of its singleton constituents in the lattice sense. Thus any order automorphism is uniquely determined by its permutation \(f\) of the singleton atoms, and that permutation necessarily carries the family \(\{B_x\}\) of coatoms onto itself. Conversely, every permutation of \(V\) preserving the ball family sends intersections of balls to intersections of balls and hence gives a lattice automorphism. Therefore
\[
\operatorname{Aut}(\mathcal L_{d,q})\cong
\{f\in\mathfrak S_V:\{f(B_x):x\in V\}=\{B_x:x\in V\}\}.
\]
This reduction uses only the order structure, without labels, coordinate choices, or a designated object/attribute identification.

**2. Nonbinary rigidity.** Suppose \(q\ge3\). The nontrivial proper closed intents are precisely singletons, coordinate lines of size \(q\), the two-point sets at Hamming distance two, and the \(B_x\). (When \(q=2\), the two types of pair are indistinguishable by size.) Each line has \(q\ge3\) singleton atoms beneath it, while each other proper closed element that is not a coatom has at most two. Consequently every lattice automorphism preserves the coordinate-line family. Two distinct words are Hamming-graph adjacent if and only if they lie on a common coordinate line. Its atom permutation \(f\) therefore lies in \(\operatorname{Aut}(H(d,q))\). Conversely, every Hamming-graph automorphism carries \(B_x\) to \(B_{f(x)}\), and hence acts on the lattice. The classical Hamming-graph automorphism formula [3] is \(\operatorname{Aut}(H(d,q))=(\mathfrak S_q)^d\rtimes\mathfrak S_d\). For completeness, its upper bound follows by fixing a base word: the induced graph on its neighbors is the disjoint union of \(d\) cliques of size \(q-1\), so a stabilizer can only permute coordinate directions and the nonbase symbols separately. An automorphism fixing those neighbors fixes every higher Hamming sphere by induction because a weight-\(r\) word, \(r\ge2\), is determined by its neighbors of weight \(r-1\). The displayed coordinate and symbol permutations attain this bound.

**3. Binary parity lift.** Let \(q=2\). Embed attributes \(y\in\mathbb F_2^d\) into the even-parity half of the \((d+1)\)-cube by \(e(y)=(y,\sum_i y_i)\), and objects \(x\) into the odd-parity half by \(o(x)=(x,1+\sum_i x_i)\), with final coordinates in \(\mathbb F_2\). If \(h=d_H(x,y)\), then \(d_H(o(x),e(y))=h+\mathbf1_{h\text{ even}}\). This distance equals one exactly when \(h=0\) or \(h=1\); hence the bipartite object–attribute incidence graph is literally the full \((d+1)\)-dimensional cube, with its parity halves retained as the two sorts. Its sort-preserving automorphism group is the index-two subgroup of \(\operatorname{Aut}(Q_{d+1})\) that preserves vertex parity. Every cube automorphism is a binary translation followed by a coordinate permutation: translate the image of zero back to zero, then permute the \(d+1\) neighbors of zero, which determine every subsequent Hamming sphere inductively. The translations that preserve parity are precisely \(V_{d+1}^{\mathrm{even}}\). By Step 1, all sort-preserving incidence automorphisms, and only those, induce lattice automorphisms. This gives \(V_{d+1}^{\mathrm{even}}\rtimes\mathfrak S_{d+1}\) and its order \(2^d(d+1)!\).

**4. Sharp enlargement and an explicit new symmetry.** An ordinary binary Hamming-graph isometry has group order \(2^d d!\), embeds faithfully in the lattice group by preserving the closed balls, and the ratio is exactly \(d+1\). Swapping the first coordinate and the parity coordinate in the lifted \((d+1)\)-cube yields on attribute words the bijection
\[
(y_1,\ldots,y_d)\longmapsto
\left(\sum_{i=1}^{d}y_i\pmod2,\ y_2,\ldots,y_d\right).
\]
It preserves all closed-ball intersections but sends \(0\) and the second standard unit vector to words of Hamming distance two (instead of one), so it is not a \(d\)-cube isometry. The inclusion is therefore strict for every \(d\ge2\), and all asserted formulas follow.

## Verification
The accompanying Python 3 standard-library checker `verify_hamming_lattice.py` computes actual closed-intent sets by direct ball intersections and verifies them against independently enumerated singleton, coordinate-line and distance-two-pair descriptions for \((d,q)\in\{(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(2,4)\}\). It exhaustively tests all atom permutations for \((2,2),(3,2),(2,3)\), finding exactly \(24,192,72\) ball-family automorphisms. Separately, it constructs all even translations and coordinate permutations of lifted cubes for binary \(d=2,3,4\) and checks each map preserves the complete ball family, finding \(24,192,1920\) distinct group elements. Command: `python3 verify_hamming_lattice.py`. The proof above, not these finite tests, establishes the unbounded parameters.

## Relationship to prior work
Howlader and Liau [1] investigate formal contexts, their lattice-theoretic and modal-logical representations, and two-sorted reasoning, but do not give this Hamming-ball automorphism classification. Rawson et al. [2] identify a general correspondence between formal concept lattices and hyperedge intersection structures, which justifies the closed-intent viewpoint; that general correspondence is credited, not new. Mirafzal and Ziaee [3] give the Hamming-graph automorphism group explicitly; that graph group is used here without a new graph-symmetry priority claim. The publicly available article *Scale-two Čech complexes of multinary Hamming graphs collapse to wedges of two-spheres* [4] states the closed-ball pair-intersection classification; it establishes a homotopy result for a Čech nerve, not the full order-automorphism group of its closed-intersection lattice. In particular, its intersection lemma already implies routine intent-enumeration formulas; those formulas are not claimed as novel here. The assessed result is the exact **concept-lattice** symmetry dichotomy and the exceptional parity-extension mechanism, including its sharp group index. Earlier equivalent formulations under two-fold graph automorphism or formal-context symmetry terminology remain possible.

## Limitations
The group consists only of order-preserving lattice automorphisms; order-reversing dualities may add other transformations and are not classified. The incidence radius is exactly one and both sorts have the same word alphabet; the statement does not extend automatically to other radii, unequal alphabets, or open graph neighborhoods. The nonbinary proof uses the established automorphism classification for Hamming graphs. The previous literature could contain an equivalent implicit observation under alternative terminology; bibliographic priority and independent external validation are not asserted.

## References
[1] P. Howlader and C.-J. Liau, *On the Logical and Algebraic Aspects of Reasoning with Formal Contexts*, arXiv:2407.13287, first public 2024-07-18, https://arxiv.org/abs/2407.13287.

[2] M. G. Rawson, A. Myers, R. Green, M. Robinson and C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, first public 2023-07-21, https://arxiv.org/abs/2307.11681.

[3] S. M. Mirafzal and M. Ziaee, *A note on the automorphism group of the Hamming graph*, arXiv:1901.07784, first public 2019-01-23, Theorem 3.4, https://arxiv.org/abs/1901.07784.

[4] *Scale-two Čech complexes of multinary Hamming graphs collapse to wedges of two-spheres*, published mathematical result, 2026-10-11, section "Proof", first item on ball intersections, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-scale-two-ech-complexes-of-multinary-hamming-graphs-collapse-to--dc62d4e0316e.
