# Five quotient singularities and rational cohomology of the Klein cubic's order-55 quotient

## Finding
Let \(X\subset\mathbb P^4_{\mathbb C}\) be the Klein cubic with equation
\[
F=\sum_{i\in\mathbb Z/5}x_i^2x_{i+1}=0.
\]
Write \(G=\langle g,\sigma\rangle\), with \(g\) diagonal of weights \((1,9,4,3,5)\) modulo \(11\) and \(\sigma(e_i)=e_{i+1}\). These transformations preserve \(X\), and \(G\cong C_{11}\rtimes C_5\) has order \(55\). For the projective quotient \(Y=X/G\):

1. Its singular locus consists of exactly five points with basket \(\frac1{11}(2,3,4)+4\,\frac15(1,2,3)\). The order-eleven point has local minimal log discrepancy \(9/11\); the order-five points each have local minimal log discrepancy \(6/5\).
2. It is a normal, \(\mathbb Q\)-factorial, klt (but noncanonical) \(\mathbb Q\)-Fano threefold with Picard rank one, global Gorenstein index \(55\), and anticanonical volume \(24/55\).
3. The topological fundamental group of \(Y(\mathbb C)\) is trivial and, as a graded rational ring,
\[
H^*(Y(\mathbb C);\mathbb Q)\cong \mathbb Q[h]/(h^4),\qquad\deg h=2.
\]
This gives a singular noncanonical Fano quotient with the rational cohomology ring of projective three-space.

## Assumptions and scope
All constructions are over \(\mathbb C\). Indices of coordinates are taken modulo five. The root \(\zeta\) is any primitive eleventh root of unity; \(\lambda\) below is any primitive fifth root. The notation \(\frac1m(w_1,w_2,w_3)\) means the analytic germ \(\mathbb A^3/\mu_m\) with the displayed diagonal weights. A change of generator multiplies all three weights by one unit modulo \(m\) and does not change the quotient germ. Minimal log discrepancies are those of the underlying variety with zero boundary, at the indicated isolated points. The quotient is the coarse projective quotient, not its stack or a resolution.

## Proof
**1. Smoothness and the action.** The derivative equations of \(F\) at a hypothetical singular point are \(2x_i x_{i+1}+x_{i-1}^{2}=0\). If one coordinate vanishes, they force all coordinates to vanish, impossible projectively. If none vanish, multiplying all five equations gives \(1=(-2)^5\), likewise impossible; hence \(X\) is smooth. With \(a=(1,9,4,3,5)\), the five residues \(2a_i+a_{i+1}\) are zero modulo eleven; thus \(g\) preserves \(F\). Cyclic permutation \(\sigma\) preserves \(F\), and \(a_{i-1}=5a_i\pmod{11}\) yields \(\sigma g\sigma^{-1}=g^5\). The resulting semidirect product has order \(55\). Every nonidentity power of \(g\) has the same five projective fixed points, the coordinate vertices \(e_i\), all of which belong to \(X\).

**2. Order-eleven points.** At \(e_i\), the partial derivative of \(F\) in coordinate \(x_{i+1}\) is nonzero, so the local tangent coordinates correspond to the other three off-vertex coordinates. Their three \(g\)-weights are \(a_j-a_i\pmod{11}\), excluding \(j=i\) and \(j=i+1\). For \(i=0\) these are \(3,2,4\); for each remaining \(i\) they differ by multiplication by an invertible residue from \((2,3,4)\). The cyclic permutation acts transitively on the five vertices, so they constitute one \(G\)-orbit with stabilizer \(C_{11}\). The image is exactly a \(\frac1{11}(2,3,4)\) singularity.

**3. Order-five points.** The cyclic permutation has five projective eigenlines spanned by
\[
v_k=\sum_{i=0}^4 \lambda^{-ki}e_i\quad(0\le k\le4),\qquad \sigma(v_k)=\lambda^k v_k.
\]
Direct substitution gives \(F(v_0)=5\) and \(F(v_k)=0\) for \(k=1,2,3,4\). For each such \(k\), the homogeneous derivative of the invariant cubic pairs the line of weight \(j=-2k\) with the square of the line of weight \(k\); it is nonzero because \(X\) is smooth. Thus, after dividing by the projective weight \(k\), the three tangent weights are exactly the nonzero residues \(\{1,2,3,4\}\setminus\{2k\}\) modulo five. As \(k\) runs from one to four, these four unordered triples are the four unit multiples of \((1,2,3)\), so all four quotient germs are \(\frac15(1,2,3)\). The group \(G\) has eleven distinct order-five subgroups, each fixing four points on \(X\). Points fixed by distinct such subgroups cannot coincide, because that would force fixation under the normal \(C_{11}\), yet no vertex is fixed by any order-five subgroup. Therefore there are \(44\) such points, split into four \(G\)-orbits of length eleven. Together with the coordinate vertices, these exhaust all points with nontrivial stabilizer, proving the basket and ruling out any other singular locus.

