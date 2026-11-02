# Nine three-spheres and the full Weyl-group homology character of the folded five-cube independence complex

## Finding
Let \(C\) be the five-regular, sixteen-vertex Clebsch graph, equivalently the folded five-cube, and let \(X=\operatorname{Ind}(C)\). Its exact integral homotopy type is
\[
 X\simeq\bigvee^{9}S^3.
\]
The full automorphism group is \(W=\operatorname{Aut}(C)\cong T\rtimes S_5\), where \(T=\mathbb F_2^5/\langle(1,1,1,1,1)\rangle\) is an elementary abelian group of order \(16\). Let \(U=\mathbb Q^5/\mathbb Q(1,1,1,1,1)\), with coordinate permutations, on which \(T\) acts trivially. For \(i\in\{1,2,3,4,5\}\), set
\[
 \chi_i(t)=(-1)^{\sum_{j\ne i} t_j}\qquad(t\in T),
\]
where the exponent is calculated modulo two from any representative. Define a five-dimensional rational \(W\)-module \(V\) with basis \(e_1,\ldots,e_5\) by
\[
 (t,p)e_i=\chi_{p(i)}(t)e_{p(i)}.
\]
Writing \(\varepsilon(t,p)=\operatorname{sgn}(p)\), the full rational homology representation is
\[
 \boxed{\ \widetilde H_3(X;\mathbb Q)\cong\varepsilon\otimes(U\oplus V).\ }
\]
All other reduced integral homology groups vanish, and \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^9\). In particular,
\[
 \dim_{\mathbb Q}H_3(X/T;\mathbb Q)=4,\qquad
 H_j(X/W;\mathbb Q)=0\quad(j>0).
\]
The second statement concerns rational homology of the orbit space, not contractibility.

## Assumptions and scope
All graphs are finite and simple. The vertices of \(C\) are the integers \(0,1,\ldots,15\), representing \(\mathbb F_2^4\). Distinct \(a,b\) are adjacent exactly when their bitwise XOR is one of \(1,2,4,8,15\). This is the quotient of the five-dimensional binary cube by its antipodal identification. Faces of \(X\) are all independent subsets, including the empty face when describing augmented chains. The ordinary action of a simplicial automorphism is oriented using the increasing vertex order. The stated module decomposition is over \(\mathbb Q\); no integral splitting of the action is asserted.

## Proof
**1. Exact integral homotopy.** A subset \(\sigma\subseteq\{0,\ldots,15\}\) is a face precisely when no pair of its vertices has XOR in \(\{1,2,4,8,15\}\). Exhaustive enumeration of all \(2^{16}\) subsets produces the face counts \(f_0=16\), \(f_1=80\), \(f_2=160\), \(f_3=120\), and \(f_4=16\), with no larger faces.

On the augmented face poset, use the ordered pivot sequence
\[
 (2,10,0,14,6,5,3,8,7,11,15,1,12,13,9,4).
\]
At each pivot \(v\), pair every currently unpaired face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever both faces are still unpaired. Process candidate faces in increasing integer bit-mask order, so the matching is deterministic. There are exactly \(192\) augmented pairs and nine remaining faces, all of size four. Discard the single pair involving the empty face, thereby leaving one critical vertex. Among the \(392\) nonempty faces, the resulting \(191\) pairs leave exactly one critical zero-cell and nine critical three-cells.

To verify acyclicity rather than assuming it, orient each covering relation of the nonempty face poset from the larger simplex to the smaller, reversing precisely the matched pairs. The complete directed graph has \(392\) vertices and \(1,200\) arcs. A topological sort visits all \(392\) vertices; it is therefore acyclic. These integer-mask enumerations are recreated by the included executable `checks/verify_clebsch.py`, with no external libraries. By the acyclic-matching theorem of discrete Morse theory, \(X\) is homotopy equivalent to a CW complex with one zero-cell, nine three-cells and no other cells. All attaching maps from two-spheres to the lone zero-cell are constant, giving the displayed wedge of nine three-spheres. This argument works integrally and excludes torsion.

