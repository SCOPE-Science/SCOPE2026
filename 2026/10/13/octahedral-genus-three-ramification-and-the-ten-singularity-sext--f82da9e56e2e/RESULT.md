# Octahedral genus-three ramification and the ten-singularity sextic of a symmetric K3 quotient

## Finding
For the symmetric K3 surface \(S\subset(\mathbf P^1)^4\) introduced by Nukui, the quotient by permutations of its four factors is a finite flat degree-\(24\) map to \(\mathbf P^2\). Its reduced branch curve is the rational sextic
\[
B:\quad -256a^6-192a^4bc-27a^2b^4+6a^2b^2c^2-27a^2c^4-4b^3c^3=0.
\]
It has exactly six ordinary cusps and four ordinary nodes. The reduced ramification divisor consists of six smooth, connected, genus-three curves, each explicitly isomorphic to
\[
H:\quad y^2=t^8+14t^4+1.
\]
The curves are the six transposition fixed divisors. Thus the special K3 quotient realizes the classical octahedral hyperelliptic genus-three curve as each ramification component. The generic six-cusp/four-node count is not asserted to be new.

## Assumptions and scope
Work over \(\mathbf C\). Write binary quartic coefficients \([\sigma_0:\sigma_1:\sigma_2:\sigma_3:\sigma_4]\) for the four unordered points on \(\mathbf P^1\). In affine root coordinates \(t_1,t_2,t_3,t_4\), the surface is the smooth K3 model
\[
\sigma_4+\sigma_0=0,\qquad \sigma_2=0,
\]
where these are the homogeneous multidegree-\((1,1,1,1)\) sections whose affine restrictions are \(t_1t_2t_3t_4+1\) and \(\sum_{i<j}t_it_j\), respectively. Its smoothness and K3 property are established in Nukui's initiating paper. The group \(\mathfrak S_4\) permutes the factors, distinct from the commuting diagonal octahedral group.

## Proof
**The quotient and branch equation.** The symmetric fourth power of \(\mathbf P^1\) is \(\mathbf P^4\), via the coefficients of the binary quartic with those four roots. The two defining invariant linear equations restrict this quotient to a plane, coordinatized by the quartic
\[
F(T,U)=aT^4+bT^3U+cTU^3-aU^4.
\]
Every unordered four-root divisor satisfying the two conditions has its \(24\) ordered realizations generically, so \(S/\mathfrak S_4\cong\mathbf P^2\) and the quotient is finite of degree \(24\). Since \(S\) is smooth and the target is regular, finite equidimensional Cohen–Macaulay flatness gives flatness. The branch support is exactly the quartic multiple-root discriminant; direct resultant expansion gives the sextic equation displayed above.

**Normalization and singularities.** Imposing a repeated root \(t\) means \(F(t,1)=\partial_TF(t,1)=0\), which gives the rational normalization parametrization
\[
\nu([T:U])=[-2T^3U^3:3T^4U^2+U^6:-T^6-3T^2U^4].
\]
Its coordinates have no common zero. The general binary quartic in the discriminant has a unique repeated root, so \(\nu\) is generically one-to-one. It follows that the sextic is irreducible and rational. The derivative of the affine parametrization has projective critical parameters precisely at \(t=0\) and \(t^4=1\), with one further critical parameter at infinity, giving six distinct singular-image candidates. The derivative vanishes at these six parameters, so every such image has singular-branch delta invariant at least one. A second source of singularities is two distinct repeated roots: they occur precisely when
\[
F(T,1)=(T^2-pT+q)^2,\qquad q^2=-1,\quad p^2=-2q.
\]
The four resulting quartics have two distinct double roots and represent four distinct ordinary double-point candidates of delta invariant at least one, disjoint from the six triple-root images. A rational plane sextic has arithmetic genus \(10\). The six singular unibranch points and four distinct two-branch points contribute at least \(6+4=10\) to its delta sum. Equality exhausts the genus formula, proving that they are exactly six ordinary \(A_2\) cusps and four ordinary \(A_1\) nodes, with no further singularities.

