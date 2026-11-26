# An explicit signed winding label for the Grötzsch recolouring chambers

## Finding

Let \(G=\mu(C_5)\) be the eleven-vertex Grötzsch graph, and let \(\mathcal R_4(G)\) be the graph of all proper vertex colourings with **named** colours \(0,1,2,3\), adjacent precisely when one vertex changes colour and propriety is retained. The two previously enumerated recolouring components are precisely the two level sets of the explicit signed winding \(\Omega\) defined below. Thus the component of an individual colouring can be found by evaluating a signed sum on its projected pentagon, without exploring the recolouring graph. In particular, this formula remains invariant when the apex itself is recoloured and the projection changes its palette.

For context, the known census gives \(12{,}480\) colourings and \(45{,}240\) edges, with \(6{,}240\) vertices per component and degree enumerator
\[
D(t)=480t^{5}+2640t^{6}+3840t^{7}+4320t^{8}+1200t^{9},
\]
diameter \(17\) per component, and a mixing threshold of five. The auxiliary metric calculation below gives radius \(15\), \(22{,}620\) edges per component, and eccentricity counts \(1{,}080,5{,}100,60\) at distances \(15,16,17\), respectively. The contribution is the explicit signed label, not the component census or the metric calculation.

## Assumptions and scope

Use indices in \(\mathbb Z/5\mathbb Z\). The vertices are originals \(v_i\), their shadows \(s_i\), and an apex \(z\). The edges are \(v_iv_{i+1}\), \(s_iv_{i-1}\), \(s_iv_{i+1}\), and \(zs_i\) for every \(i\); there are no others. This is Mycielski's construction on the pentagon. A colouring is a function from these eleven vertices to the **fixed four-element palette**, not a colour partition modulo permutations. A move changes the value at exactly one vertex.

For a proper colouring \(c\), set \(a=c(z)\). Define a three-colouring \(r(c)\) of the original pentagon by
\[
r_i(c)=\begin{cases}c(v_i),&c(v_i)\ne a,\\c(s_i),&c(v_i)=a.\end{cases}
\]
All its values lie among the three colours different from \(a\). Let \(q_a\) rank these three colours in increasing numerical order as \(0,1,2\), and put \(h_i=q_a(r_i(c))\). Let \(\varepsilon_i=1\) if \(h_{i+1}-h_i\equiv1\pmod3\), and \(\varepsilon_i=-1\) otherwise. Then
\[
\boxed{\Omega(c)=(-1)^a\,\frac{1}{3}\sum_{i=0}^{4}\varepsilon_i\in\{-1,+1\}.}
\]
This quantity is the **signed winding**. The choice of sorted named colours, and the factor \((-1)^a\), are part of the normalization; without them the statement of the invariant at apex recolourings is not the one claimed.

## Proof

**Optimality of four colours.** The pentagon has chromatic number three. A proper three-colouring of its Mycielskian would assign some colour \(a\) to the apex, and no shadow could receive \(a\). Replacing the colour of every original vertex coloured \(a\) with the colour of its own shadow yields a proper two-colouring of the original pentagon: the shadow sees both of the original's neighbours. This is impossible. Extending a three-colouring of the pentagon by copying it to the shadows and giving the apex a fourth colour proves \(\chi(G)=4\).

**Well-defined signed winding.** The three-colouring \(r(c)\) is proper on the original pentagon. Adjacent originals cannot both have colour \(a\), and a shadow is adjacent to both neighbours of its original; this establishes properness in all cases. Every difference \(h_{i+1}-h_i\) has residue \(1\) or \(-1\) modulo three. The sum of five such signed differences is an odd multiple of three, necessarily \(3\) or \(-3\); hence \(\Omega(c)\) belongs to the stated two-element set.

**Invariance when the apex is fixed.** The projected three-colouring changes at most one position. A legal change in a proper three-colouring of a cycle requires that the two neighbours of that position share a colour, so the contributions of the two incident directed edges sum to zero both before and after.

