# Integral dihedral homology of pure Morse complexes of cycles

## Finding

Let \(n\ge5\), let \(C_n\) be the graph with vertices \(i\in\mathbb Z/n\mathbb Z\) and edges \(e_i=\{i,i+1\}\), and let \(P_n=\mathcal M_{\mathrm{pure}}(C_n)\) be the pure discrete-Morse complex: its vertices are incident vertex–edge pairs of \(C_n\), and its facets are the acyclic incidence matchings of cardinality \(n-1\). The natural dihedral group \(D_n=\langle r,s\mid r^n=s^2=1,\ srs=r^{-1}\rangle\) acts by \(r(i)=i+1\) and \(s(i)=-i\). Define the integral one-dimensional character \(\eta_n\) by \(\eta_n(r)=(-1)^{n-1}\) and \(\eta_n(s)=1\).

**Theorem.** As integral \(\mathbb Z[D_n]\)-modules,
\[
\widetilde H_2(P_n;\mathbb Z)\cong\mathbb Z_{\mathrm{triv}},\qquad
\widetilde H_{n-2}(P_n;\mathbb Z)\cong
\eta_n\otimes_{\mathbb Z}\mathbb Z[D_n/\langle r\rangle],
\]
and every other reduced integral homology group vanishes. The second module is the sign-twisted integral permutation lattice on two points: rotations act by \((-1)^{n-1}I\), and a reflection interchanges its two suitably oriented basis vectors. In particular, for odd \(n\), the top homology is the ordinary rank-two permutation lattice; for even \(n\), rotations act by \(-I\). This is an *integral* statement, not only a rational character identity.

Consequently, the rational homology of the full dihedral quotient has a one-dimensional class in degree \(2\) for all \(n\ge5\), and an additional one-dimensional class in degree \(n-2\) precisely for odd \(n\). No other reduced rational quotient homology survives.

## Assumptions and scope

Incidence pairs are encoded as \(w_{2i}=(i,e_i)\) and \(w_{2i+1}=(i+1,e_i)\), with subscripts read modulo \(2n\). These label edges of the incidence cycle \(C_{2n}\). The induced dihedral generators act as \(r(w_j)=w_{j+2}\) and \(s(w_j)=w_{2n-1-j}\). A simplicial face is a submatching extendible to a maximal acyclic incidence matching of size \(n-1\). We require \(n\ge5\) so that the known homology degrees \(2\) and \(n-2\) are distinct. The quotient assertion concerns rational singular homology of the geometric orbit space, not integral quotient torsion or equivariant homotopy equivalence.

## Proof

**1. Facets and ordinary homology.** A maximal incidence matching of size \(n-1\) is obtained by deleting one edge from \(C_n\) and choosing a root in the resulting spanning path. All matched incidences are oriented toward that root; conversely each such facet yields its deleted edge and root. There are \(n^2\) facets. In the incidence cycle these are precisely the matchings of size \(n-1\); they leave two unmatched vertices of opposite incidence-bipartition types, and matching along the two complementary paths is forced. Chari–Joswig, Theorem 4.1, proves
\[
P_n\simeq S^2\vee S^{n-2}\vee S^{n-2}
\quad(n\ge4).
\]
Therefore \(\widetilde H_2\cong\mathbb Z\), \(\widetilde H_{n-2}\cong\mathbb Z^2\), and all other reduced integral groups vanish for \(n\ge5\). This **nonequivariant homotopy calculation is prior work**, used here as a premise.

**2. A primitive integral top-homology basis.** In the abstract full simplex on the incidence vertices define the ordered alternating sets \(E=(w_0,w_2,\ldots,w_{2n-2})\) and \(O=(w_1,w_3,\ldots,w_{2n-1})\). Neither set is a face of \(P_n\), but deletion of any one member of either set gives an \((n-2)\)-dimensional facet. Hence their formal oriented boundaries \(z_E=\partial[E]\) and \(z_O=\partial[O]\) are integral cycles in \(P_n\). They are nonzero, have disjoint facet supports, and have coefficients \(\pm1\) on every supported facet. Because the complex has dimension \(n-2\), its top boundary group is zero. The preceding rank-two homology calculation implies every top rational cycle has a unique expansion \(a z_E+b z_O\). If that cycle is integral, the coefficient on any facet of \(z_E\), respectively \(z_O\), forces \(a,b\in\mathbb Z\). Thus \(z_E,z_O\) are an integral basis of top homology, not merely generators over \(\mathbb Q\).

The rotation induces an \(n\)-cycle on each of \(E,O\), so \(r(z_E)=(-1)^{n-1}z_E\) and \(r(z_O)=(-1)^{n-1}z_O\). Reflection exchanges \(E\) and \(O\). Since \(s^2=1\), a choice of sign for the second basis vector makes \(s\) interchange the two basis vectors without an extra sign. This proves the claimed integral top-homology module.

