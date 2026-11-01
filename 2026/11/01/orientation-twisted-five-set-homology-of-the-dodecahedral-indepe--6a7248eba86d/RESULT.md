# Orientation-twisted five-set homology of the dodecahedral independence complex

## Finding
Let \(D=GP(10,2)\) be the twenty-vertex dodecahedral graph and let \(X=\operatorname{Ind}(D)\) be its ordinary simplicial independence complex. Write \(G=\operatorname{Aut}(D)\cong A_5\times C_2\). There are precisely five independent vertex sets of cardinality eight; denote their \(G\)-set by \(\mathcal I\). Let \(\varepsilon:G\to\{\pm1\}\) be the orientation character of the natural cellular action on the embedded dodecahedron (the nontrivial character of the central inversion factor). Then

\[
\widetilde H_5(X;\mathbb Q)\ \cong_{\mathbb Q[G]}\ \mathbb Q_{\varepsilon}\otimes\left(\mathbb Q^{\mathcal I}/\mathbb Q\mathbf1\right),
\qquad \widetilde H_j(X;\mathbb Q)=0\quad(j\ne5).
\]

Equivalently, for every \(g\in G\), the complete rational character is
\[
\operatorname{tr}\bigl(g\mid\widetilde H_5(X;\mathbb Q)\bigr)
=\varepsilon(g)\bigl(\#\operatorname{Fix}_{\mathcal I}(g)-1\bigr).
\]
The degree-five representation restricts to the irreducible four-dimensional augmentation representation of \(A_5\), and central inversion acts as minus the identity. In particular it has no nonzero vectors fixed by all graph symmetries.

## Assumptions and scope
The graph has vertices \(a_i,b_i\) for \(i\in\mathbb Z/10\mathbb Z\), and edges \(a_i a_{i+1}\), \(a_i b_i\), and \(b_i b_{i+2}\), with each undirected edge included once. Faces of \(X\) are **all** independent vertex sets, including the empty face in the augmented chain complex. The claim is for **rational** reduced homology and the **ordinary** graph automorphism action. It does not identify an integral \(\mathbb Z[G]\)-lattice or claim an equivariant homotopy equivalence.

For a planar automorphism, \(\varepsilon(g)\) is \(+1\) if the cyclic order of the three neighbors at every vertex is preserved by the automorphism and \(-1\) if reversed. Three-connected planarity makes this intrinsic up to overall reversal of the chosen orientation.

## Proof
**1. Rational homology concentration.** Exhaustive independent-set enumeration in the explicit graph gives, by cardinality from zero to eight,
\[
(f_0,\ldots,f_8)=(1,20,160,660,1510,1912,1240,320,5).
\]
Here \(f_k\) counts independent \(k\)-element sets, not simplicial dimension. For \(d=1,\ldots,7\), the exact binary boundary ranks \(\operatorname{rank}_{\mathbb F_2}(\partial_d)\), with \(\partial_d:C_d\to C_{d-1}\), are
\[
(19,141,519,991,921,315,5).
\]
The augmentation \(\partial_0:C_0\to C_{-1}\) has rank one. These counts and ranks yield reduced \(\mathbb F_2\)-Betti numbers \((0,0,0,0,0,4,0,0)\) in dimensions zero through seven. Rational Betti numbers cannot exceed mod-two Betti numbers, by the integral universal coefficient theorem. The reduced Euler characteristic is \(-4\), so the sole nonzero reduced rational homology group is four-dimensional and lies in degree five. This step makes no assertion about possible odd-primary torsion in integral homology.

**2. The two character expressions.** Any automorphism acts simplicially on augmented chains. The Hopf trace formula, using the preceding rational homology concentration, gives
\[
\operatorname{tr}(g\mid\widetilde H_5(X;\mathbb Q))=
\sum_{S\in X,\,gS=S}(-1)^{|S|}\operatorname{sgn}(g|_S).
\]
The empty face contributes \(+1\) to the displayed sum. For nonempty \(S\), \(\operatorname{sgn}(g|_S)\) is the sign of the induced permutation of its sorted vertices. The formula follows by taking alternating traces of the augmented chains, including the degree-minus-one augmentation term.

**3. Exact exhaustion of graph symmetries.** Exhaustive finite graph-isomorphism search gives exactly \(120\) automorphisms. The action on the five maximum independent sets has exactly \(60\) images, all even permutations; it is \(A_5\). The natural embedding of the dodecahedral graph has a well-defined orientation sign, with \(60\) preserving and \(60\) reversing automorphisms. The independent-set character sum in step 2 was evaluated exactly for **every** automorphism and compared with \(\varepsilon(g)(\#\operatorname{Fix}_{\mathcal I}(g)-1)\). The following complete census records \((\varepsilon,\#\operatorname{Fix},\operatorname{tr};\text{multiplicity})\):
\[
(+1,5,4;1),\ (+1,2,1;20),\ (+1,1,0;15),\ (+1,0,-1;24),
\]
\[
(-1,5,-4;1),\ (-1,2,-1;20),\ (-1,1,0;15),\ (-1,0,1;24).
\]
All steps are specified by the finite graph and reproduced by the standalone exact verifier. The enumeration is exhaustive, not a sample or statistical inference.

**4. Character-to-module conclusion.** The reduced permutation module \(\mathbb Q^{\mathcal I}/\mathbb Q\mathbf1\) has character \(\#\operatorname{Fix}_{\mathcal I}(g)-1\). Tensoring with \(\mathbb Q_\varepsilon\) multiplies its character by \(\varepsilon(g)\). Step 3 proves equality of the rational characters on all group elements. Semisimplicity of \(\mathbb Q[G]\) implies the asserted rational-module isomorphism. The image on \(\mathcal I\) is the usual five-point \(A_5\) action, which is two-transitive, so its reduced permutation module is irreducible over \(\mathbb Q\). The central inversion has \(\varepsilon=-1\) and fixes all five sets, giving trace \(-4\) and hence action \(-I\).

## Verification
Run `python verify_character.py` from the directory containing this file, with Python 3 and NetworkX installed. The verifier constructs \(GP(10,2)\), checks isomorphism to the standard dodecahedral graph, enumerates all \(5828\) independent sets, computes the seven exact mod-two boundary ranks by bitset elimination, enumerates all \(120\) graph automorphisms, checks orientation signs at every vertex, and checks all \(120\) signed Lefschetz identities. The packaged `verification_output.txt` contains its complete output; a fresh execution returned `VERIFY_OK`. In particular the binary chain computations give only a **rational** homology-concentration premise; the character proof uses no assumption of integral torsion-freeness.

## Relationship to prior work
Barmak's 2010 work develops the topology of independence complexes of graphs. A published result on the dodecahedral independence complex establishes the nonequivariant wedge of four five-spheres; that conclusion alone does not determine the four-dimensional symmetry module. Lew's 2021 thesis, Section 4.5.2, identifies the five maximum independent sets of the same graph but calculates the homology of the **different** threshold complex \(I_8(D)\), not the symmetry module of \(\operatorname{Ind}(D)\). The present assertion is specifically the complete orientation-twisted character of the ordinary independence complex. Related existing icosahedral representation calculations concern neighborhood, graph-configuration, or scale-three Rips complexes, not this module.

## Limitations
The module is determined over \(\mathbb Q\), not over \(\mathbb Z\) or finite fields. The completeness of the calculation is finite and reproducible, but an equivalent statement in unindexed literature remains possible. A relevant published nonequivariant record was available as an indexed summary, while its full underlying text was not accessible during the comparison; no claim of whole-document exclusion is made. Independent mathematical assessment has not been performed.

## References
- Jonathan A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first public version 2010-07-02; Advances in Mathematics 241 (2013).
- Alan Lew, *Studies in Topological Combinatorics*, PhD thesis, 2021, Section 4.5.2, pp. 88–89, https://www.math.cmu.edu/users/alanlew/files/theses/phd%20thesis.pdf.
- *The dodecahedral independence complex is a wedge of four 5-spheres*, published mathematical finding indexed as `ba0161fd495f` (2026-10-04); title and abstract available, full text not accessed.
