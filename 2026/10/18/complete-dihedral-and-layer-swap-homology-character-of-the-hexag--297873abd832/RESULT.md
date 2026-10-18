# Complete dihedral and layer-swap homology character of the hexagonal-prism perfect-matching complex

## Finding

Let \(G=C_6\square K_2\), the hexagonal-prism graph, and let \(K=\mathcal M_p(G)\) be the simplicial complex of edge matchings extendable to perfect matchings. The natural action of \(D_6\times C_2\) on the reduced rational second homology is
\[
\widetilde H_2(K;\mathbb Q)\cong
\big((A\oplus B\oplus V_1)\boxtimes\mathbf 1\big)
\oplus\big(V_2\boxtimes\varepsilon\big).
\]
Here \(D_6=\langle r,s:r^6=s^2=1,\ srs=r^{-1}\rangle\), the second factor \(C_2=\langle t\rangle\) exchanges the prism layers, and \(\mathbf1,\varepsilon\) are its trivial and sign representations. As \(D_6\)-modules, the lines \(A,B\) have \(A(r)=1,A(s)=-1\) and \(B(r)=-1,B(s)=1\). For \(j=1,2\), \(V_j\) is the rational two-dimensional dihedral representation with rotation trace \(2\cos(2\pi ja/6)\) on \(r^a\) and reflection trace zero. Thus the six-dimensional homology contains the frequency-one plane in the layer-even sector and the frequency-two plane in the layer-odd sector.

For all integers \(0\le a<6\) and \(b,c\in\{0,1\}\), its full character is
\[
\operatorname{tr}\big(r^as^bt^c\big|\widetilde H_2(K;\mathbb Q)\big)=
\begin{cases}
1+(-1)^a+2\cos(\pi a/3)+(-1)^c2\cos(2\pi a/3),&b=0,\\
-1+(-1)^a,&b=1.
\end{cases}
\]
Equivalently, the four rows indexed by \((b,c)=(0,0),(0,1),(1,0),(1,1)\), and columns \(a=0,1,2,3,4,5\), are respectively
\[
(6,0,0,0,0,0),\quad(2,2,2,-4,2,2),\quad
(0,-2,0,-2,0,-2),\quad(0,-2,0,-2,0,-2).
\]
Its integral reduced homology is \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^6\) and vanishes in every other degree.

## Assumptions and scope

Graph vertices are \((\ell,i)\), where \(\ell\in\{0,1\}\) and \(i\in\mathbb Z/6\mathbb Z\). The eighteen graph edges consist of twelve horizontal edges \((\ell,i)(\ell,i+1)\) and six vertical edges \((0,i)(1,i)\). A face of \(K\) is exactly a subset of at least one perfect matching; in particular this is not the ordinary matching complex. The graph maps are \(r(\ell,i)=(\ell,i+1)\), \(s(\ell,i)=(\ell,-i)\), and \(t(\ell,i)=(1-\ell,i)\). All homology is reduced simplicial homology. Rational representations are considered over characteristic zero. No statement is made for other prism lengths.

## Proof

**Integral chain computation.** Give the eighteen graph edges a fixed lexicographic ordering, so every face is canonically oriented by increasing edge index. Exhaustive perfect-matching enumeration chooses the least unmatched graph vertex and branches over each incident edge joining it to another unmatched vertex. By induction on the number of unmatched vertices, this procedure lists every perfect matching exactly once after deduplication. It gives exactly twenty perfect matchings. Closing the resulting maximal faces under taking subsets gives 822 faces including the empty face; the counts in cardinalities zero through six are \((1,18,117,276,270,120,20)\).

Form the augmented integral simplicial chain complex, with \(\partial[e_1,\ldots,e_k]=\sum_{j=1}^k(-1)^{j-1}[e_1,\ldots,\widehat e_j,\ldots,e_k]\). For a unit incidence \(u=[\partial\tau:\sigma]=\pm1\) between adjacent-dimensional chain generators, replace the boundary of every other generator \(x\) of degree \(\deg\tau\) by
\[
\partial' x=\partial x-\frac{[\partial x:\sigma]}{u}\partial\tau,
\]
then delete \(\sigma\) and \(\tau\). This is an integral chain-homotopy cancellation: the unit pivot splits off a contractible two-generator complex over \(\mathbb Z\), and the displayed formula is its exact Schur complement. Both chain groups remain free with integral bases. Applying the deterministic minimum-fill unit-pivot rule defined in the accompanying executable produces exactly 408 such cancellations. The residual augmented chain complex has precisely six generators, all in simplicial degree two, and zero differential. Therefore its only nonzero reduced integral homology is \(\mathbb Z^6\) in degree two. The executable checks the augmented chain identity, every chosen pivot, and the final reduction.

