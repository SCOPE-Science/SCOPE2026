# Exact level-\(p\) stabilizer hierarchy for canonical elementary type-I and type-II TQD states on the tetrahedral sphere
## Finding
Let \(p\) be an odd prime and let \(G=\mathbb Z_p^n\). Consider the tetrahedral triangulation of the two-sphere with ordered vertices \(0<1<2<3\), and the canonical twisted-quantum-double (TQD) ground state for a standard elementary nontrivial type-I cocycle or a standard elementary nontrivial type-II cocycle in the normal form of Fechisin et al. The same conclusion holds for any nonzero power of one such elementary cocycle factor.

Writing \(d=|G|\), the least stabilizer hierarchy index for this canonical state is
\[
\min\{k:\text{the canonical state is the unique codeword of an }X\mathcal C_d^{(k)}\text{ stabilizer code}\}=p.
\]
Thus the source's level-\(p\) construction is minimal for these canonical tetrahedral states.

## Assumptions and scope
The claim is state-specific and gauge-specific: it uses the standard elementary type-I or type-II cocycle representatives displayed in Eq. (67) of Fechisin et al., on the tetrahedral sphere with the indicated branching. It does not assert the full phase-level conjecture of that paper, does not treat arbitrary triangulations, and does not treat products in which distinct elementary cocycle factors could cancel after restriction.

A flat edge configuration is written using vertex potentials \(q_0,q_1,q_2,q_3\in G\), with \(q_0=0\), as
\[
e_{ij}=q_j-q_i.
\]
This parametrizes all flat configurations: the three faces containing vertex \(0\) determine every remaining edge, and the fourth face relation then follows automatically.

For a scalar coordinate, define the carry function on representatives \(0,1,\ldots,p-1\) by
\[
C(y,z)=\frac{y+z-[y+z]_p}{p}\in\{0,1\}.
\]
Fechisin et al. identify this function with reduced polynomial degree exactly \(p\), and therefore with a precision-one diagonal phase appearing first at hierarchy level \(p\).

## Proof
Fix the star translation at the minimal vertex \(0\), using a group element \(g\) whose active coordinate is nonzero. The TQD star rule is a product of one cocycle contribution for each incident oriented face. Because vertex \(0\) is first in every incident face, the three contributions have arguments of the form \((g,e_{0i},e_{ij})\), possibly inverted according to orientation.

For an elementary type-I factor, vary only its active group coordinate. For an elementary type-II factor, choose \(g\) nonzero in the first cocycle coordinate and vary only the coordinate on which the carry is taken. In both cases the exponent of the amplitude ratio on flat support has the form
\[
F(q_1,q_2,q_3)=
\sigma_{12}C(q_1,q_2-q_1)
+\sigma_{13}C(q_1,q_3-q_1)
+\sigma_{23}C(q_2,q_3-q_2),
\]
multiplied by a nonzero scalar in \(\mathbb F_p\), where each \(\sigma_{ij}\in\{1,-1\}\) records an orientation choice. All differences are reduced modulo \(p\) before the carry is evaluated.

Now restrict the flat-support affine subspace to \(q_1=0\). Since \(C(0,z)=0\), the first two terms vanish and
\[
F(0,q_2,q_3)=\sigma_{23}C(q_2,q_3-q_2)
\]
up to the same nonzero scalar. The map
\[
(q_2,q_3)\longmapsto(q_2,q_3-q_2)
\]
is invertible affine-linear over \(\mathbb F_p^2\). By the affine-invariance theorem for exact diagonal hierarchy level in Fechisin et al., this restricted phase has the same exact level as \(C(y,z)\), namely \(p\). Multiplication by a nonzero scalar and inversion do not lower the reduced degree. Hence the vertex-\(0\) support-displacement amplitude ratio of the canonical state has exact level \(p\).

It remains to rule out a different lower-level stabilizer presentation of the same state. The stabilizer-state classification of Fechisin et al. expresses an \(X\mathcal C_d^{(k)}\) stabilizer state as a uniform affine-support state with a hierarchy-bounded phase, and its finite-difference formula implies that the amplitude ratio along every displacement contained in the support is a diagonal phase of level at most \(k\). The vertex-\(0\) flat translation is such a support displacement. Therefore a hypothetical representation with \(k<p\) would force its amplitude ratio to have level below \(p\), contradicting the preceding restriction argument.

Lemma V.3 of Fechisin et al. supplies an \(X\mathcal C_d^{(p)}\) construction for canonical TQD states whose twist contains a type-I or type-II elementary factor. Thus the lower and upper bounds coincide, and the minimum is \(p\).

## Verification
The analytic proof is uniform in every odd prime \(p\). The included `artifacts/verify.py` is only a corroborating finite check. It enumerates all eight choices of orientation signs for \(p\in\{3,5,7,11\}\), verifies the \(q_1=0\) reduction to a signed carry function, interpolates the unique reduced polynomial of that carry slice, and checks that its algebraic degree is exactly \(p\). The script returns `VERIFY_OK`.

The finite computation is not used to infer the all-prime statement. The all-prime lower bound instead uses the source's exact carry-degree theorem, its affine invariance theorem, and its stabilizer-state finite-difference classification.

## Relationship to prior work
Fechisin et al. construct the canonical TQD wavefunction as an \(X\mathcal C_d\) stabilizer state and prove that type-I and type-II elementary cocycles require level \(p\) for their natural star operators. They explicitly observe that this operator-level fact does not by itself exclude a different lower-level stabilizer code for the same canonical state. The result above closes that state-specific gap on the tetrahedral sphere by showing that the level-\(p\) carry survives after imposing flatness and then invoking the source's state classification.

Hu, Wan, and Wu provide the TQD Hamiltonian and cocycle construction but do not address Clifford-hierarchy minimality. Cui, Gottesman, and Krishna characterize diagonal gates in the Clifford hierarchy and supply the degree/precision framework used by later work, but do not analyze TQD flat-support states.

## Limitations
No claim is made for arbitrary sphere triangulations, for noncanonical ground-state representatives, for mixed products of elementary type-I/type-II factors, or for type-III-only twists. In particular, this finding does not prove the broad phase-level conjecture in Fechisin et al.; it establishes one natural canonical-state case on the minimal triangulated sphere.

The lower bound also relies on the standard cocycle gauge used in the anchor source. A different cocycle representative can alter the visible phase polynomial while leaving the topological phase unchanged, so extending the argument to a gauge-invariant phase statement requires additional work.

## References
1. C. Fechisin, K. Cooney, M. Raja, V. V. Albert, D. J. Williamson, K. Kawagoe, and S. Musser, *Clifford-hierarchy stabilizer formalism with applications to twisted quantum doubles*, arXiv:2610.00464v1 (2026). Relevant items: Theorem IV.8, Definition V.2, Lemma V.3, Eq. (67), and Theorem A.11.
2. Y. Hu, Y. Wan, and Y.-S. Wu, *Twisted quantum double model of topological phases in two dimensions*, arXiv:1211.3695v2.
3. S. X. Cui, D. Gottesman, and A. Krishna, *Diagonal gates in the Clifford hierarchy*, arXiv:1608.06596v1.
