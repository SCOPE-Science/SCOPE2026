# Fischer–Servi confluence on the two minimal nondistributive lattices

## Finding

The two five-element minimal nondistributive lattices support exactly **\(1{,}395\)** and **\(1{,}079\)** reflexive transitive modal relations satisfying the two Fischer–Servi inclusions specified below, respectively. For the five-element modular diamond \(M_3\), the \(1{,}395\) labelled relations form precisely **\(341\)** isomorphism classes. For the nonmodular pentagon \(N_5\), every order automorphism is the identity, so there are **\(1{,}079\)** classes.

On \(M_3\), with bottom \(0\) and top \(4\), the numbers of relations according to the truth of \(0R4\) and \(4R0\) are \(870,262,262,1\) in the order neither, first only, second only, both. On \(N_5\), the corresponding counts are \(618,230,230,1\). In particular, the two extreme arrows occur together only for the universal modal relation. This last uniqueness holds **for every bounded poset**, not just these lattices.

## Assumptions and scope

Fix a bounded poset \((P,\le)\) and a binary relation \(R\subseteq P\times P\). Throughout, \(R\) is reflexive and transitive and satisfies:

\[\begin{aligned}
(\mathrm{FS}_1):\quad & x\le y\land yRz\ \Longrightarrow\ (\exists u)\,xRu\land u\le z,\\
(\mathrm{FS}_2):\quad & xRy\land z\le y\ \Longrightarrow\ (\exists u)\,u\le x\land uRz.
\end{aligned}\]

These are exactly \((\le\circ R)\subseteq(R\circ\le)\) and \((R\circ\ge)\subseteq(\ge\circ R)\) under left-to-right relational composition; no extra normality or persistence axioms are imposed. The first lattice \(M_3\) has elements \(\{0,1,2,3,4\}\) with \(0<1,2,3<4\) and pairwise incomparable middle points. The second, \(N_5\), has \(0<1<2<4\) and \(0<3<4\), with \(3\) incomparable with \(1,2\). All counts concern relations on these **specified labelled carriers**; isomorphism classes are under order automorphisms.

## Proof

**General endpoint lemma.** If \(0R4\) and \(4R0\), use \(x\le4\), \(4R0\), and \((\mathrm{FS}_1)\) to obtain \(xRu\le0\), whence \(xR0\), for every \(x\in P\). Separately, use \(0R4\), \(z\le4\), and \((\mathrm{FS}_2)\) to obtain \(u\le0\) with \(uRz\), hence \(0Rz\), for every \(z\in P\). By transitivity, \(xRz\) for all \(x,z\); the converse is immediate because the universal relation satisfies both inclusions.

**Exhaustive finite proof.** On a five-point carrier there are \(20\) ordered pairs of distinct elements. Reflexivity forces the other five pairs. The attached complete checker `verify_minimal_lattices.c` iterates each of the \(2^{20}=1{,}048{,}576\) assignments to the off-diagonal pairs **separately for each lattice**. For each relation it checks all ordered triples for transitivity and evaluates both displayed implications by exhaustive quantification over the five possible witnesses \(u\). Thus each admissible relation appears exactly once, with no search pruning or unstated assumptions. The counter values are exactly \(1{,}395\) and \(1{,}079\), and the four endpoint partitions are those stated in the finding.

The order automorphism group of \(M_3\) permutes its three incomparable middle points and is \(S_3\). For each passing relation the program checks invariance under all six explicit permutations of those points. Its fixed-point counts are \(1{,}395\) for the identity, \(199\) for each of the three transpositions, and \(27\) for each of the two three-cycles. Burnside's lemma gives
\[\frac{1395+3\cdot199+2\cdot27}{6}=341.\]
In \(N_5\), point \(1\) is the unique atom with a proper successor other than the top; point \(2\) is its unique successor below the top; and point \(3\) is the remaining atom. Thus the only order automorphism is the identity, and the isomorphism count equals the labelled count.

## Verification

Compile `verify_minimal_lattices.c` with `cc -std=c11 -O2 verify_minimal_lattices.c -o verify_minimal_lattices` and run `./verify_minimal_lattices`. It prints both labelled counts, both four-cell endpoint distributions, the six fixed-point counts for \(M_3\), and its isomorphism count. There is no randomized step and no external library. The only computational step is an exhaustive finite certificate; the general endpoint lemma is proved above without computation.

## Relationship to prior work

Fernández-Duque, *Fine Selection for Intuitionistic Modal Logic* (2026), studies the finite-model property for intuitionistic modal frames. Girlando–Kuznets–Marin–Straßburger, *A Decision Procedure for Intuitionistic Modal Logic IS4 (and IK4)* (2026), develops constructive decision procedures and finite countermodels. Standard Fischer–Servi relational inclusions occur in the literature on FS frames. None of the material inspected supplies the simultaneous complete census and symmetry classification on \(M_3\) and \(N_5\); those five-element lattices are the two classical minimal forbidden sublattices for distributivity. No theorem in the cited sources is claimed to establish these exact counts.

## Limitations

The counts apply only to the two specified five-element posets and to the **explicit pair of relational inclusions above**; they are not counts for every variant of intuitionistic modal frame semantics. No claim is made about arbitrary larger lattices, formula equivalence of distinct frames, or the number of inequivalent modal theories. Historical priority of this exact finite census is not established independently; an older unindexed enumeration or table could cover it. The complete enumeration is mechanically checkable, but no separate independent audit has occurred.

## References

- D. Fernández-Duque, *Fine Selection for Intuitionistic Modal Logic* (2026), arXiv:2609.27078v1, first publicly submitted 2026-09-22. https://arxiv.org/abs/2609.27078
- M. Girlando, R. Kuznets, S. Marin, L. Straßburger, *A Decision Procedure for Intuitionistic Modal Logic IS4 (and IK4)* (2026), arXiv:2609.24922v1, first publicly submitted 2026-09-21. https://arxiv.org/abs/2609.24922
- Literature on Fischer–Servi frames, with explicit conditions \((\le\circ R)\subseteq(R\circ\le)\) and \((R\circ\ge)\subseteq(\ge\circ R)\), see FS-forest frame Definition 6.6 in *Gödel modal logic*, https://www.iiia.csic.es/media/filer_public/3e/0c/3e0c5be1-23cf-4c28-a8a8-69786382fc29/godal-modal-fgmr-sent.pdf .
