# Characteristic-three Frobenius collapse of Klein’s reducible-polar tower and its arithmetic support

## Finding

Let \(F=x^3y+y^3z+z^3x\), and form the primitive integral Klein polynomial \(K=\Phi_{21}\) using the explicit invariant-theoretic determinant construction below. Put \(G=\nabla F\), and let \(D_k\) be the Cartier divisor on \(\mathbf P^2_{\mathbb Z_{(3)}}\) defined by \(K(G^{\circ k})\), for every integer \(k\geq0\). The degree of \(D_k\) is \(21\cdot3^k\). In the algebraic closure of characteristic three,

\[
(D_k)_{\overline{\mathbf F}_3}=3^k\,(D_0)_{\overline{\mathbf F}_3},\qquad k\geq0.
\]

Here \((D_0)_{\overline{\mathbf F}_3}\) is a **reduced union of 21 distinct lines**. The integral quotient \(Q_{42}:=K(G)/K\), whose generic fiber is the published 21-conic polar arrangement, satisfies

\[
\overline{Q}_{42}=\overline K^{\,2},\qquad
\overline{K(G)}=\overline K^{\,3}.
\]

Consequently the degree-42 polar-conic divisor becomes a double Klein line divisor, and the 21 reducible polars together become a triple Klein line divisor, even though the Klein quartic itself remains smooth in characteristic three.

For this particular integral coordinate model, all 21 reduced lines are defined over \(\mathbf F_{3^6}\). Exactly three lines have minimal field of definition \(\mathbf F_{3^3}\) and eighteen have minimal field \(\mathbf F_{3^6}\). The reduced intersection support has 28 triple and 21 quadruple points, with the **arithmetic field-degree profiles**

| Reduced-support multiplicity | Minimal degree 1 | Minimal degree 3 | Minimal degree 6 |
|---|---:|---:|---:|
| Three lines | 1 | 3 | 24 |
| Four lines | 0 | 3 | 18 |

No reduced component or multiple point has minimal field degree two. The unique \(\mathbf F_3\)-rational triple point is \([1:1:1]\). The geometric intersection counts are classical; the new assertions concern the nonreduced polar tower and the exact finite-field descent pattern of this specific support.

## Assumptions and scope

Everything is over the **specific integer model** with homogeneous coordinates \([x:y:z]\), not an arbitrary integral form of the configuration. Let

\[
H=xy^5+yz^5+zx^5-5x^2y^2z^2.
\]

Write \(M\) for the bordered Hessian matrix with upper-left block \(\operatorname{Hess}(F)\), upper-right column \(\nabla H\), lower-left row \((\nabla H)^T\), and lower-right entry zero. Define

\[
B=\frac{\det M}{9},\qquad
K=\frac{1}{14}\det\left(\frac{\partial(F,H,B)}{\partial(x,y,z)}\right).
\]

Both divisions yield polynomials over \(\mathbb Z\), verified coefficientwise. The chosen normalization makes the coefficient of \(x^{21}\) in \(K\) equal to \(1\), and \(K\) is invariant under the cyclic substitution \((x,y,z)\mapsto(y,z,x)\). All reductions use this integral model; no characteristic-zero normalizing constant is inverted in characteristic three. The scheme-theoretic divisor equality is in \(\mathbf P^2_{\overline{\mathbf F}_3}\). Finite-field degrees refer to its **specific coordinate field**.

## Proof

**1. Polynomial normalization and quotient.** Exact integer determinants give \(\det M\in9\mathbb Z[x,y,z]\) and \(\det(\partial(F,H,B)/\partial(x,y,z))\in14\mathbb Z[x,y,z]\). The resulting \(K\) is homogeneous of degree 21, primitive, cyclically invariant, and has coefficient \(1\) at \(x^{21}\). Integer polynomial division gives zero remainder on division of \(K(G)\) by \(K\), with quotient \(Q_{42}\in\mathbb Z[x,y,z]\) of degree 42. The construction agrees with the conic arrangement of Pokora–Roé and Gévay–Pokora in characteristic zero. In particular \(D_1\) is the union of its 21 lines and 21 smooth conics there.

**2. Frobenius degeneration for every iterate.** Over \(\mathbf F_3\), direct differentiation gives

\[
\overline G=(z^3,x^3,y^3)=\sigma\circ\operatorname{Fr}_3,
\]

where \(\sigma\) is the cyclic coordinate permutation. Since \(\overline K\) is cyclically invariant and its coefficients are in \(\mathbf F_3\), repeated substitution and the freshman's-dream identity give the **polynomial identity**

\[
\overline{K(G^{\circ k})}=\overline K^{\,3^k},\qquad\text{for all integers }k\ge0.
\]

For \(k=1\), the integral quotient identity in Step 1, combined with the fact that \(\overline K\ne0\), gives \(\overline{Q}_{42}=\overline K^2\) by cancellation in the domain \(\mathbf F_3[x,y,z]\). The polynomial identity yields the claimed effective Cartier-divisor equality, not merely a set-theoretic support equality. The gradient coordinates \((z^3,x^3,y^3)\) have no common zero on \(\mathbf P^2\), so the quartic remains smooth in characteristic three. The polar degeneration comes from inseparability of the gradient map, not a degeneration of the original quartic.

