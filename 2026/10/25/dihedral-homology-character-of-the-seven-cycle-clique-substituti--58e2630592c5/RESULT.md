# Dihedral homology character of the seven-cycle clique-substitution independence complex

## Finding
For every integer \(q\ge2\), form the lexicographic product \(B_q=C_7[K_q]\) and its independence complex \(X_q=\operatorname{Ind}(B_q)\). Write \(D_7=\langle r,s\mid r^7=s^2=1,\;srs=r^{-1}\rangle\), acting on the seven clique layers by \(r(i)=i+1\) and \(s(i)=-i\) modulo seven, without changing colors. The complete **rational dihedral homology representation** is
\[
\widetilde H_1(X_q;\mathbb Q)\cong\varepsilon,\qquad
\widetilde H_2(X_q;\mathbb Q)\cong
\mathbf1^{\oplus a_q}\oplus\varepsilon^{\oplus b_q}\oplus W^{\oplus c_q},
\]
where \(\varepsilon\) is the one-dimensional reflection-sign representation, \(W\) is the six-dimensional rational irreducible (character \(6,-1,0\) on the identity, a nontrivial rotation, and a reflection, respectively), and
\[
a_q=\frac{(q-1)(q^2-2q+2)}2,\quad
b_q=\frac{(q-1)(q^2-2)}2,\quad
c_q=q(q-1)^2.
\]
All other reduced homology groups vanish. In particular, the degree-two character has values \(7q(q-1)^2\) on the identity, \(0\) on nontrivial rotations, and \(-(q-1)(q-2)\) on reflections. The invariant degree-two subspace has dimension \(a_q\). The underlying **integral**, nonequivariant homology, already encompassed by existing polyhedral-join splitting theory, is \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z\), \(H_2\cong\mathbb Z^{7q(q-1)^2}\), zero otherwise.

## Assumptions and scope
Vertices are \((i,t)\in\mathbb Z/7\mathbb Z\times\{0,\ldots,q-1\}\). Vertices in one layer span a clique; vertices in consecutive cycle layers are completely joined; vertices in distinct nonconsecutive layers are nonadjacent. An independent set therefore chooses at most one color in each layer and has a layer set independent in \(C_7\). The dihedral action permutes layers but fixes all color labels. Homology is simplicial homology of the geometric realization; reduced chains use the empty face in degree \(-1\). No claim is made for other base cycles, for other lexicographic factors, or for the larger wreath-product action.

## Proof
**1. Integral homology and absence of hidden torsion.** Put \(K=\operatorname{Ind}(C_7)\). Its faces are seven vertices, fourteen edges, seven triangles and the empty simplex. The triangles have cyclic layer sets \(\{i,i+2,i+4\}\). Each triangle has the unique free edge \(\{i,i+4\}\) of cyclic distance three. Collapsing the seven triangle/free-edge pairs leaves precisely the edges \(\{i,i+2\}\), a heptagonal cycle; hence \(K\simeq S^1\) integrally.

The augmented \(0\)-chains of every clique fiber split over \(\mathbb Z\) as \(M_i=\mathbb Ze_{i,0}\oplus U_i\), where the augmentation sends \(e_{i,0}\) to one and \(U_i=\ker(\mathbb Z^q\to\mathbb Z)\) has rank \(q-1\). Explicit generators of \(U_i\) are \(e_{i,t}-e_{i,0}\), \(1\le t<q\). Expanding the face-chain tensor products by this splitting, the augmented simplicial chain complex of \(X_q\) is an **integral direct sum of subcomplexes indexed by faces** \(T\in K\): for each \(T\), its tensor factor \(\bigotimes_{i\in T}U_i\) has zero augmentation differential and its remaining factors are the augmented simplicial chains of \(\operatorname{lk}_K T\), with degree shifted by \(|T|\). (This statement refers to chain complexes with the usual orientations; reordering joins carries the Koszul signs.) The splitting is invariant under the stated dihedral action because all fibers use the same distinguished color.

For \(T=\emptyset\), the summand is the augmented chain complex of \(K\), giving one class in degree one. Links of singleton faces are independence complexes of four-vertex paths and are contractible. Seven distance-two layer pairs have links consisting of two isolated points, each contributing \((q-1)^2\) classes in degree two. The seven distance-three pairs have a point as link and contribute none. Finally all seven maximal independent triples have link \(\{\emptyset\}\), contributing \((q-1)^3\) classes in degree two apiece. All of these link homology groups are free over \(\mathbb Z\). Thus \(\widetilde H_1(X_q;\mathbb Z)\cong\mathbb Z\) and \(\widetilde H_2(X_q;\mathbb Z)\cong\mathbb Z^{7((q-1)^2+(q-1)^3)}=\mathbb Z^{7q(q-1)^2}\), with no other reduced homology and no torsion.