**2. The full automorphism group.** The five XOR edge directions arise from the five coordinate toggles of \(\mathbb F_2^5/\langle\mathbf1\rangle\). The \(16\) translations and \(120\) coordinate permutations give \(1,920\) distinct automorphisms. Conversely an automorphism is determined by its image of a fixed vertex (\(16\) choices) and its permutation of that vertex's five neighbors (at most \(120\) choices): each of the ten vertices at distance two is uniquely determined by the pair of neighbors of the base vertex adjacent to it. Hence this is the full automorphism group.

**3. Equivariant character.** Fix \(g=(t,p)\in W\). The simplicial Lefschetz number is the finite, signed fixed-face sum
\[
 L(g)=\sum_{\substack{\varnothing\ne\sigma\in X\\g\sigma=\sigma}}
 (-1)^{|\sigma|-1}\operatorname{sgn}(g|_{\sigma}).
\]
By the proved integral homotopy type, \(L(g)=1-\operatorname{tr}(g|\widetilde H_3(X;\mathbb Q))\). Computing the sum on every one of the \(392\) nonempty faces and each of the \(1,920\) distinct group elements gives, with \(f(p)=|\{i:p(i)=i\}|\),
\[
 \operatorname{tr}(g|\widetilde H_3(X;\mathbb Q))
 =\operatorname{sgn}(p)\left(f(p)-1+
 \sum_{i:p(i)=i}\chi_i(t)\right).
\]
The verifier tests this equality separately for all \(1,920\) elements; it does not infer an entire character from a few samples. The right side is precisely the character of \(\varepsilon\otimes(U\oplus V)\). Semisimplicity of finite-group rational representations and equality of characters establish the claimed rational module isomorphism.

**4. Quotient homology.** Restrict the character to translations. The invariant dimension is the exact average \(16^{-1}\sum_{t\in T}\chi_{\widetilde H_3}(t)=4\). Averaging over all \(1,920\) group elements instead gives zero. A finite group action on a finite complex can be made simplicially admissible by barycentric subdivision, and transfer over \(\mathbb Q\) identifies the rational homology of its orbit space with the invariant homology. All other positive-degree homology groups already vanish, so the quotient statements follow.

## Verification
Run `python3 checks/verify_clebsch.py` using Python 3 and its standard library. Its deterministic final marker is `CLEBSCH_WD5_NINE_SPHERES_CHARACTER_OK`. The checker reconstructs graph edges, every independent face, the complete oriented Morse Hasse diagram and a topological ordering, all \(1,920\) distinct automorphisms, their signed fixed-face Lefschetz numbers, the proposed character values, and both group-average invariant dimensions. A separate boundary-rank computation over \(\mathbb F_2\) found reduced Betti number nine in degree three and zero in other degrees; this finite-field calculation is only a cross-check, not the integral proof.

## Relationship to prior work
Berghoff develops a general spectral-sequence framework for the homology of independence complexes, with concrete examples principally from paths, cycles and their relatives; the inspected original preprint does not give the Clebsch calculation or a \(W(D_5)\)-character. The five-regular Clebsch graph and its automorphism group are classical, as described in Brouwer's graph reference. The four-dimensional cube graph, the Clebsch Lovász neighborhood complex, and the Clebsch ordinary matching complex are different simplicial objects: claims about their homology do not imply this homotopy classification or the stated module. Contemporary work on first homology of clique complexes of strongly regular graphs is relevant context but does not, from the accessible abstract, resolve the present degree-three symmetry character. The novelty assessment remains limited to the inspected and indexed literature; bibliographic exhaustiveness is not claimed.

## Limitations
The result is for this exact sixteen-vertex folded five-cube, not every folded hypercube or every strongly regular graph. The homotopy classification is integral; the explicit automorphism-module splitting and quotient claims are rational. No integral splitting of the automorphism lattice, integral homology of the quotients, or quotient homotopy type is claimed. The accompanying computation verifies a finite face poset and finite group exhaustively; it does not constitute a general infinite-family argument. Equivalent unindexed work cannot be excluded.

## References
- M. Berghoff, *On the homology of independence complexes*, arXiv:2008.06267 (first public version 2020-08-14), https://arxiv.org/abs/2008.06267 .
- A. E. Brouwer, *Clebsch graph*, https://aeb.win.tue.nl/graphs/Clebsch.html (description of the folded five-cube and automorphisms).
- S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328 (2026; abstract examined, full text not verified), https://arxiv.org/abs/2606.27328 .
