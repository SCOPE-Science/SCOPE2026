# Polar-reflection incidence at the Fermat member of the Dwork quartic pencil

## Finding

Let \(F_\lambda=x_0^4+x_1^4+x_2^4+x_3^4+\lambda x_0x_1x_2x_3\) over \(\mathbb C\), and let \(U=\{\lambda\in\mathbb A^1: \lambda^4\ne256\}\), so that the surfaces \(S_\lambda=V(F_\lambda)\subset\mathbb P^3\) are smooth. For \(p=[p_0:p_1:p_2:p_3]\in\mathbb P^3\), form the cubic first polar \(C_{p,\lambda}(x)=\sum_i p_i(\partial F_\lambda/\partial x_i)(x)\) and the linear third polar \(6L_{p,\lambda}(x)\), where \(L_{p,\lambda}(x)=\sum_i(4p_i^3+\lambda\prod_{j\ne i}p_j)x_i\). Let \(\mathscr I\subset\mathbb P^3\times U\) be the closed incidence scheme given by \(L_{p,\lambda}\mid C_{p,\lambda}\).

**Theorem.** There exists a Zariski-open neighborhood \(W\subset U\) of \(0\) such that, as a scheme over \(W\),
\[
\mathscr I|_W\ \cong\ \coprod_{24}W\ \amalg\ \coprod_{28}\operatorname{Spec}\mathbb C,
\]
where each isolated reduced point lies over \(\lambda=0\). The horizontal components are precisely the 24 constant sections whose centers have two nonzero coordinates in ratio a fourth root of unity. The 28 vertical points consist of the four coordinate points and the 24 two-supported points whose nonzero-coordinate ratio has fourth power \(-1\).

In particular, for every \(\lambda\in W\setminus\{0\}\), the smooth quartic \(S_\lambda\) has exactly 24 **outer quasi-Galois points**, namely \([e_i+\zeta e_j]\) for \(0\le i<j\le3\) and \(\zeta^4=1\). At \(\lambda=0\) it has exactly 28 outer quasi-Galois points: these 24 plus the four coordinate points. The latter 28-count is known from Miura--Taki; the new content is the deformation-incidence decomposition and resulting exact nearby count.

## Assumptions and scope

The field is \(\mathbb C\); all scheme structures and divisibility are over this field. The result applies on some nonempty Zariski-open neighborhood of the Fermat parameter \(0\), **not** to every smooth nonzero parameter. A quasi-Galois point here means a point outside the smooth quartic whose projection has a nontrivial fiber-preserving birational automorphism. For such exterior points, the Miura--Taki polar-divisibility criterion (their Proposition 3.5) is used. The scheme \(\mathscr I\) itself records divisibility also at points lying on the quartic: this distinction accounts for 24 of the vertical points.

## Proof

**1. Smoothness and the closed incidence.** The gradient of \(F_\lambda\) at \(p\) has components \(4p_i^3+\lambda\prod_{j\ne i}p_j\). If it vanishes, Euler's identity puts \(p\) on \(S_\lambda\). If one coordinate vanishes, the gradient equations force all four coordinates to vanish; otherwise multiply the four equations \(4p_i^4+\lambda P=0\), with \(P=\prod_i p_i\ne0\), obtaining \(\lambda^4=256\). Conversely the latter condition yields singular points by choosing compatible fourth roots. Hence \(S_\lambda\) is smooth exactly for \(\lambda^4\ne256\), and \(L_{p,\lambda}\) is never the zero form on \(\mathbb P^3\times U\). On each open chart where some coefficient of \(L\) is nonzero, substitution into \(C\) produces polynomial divisibility equations, making \(\mathscr I\) a closed subscheme. Its projection to \(U\) is proper.

**2. Its complete Fermat fiber.** At \(\lambda=0\), up to nonzero scalars,
\[
C_{p,0}=\sum_i p_ix_i^3,\qquad L_{p,0}=\sum_i p_i^3x_i.
\]
If \(p\) has at least three nonzero coordinates, the cubic \(C_{p,0}\) is an irreducible smooth diagonal cubic on its smallest coordinate projective subspace; it therefore has no linear factor. With one nonzero coordinate divisibility is automatic, giving four coordinate points. With two nonzero coordinates, after scaling and permuting let \(p=(1,r,0,0)\). Substitution \(x_0=-r^3x_1\) gives \(r-r^9=0\), i.e. \(r^8=1\) because \(r\ne0\). This gives eight points per unordered coordinate pair, or \(48\) such points, and \(52\) total.

