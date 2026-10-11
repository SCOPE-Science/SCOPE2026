# Dihedral rational homology of bidirectional-polygon multipath complexes

## Finding
For an integer \(m\ge3\), let \(B_m\) be the directed graph on \(\mathbb Z/m\mathbb Z\), with two opposing arrows between each adjacent pair. Let \(X_m\) be its multipath complex: a face is a subset of arrows whose directed graph is a disjoint union of directed paths and isolated vertices. The natural dihedral action on vertices induces an action on \(X_m\). Set \(\rho(v)=v+1\) and \(\sigma(v)=-v\), giving \(D_m=\langle\rho,\sigma\mid\rho^m=\sigma^2=1,\sigma\rho\sigma=\rho^{-1}\rangle\).

Define the lower homological degree by
\[
j(m)=\begin{cases}
(m-1)/2,&m\equiv1\pmod4,\\
(m-2)/2,&m\equiv2\pmod4,\\
(m-3)/2,&m\equiv3\pmod4,\\
m/2-1,&m\equiv0\pmod4.
\end{cases}
\]
The reduced rational homology of \(X_m\) is zero outside degrees \(j(m)\) and \(m-2\). The complete representations in the nonzero degrees are as follows.

**Top degree.** On \(\widetilde H_{m-2}(X_m;\mathbb Q)\cong\mathbb Q^2\), there is a basis with
\[
\rho\longmapsto(-1)^{m-1}I_2,\qquad
\sigma\longmapsto\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

**Lower degree.** On \(\widetilde H_{j(m)}(X_m;\mathbb Q)\), the matrices may be chosen as follows:

* If \(m\) is odd, \(\rho\mapsto 1\) and \(\sigma\mapsto(-1)^{\lfloor(m-5)/4\rfloor}\).
* If \(m\equiv2\pmod4\), \(\rho\mapsto1\) and \(\sigma\mapsto(-1)^{(m-6)/4}\).
* If \(m\equiv0\pmod4\), the rank is three and
  \[
  \rho\longmapsto(-1)\oplus\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
  \sigma\longmapsto(-1)^{m/4-1}\oplus\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
  \]

In particular, the lower-degree rotation action is trivial unless the polygon has a multiple of four vertices. In the latter case it contains an order-four two-dimensional summand together with a rotation-sign line.

## Assumptions and scope
All homology is reduced singular/simplicial homology over \(\mathbb Q\), for every existing bidirected cycle of length \(m\ge3\); its dihedral symmetry acts by permutation of directed arrows. Orient simplices using any fixed total ordering of arrows. The original integral homology ranks and their degree concentration follow from Caputi–Collari–Smith, Theorem 2.10, after setting their parameter \(n=m-1\). Only the rational representation structure is determined here. For \(m=3\), the lower degree is zero and the reduced degree-zero homology is included.

## Proof
**1. Reduced Lefschetz formula.** For a dihedral automorphism \(g\), the reduced Lefschetz number is
\[
\widetilde\Lambda(g)=\sum_{q\ge0}(-1)^q\operatorname{tr}\bigl(g\mid\widetilde H_q(X_m;\mathbb Q)\bigr)
=-\!\sum_{S}(-1)^{o_g(S)},
\]
where the second sum runs over all \(g\)-invariant multipath faces \(S\), including the empty face, and \(o_g(S)\) is the number of \(g\)-orbits of arrows contained in \(S\). Indeed, an orbit of length \(r\) contributes \((-1)^r\) from the reduced Euler sign and \((-1)^{r-1}\) from the permutation of simplex vertices, giving the factor \(-1\) per orbit. The minus sign outside the sum is the reduced augmentation convention.

**2. Rotations.** For \(g=\rho^a\), put \(d=\gcd(m,a)\), with \(\gcd(m,0)=m\). If \(d\ge3\), invariant arrow-orbit selections correspond bijectively to multipath faces of the bidirected \(d\)-gon. The quotient local in/out-degree constraints are identical to the lifted ones, and the only directed cycles that require exclusion are reverse-arrow pairs or a complete consistently oriented polygon. Thus the reduced Lefschetz number is the reduced Euler characteristic of that smaller polygon. Theorem 2.10 of Caputi–Collari–Smith gives the latter as \(3\) if \(d\equiv2\pmod4\), and \(-1\) otherwise. For \(d=1\), only the empty invariant face remains; for \(d=2\), the empty face and four individual arrow orbits remain. Direct signed counting gives \(-1\) and \(3\), respectively, so for all rotations
\[
\boxed{\widetilde\Lambda(\rho^a)=\begin{cases}3,&\gcd(m,a)\equiv2\pmod4,\\-1,&\text{otherwise}.\end{cases}}
\]

**3. Reflections.** Put \(g=\rho^a\sigma\). An arrow on an undirected edge fixed setwise by \(g\) cannot occur in an invariant multipath, because its reverse would also be present. Likewise, each pair of edges adjacent to a fixed vertex is forbidden: either invariant orientation gives two inputs or two outputs at that vertex. All surviving arrow pairs fold to a bidirected linear path with
\[
t=\begin{cases}
(m-3)/2,&m\text{ odd},\\
m/2-2,&m\text{ even and }a\text{ even},\\
m/2-1,&m\text{ even and }a\text{ odd}
\end{cases}
\]
undirected edges. Selection of reflected arrow orbits is exactly selection of a multipath in this bidirected line. The signed orbit sum is therefore the reduced Euler characteristic of its multipath complex. Caputi–Collari–Smith, Proposition 2.2, identifies this complex with \(S^{\lfloor(t-1)/2\rfloor}\); for \(t=0\), use the augmented \(S^{-1}\) convention. Hence
\[
\boxed{\widetilde\Lambda(\rho^a\sigma)=(-1)^{\lfloor(t-1)/2\rfloor}.}
\]

**4. The top cycles.** Every \((m-2)\)-simplex is an oriented path of \(m-1\) arrows obtained by removing one arrow from a fully clockwise or fully counterclockwise directed polygon. The boundaries of the two forbidden complete oriented \((m-1)\)-simplices give cycles \(z_+\) and \(z_-\) with disjoint support. There are no simplices in the next dimension, so these are nonzero, independent top homology classes. By Theorem 2.10 there are precisely two top generators. Rotations permute the \(m\) arrows of either orientation with sign \((-1)^{m-\gcd(m,a)}\), whereas reflections exchange the two cycles. Rescaling one basis element if necessary gives
\[
\rho\mapsto(-1)^{m-1}I_2,\quad\sigma\mapsto\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
The top contribution to \(\widetilde\Lambda(\rho^a)\) is \(2(-1)^{\gcd(m,a)}\), while its contribution to a reflection Lefschetz number is zero.

**5. Recover the lower representation.** The cited integral homology theorem gives exactly one remaining nonzero reduced degree, \(j(m)\), with rank one if \(4\nmid m\) and rank three otherwise. Subtracting the top contribution from the formulas in Steps 2–3 and multiplying by \((-1)^{j(m)}\) gives the lower character. For rotations, this is
\[
\operatorname{tr}(\rho^a\mid\widetilde H_{j(m)})=
\begin{cases}
1,&4\nmid m,\\
3,&4\mid m\text{ and }4\mid a,\\
-1,&4\mid m\text{ and }4\nmid a.
\end{cases}
\]
For reflections it is respectively \((-1)^{\lfloor(m-5)/4\rfloor}\) when \(m\) is odd, \((-1)^{(m-6)/4}\) when \(m\equiv2\pmod4\), and \((-1)^{m/4-1+a}\) when \(4\mid m\). When \(4\mid m\), a rotation with eigenvalues \(-1,i,-i\), together with a reflection acting as \((-1)^{m/4-1}\) on the \(-1\) line and by coordinate reflection on the square plane, has precisely this character. All matrices displayed in the statement define representations of \(D_m\); finite-dimensional characteristic-zero representations are determined by their characters. This establishes every case.

## Verification
The accompanying standalone `verify_dihedral_multipath.py` uses independent integer algorithms: exhaustive arrow-subset enumeration and signed chain traces for polygon lengths \(3\) through \(8\), exact mod-two boundary matrix ranks at the same lengths, exhaustive orbit-subset checks for all dihedral elements through length \(13\), and algebraic character formula checks through length \(80\). A verified run printed `DIRECT_OK 1954 faces 66 signed simplicial traces`, `ORBIT_OK 176 dihedral elements checked`, `CHARACTER_OK m=3..80`, and `VERIFY_OK`. The all-length proof is Steps 1–5, not the finite checks.

## Relationship to prior work
Caputi, Collari and Smith (2026), Proposition 2.2 and Theorem 2.10, compute the homotopy of bidirectional paths and the integral homology ranks of bidirectional polygons. Their paper does not give the action of rotations or reflections on polygon homology. The earlier work of Vrećica and Živaljević develops connectivity of the larger cycle-free chessboard complexes of complete digraphs; a large complete-digraph complex is not an equivariant homology decomposition of its sparse polygon subcomplex. This finding derives a complete graded dihedral rational representation, not a new nonequivariant Betti-number formula.

## Limitations
The result relies on the cited known integral homology concentration, while independently proving the character formulas and top-cycle action. It determines rational representations, not integral \(\mathbb Z[D_m]\)-lattices, torsion actions for other graph families, or equivariant homotopy types. A nonindexed equivalent character computation could exist; this is not an independence or publication certification.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first public 2026-01-09), especially Proposition 2.2 and Theorem 2.10. https://arxiv.org/pdf/2601.05670
2. S. T. Vrećica and R. T. Živaljević, *Cycle-free chessboard complexes and symmetric homology of algebras*, arXiv:0710.5252 (2007), especially Sections 1–2. https://arxiv.org/pdf/0710.5252