**Action and character.** Every graph automorphism permutes edge-vertices of \(K\). For an oriented simplex \(\sigma\) fixed setwise by an automorphism \(g\), the induced chain map acts by the sign of the permutation of its vertices. Hopf's trace identity for the finite augmented complex gives the reduced Lefschetz character
\[
L(g)=-1+\sum_{\substack{\varnothing\ne\sigma\in K\\g\sigma=\sigma}}
(-1)^{\lvert\sigma\rvert-1}\operatorname{sgn}(g\vert_{\sigma}).
\]
The \(-1\) is the augmented degree-minus-one chain trace. Because homology is concentrated in degree two, \(L(g)=\operatorname{tr}(g\vert\widetilde H_2(K;\mathbb Q))\). Enumerating all setwise-invariant faces with the stated orientation sign for each of the twenty-four elements \(r^as^bt^c\) yields the four six-entry rows displayed above. The standalone verifier computes these integers directly from the 822-face set; its symmetry maps are explicit vertex permutations, not a presumed homology action.

**Identification of the module.** Character values of \(A\oplus B\oplus V_1\) on rotations are \(1+(-1)^a+2\cos(\pi a/3)\), and on reflections they are \(-1+(-1)^a\). The \(V_2\) character is \(2\cos(2\pi a/3)\) on rotations and zero on reflections. Tensoring \(V_2\) by \(\varepsilon\) introduces \((-1)^c\), giving exactly the computed twenty-four traces. Since \(A,B,V_1,V_2\) are rational irreducible \(D_6\)-modules and finite-dimensional characteristic-zero representations are semisimple, equality of characters proves the asserted rational-module decomposition.

## Verification

Run `python3 hexagonal_prism_perfect_matching_character.py` with Python 3.10 or later, using only the standard library. It constructs graph edges, recursively enumerates perfect matchings and all faces, verifies initial and intermediate augmented chain identities, performs 408 integral unit cancellations, checks the six terminal degree-two generators, and independently evaluates the twenty-four signed fixed-simplex traces. The program checks the character formula for every group element and displays the four complete trace rows. An additional edge-order randomization stress test, outside the delivered reproducibility dependency, matched five characteristic symmetry classes in thirty independent relabelings.

## Relationship to prior work

Agarwal and Basak, arXiv:2608.30601 (first version August 31, 2026; revised September 14, 2026), Theorem 25, established the non-equivariant wedge-of-six-two-spheres homotopy type at this prism length. Their theorem supplies the six-dimensional rank but not the representation of the dihedral rotations, two reflection classes, or layer exchange. The present calculation is an equivariant refinement; the ordinary homotopy type alone does not determine any of the nonidentity character values. Chandrakar and Singh, arXiv:2407.05809, analyzed perfect matching complexes of polygonal line tilings and rectangular ladders, not this circular prism action. Related published symmetry calculations concern different complexes (independence or total-cut complexes on circular ladders), and different graphs (ordinary matching homology of a linear ladder or Möbius-ladder perfect matching homology); they do not imply the stated character.

## Limitations

The equivariant decomposition is over \(\mathbb Q\); no classification of the integral group-ring module is asserted. This finite calculation applies to the hexagonal prism only and does not provide a formula for every circular ladder. Literature and indexed-record searches did not identify an equivalent result, but inaccessible or unindexed sources could affect originality.

## References

1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first posted August 31, 2026, version 2 September 14, 2026, especially Theorem 25 and Section 5.2.
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first posted July 8, 2024.
3. J. P. Serre, *Linear Representations of Finite Groups*, Springer, 1977 (character orthogonality and semisimplicity).