**Invariance at an apex move \(a\to b\).** Both \(a,b\) are absent on all shadows. Write \(d,e\) for the other two colours. For the moment compare the old and new projected words in a common palette \(X,d,e\), where \(X\) stands for \(b\) in the old word and \(a\) in the new. Order this palette cyclically as \(X,d,e\), and let \(g(u,v)=\pm1\) be the signed step between distinct letters in that order. Put \(A=\{i:c(v_i)\in\{a,b\}\}\) and \(B=\mathbb Z/5\mathbb Z\setminus A\). Both are nonempty, since the pentagon cannot be properly coloured using just two colours. Along each maximal consecutive block of \(A\), the original colours alternate; write \(p_i=+1\) if the old projected word uses \(X\) at \(i\), and \(p_i=-1\) if the new one does. The other word uses the shadow colour \(t_i\in\{d,e\}\). Write \(s_i=g(X,t_i)\).

On an internal edge \(i\to i+1\) in an \(A\)-block the old minus new step is \(p_i(s_i+s_{i+1})\). Summing internal edges of a block with first and last positions \(\ell,r\) leaves \(p_\ell s_\ell-p_r s_r\), also zero by this formula for a singleton. At a boundary edge, the shadow colour is the opposite of the adjacent \(B\)-colour (the shadow is adjacent to that original). Hence the entering and leaving boundary edges contribute \(2p_\ell s_\ell\) and \(-2p_r s_r\). Edges wholly in \(B\) contribute zero. The total difference is therefore three times the sum of entering boundary factors minus leaving boundary factors, where the factor at a boundary edge with endpoints \(i\in A,j\in B\) is \(p_i g(c(v_j),X)\).

If there are \(k\) blocks of each type, the product of the \(2k\) boundary factors is \((-1)^{5-2k}=-1\). Indeed the factors from the two ends of each block multiply to \((-1)^{\text{length}-1}\), by alternation of \(p_i\) on \(A\)-blocks and of the two original colours on \(B\)-blocks. Thus an odd number of the factors are negative. The difference of the entering and leaving sums (each has \(k\) terms) is \(2\) modulo \(4\). The old and new step sums in the common palette both belong to \(\{-3,3\}\); their difference is nonzero and they have opposite signs.

To return to the sorted palettes, identify the new palette with the old one by the transposition \((a\ b)\), sending the new \(a\) to the old \(b\). Its restriction between the sorted three-letter palettes has sign \((-1)^{a+b+1}\): deleting row \(a\) and column \(b\) from the four-letter permutation matrix changes the determinant by the cofactor sign \((-1)^{a+b}\). Permuting three letters multiplies the step sum by the sign of that permutation. If the old and new sums in their own sorted palettes are \(W_a,W_b\), common-palette opposition therefore gives \(W_a=(-1)^{a+b}W_b\), exactly the required equality of signed windings.

**Exhaustive connectivity and metric certificate.** The attached programs give two separate complete enumerations. The recursive vertex-colouring search extends every legal partial assignment; the second program instead enumerates the \(240\) proper four-colour assignments of the original pentagon and forms all admissible independent shadow choices for each apex colour. Both yield precisely \(12{,}480\) distinct states. Legal moves are formed by a neighbour-colour test in the first implementation and, independently, by grouping states that agree at ten of the eleven positions in the second. The resulting edge set has \(45{,}240\) undirected edges, and both BFS and disjoint-set union give exactly two components of size \(6{,}240\). Each component has constant \(\Omega\), with \(6{,}240\) colourings of each sign, so these are **exactly** the two invariant classes. For each fixed apex colour, its \(3{,}120\) colourings split into two connected induced subgraphs of size \(1{,}560\), one per sign; each pair of different apex colours has \(190\) cross-edges within each sign. This supplies a more refined finite connectivity witness.

