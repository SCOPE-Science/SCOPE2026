# No hidden singular components in a characteristic-two elementary-symmetric quartic

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(n\ge 11\) be an integer with \(n\equiv3\pmod8\). Write \(e_4=e_4(x_1,\ldots,x_n)\) for the fourth elementary symmetric polynomial, and let
\[
X_n=V(e_4)\subset\mathbb P_k^{n-1}.
\]
For an unordered partition \(\pi=\{B_1,B_2,B_3\}\) of \([n]\) into three nonempty blocks, let \(P_\pi\) be the projective linear subspace on which coordinates are constant within each block. Let \(\mathcal P_n\) consist of partitions with \(|B_i|\equiv1\pmod8\) for all three blocks. Then the **entire reduced singular locus**, including all its lower-dimensional strata, is
\[
\operatorname{Sing}(X_n)_{\mathrm{red}}=\bigcup_{\pi\in\mathcal P_n}P_\pi.
\]
Every \(P_\pi\cong\mathbb P^2\) is a distinct irreducible component, and there are no additional components, not even isolated or curve components. The number of components is
\[
N_n=\frac16\sum_{\substack{a+b+c=n\\a,b,c\ge1\\a\equiv b\equiv c\equiv1\ (8)}}\frac{n!}{a!b!c!}.
\]
The hypersurface \(X_n\) is integral and normal. At a generic point of each component, the Jacobian singular scheme is reduced and the transverse hypersurface singularity is an ordinary nondegenerate quadratic double point (in the characteristic-two sense: nondegenerate polar quadratic form). In particular, \(N_{11}=55\) and \(N_{19}=462061\).

For \(n=11\), these 55 components have an explicit incidence structure. Index them by the 2-subsets \(\{i,j\}\subset[11]\): \(P_{ij}\) allows \(x_i,x_j\) to vary and equates the other nine coordinates. Distinct \(P_{ij}\) and \(P_{k\ell}\) meet in a projective line exactly when their index pairs share one element; otherwise they meet only at \([1:\cdots:1]\). Thus their line-intersection graph is the triangular graph \(T(11)\), with 55 vertices and 495 edges. Precisely 11 distinguished lines each belong to 10 component planes, and all component planes contain the diagonal point.

The component description and generic quadratic Hessian rank for maximal-dimensional partition spaces are established in earlier literature (Xie, 2026). The additional claim proved here is **exhaustiveness of that list as the whole reduced singular support**, with no hidden smaller-dimensional components; the stated eleven-variable incidence description is a concrete consequence.

## Assumptions and scope

The base field is algebraically closed of characteristic exactly \(2\). The index \(n\) ranges over all integers at least \(11\) congruent to \(3\) modulo \(8\). The singular scheme means the closed projective subscheme defined by \(e_4\) and all first partial derivatives; the equality above is one of **reduced** closed subschemes, not a claim that the unreduced Jacobian ideal is radical everywhere. The quadratic statement concerns generic points on components, not their intersections. The classification has no unproved parameter restriction inside its stated domain.

## Proof

**1. Irreducibility.** For \(r=2,3,4\), the identity \(e_r(x_1,\ldots,x_m)=x_m e_{r-1}(x_1,\ldots,x_{m-1})+e_r(x_1,\ldots,x_{m-1})\) is linear in \(x_m\). A primitive degree-one polynomial over the UFD of preceding variables is irreducible. For \(r=2\), \(e_1\) is irreducible and does not divide \(e_2\): specialize two coordinates to \(1\) and the rest to \(0\). Consequently \(e_2\) is irreducible on at least three variables. For \(r=3\), \(e_2\) is irreducible and does not divide \(e_3\): take three nonzero coordinates \(1,t,t/(1+t)\) with \(t\notin\{0,1\}\), giving \(e_2=0\) and \(e_3\ne0\). Consequently \(e_3\) is irreducible on at least four variables. Finally, \(e_3\) does not divide \(e_4\): four coordinates equal to \(1\), with all others \(0\), give \(e_3=0\) and \(e_4=1\). This proves irreducibility of \(e_4\) for \(n\ge5\).