**4. Discrepancies and Fano data.** At a diagonal isolated cyclic quotient \(\frac1m(b_1,b_2,b_3)\), the toric lattice-point discrepancy formula gives the local minimal log discrepancy as the minimum, over \(1\le j<m\), of \(\sum_{s=1}^3 (jb_s\bmod m)/m\). For \(\frac1{11}(2,3,4)\), these ten integer numerators are \(9,18,16,14,23,10,19,17,15,24\), yielding \(9/11\). For \(\frac15(1,2,3)\), the four numerators are \(6,7,8,9\), yielding \(6/5\). The local canonical indices are respectively \(11\) and \(5\), since the sums of the weights are units modulo the group orders. As the action has no codimension-one fixed locus, \(K_X=\pi^*K_Y\). The cubic adjunction formula gives \(-K_X=2H\) and \(H^3=3\), so \((-K_Y)^3=24/55\). This finite quotient is normal and \(\mathbb Q\)-factorial; the pullback of \(-K_Y\) is ample, and \(\rho(Y)=1\) because \(\rho(X)=1\). The least common multiple of the local canonical indices is \(55\).

**5. Topology.** Lefschetz hyperplane theory gives \(\pi_1(X)=1\) and rational Betti numbers \((b_0,b_1,b_2,b_3,b_4,b_5,b_6)=(1,0,1,10,1,0,1)\). The holomorphic automorphism \(g\) has exactly five isolated fixed points and no eigenvalue one on their tangent spaces, so each has topological Lefschetz index \(+1\). The Lefschetz trace identity gives \(5=4-\operatorname{Tr}(g\mid H^3(X;\mathbb Q))\), hence the trace is \(-1\). A ten-dimensional rational \(C_{11}\)-module is a direct sum of copies of the trivial module and the degree-ten cyclotomic module. The dimension and trace force precisely one cyclotomic copy and no invariants. Thus \(H^3(X;\mathbb Q)^G=0\); the one-dimensional even groups are fixed by \(G\). Cohomology of a finite quotient with rational coefficients equals the invariant cohomology of the original space, giving the asserted Betti numbers. The descended ample class has nonzero third power, so the full graded cohomology ring is \(\mathbb Q[h]/(h^4)\). Finally, the quotient fundamental-group theorem for finite actions on simply connected spaces identifies \(\pi_1(Y)\) with \(G\) modulo the normal subgroup generated by point stabilizers. The \(C_{11}\) and \(C_5\) subgroups have fixed points and generate \(G\), hence \(\pi_1(Y)=1\).

## Verification
The supplied `verify.py` uses integer modular arithmetic to check preservation of the cubic, the semidirect relation, all five order-eleven tangent triples, the four order-five tangent triples, and both complete age spectra. It returns `VERIFY_OK`. The all-points argument, geometric quotient analysis, and topological conclusions are proved above and are not inferred from finite tests.

## Relationship to prior work
Ballard–Duncan–Zhang (2026) prove equivariant unirationality for the Klein cubic under \(\mathrm{PSL}_2(\mathbb F_{11})\), explicitly singling out its order-55 subgroup in their group-action classification. Cheltsov–Tschinkel–Zhang (2025) list that same subgroup as an unresolved equivariant-unirationality case. Roulleau (2010) studies the order-eleven automorphism and intermediate Jacobian of the Klein cubic. Those works provide the motivating action, older automorphism data, and equivariant birational context; the inspected relevant sections do not provide the complete order-55 coarse-quotient singularity basket together with discrepancy, volume, and rational cohomology. Standard cyclic-quotient and topological tools are used in a new concrete combined classification; a possible implicit consequence of broader equivariant-quotient literature remains a novelty risk.

## Limitations
The result concerns the specified complex order-55 subgroup and its coarse quotient, not the quotient by all of \(\mathrm{PSL}_2(\mathbb F_{11})\). Rational cohomology is computed; integral torsion groups are not. No assertion of rationality of \(Y\), its crepant resolutions, its intersection cohomology, or its algebraic \(\mathbb A^1\)-homotopy type is made. No independent mathematical audit has been performed.

## References
1. M. Ballard, A. Duncan, Z. Zhang, *Equivariant Unirationality of Cubic Threefolds*, arXiv:2610.09962v1 (October 7, 2026), Sections 1 and 5.
2. I. Cheltsov, Yu. Tschinkel, Z. Zhang, *Equivariant unirationality of Fano threefolds*, arXiv:2502.19598v1 (February 26, 2025), Section 5.
3. X. Roulleau, *The Fano surface of the Klein cubic threefold*, arXiv:1001.4853v1 (January 27, 2010), Sections 2 and 3.
4. The standard Lefschetz hyperplane and fixed-point formulas, the finite-orbit-space fundamental-group theorem, and the toric cyclic-quotient minimal-log-discrepancy formula are invoked in their usual characteristic-zero complex settings.