**2. Symmetry in degree one.** The face \(T=\emptyset\) summand is \(K\), with cycle edges \(\{i,i+2\}\). Layer rotations preserve its orientation; each layer reflection reverses it. Therefore \(\widetilde H_1(X_q;\mathbb Q)\cong\varepsilon\).

**3. Exact degree-two character.** For any simplicial automorphism \(g\), its Lefschetz number is \(L(g)=\sum_{j=0}^2(-1)^j\operatorname{tr}(g\mid C_j(X_q;\mathbb Q))=\sum_{j=0}^2(-1)^j\operatorname{tr}(g\mid H_j(X_q;\mathbb Q))\). A nonidentity rotation fixes no nonempty face setwise: its orbits on layers have length seven, exceeding the maximum independent-set size three. Its chain Lefschetz number vanishes. Since it acts as \(+1\) on both \(H_0\) and \(H_1\), its degree-two trace is zero.

A reflection is conjugate to \(s:i\mapsto-i\). It fixes one layer, swaps two independent layer pairs and stabilizes one independent layer triple. Accordingly the **signed** chain traces \((C_0,C_1,C_2)\) are \((q,-2q,-q^2)\): the exchanged pairs reverse the orientation of a fixed edge, and the single invariant triple has its two exchanged vertices reversing the triangle orientation. Thus \(L(s)=q+2q-q^2=3q-q^2\). Since reflection traces on \(H_0\) and \(H_1\) are \(+1\) and \(-1\), respectively, \(\operatorname{tr}(s\mid H_2)=L(s)-2=-(q-1)(q-2)\). At the identity the degree-two trace is its rank \(7q(q-1)^2\).

**4. Rational irreducibles.** The rational representations of \(D_7\) consist of \(\mathbf1\), \(\varepsilon\), and the six-dimensional module \(W\) (the sum of the three Galois-conjugate two-dimensional complex irreducibles). Their characters at identity, a nontrivial rotation, and a reflection are \((1,1,1)\), \((1,1,-1)\), and \((6,-1,0)\), respectively. If their multiplicities in degree two are \((a,b,c)\), the three character values give \(a+b+6c=7q(q-1)^2\), \(a+b-c=0\), \(a-b=-(q-1)(q-2)\). Unique solution: \(c=q(q-1)^2\), \(a=(q-1)(q^2-2q+2)/2\), \(b=(q-1)(q^2-2)/2\). These are nonnegative integers for every integer \(q\ge2\), completing the classification.

## Verification
The bundled standalone `checker.py` enumerates every simplex, computes exact binary boundary ranks, evaluates signed chain traces directly, and verifies each character equation for \(q=2,3,4\). Its observed face vectors are \((14,56,56)\), \((21,126,189)\), and \((28,224,448)\); Betti vectors \((1,1,14)\), \((1,1,84)\), and \((1,1,252)\). The finite tests are independent sanity checks only: the above integral chain splitting and Lefschetz argument establish the all-\(q\) theorem.

## Relationship to prior work
Okura (2021) analyzes independence complexes of lexicographic products with **forest** bases, not this cyclic dihedral action. Carnero Bravo (2023, Theorem 28 in the accessible revised text) gives a nonequivariant wedge decomposition for the independence complex of \(C_n\circ H\) for every \(n\ge5\). In particular the nonequivariant homology just noted is a consequence of prior theory and **is not the novel claim here**. The result above adds the complete natural \(D_7\)-representation and the reflection-sensitive invariant dimension, neither of which follows from an unspecified nonequivariant homotopy equivalence. A separate study of polyhedral joins over forest independence complexes likewise has a different base hypothesis.

## Limitations
The asserted representation is rational; we do not classify the integral \(\mathbb Z[D_7]\)-lattice or color-permutation symmetry. A nonequivariant homotopy splitting need not preserve dihedral action. The finite checker establishes only the tested cases. An equivalent character calculation absent from the inspected literature remains a residual originality risk; no claim of exhaustive bibliographic uniqueness or independent review is made.

## References
- Kengo Okura, *Independence Complex of the Lexicographic Product of a Forest*, arXiv:2109.04181 (first public 2021-09-09), https://arxiv.org/abs/2109.04181.
- Andrés Carnero Bravo, *Polyhedral joins and graph complexes*, arXiv:2307.14321 (first public 2023-07-26), Theorems 20 and 28 of the open revised full text, https://arxiv.org/html/2307.14321v3.
- Kengo Okura, *On the Homotopy Type of the Polyhedral Join over the Independence Complex of a Forest*, arXiv:2303.11984 (first public 2023-03-21), https://arxiv.org/abs/2303.11984.
