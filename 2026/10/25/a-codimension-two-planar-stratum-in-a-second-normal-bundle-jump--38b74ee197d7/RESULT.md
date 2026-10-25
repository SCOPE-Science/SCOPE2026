# A codimension-two planar stratum in a second normal-bundle jump locus

## Finding

Let \(X=\operatorname{Bl}_{L}\mathbb P^3_{\mathbb C}\) for the line \(L=V(x_2,x_3)\). Write \(H\) for the pullback of a hyperplane and \(E\) for the exceptional divisor. In the smooth irreducible fixed-source parameter space \(U\) of unramified maps \(f:\mathbb P^1\to X\) with \((H\cdot f_*[\mathbb P^1],E\cdot f_*[\mathbb P^1])=(4,2)\), let \(P\) be the locus where the blowdown image lies in a plane.

**Theorem.** The locus \(P\) is a nonempty, irreducible, codimension-two subvariety of \(U\). For every \(f\in P\),
\[
N_f\cong\mathcal O_{\mathbb P^1}(4)\oplus\mathcal O_{\mathbb P^1}(8).
\]
In particular \(P\subset J_{\mathcal O(-7)}^2\), the locus where the relative cohomology matrix in [1] drops rank by at least two. This matrix has size \(16\times16\) and generic rank \(16\), so the determinantal expected codimension of \(J_{\mathcal O(-7)}^2\) is \(4\). Its actual codimension is at most \(2\); consequently the second jump locus cannot be pure of its determinantal expected codimension.

This is an inclusion of an irreducible codimension-two geometric subvariety, not an assertion that \(P\) is an irreducible component of the entire second jump locus.

## Assumptions and scope

Work over \(\mathbb C\). A map is *unramified* when its differential is injective on all geometric tangent fibers; then its normal sheaf is a rank-two vector bundle. The source \(\mathbb P^1\) is fixed (not quotiented by source automorphisms). The incidence-defined planar locus uses planes varying with the map. This statement concerns the particular curve class \((4,2)\), not arbitrary rational curves or positive characteristic.

Following [1, Section 6], a Cox representative for this family is
\[
(u_0,u_1,v_2,v_3,w),\quad
u_i\in H^0(\mathbb P^1,\mathcal O(4)),\quad
v_j,w\in H^0(\mathbb P^1,\mathcal O(2)),
\]
where the two \(v\)'s have no simultaneous zero, the triple \((u_0,u_1,w)\) has no simultaneous zero, and blowdown coordinates are \([u_0:u_1:wv_2:wv_3]\). The parameter space is the corresponding open subset of a Cox quotient; in this class its dimension is \(17\).

## Proof

**1. Planarity is an irreducible codimension-two condition.** Fix \((v_2,v_3,w)\) in the base-point-free open locus. The quadratics \(v_2,v_3\) are linearly independent, and \(w\neq0\). Let \(V=H^0(\mathbb P^1,\mathcal O(4))\), of dimension \(5\), and let \(W=w\langle v_2,v_3\rangle\subset V\), of dimension \(2\). A plane contains the blowdown image exactly when there are scalars, not all zero, with
\[
a u_0+b u_1+c wv_2+d wv_3=0.
\]
Since \(v_2,v_3\) are linearly independent, \((a,b)\neq(0,0)\). Equivalently, the two vectors \([u_0],[u_1]\in V/W\cong\mathbb C^3\) have rank at most \(1\). The generic \(3\times2\) rank-at-most-one determinantal variety is irreducible of codimension \((3-1)(2-1)=2\). These fiberwise determinantal loci form a locally trivial family over the irreducible open parameter space of \((v_2,v_3,w)\), with affine factors for the components of \(u_0,u_1\) in \(W\). Their quotient by the free Cox rescalings remains irreducible and of codimension \(2\). Intersecting with the open unramified locus preserves this conclusion provided the intersection is nonempty, as proved in step 3. In particular \(\dim P=15\).

Any containing plane is transverse to \(L\): a plane containing \(L\) has equation \(cx_2+dx_3=0\), contradicting independence of \(v_2,v_3\). Thus its inverse image in \(X\) is the smooth proper transform \(S\cong\operatorname{Bl}_{p}\mathbb P^2\), where \(p\) is the single intersection with \(L\).

**2. Normal splitting is forced by the surface.** This surface is a Cartier divisor linearly equivalent to \(H\). The map \(f\) factors through \(S\); since \(f\) is unramified in \(X\), it is unramified in \(S\). The surface normal sequence is
\[
0\longrightarrow N_{f/S}\longrightarrow N_{f/X}\longrightarrow f^*N_{S/X}\longrightarrow0.
\]
The last term is \(\mathcal O(4)\). Since \(K_S=-3H|_S+E|_S\) and \(H\cdot f_*[\mathbb P^1]=4\), \(E\cdot f_*[\mathbb P^1]=2\), the tangent sequence of the immersed map to \(S\) gives
\[
\deg N_{f/S}=(-K_S)\cdot f_*[\mathbb P^1]-2=(3\cdot4-2)-2=8.
\]
Thus \(N_{f/S}=\mathcal O(8)\). Because \(\operatorname{Ext}^1(\mathcal O(4),\mathcal O(8))=H^1(\mathbb P^1,\mathcal O(4))=0\), the exact sequence splits, as claimed.