**3. The degree-two character on the rotation generator.** Every orbit of the generator \(r\) on the \(2n\) incidence vertices has length \(n\), while a face contains at most \(n-1\) vertices. Thus no nonempty face is \(r\)-invariant. The signed *reduced* simplicial Lefschetz number is \(\widetilde L(r)=-1\), contributed solely by the empty augmented simplex. The preceding top-homology basis has trace \(2(-1)^{n-1}\). As only degrees \(2\) and \(n-2\) can contribute, the Lefschetz identity gives
\[
-1=\operatorname{tr}(r\mid\widetilde H_2)
+(-1)^{n-2}\,2(-1)^{n-1}
=\operatorname{tr}(r\mid\widetilde H_2)-2.
\]
Consequently \(r\) acts as \(+1\) on the rank-one integral group \(\widetilde H_2\).

**4. Reflection-fixed faces and the degree-two character.** For \(s(w_j)=w_{2n-1-j}\), the incidence-vertex orbits are \(Q_j=\{w_j,w_{2n-1-j}\}\) for \(0\le j<n\). The orbits \(Q_0,Q_{n-1}\) contain adjacent incidence edges and cannot occur in a face. Each remaining \(Q_j\), \(1\le j\le n-2\), occurs in a face. Moreover, a union of these orbits is a face **if and only if** all chosen indices \(j\) have the same parity. To verify the only-if part, consider the circularly ordered \(2n\) incidence edges of a facet: \(n-1\) selected edges must be nonadjacent, so the total excess of circular spacings above the minimum spacing of two is precisely \(2\). Selecting both an odd-index and even-index \(Q_j\) forces four selected incidence edges, in circular order, of alternating parities; each of their four intervening spacings is odd and at least three. The required excess is at least four, a contradiction. Conversely, the incidence edges from all allowable odd indices, or from all allowable even indices, form a matching that can be completed by alternating edges across the remaining two gaps to a facet of size \(n-1\); any subcollection is consequently a face.

There are \(a=\lfloor(n-2)/2\rfloor\) and \(b=\lceil(n-2)/2\rceil\) eligible indices of the two parities. Both numbers are positive. The geometric fixed-point set \(|P_n|^s\) is therefore the disjoint union of two simplices of dimensions \(a-1\) and \(b-1\): a fixed point has equal barycentric coordinates on both members of each selected orbit. Thus \(\chi(|P_n|^s)=2\), and its reduced Lefschetz number is \(\widetilde L(s)=1\). Reflection exchanges the two top-homology basis vectors, hence has top trace zero. Therefore \(\operatorname{tr}(s\mid\widetilde H_2)=1\). As \(r,s\) generate \(D_n\), its action on \(\widetilde H_2\cong\mathbb Z\) is trivial.

**5. Rational quotient consequence.** For a finite group acting simplicially, rational homology of the geometric quotient identifies with invariants in the original rational homology (e.g. by barycentric subdivision and averaging). The trivial degree-two module contributes one invariant. When \(n\) is odd, the top two-point permutation module has a one-dimensional invariant subspace. When \(n\) is even, the rotation acts by \(-I\), so its top invariants vanish. These are all possibilities by the nonequivariant concentration theorem.

## Verification

The two standalone Python 3 programs `verify_faces.py` and `verify_chains.py` use only the standard library. Run `python3 verify_faces.py` and `python3 verify_chains.py` from their containing directory. The first independently enumerates all faces generated by rooted spanning paths for \(5\le n\le11\), checks all \(2n\) dihedral elements and signed Lefschetz traces, and counts reflection-invariant face orbits. The second generates facets by deleting opposite-parity incidence vertices, computes augmented boundary ranks over both \(\mathbb F_2\) and \(\mathbb F_{101}\) for \(5\le n\le9\), and verifies the two top boundary cycles. Both pass; finite checks corroborate rather than replace the infinite-family proof.

## Relationship to prior work

Chari and Joswig proved the precise nonequivariant sphere-wedge classification of \(P_n\) used in Step 1 and studied the face structure; their Theorem 4.1 does not identify the integral action of each dihedral generator on both homology groups. Lin and Scoville determine the automorphism group of the **full** Morse complex of a cycle but do not state this pure-complex integral homology representation. Ayala, Fernández, Quintero and Vilches study the structure of pure Morse complexes using spanning trees; only their abstract was available for comparison, so possible related full-text results remain a bibliographic risk. The present theorem concerns the explicit integral dihedral action, not the known ordinary homotopy type.

## Limitations

The result is restricted to the pure complex of a simple cycle with \(n\ge5\) and its geometrically induced \(D_n\)-action. It does not claim that the full Morse complex has this representation, does not determine the action of every potentially larger abstract automorphism group, and does not determine torsion in the integral homology of the quotient. A first-party proof of the nonequivariant homotopy theorem is not reproduced; its exact published theorem is explicitly invoked. Searches cannot establish absolute novelty, and the potentially related 2008 source was not inspected beyond its abstract.

## References

1. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234, first posted 2000-11-28, especially Definition 2 and Theorem 4.1, https://arxiv.org/pdf/math/0011234.
2. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907, 2019, https://arxiv.org/pdf/1904.10907.
3. R. Ayala, L. M. Fernández, A. Quintero and J. A. Vilches, *A note on the pure Morse complex of a graph*, *Topology and its Applications* **155** (2008), 2084–2089, doi:10.1016/j.topol.2007.04.023 (abstract inspected).