**3. Exact factorization and arithmetic of the reduced support.** Work in the field

\[
E=\mathbf F_3[U]/(U^6+U^5+U^4+U^3-U+1).
\]

The displayed modulus is irreducible, as established by exhaustive finite-field arithmetic in the accompanying verifier. Over \(\mathbf F_3\), the root polynomial factors exactly as

\[
\begin{aligned}
t^{21}-t^7+1={}&(t^3-t^2+t+1)\\
&\cdot(t^6+t^5+t^4+t^3-t+1)\\
&\cdot(t^6+t^5+t^4-t^3-t^2+1)\\
&\cdot(t^6-t^5-t^4+t^3+1),
\end{aligned}
\]

with all four factors irreducible over \(\mathbf F_3\). This also gives one Frobenius 3-cycle and three Frobenius 6-cycles on the lines. Let \(\mathcal T\subset E\) be the roots of \(t^{21}-t^7+1\); exact enumeration yields 21 distinct roots. For every \(t\in\mathcal T\), set

\[
\ell_t=x-ty+(t^{12}-t^{-2})z.
\]

None of the roots is zero. Expanding the degree-21 product in the field \(E[x,y,z]\) gives the exact normalized identity

\[
\overline K=\prod_{t\in\mathcal T}\ell_t.
\]

This is a coefficient-by-coefficient identity, **not** an inference from testing polynomial values at finitely many points. The 21 forms are pairwise distinct because their \(x\)-coefficient is normalized to one and their \(y\)-coefficients distinguish the roots. Hence \(\overline K\) is geometrically reduced with exactly 21 lines.

**4. Exhaustive projective intersections and Frobenius descent.** For each of the \(\binom{21}{2}=210\) unordered line pairs, compute their cross product in \(E^3\) and normalize the first nonzero coordinate to one. Exactly 49 projective points result, with 28 points lying on three lines and 21 on four; the identity \(28\binom32+21\binom42=210\) also checks all pair incidences. The minimal field degree of a normalized line or point is the least \(d\in\{1,2,3,6\}\) fixed projectively under coordinatewise \(3^d\)-power Frobenius. Checking all 21 lines and 49 points yields the field-degree table in the statement, including the unique rational triple point. Because all factors and intersections have been enumerated exactly, the classification is exhaustive over the algebraic closure.

## Verification

Run `python verify_klein_polar.py` in a Python environment with SymPy available. The script reconstructs the three invariant polynomials entirely from their definitions; verifies both integral divisibilities, the exact integer quotient, cyclic invariance, and the characteristic-three congruence; proves its 729-element arithmetic quotient is a field; exactly expands all 21 factors; and enumerates every pair incidence and Frobenius orbit degree. It finishes with

`KLEIN_POLAR_CHAR3_FROBENIUS_TOWER_AND_F729_ARITHMETIC_CERTIFICATE_PASS`

The infinite iterate statement is the symbolic proof in Step 2, not a finite computation extrapolated to arbitrary \(k\).

## Relationship to prior work

Pokora–Roé, *The 21 reducible polars of Klein's quartic* (first posted March 16, 2018), §2, defines \(\Phi_{63}=\Phi_{21}\Phi_{42}\) and establishes the complex 21-line/21-conic arrangement. Its §7 proves **reducedness** for the iterated complex pullbacks (Proposition 7.5), precisely the opposite behavior to the characteristic-three special fibers proved here. Gévay–Pokora, *Klein's arrangements of lines and conics* (2022), §3.1, prints the determinant construction used here and an explicit factorization procedure, over characteristic zero. Pokora–Roé, *Harbourne Constants, Pull-Back Clusters and Ramified Morphisms* (2019), studies the general complex pullback setting. The classical 21 quadruple/28 triple geometric incidence profile, as well as arithmetic persistence of the reduced line-arrangement lattice in odd characteristic, is not a new claim. None of these known statements implies the exact nonreduced polar specializations and complete Frobenius field-degree table stated here.

## Limitations

The proof establishes the **scheme-theoretic divisors** defined by the displayed integral equations; it does not assert that every positive-characteristic intrinsic Steinerian or polar-moduli construction equals their reduction, or that the same field-degree pattern holds for different integral projective coordinate models. The 21 line factors are defined over \(E\), although only their product is defined over \(\mathbf F_3\). The numerical finite-field census is exact and exhaustive for these polynomial equations but does not replace the separate proof of every-iterate Frobenius identity. Historical originality is assessed against accessible primary texts and research records; unindexed precedent cannot be completely excluded. No independent mathematical audit has been carried out.

## References

1. P. Pokora and J. Roé, *The 21 reducible polars of Klein's quartic*, arXiv:1803.06411 (v1, March 16, 2018), §§1, 2, 7. https://arxiv.org/abs/1803.06411
2. G. Gévay and P. Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309 (2022), §3.1. https://arxiv.org/abs/2211.15309
3. P. Pokora and J. Roé, *Harbourne Constants, Pull-Back Clusters and Ramified Morphisms*, Results in Mathematics (2019), DOI 10.1007/s00025-019-1031-x. https://doi.org/10.1007/s00025-019-1031-x
