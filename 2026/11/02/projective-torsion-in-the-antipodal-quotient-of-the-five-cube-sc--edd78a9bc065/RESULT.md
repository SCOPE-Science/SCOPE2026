# Projective torsion in the antipodal quotient of the five-cube scale-three Rips complex

## Finding
Let \(Q_5=\{0,1\}^5\) carry Hamming distance, and let \(X=\operatorname{VR}_{\le3}(Q_5)\). The central involution \(\tau(v)=v\oplus(1,1,1,1,1)\) acts freely on its geometric realization. For the *geometric orbit space* \(Y=|X|/\langle\tau\rangle\), integral homology is
\[
H_j(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z/2,&j=1,3,\\
\mathbb Z^5,&j=7,\\
0,&\text{all other }j.
\end{cases}
\]
Moreover, writing \(t\in H^1(Y;\mathbb F_2)\) for the class classifying the double cover, the mod-two cohomology ring consists of \(\mathbb F_2[t]/(t^5)\), together with five additional degree-seven classes. All positive-degree products involving those five classes vanish. In particular, \(t^4\ne0\) and \(t^5=0\). The integral cohomology has a degree-two class \(b\) with \(2b=0\), \(b^2\ne0\), and \(b^3=0\), plus five free degree-seven classes with zero positive-degree products.

## Assumptions and scope
The simplicial complex is *inclusive* at Hamming radius three: a nonempty subset is a simplex exactly when all pairwise distances are at most three. The action is induced by complementing all five bits; the quotient is taken **after geometric realization**, not by first equipping the sixteen antipodal vertex-orbits with a quotient metric and then forming another Rips complex. Coefficients and the ring structure are as stated above. No homotopy-equivalence claim to a wedge containing projective space is made.

## Proof
**1. Previously established integral homology of the cover.** Feng's scale-three hypercube homotopy theorem, applied at dimension five, gives
\[
X\simeq S^4\vee\bigvee^{10}S^7.
\]
Thus its only nonzero positive-dimensional integral homology is \(H_4(X;\mathbb Z)=\mathbb Z\) and \(H_7(X;\mathbb Z)=\mathbb Z^{10}\).

**2. Primitive antipodal-paired generators in degree seven.** The ten coordinate four-facets of \(Q_5\), indexed by a fixed coordinate and its value, are all copies of \(Q_4\). Within each, the scale-three Rips complex is the boundary of the eight-dimensional cross-polytope: its sixteen vertices split into eight opposite pairs. Let \(z_{i,a}\) denote an oriented fundamental seven-cycle in the facet fixing coordinate \(i\) at \(a\in\{0,1\}\).

The maximal-simplex dual-cocycle argument of Adams–Virk can be verified explicitly here. For a given four-facet, order its four free coordinates, take all eight vertices for which the sum of the first three free bits is even and the fourth free bit is arbitrary, and call this seven-simplex \(\sigma_{i,a}\). This simplex is maximal even in \(X\), and its vertices span their entire four-facet. Hence its indicator integral cochain is a cocycle. It evaluates to \(\pm1\) on \(z_{i,a}\) and to zero on each of the other nine cycles. The resulting unimodular pairing proves that the ten homology classes form a primitive independent sublattice. Since \(H_7(X;\mathbb Z)\) has rank ten and no torsion, they form an integral basis.

The involution exchanges \(z_{i,0}\) and \(z_{i,1}\). On the cross-polytope sphere, complementing its four free coordinates flips all eight opposite pairs, with orientation determinant \((-1)^8=+1\). Orient both parallel facets compatibly. Therefore
\[
H_7(X;\mathbb Z)\cong\mathbb Z[\mathbb Z/2]^5
\]
as a module for the antipodal group. The action is free on simplices: a setwise-invariant nonempty simplex would have to contain a vertex and its Hamming-distance-five complement. In particular, its Lefschetz number is zero. Since the degree-seven trace is zero, \(0=1+\operatorname{tr}(\tau|H_4)-0\) proves that \(\tau\) acts by minus one on \(H_4(X;\mathbb Z)\).

**3. The mod-two Cartan–Leray calculation.** Because \(\tau\) acts freely, the Borel construction of \(X\) is homotopy equivalent to \(Y\). Consider the multiplicative cohomology spectral sequence
\[
E_2^{p,q}=H^p(\mathbb Z/2;H^q(X;\mathbb F_2))\Longrightarrow H^{p+q}(Y;\mathbb F_2).
\]
Its only nonzero rows are \(q=0,4,7\). The row \(q=0\) is \(\mathbb F_2[t]\), the row \(q=4\) is \(\mathbb F_2[t]u\) for a class \(u\) in bidegree \((0,4)\), and the row \(q=7\) consists of exactly five copies of \(\mathbb F_2\) at column zero, because \(H^7(X;\mathbb F_2)\) is five regular modules and regular modules have vanishing higher group cohomology.

The only potentially nonzero differential from the last row to the middle row is \(d_4\). It vanishes: for a class \(v\) in bidegree \((0,7)\), the relation \(tv=0\) forces \(t\,d_4v=0\), while multiplication by \(t\) is injective in the middle row on the \(E_4\)-page. The remaining possible differentials are \(d_5(u)=c\,t^5\) and \(d_8\) from the last row to the bottom row. If \(c=0\), the \(d_5\) family vanishes by multiplicativity; the same \(tv=0\) argument then forces \(d_8=0\), leaving nonzero classes \(t^k\) for arbitrarily large \(k\). This contradicts finite dimensionality of \(Y\). Therefore \(c=1\), and by multiplicativity \(d_5(t^ku)=t^{k+5}\) for all \(k\ge0\). The last row survives, and no other classes survive in degrees above four except the five degree-seven classes. This proves the mod-two cohomology ring asserted above, including the nonzero fourth power of \(t\).

**4. Integral homology and products.** Rational transfer gives \(H_7(Y;\mathbb Q)=\mathbb Q^5\) and no other positive-dimensional rational homology. The integral transfer identity \(\pi_*\operatorname{tr}=2\operatorname{id}\) and the torsion-free homology of \(X\) imply that all torsion in \(H_*(Y;\mathbb Z)\) is two-primary. The mod-two cohomology dimensions and the universal-coefficient theorem show that there is exactly one two-primary cyclic summand in each of homological degrees one and three, and no others. Since \(X\) is simply connected and is the universal double cover of \(Y\), \(H_1(Y;\mathbb Z)=\mathbb Z/2\). In the integral homological Cartan–Leray spectral sequence, total degree three comes only from \(H_3(\mathbb Z/2;\mathbb Z)=\mathbb Z/2\), so \(H_3(Y;\mathbb Z)=\mathbb Z/2\). The remaining integral groups follow. The Bockstein of \(t\) is a class \(b\in H^2(Y;\mathbb Z)\) whose mod-two reduction is \(t^2\); hence \(b^2\) reduces to \(t^4\ne0\), proving the stated integral product. No degree-seven generator has a nonzero product with a positive-degree element, by the already established degree-vanishing.

## Verification
Run `python verify.py` with Python 3.8 or later. It constructs every simplex independently from the Hamming metric, verifies the complete face vector \((32,400,2560,9280,19872,25312,18560,7080,1120,80)\), verifies the ten facet cross-polytope structures, finds ten globally maximal seven-simplices giving a unimodular evaluation matrix against the facet cycles, checks the antipodal pairing of facets and the absence of invariant simplices, and recovers the Lefschetz sign on fourth homology. The group-cohomology differential and universal-coefficient arguments are mathematical deductions given in the proof, not claims of numeric exhaustive enumeration of all quotient cochains.

## Relationship to prior work
Feng determines the nonequivariant integral sphere-wedge type at radius three. Adams and Virk establish independent cross-polytopal classes and furnish the dual-maximal-simplex method used in degree seven. Galetto, Montaño and Wellner determine the hyperoctahedral representations over characteristic-zero fields, a stronger published result concerning rational action on the **cover**; the rational representation and the rank-five rational orbit homology are not claimed as new here. Those results do not state the integral homology or the projective-type cup-product structure of this specific *geometric orbit space*. The finding here is the integral quotient classification and its multiplicative mod-two consequence, based on an explicit free-action spectral-sequence analysis.

## Limitations
No integral homotopy type, ring with twisted local coefficients, or integral homology for the quotient by the full hyperoctahedral group is asserted. The mod-two Cartan–Leray argument determines the ring and groups, not the attaching maps of a CW model. The existing characteristic-zero equivariant decomposition must not be represented as new. The source comparison does not eliminate all possible unindexed or unpublished equivalent calculations.

## References
- Z. Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs*, arXiv:2305.07084, initially public 2023-05-11; Theorem 24.
- H. Adams and Ž. Virk, *Lower Bounds on the Homology of Vietoris–Rips Complexes of Hypercube Graphs*, arXiv:2309.06222, initially public 2023-09-12; Theorem 4.1, Lemma 4.5 and its integral dual-cocycle proof.
- F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784, initially public 2026-06-18; Theorem 6.2 and characteristic-zero representation coverage.