**3. Scheme-theoretic transverse calculation.** In the chart \(p=(1,r,s,t)\), let \(R(r,s,t,\lambda;x_1,x_2,x_3)\) be the restriction of \(C_{p,\lambda}\) to the hyperplane \(L_{p,\lambda}=0\), multiplied by the cube of the coefficient of \(x_0\) in \(L_{p,\lambda}\). That coefficient equals \(4\) at each Fermat fiber point in this chart. Let \(a_1,a_2,a_3\) be the coefficients of \(x_1^3,x_2^3,x_3^3\) in \(R\). At \(\lambda=0\), they are
\[
(a_1,a_2,a_3)=256(r-r^9,s-s^9,t-t^9).
\]
Their Jacobian with respect to \((r,s,t)\) is invertible at every Fermat incidence point: it is \(\operatorname{diag}(256,256,256)\) at \((0,0,0)\) and \(\operatorname{diag}(-2048,256,256)\) at \((r,0,0)\) with \(r^8=1\). Coordinate permutations handle all other charts. Hence the three equations \(a_1=a_2=a_3=0\) cut out a unique analytic (indeed formal) parameter curve near each of the 52 points.

At \(p=(1,r,0,0)\), for \(r^8=1\) or \(r=0\), all three pure-cube equations hold identically for every \(\lambda\). By uniqueness, the nearby parameter curve is the **constant** section \(p\). Along it, the entire remainder, before multiplication by the nonzero factor \(4^3\), is
\[
4(r-r^9)x_1^3+\lambda(1-r^4)x_1x_2x_3.
\]
Consequently the full local incidence ring is \(\mathbb C[[\lambda]]\) if \(r^4=1\), and is \(\mathbb C[[\lambda]]/(\lambda)\) if \(r^4=-1\) or \(r=0\). In particular all 52 special-fiber points are reduced, exactly 24 remain horizontal, and exactly 28 are isolated vertical points. This calculation proves their multiplicities, not just their set-theoretic locations.

**4. Passage to an algebraic open set.** Since the special fiber of the proper morphism \(\mathscr I\to U\) is zero-dimensional, upper semicontinuity and properness make the morphism finite after shrinking \(U\) about \(0\). The complete local descriptions above exclude other horizontal branches meeting the special fiber. Any further components or exceptional fibers away from \(0\) have closed image under this finite morphism; remove that image by a further Zariski-open shrink. The 24 constant sections and 28 reduced vertical points then exhaust the scheme over some \(W\ni0\), giving the asserted decomposition.

**5. Conversion to quasi-Galois points.** For \(r^4=1\), the involution on the chosen two coordinates \((x_i,x_j)\mapsto(-r^{-1}x_j,-rx_i)\), fixing the others, preserves \(F_\lambda\), has center \([e_i+re_j]\), and fixes the complementary projection directions. Its center is exterior because \(F_\lambda(e_i+re_j)=1+r^4=2\). Miura--Taki's criterion identifies all other exterior quasi-Galois centers with exterior points of \(\mathscr I\); there are none over \(W\setminus\{0\}\). At \(\lambda=0\), the four coordinate points are also exterior, while the other 24 special-fiber two-supported points satisfy \(1+r^4=0\) and lie on the quartic. Thus the exterior counts are 24 and 28 respectively.

## Verification

The standalone `check.py` uses exact SymPy expansions to check the directional first and third polar formulas, pure-cube Jacobians, the fixed-section remainder, and invariance of all four-root reflecting involutions. Run `python check.py` with Python 3 and SymPy installed. Successful output begins with `VERIFY_OK directional_polar_and_third_polar` and ends with `VERIFY_OK reflection_invariance_for_all_fourth_roots`. The global finiteness and passage to \(W\) use standard properness and upper-semicontinuity arguments; no finite computation substitutes for these steps.

## Relationship to prior work

Miura--Taki (arXiv:2608.25445v1, revised v2) give the polar-divisibility criterion for exterior quasi-Galois points, characterize several quartic-surface situations, and determine the 28 points of the Fermat quartic in their Section 5. These results are premises and are not claimed as new. Miura--Takahashi (arXiv:2610.09331) treat projective liftings and quasi-Galois points of Fermat varieties. The Dwork pencil and its symmetry groups have been studied extensively. The result above instead determines the **relative polar-divisibility incidence scheme**, including its 28 disappearing reduced points, and proves exact persistence near the Fermat fiber. It does not infer uniqueness merely from a group-size calculation.

## Limitations

The neighborhood \(W\) is not given by an explicit polynomial condition; isolated nonzero parameters where extra centers could occur have not been classified. The incidence scheme deliberately includes 24 special points lying on the Fermat surface, which are not exterior quasi-Galois points. Novelty is relative to the inspected literature and mathematical-record searches, not an assertion of exhaustive historical priority. The proof concerns projective polar incidences, not all abstract automorphisms of the K3 surfaces.

## References

1. K. Miura and S. Taki, *Quasi-Galois points for quartic surfaces*, arXiv:2608.25445v1 (first posted 2026-08-26), v2 (2026-10-08), especially Proposition 3.5 and Theorem 5.4.
2. K. Miura and T. Takahashi, *Projective Lifting Theorem, Complex Reflection Groups, and Quasi-Galois Points for Fermat Varieties*, arXiv:2610.09331v1 (2026-10-07).
3. A. Banerjee and G. W. Moore, *Hyperkähler Isometries Of K3 Surfaces*, arXiv:2009.11769 (2020), for background on Dwork-pencil symmetries.
