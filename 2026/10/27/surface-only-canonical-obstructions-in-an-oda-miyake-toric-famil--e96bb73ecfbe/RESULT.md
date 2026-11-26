# Smooth canonical-degree-zero curves on a toric boundary surface

## Finding
For an integer \(d\ge2\), consider the smooth complete toric threefold \(X_d=Z''_{13}(-2,2,0,d)\) and its invariant divisor \(D_7\). On \(D_7=\operatorname{Bl}_p(\mathbb P^1\times\mathbb P^1)\), with ruling pullbacks \(F_x,F_y\) and exceptional curve \(E\),
\[
K_{X_d}|_{D_7}=(d-1)F_x-2F_y+3E.
\]
It is neither pseudo-effective nor the negative of a pseudo-effective class. A general curve of bidegree \((d-1,2)\) in the product avoids \(p\). Its strict transform is a smooth irreducible curve \(C_d\) of genus \(d-2\) and canonical degree \(K_{X_d}\cdot C_d=0\). These curves are not torus invariant. Here canonical degree zero is a numerical condition, not an assertion that \(\omega_{X_d}|_{C_d}\) is trivial.

The known tensor-generation test and wall-degree table for the full four-parameter family [3] already imply that \(\omega_{X_d}\) is not tensor-generating although no invariant curve has canonical degree zero. This is the context for the surface calculation, not a new solution to the invariant-curve question. The additional geometry is the opposite signs on the two nef ruling classes and the resulting explicit moving smooth curves that avoid the exceptional locus, with prescribed genus \(d-2\).

## Assumptions and scope
Work over \(\mathbb C\). The fan, in \(\mathbb Z^3\), has rays
\[
\begin{array}{llll}
v_1=(1,1,2),&v_2=(1,0,0),&v_3=(0,-1,0),&v_4=(0,0,-1),\\
v_5=(-1,-2,d),&v_6=(0,1,0),&v_7=(0,0,1),&v_8=(-1,0,d+1),
\end{array}
\]
and maximal cones \(124,234,345,456,146,167,127,237,358,568,378,678\), where the digits index the generators. Smoothness and completeness follow from [1, Construction 6.1 and Remark 6.2] and [2, §4]. The varieties are nonprojective by the projectivity criterion in [2], since \(b=2\ne0\) and \(a=-2\ne c=0\). A line bundle is tensor-generating when its integral tensor powers generate the perfect derived category.

## Proof
**Known ambient obstruction and invariant degrees.** In the four-parameter test [3, Steps 2–3], the \(v_7\) ray condition requires a real \(t\) with \(ct<1-d\), impossible for \(c=0,\ d\ge2\). Equivalently, the canonical ray criterion [1, Corollary 3.6] fails because
\[
v_7=\frac{v_2+v_8}{d+1}+\frac{d-1}{2(d+1)}(v_3+v_6),
\]
a convex combination of rays adjacent to \(v_7\) with positive weights summing to one. The degree table below is the specialization of [3, Step 3]. Its entries are \((-K_{X_d})\cdot V(ij)\); none vanishes at \(d\ge2\).

| Wall | Degree | Wall | Degree | Wall | Degree |
|:--|--:|:--|--:|:--|--:|
| 12 | 2 | 14 | −1 | 16 | 2 |
| 17 | 3 | 23 | 2 | 24 | 3 |
| 27 | −1 | 34 | \(d\) | 35 | 3 |
| 37 | \(1-d\) | 38 | −1 | 45 | 2 |
| 46 | \(d+5\) | 56 | −1 | 58 | 2 |
| 67 | \(-d-2\) | 68 | 3 | 78 | 2 |

**Restricted class and signs.** In the quotient by \(\mathbb Z v_7\), the rays of the star fan have cyclic order \((1,0),(1,1),(0,1),(-1,0),(0,-1)\), with cones between consecutive rays. This subdivides one cone of the product fan and identifies \(D_7\) with its blowup at one fixed point. Its boundary curves, indexed by \(1,2,6,8,3\), have classes \(E,F_x-E,F_y-E,F_x,F_y\). Negating the corresponding entries of the table gives canonical degrees \(-3,1,d+2,-2,d-1\). Since \(F_x^2=F_y^2=F_xE=F_yE=0,\ F_xF_y=1,\ E^2=-1\), already the three degrees on \(E,F_x,F_y\) determine the displayed canonical class. Its degrees on the nef ruling pullbacks are \(-2\) and \(d-1\), of opposite sign. Each sign of the restricted class has negative intersection with one of these nef divisors and so is not pseudo-effective. In particular neither sign is big, giving the obstruction directly on \(D_7\) by [1, Theorem 1.1].

**Moving curves disjoint from the blowup center.** The linear system of bidegree \((d-1,2)\) on the product is very ample since \(d-1\ge1\). Its general member is smooth and irreducible by Bertini and does not pass through \(p\) because the system is basepoint-free. The strict transform has class \((d-1)F_x+2F_y\); the exceptional term does not contribute to its degree. The two ruling terms contribute \(2(d-1)-2(d-1)=0\). Adjunction on the product gives genus \(((d-1)-1)(2-1)=d-2\). The prior nonzero wall degrees rule out torus invariance of any such member.

## Reproducibility and limitations
The accompanying `artifacts/verify_toric_example.py` checks the wall relations, convex combination and intersection identities for ten integral values (eight in the range \(d\ge2\)). Run `python3 artifacts/verify_toric_example.py` from the package directory. These checks do not prove smooth-curve existence or establish priority. The affine wall formulas, toric intersections, and Bertini argument give the unrestricted claim in its stated range. No classification of other subfamilies, of all degree-zero curves, or of linear triviality on these curves is made.

## Relationship to prior work
Ito–Zeng–Zeng [1] supply the criterion and pose the family-specific Question 6.6; their Remark 7.6 already exhibits the general surface-without-invariant-curve phenomenon. Within the same four-parameter family, [4] gives a negative answer on a different slice \(Z''_{13}(a,2,0,0)\) for \(a\ge4\), using the same blowup surface and a non-invariant rational degree-zero curve through the blowup center before transformation. In that slice the restricted anticanonical class is effective, represented by \((F_1-E)+2(F_2-E)\) in the ruling notation of [4]. In contrast, the restricted class here has neither sign pseudo-effective and gives degree-zero curves avoiding the center. The all-parameter invariant-curve degrees and tensor-generation criterion are stated in [3], so their application here is context, not part of the distinct contribution. The supplied comparison does not establish historical priority for the surface geometry.

## References
1. D. Ito, M. R. Zeng and X. Zeng, *Tensor-generating line bundles on toric varieties*, arXiv:2610.22279, Theorem 1.1, Corollary 3.6, Construction 6.1, Question 6.6 and Remark 7.6.
2. O. Fujino and H. Sato, *On non-projective complete toric varieties*, arXiv:2412.02392, §4.
3. [*A closed four-parameter canonical tensor-generation test for the Oda–Miyake family*](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-a-closed-four-parameter-canonical-tensor-generation-test-for-the--838005eaafd0/RESULT.md), proof Steps 2–3.
4. [*An invariant-surface obstruction without invariant-curve obstructions in non-projective toric threefolds*](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-an-invariant-surface-obstruction-without-invariant-curve-obstruc--855d8bd424a2/RESULT.md), Finding.