**2. Translation invariance on the affine cone.** For a scalar \(t\in k\), the elementary-symmetric translation identity gives
\[
e_4(x+t\mathbf1)=\sum_{j=0}^{4}\binom{n-j}{4-j}t^{4-j}e_j(x),\qquad e_0=1.
\]
When \(n\equiv3\pmod8\), the four coefficients with \(j<4\) are even (Lucas's binary binomial criterion), so \(e_4(x+t\mathbf1)=e_4(x)\). Differentiating, every first derivative is also invariant. We use this **on affine representatives** of projective points; scalar translation is not asserted to define a projective automorphism. It is legitimate for classifying nonconstant-coordinate representatives, and the all-equal vector is handled directly.

**3. At most three values.** Put \(e_j=e_j(x_1,\ldots,x_n)\). The generating series identity \(\prod_{h\ne i}(1+x_hT)=\prod_h(1+x_hT)/(1+x_iT)\) yields, in characteristic two,
\[
\partial_i e_4=e_3+x_i e_2+x_i^2e_1+x_i^3.
\]
At a singular point, every coordinate is therefore a root of the monic cubic \(Q(Z)=Z^3+e_1Z^2+e_2Z+e_3\). In an algebraically closed field there are at most three distinct coordinate values.

**4. Three distinct values.** Translate one value to \(0\), leaving \(a\ge1\) copies of a nonzero value \(u\), \(b\ge1\) copies of another nonzero value \(v\ne u\), and \(c\ge1\) zeros. Because \(0,u,v\) are three distinct roots, necessarily \(Q(Z)=Z(Z+u)(Z+v)\). Thus \(e_1=u+v\), \(e_2=uv\), and \(e_3=0\). The equality
\[
(a\bmod2)u+(b\bmod2)v=u+v
\]
forces \(a,b\) to be odd, since \(u,v,u+v\) are all nonzero. With odd \(a,b\), the equality
\[
\binom a2 u^2+\binom b2 v^2=0
\]
forces both binomial coefficients to vanish modulo two: otherwise it would force \(u=0\), \(v=0\), or \(u=v\). Therefore \(a\equiv b\equiv1\pmod4\). Under these congruences, the coefficient of \(T^4\) in \((1+uT)^a(1+vT)^b\) equals
\[
e_4=\binom a4 u^4+\binom b4 v^4.
\]
Vanishing of \(e_4\) now forces both coefficients to be even, for otherwise \(u=0\), \(v=0\), or \(u=v\). Lucas's theorem yields \(a\equiv b\equiv1\pmod8\), and \(c=n-a-b\equiv1\pmod8\). Hence the original point belongs to a \(P_\pi\) with three block sizes congruent to \(1\) modulo \(8\).

**5. Exactly two distinct values.** Translate one value to \(0\), leaving \(a\) copies of \(u\ne0\) and \(n-a\) zeros. The equation and the gradients at either value reduce to
\[
\binom a4u^4=0,\qquad\binom a3u^3=0,\qquad\binom{a-1}3u^3=0.
\]
Their simultaneous binary parity criterion is exactly \(a\equiv1\) or \(2\pmod8\). If \(a\equiv1\pmod8\), the zero block has size \(2\pmod8\), and it can be split into two nonempty blocks of sizes \(1\pmod8\). If \(a\equiv2\pmod8\), split the nonzero block instead. Either construction places the point in one of the listed three-block partition planes.

**6. One value and the converse.** An all-equal projective point is the diagonal point, lying in every \(P_\pi\). Conversely, on a partition plane with block sizes \(1\pmod8\), the elementary-symmetric generating product is, modulo \(T^5\), simply \((1+uT)(1+vT)(1+wT)\). Its fourth coefficient is zero; after deleting a variable, the analogous generating product has degree at most two modulo \(T^4\), so every derivative also vanishes. Thus every listed plane lies in the singular support. Steps 3–5 prove there are no other singular points. Since all components are distinct irreducible projective planes of the same dimension, this is exactly the irreducible-component decomposition of the reduced singular scheme.

**7. Generic transverse type.** Let \(u,v,w\) be pairwise distinct generic block values. The Hessian entry for distinct indices is \(\partial_i\partial_j e_4=e_2(x\text{ with }i,j\text{ deleted})\), and the diagonal Hessian entries are zero. Entries between different blocks vanish. Within the block of value \(u\), each off-diagonal entry is \((u+v)(u+w)\ne0\); analogously for the other blocks. For a block of odd size \(m\), the matrix with zero diagonal and constant nonzero off-diagonal value has rank \(m-1\) in characteristic two. The Hessian rank is therefore \((|B_1|-1)+(|B_2|-1)+(|B_3|-1)=n-3\), equal to the codimension of \(P_\pi\) in projective space. The gradient ideal consequently defines the plane generically without thickening, and a normal transverse slice has a quadratic initial form with nondegenerate polar form. It is an ordinary transverse double point. The total singular support has dimension two. Since \(X_n\) is an integral hypersurface of dimension \(n-2\ge9\), it is regular in codimension one and Cohen–Macaulay; Serre's criterion proves normality.

**8. Enumeration and the first incidence arrangement.** The multinomial count over ordered triples counts each unordered three-block partition exactly \(3!\) times, proving the formula. At \(n=11\), the only possible block sizes are \(9,1,1\), giving \(\binom{11}{2}=55\) planes. For distinct index pairs \(I,J\), their defining coordinate equalities identify all coordinates when \(I\cap J=\varnothing\); when \(I\cap J=\{i\}\), all coordinates except \(x_i\) become equal. Thus the intersections are respectively the diagonal point and the distinguished line \(L_i\). Each 2-subset shares exactly one element with \(2(11-2)=18\) others, so there are \(55\cdot18/2=495\) line-intersecting pairs. For each \(i\), the 10 pairs containing \(i\) give the 10 planes through \(L_i\).

## Verification

The accompanying standard-library-only `verify.py` evaluates \(e_4\) and its first derivatives exactly over \(\mathbb F_4\), grouped by coordinate multiplicities. It exhausts all four-value multiplicity patterns for \(n=11\) (364 patterns) and \(n=19\) (1540 patterns), checking the claimed characterization in each case. It also checks Lucas-parity translation coefficients for both sizes, the component counts \(55\) and \(462061\), the Hessian ranks \(8\) and \(16\) at representatives with three distinct block values, and all 1485 pairs of the 55 planes (495 line and 990 point intersections). Run `python3 verify.py`; expected last line: `VERIFY_OK`.

These finite-field checks are consistency tests, not proofs for every algebraically closed field or every index. The proof above derives the universal claim from polynomial identities, Lucas parity, and Serre's criterion.

## Relationship to prior work

Cafure–Matera–Privitelli (2011 preprint, Section 3) provide a partition-space framework and dimension bounds for symmetric hypersurface singularities. Orzel (2025/2026) gives order-two zero-locus dimension bounds in positive characteristic. Xie (2026, Theorems 1.1 and 1.3, Sections 2 and 4) proves the sharp dimension formula and identifies the **maximal-dimensional partition-plane components** in the present parameter range; Xie also computes their generic Hessian rank. None of those contributions is claimed as new. Xie, Section 7, explicitly leaves smaller-dimensional and embedded components unclassified in general. The new assertion here is that for this entire natural arithmetic subfamily **no extra lower-dimensional reduced components exist**; its proof uses a special degree-four, characteristic-two translation and two-/three-value argument. In \(n=11\), it also yields the complete 55-plane incidence configuration as the entire support, rather than merely an arrangement contained within it.

## Limitations

The equality concerns the reduced singular scheme. It does not claim that the global Jacobian ideal equals the intersection of plane ideals, classify nilpotent/embedded local structure at their intersections, or extend to other congruence classes or to characteristic other than two. Ordinary-double-point structure is claimed only generically on each plane. The conclusion is proved mathematically here but has not undergone independent external review. Equivalence to an unstated consequence of broader prior theory remains a literature risk; novelty rests on the **full-support exclusion** rather than on Xie's already-known maximal-dimensional components.

## References

1. A. Cafure, G. Matera, M. Privitelli, *Singularities of symmetric hypersurfaces and an application to Reed–Solomon codes*, arXiv:1109.2265v1 (first public 2011-09-10), Sections 2–3. https://arxiv.org/html/1109.2265v1
2. I. Orzel, *Computing the Elementary Symmetric Polynomials in Positive Characteristics*, arXiv:2509.05009v3 (original submission 2025-09-05), Section 2. https://arxiv.org/html/2509.05009v3
3. Y. Xie, *Derivative and multiplicity loci of elementary symmetric polynomials in positive characteristic*, arXiv:2610.00259v1 (2026-09-24), Theorems 1.1, 1.3 and 1.4, Sections 2, 4, and 7. https://arxiv.org/html/2610.00259v1
