# The rational cube-symmetry module of the three-non-matching complex

## Finding

Take the graph \(Q_3\) on the binary words of length three, with edges at Hamming distance one. Let \(K\) be the simplicial complex on its twelve edges whose faces are the edge sets with no matching of size three. Under the full graph automorphism group \(B_3=(C_2)^3\rtimes S_3\), its reduced degree-three rational homology is
\[
\widetilde H_3(K;\mathbb Q)\cong P\oplus(\epsilon\otimes U)\oplus(\epsilon\otimes\textstyle\bigwedge^2 U).
\]
Here \(P\) permutes the three coordinate directions, \(U\) is the signed coordinate module (a bit flip negates that coordinate), and \(\epsilon\) is the sign of the coordinate permutation, trivial on bit flips. In particular, the antipodal flip has trace three, with six invariant and three anti-invariant dimensions. The claim concerns a rational module, not an integral lattice or equivariant homotopy classification.

## Homotopy input and exact computation

The nonequivariant homotopy type \(\bigvee^9 S^3\) is independently stated in *Complete non-matching homotopy filtration of the three-dimensional cube* (Resultary `3f5c353dbcef`, Finding and critical-cell table). For a self-contained certificate of the required concentration in degree three, order edges by increasing smaller endpoint \(v\in\{0,\ldots,7\}\), then by increasing bit index \(j\) in the larger endpoint \(v\mathbin{\rm xor} 2^j\). Enumerate all edge masks and exclude those containing one of the 44 triples with six distinct endpoints. The 601 augmented faces have vector \((1,12,66,176,222,108,16)\) starting with the empty face. On this face family, successively pair available masks differing only in the current pivot bit, in the order
\[
(2,10,11,5,0,4,9,6,7,3,8,1).
\]
Drop the pairing of the empty face with bit 2. The resulting ordinary matching has 295 pairs; its critical cells are the vertex at bit 2 and the nine three-simplices with masks \(51,105,177,1186,1289,1314,2569,2577,2720\). Orient unmatched Hasse covers upward and matched covers downward. The attached verifier topologically sorts all 600 nonempty faces, proving acyclicity for this pairing. Discrete Morse theory yields a CW model with one 0-cell and nine 3-cells only, hence the stated wedge and concentration of integral reduced homology in degree three.

Every cube automorphism comes from a coordinate permutation and a bit-flip vector: once the image of the zero word and those of its three neighbors are known, distances from these vertices determine the other images. For any such automorphism \(g\), the reduced Lefschetz trace formula and degree-three concentration give
\[
\mathrm{tr}(g\mid\widetilde H_3(K;\mathbb Q))
=\sum_{F\in K:\ gF=F}(-1)^{|F|}\mathrm{sgn}(g\mid_F).
\]
The empty face contributes one. An invariant face is a union of cycles of the edge permutation, and a face consisting of \(c\) such cycles contributes \((-1)^c\). For example, the antipodal flip has six cycles of length two; exactly \((1,6,12,4)\) invariant faces use \(0,1,2,3\) of them respectively and none use more. Its trace is \(1-6+12-4=3\).

For a coordinate permutation \(\sigma\) and bit flips \(b\), the proposed module's character is
\[
\#\mathrm{Fix}(\sigma)+\mathrm{sgn}(\sigma)(\mathrm{tr}\,U+\mathrm{tr}\,\bigwedge^2U).
\]
The two traces on the right sum, respectively, the signed contributions of fixed axes and invariant unordered axis pairs, including the orientation sign of interchanging the two axes in a fixed pair. Evaluating both character expressions for every one of the 48 automorphisms gives equality element by element. The common histogram is \(-1:6,\ 0:16,\ 1:15,\ 3:10,\ 9:1\). Rational representations of a finite group are semisimple and distinguished by their characters, proving the claimed decomposition.

## Verification

The unchanged standard-library `verify.py` rebuilds the faces, verifies Morse acyclicity and all 48 signed Lefschetz sums, and compares with the proposed character. Its expected output is `verification_output.json`. The mod-two boundary-rank cross-check in the output is not a replacement for the integral Morse argument.

## Relation to other results

Linusson, Shareshian and Welker, arXiv:`math/0410345`, Theorem 1.4, obtain nine three-spheres for the complete bipartite \(K_{4,4}\) complex. The complete-bipartite equivariant prediction is Conjecture 1.14 in the inspected arXiv text. The cube lacks the antipodal perfect matching; the ambient theorem does not itself give the cube's rank. Once the rank is known, the edge-addition injection of Shan and Wang, arXiv:`2609.02621`, Theorem 2.1, identifies rational \(H_3\) with that of the ambient complex under the cube group. Holmsen and Lee, arXiv:`2003.11270`, Theorem 1.2, give general link-vanishing bounds rather than the cube character.

The complete-bipartite hook-tensor result (Resultary `f6ab14dd0ec4`, Finding) then gives an alternate route to the part-preserving restriction by restricting the ambient \(S_4\times S_4\) module. That restriction does not determine the full group action: the antipodal flip exchanges the bipartition classes, and twisting an extension by the sign of the part swap leaves the restriction the same. The cube calculation explicitly resolves the part-swapping coset and compares the full character. The nonequivariant classification is input, not the distinct contribution here. No priority is inferred from the catalogue dates.