**3. Explicit nonempty unramified witness.** In homogeneous coordinates \([s:t]\) take
\[
\begin{aligned}
u_0&=s^2(s^2+t^2),\\
u_1&=s^3t+st^3+t^4,\\v_2&=s^2,\\v_3&=t^2,\\w&=s^2+t^2.
\end{aligned}
\]
The Cox base-point conditions hold: \(v_2,v_3\) have no common zero, and at a zero of \(w\), \(u_1=t^4\neq0\). The blowdown image satisfies \(x_0=x_2\), so is planar.

For an exact immersion check, form the \(5\times3\) matrix \(\Psi=(-A_E,D_s,D_t)\) from [1, Corollary 6.3] in row order \((u_0,u_1,v_2,v_3,w)\). Index rows from \(0\). Two of its \(3\times3\) minors are
\[
\begin{aligned}
D_{124}&=4s\big(s^5+2s^3t^2+4s^2t^3+st^4+2t^5\big),\\
D_{134}&=-4t^2\big(s^4+2s^2t^2-2st^3+t^4\big).
\end{aligned}
\]
The displayed degree-five and degree-four factors are coprime: their dehomogenizations at \(t=1\) have resultant \(1984\neq0\). At \(t=0\) the first minor is nonzero. Consequently the two minors have no common projective zero, and \(\Psi\) has rank three at every point. The cited resolution criterion therefore proves that the map is unramified.

**4. Depth and expected codimension.** The previous splitting gives \(h^1(N_f(-7))=h^1(\mathcal O(-3)\oplus\mathcal O(1))=2\). Iwasaki's relative cohomology resolution identifies this dimension with the cokernel dimension of \(\Theta^1_{\mathcal O(-7)}\). Its source and target both have rank \(16\); a general map has bundle \(\mathcal O(6)^2\) by [1, Proposition 6.7], hence the generic matrix rank is \(16\). Therefore every map in \(P\) belongs to the rank-at-most-\(14\) locus \(J_{\mathcal O(-7)}^2\). The rank-\(14\) degeneracy condition on an unrestricted \(16\times16\) matrix has expected codimension \((16-14)^2=4\), as in [1, Proposition 5.6]; the included \(15\)-dimensional \(P\) has codimension \(2\). This proves the theorem.

## Verification

The accompanying standard-library-only Python program `verify.py` reconstructs both displayed homogeneous minors and confirms their coprimality over \(\mathbb Q\). It also independently constructs the \(16\times16\) relative cohomology matrix from [1, Appendix A, equation (A.1)] and checks its exact rank is \(14\) at the displayed witness. Execution returns `VERIFY_OK`. These computations certify the explicit witness, while the arbitrary-map splitting and codimension assertions follow from the preceding algebraic arguments.

## Relationship to prior work

Iwasaki [1] supplies the Cox parameter space, the relative normal bundle resolution, the rank-locus framework, the general splitting \(\mathcal O(6)^2\), and the codimension-one first jump. The new statement identifies a geometrically defined irreducible codimension-two locus entirely inside the deeper, rank-drop-two locus, determines its normal splitting, and shows that the deeper determinantal locus has excess dimension compared with its expected codimension. Cela–Lian [2] determine normal splitting for general curves with secancy conditions, not the second jumping stratum of these special planar maps. Eisenbud–Van de Ven's classical work on smooth rational space curves is background, but does not directly classify this line-blowup stratum. The distinction is between what these cited theorems imply and the additional geometric rank-degeneration construction here.

## Limitations

The theorem does not determine all irreducible components, cycle multiplicities, or scheme structure of \(J_{\mathcal O(-7)}^2\), and does not assert its exact codimension is \(2\): it proves an upper bound via a distinguished codimension-two subvariety. The generic-freeness and immersion assertions use characteristic zero; positive characteristic is not claimed. The originality comparison does not exclude every unindexed or implicit previous derivation. No independent mathematical audit has been performed.

## References

[1] Hikari Iwasaki, *Normal Bundle Splitting Strata of Rational Curves in Toric Varieties*, arXiv:2609.39309v1 (public September 30, 2026), Sections 5–6 and Appendix A. https://arxiv.org/html/2609.39309v1

[2] Alessio Cela and Carl Lian, *Interpolation for rational curves with secants*, arXiv:2607.01432v1 (public July 1, 2026), Sections 1, 3, and 5. https://arxiv.org/html/2607.01432v1

[3] David Eisenbud and Antonius Van de Ven, *On the normal bundles of smooth rational space curves*, Math. Ann. 256 (1981), 453–463, as referenced in [1] and [2].
