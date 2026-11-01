# Full dihedral and color-symmetry homology of the seven-cycle categorical product

## Finding
Let \(G=C_7\times K_3\) be the **categorical** graph product, and let \(X=\operatorname{Ind}(G)\). The natural group \(D_7\times S_3\) acts on vertices by
\[
(i,a)\longmapsto (\delta i+t,\sigma(a)),\qquad t\in\mathbb Z/7\mathbb Z,\quad \delta\in\{+1,-1\},\quad\sigma\in S_3.
\]
There are exactly two nonzero reduced rational homology representations:
\[
\widetilde H_3(X;\mathbb Q)\cong \varepsilon_{D_7}\boxtimes\operatorname{sgn}_{S_3},\qquad
\widetilde H_4(X;\mathbb Q)\cong\mathbf1_{D_7}\boxtimes(\operatorname{sgn}_{S_3}\oplus\operatorname{Std}_{S_3}).
\]
Here \(\varepsilon_{D_7}\) is the reflection-sign character, \(\operatorname{sgn}_{S_3}\) is color-permutation sign, and \(\operatorname{Std}_{S_3}\) is the two-dimensional standard rational representation. All other reduced rational homology vanishes. Hence
\[
\widetilde H_j(X/(D_7\times S_3);\mathbb Q)=0\qquad\text{for all }j\ge0.
\]
The integral calculation also gives \(X\simeq S^3\vee\bigvee^3 S^4\), a nonequivariant classification supplied as a check rather than asserted as the new contribution.

## Assumptions and scope
The graph \(G\) has vertices \((i,a)\) with \(i\in\mathbb Z/7\mathbb Z\) and \(a\in\{0,1,2\}\). Distinct vertices \((i,a)\), \((j,b)\) are adjacent exactly if \(j-i\equiv\pm1\pmod7\) and \(a\ne b\). The complex \(X\) has one simplex for each nonempty independent vertex set. Group actions on oriented simplices include the sign of the induced vertex-order permutation. Claims about orbit homology have **rational** coefficients; the theorem does not assert integral acyclicity of the quotient, nor any independence among results on other cycle lengths.

## Proof
**Exact finite chain model.** Encode each vertex as \(3i+a\) and every nonempty independent set as a positive integer bit mask. Exhaustive recursion on independent sets yields \(5,281\) nonempty faces, with simplex counts by dimension
\[
(21,168,658,1365,1554,1022,402,84,7).
\]

**Integral discrete Morse reduction.** Apply sequential admissible face pairings in the vertex order
`[8,13,3,20,2,9,5,16,19,7,10,4,14,17,11,0,1,15,12,6,18]`.
At each pivot, pair each still-unmatched simplex not containing the pivot with its still-unmatched coface obtained by inserting that vertex. There are \(2,638\) pairs and precisely five critical faces: one vertex, one three-simplex and three four-simplices. The complete directed Hasse diagram, with exactly those matched edges reversed, is acyclic; a topological ordering visits all \(5,281\) nodes.

The signed integral gradient-chain projection is defined by sending a critical cell to itself, an upper matched cell to zero, and a lower matched cell \(\alpha\) paired with \(\beta\) to
\[
p(\alpha)=-[\beta:\alpha]^{-1}\!\sum_{\gamma\in\partial\beta,\ \gamma\ne\alpha}[\beta:\gamma]p(\gamma).
\]
This recursion is well founded by acyclicity. Applying it to the signed boundaries of each critical four-cell gives zero on the one critical three-cell. The integral Morse differential therefore vanishes. Since there is one three-cell and three four-cells attached to a vertex, the attaching maps have zero degrees in \(\pi_3(S^3)\cong\mathbb Z\); hence the asserted nonequivariant wedge type follows.

**All group actions.** For each of the \(14\times6=84\) distinct natural automorphisms, construct integral cycle lifts of the critical degree-three and degree-four generators. The lifts contain respectively \(16\) and \(90,96,154\) oriented faces; their boundaries vanish and they project to the respective standard critical bases. Acting on every oriented simplex and then applying \(p\) yields the exact integer homology matrices. All cycle rotations act trivially in both positive homology degrees. Dihedral reflections act by \(-1\) in degree three and trivially in degree four. For a color permutation \(\sigma\), its degree-three trace equals \(\operatorname{sgn}(\sigma)\); its degree-four trace is \(3,-1,0\) when \(\sigma\) is respectively the identity, a transposition, or a three-cycle. These latter three values are exactly the character of \(\operatorname{sgn}\oplus\operatorname{Std}\).

Independently, the signed count of simplices fixed setwise by each automorphism agrees with the Lefschetz identity \(L(g)=1-\operatorname{tr}(g\mid H_3)+\operatorname{tr}(g\mid H_4)\) in all 84 cases. Since averaging either positive-degree character over the full group gives zero, no positive-degree rational invariant survives. Rational cellular transfer after equivariant subdivision identifies rational homology of the finite-group orbit space with the invariant homology, proving the quotient conclusion.

## Verification
Run `python3 verify_c7_product.py` with Python's standard library; it prints
`C7K3_COMPLETE_INTEGER_MORSE_AND_84_EQUIVARIANT_CHARACTERS_OK` on success. The checker independently constructs the finite graph, all simplices, all matching pairs, the complete Morse directed graph, integer chain projections and cycle lifts, and all 84 signed automorphism matrices. It checks the critical Morse boundary, the character table, triviality of the sevenfold rotation action and the Lefschetz relation. All tests are exhaustive for this exact finite object, not extrapolations from sample cases.

## Relationship to prior work
Antolín Camarena and Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs* (arXiv:2307.12401, first public 2023-07-23), specifically name \(C_7\times K_3\), report nontrivial free homology in two adjacent degrees, and prove broad nonequivariant restrictions; see their Theorem 23 and discussion preceding Question 24. Those claims are not presented as original here. The distinct information is the **natural, specified, 84-element group action** on rational homology, its decomposition into irreducibles, and the rational orbit-space consequence. The later study *On independence complexes of graph products* (arXiv:2505.06457) discusses related graph products; it is supporting literature, not the qualifying initial public source. The graph \(C_7\times K_4\) has also been studied, but changing the number of colors neither determines the three-color character nor its quotient invariants.

## Limitations
This is a complete calculation for one naturally motivated 21-vertex graph, not an infinite-family formula or a proof of the general torsion-freeness question. It computes rational equivariant homology, not integral torsion in the quotient. Equivalent unpublished or unindexed calculations remain possible; negative literature searches are not mathematical novelty proofs.

## References
1. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first submitted 2023-07-23), https://arxiv.org/html/2307.12401v2.
2. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457 (2025), https://arxiv.org/abs/2505.06457.
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145 (standard discrete-Morse background).