**Ramification and the octahedral curve.** For a transposition \((ij)\), its divisorial fixed locus is the diagonal \(R_{ij}=S\cap\{t_i=t_j\}\). On \(R_{12}\), write \(t_1=t_2=t\) and let the remaining ordered coordinates be \(u,v\). The two surface equations reduce, on a dense affine open, to
\[
uv=-t^{-2},\qquad u+v=\frac{1-t^4}{2t^3}.
\]
Thus
\[
(2t^3(u-v))^2=t^8+14t^4+1.
\]
The right side has eight distinct complex roots. The resulting quadratic extension of \(\mathbf C(t)\) is connected and gives a genus-three hyperelliptic double cover. The diagonal fixed locus is smooth because a fixed locus of a finite-order automorphism on a smooth characteristic-zero variety is smooth; the displayed degree-two map and its connected function field identify its entire compactification with this genus-three curve (there are no extraneous components: the diagonal incidence projects finitely onto the repeated-root coordinate, and its general fiber has two points). Each of the other five transpositions is conjugate and gives the same curve.

Every even permutation belongs to the symplectic subgroup of this \(\mathfrak S_4\) action on the K3 surface and therefore has no fixed divisor unless it is the identity. The square of any four-cycle is an even double transposition, so a four-cycle cannot have a fixed divisor either. The remaining odd nonidentity elements are transpositions. Hence the reduced ramification divisor is precisely \(\sum_{i<j}R_{ij}\), with generic ramification index two. As an independent genus consistency check, writing \(H_i\) for pullbacks of hyperplane classes from the factors, the diagonal class is \(H_1+H_2\) and the two defining divisors have class \(\sum_i H_i\). Thus \(R_{12}^2=4\); adjunction on the K3 gives \(g(R_{12})=3\). The commuting diagonal octahedral group acts on the repeated coordinate \(t\) and preserves its eight branch points, giving geometric meaning to the octahedral model.

## Verification
The standalone exact symbolic program `check.py` checks the discriminant, parametrized repeated-root factorization, discriminant of the residual quadratic, squarefreeness of its degree-eight polynomial, the four distinct double-double-root quartics, and the six cusp-parameter images. Its output is `OCTAHEDRAL_K3_RAMIFICATION_EXACT_OK`. The infinite statements about quotient, fixed loci, and genus are justified above rather than inferred from finite testing.

## Relationship to prior work
Nukui (2026, arXiv:2602.11742v1) establishes the smooth K3 model and commuting \(\mathfrak S_4\) actions, but does not identify the quotient discriminant's singularities or its ramification curves with the special octahedral genus-three hyperelliptic curve. Tokunaga (2002), Example 6.1, constructs a generic plane section of the quartic discriminant with four nodes and six cusps: the generic singularity count and general \(\mathfrak S_4\)-cover construction are already known, and are not claimed as novel. The polynomial \(t^8+14t^4+1\) itself is a classical octahedrally symmetric curve; the contribution is its occurrence as the complete six-component ramification divisor in the explicitly specified K3 quotient, together with the special explicit plane branch model. No stronger equivalent description of this specific realization was found in the checked sources.

## Limitations
The theorem concerns this particular smooth complex K3 and the permutation subgroup, not all abstract automorphisms or all diagonal octahedral quotients. It determines reduced ramification and reduced branch support, not embedded singular structures at special branch points or the full resolution of the quotient as a stack. The specialization's cusp/node count alone is subsumed by generic discriminant-section literature. A further earlier equivalent special-K3 presentation cannot be excluded without additional bibliographic work. There has been no independent audit.

## References
- H. Nukui, *On the K3 surface with S4 × S4 action*, arXiv:2602.11742v1 (first public February 12, 2026), https://arxiv.org/abs/2602.11742 .
- H. Tokunaga, *Galois covers for S4 and A4 and their applications*, Osaka Journal of Mathematics **39** (2002), 621–645, Example 6.1, https://projecteuclid.org/journals/osaka-journal-of-mathematics/volume-39/issue-3/Galois-covers-for-mathfrakS_4-and-mathfrakA_4-and-their/ojm/1150996244.full .
- Classical octahedral hyperelliptic genus-three curves: the polynomial model is included for geometric identification, not asserted as a previously unknown abstract curve.