The degree counts follow by examining every legal one-vertex move. The radius, diameter and eccentricity distributions are determined by BFS from one representative of each orbit under the colour-permutation group \(S_4\) and the dihedral symmetry \(D_5\) of the pentagon. Both programs independently construct this quotient, with \(56\) orbits, of which \(48\) have size \(240\) and \(8\) have size \(120\). Each group element preserves the recolouring metric, so checking all orbit representatives proves the bounds for **all** \(12{,}480\) vertices. The total eccentricity counts are \(2{,}160,10{,}200,120\) at distances \(15,16,17\); an odd palette permutation interchanges the two equal components, giving the per-component figures.

**Five-colour threshold.** The graph is three-degenerate. For example, successively delete vertices in the order \(s_0,v_1,s_2,v_0,v_4,v_3,s_4,v_2,s_1,s_3,z\); each has at most three neighbours remaining. In a \(d\)-degenerate graph every pair of proper named \(k\)-colourings is connected whenever \(k\ge d+2\): inductively reconfigure after deleting a vertex of degree at most \(d\), recolouring that vertex to an available spare colour whenever it blocks a step. This established bound gives connectivity for every \(k\ge5\). Four colours are not connected by the preceding result, and three colours do not suffice, proving the sharp threshold.

## Verification

Run `python3 verify_coloring_recursive.py` and `python3 verify_coloring_independent.py` from the same extracted directory. They use only the Python standard library. Their counted universes are exhaustive: the first assigns every possible colour to each vertex subject to prior-edge constraints; the second lists every proper outer-cycle word and every permitted apex/shadow assignment. One forms edges from recolouring constraints; the other forms all pairs at Hamming distance exactly one. Each computes all connected components and exact eccentricities using graph automorphism orbits, with no randomness or heuristics. The enumeration also checks the signed labels on all edges as a diagnostic; invariance is proved above.

## Relationship to prior work

The earlier enumeration [6] proves that there are two components, gives their sizes, edge and degree data and diameter, and shows that odd palette permutations and pentagon reflections exchange them. It also proves the five-colour mixing threshold. The chamber action by these symmetries does not by itself supply a directly evaluable signed label for an arbitrary input colouring. Cereceda, van den Heuvel and Johnson proved the degeneracy-plus-two bound and winding invariance for three-colourings of a cycle. The displayed formula lifts that invariant to the four-colouring chambers of the Mycielski graph; the extra issue is the transition between different three-letter palettes at an apex move. Brewster and Moore's cycle-wind characterization assumes a circular-colouring ratio strictly below four. No priority claim is made for the auxiliary census.

## Limitations

This result is for the **one** eleven-vertex Grötzsch graph with named colours and one-vertex moves. It is not an infinite-family connectivity or mixing-time theorem. Invariance of the label is proved directly; completeness of the label uses the two-component enumeration. An equivalent explicit label could exist under graph-homomorphism or projective-quadrangulation terminology.

## References

1. L. Cereceda, J. van den Heuvel, M. Johnson, *Connectedness of the Graph of Vertex-Colourings*, LSE-CDAM-2005-11 (July 2005), especially Theorem 3 and Lemma 4; public report: https://matthewjohnsondurham.github.io/papers/cdam-2005-11.pdf .
2. B. Mohar, G. Simonyi, G. Tardos, *Local chromatic number of quadrangulations of surfaces*, arXiv:1010.0133 (first arXiv public date 2010-10-01), https://arxiv.org/abs/1010.0133 .
3. R. C. Brewster, J. A. Noel, *Mixing Homomorphisms, Recolourings, and Extending Circular Precolourings*, arXiv:1412.3493 (first arXiv public date 2014-12-10), https://arxiv.org/abs/1412.3493 .
4. R. C. Brewster, S. McGuinness, B. Moore, J. A. Noel, *A Dichotomy Theorem for Circular Colouring Reconfiguration*, arXiv:1508.05573 (2015-08-23), https://arxiv.org/abs/1508.05573 .
5. R. C. Brewster, B. Moore, *Characterizing Circular Colouring Mixing for \(p/q<4\)*, arXiv:2008.12185 (2020-08-27), https://arxiv.org/abs/2008.12185 .
6. *Two recolouring chambers of the Grötzsch graph* (2026), https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-two-recolouring-chambers-of-the-gr-tzsch-graph--42ecfc11d759 .
