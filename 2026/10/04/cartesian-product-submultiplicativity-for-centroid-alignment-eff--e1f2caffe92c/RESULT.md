# Cartesian-product submultiplicativity for centroid-alignment efficiency
## Finding
For a family \(\mathcal C=(C_1,\ldots,C_m)\) of compact convex bodies with nonempty interior in \(\mathbb R^n\), define
\[
M(\mathcal C)=\max_{v_1,\ldots,v_m\in\mathbb R^n}\operatorname{Vol}_n\!\left(\bigcap_{i=1}^m(C_i+v_i)\right)
\]
and
\[
L(\mathcal C)=\operatorname{Vol}_n\!\left(\bigcap_{i=1}^m(C_i-\operatorname{cen} C_i)\right).
\]
Write \(E(\mathcal C)=L(\mathcal C)/M(\mathcal C)\), and let \(c_{n,m}\) be the infimum of \(E(\mathcal C)\) over all such families of exactly \(m\) bodies in \(\mathbb R^n\).

For all integers \(n,d\ge1\) and \(m\ge1\),
\[
c_{n+d,m}\le c_{n,m}c_{d,m}.
\]
Consequently, for each fixed \(m\),
\[
\lim_{n\to\infty}c_{n,m}^{1/n}=\inf_{n\ge1}c_{n,m}^{1/n}.
\]
Feldman proves \(c_{2,m}=4/9\) for every \(m\ge2\), while one-dimensional centroid alignment is optimal, so \(c_{1,m}=1\). Therefore
\[
c_{n,m}\le \left(\frac49\right)^{\lfloor n/2\rfloor}\qquad(n\ge1,\ m\ge2).
\]
Combined with Feldman's universal lower bound, this places every fixed-cardinality problem in the explicit bracket
\[
\left(\frac{2}{n+1}\right)^n\le c_{n,m}\le \left(\frac49\right)^{\lfloor n/2\rfloor}\qquad(n\ge2,\ m\ge2).
\]
The upper bound is not claimed sharp.

## Assumptions and scope
All bodies are compact, convex, and have nonempty interior. Only translations are optimized. The centroid is taken with respect to Lebesgue volume. The number \(m\) of bodies is fixed when defining \(c_{n,m}\). The theorem concerns the infimum over exactly \(m\) bodies; it does not replace Feldman's separate infimum in which the family size may vary.

## Proof
Take families \(\mathcal A=(A_1,\ldots,A_m)\) in \(\mathbb R^n\) and \(\mathcal B=(B_1,\ldots,B_m)\) in \(\mathbb R^d\), and form
\[
\mathcal A\boxtimes\mathcal B=(A_1\times B_1,\ldots,A_m\times B_m)
\]
in \(\mathbb R^{n+d}\).

Centroids factor under Cartesian products:
\[
\operatorname{cen}(A_i\times B_i)=\bigl(\operatorname{cen}A_i,\operatorname{cen}B_i\bigr).
\]
Hence the centroid-aligned intersection factors exactly, and product measure gives
\[
L(\mathcal A\boxtimes\mathcal B)=L(\mathcal A)L(\mathcal B).
\]

For arbitrary translations write \(v_i=(x_i,y_i)\in\mathbb R^n\times\mathbb R^d\). Then
\[
\bigcap_{i=1}^m\bigl((A_i\times B_i)+v_i\bigr)
=
\left(\bigcap_{i=1}^m(A_i+x_i)\right)
\times
\left(\bigcap_{i=1}^m(B_i+y_i)\right).
\]
Therefore every translated-intersection volume is the product of an \(\mathcal A\)-overlap and a \(\mathcal B\)-overlap. It is at most \(M(\mathcal A)M(\mathcal B)\), and choosing maximizing translations independently in the two factors attains this product. Thus
\[
M(\mathcal A\boxtimes\mathcal B)=M(\mathcal A)M(\mathcal B),
\qquad
E(\mathcal A\boxtimes\mathcal B)=E(\mathcal A)E(\mathcal B).
\]

Given \(\varepsilon>0\), choose \(\mathcal A\) and \(\mathcal B\) with efficiencies below \(c_{n,m}+\varepsilon\) and \(c_{d,m}+\varepsilon\). The product family has exactly \(m\) bodies, so
\[
c_{n+d,m}\le(c_{n,m}+\varepsilon)(c_{d,m}+\varepsilon).
\]
Letting \(\varepsilon\downarrow0\) proves submultiplicativity.

Feldman's lower bound makes every \(c_{n,m}\) positive. Therefore \(a_n=\log c_{n,m}\) is finite and satisfies \(a_{n+d}\le a_n+a_d\). Fekete's subadditive lemma yields existence of \(\lim a_n/n\), equal to its infimum; exponentiating gives the asserted root limit.

For \(m\ge2\), Feldman's planar result gives \(c_{2,m}=4/9\). Repeated products give \(c_{2k,m}\le(4/9)^k\). If \(n=2k+1\), append a one-dimensional factor, for which centroid alignment is optimal and \(c_{1,m}=1\). This proves the stated bound in every dimension.

## Verification
The proof is exact and does not infer an infinite-dimensional statement from finite experiments. The only limiting steps are the definition of an infimum, handled with an arbitrary \(\varepsilon>0\), and Fekete's lemma applied to the positive sequence \(c_{n,m}\). The factorization of both the lazy volume and the optimized volume follows directly from the Cartesian-product identity for intersections and product Lebesgue measure.

As boundary checks: \(m=1\) gives \(c_{n,1}=1\), consistent with submultiplicativity. For \(n=2\), the consequence recovers \(4/9\). For odd dimensions the extra interval factor contributes efficiency exactly \(1\), not an approximation.

## Relationship to prior work
Feldman introduces \(c_{n,m}\), proves the family-size-free lower bound \((2/(n+1))^n\), proves the exact planar fixed-cardinality value \(c_{2,m}=4/9\) for every \(m\ge2\), and asks whether two bodies already approach the family-size-free lower bound in dimensions \(n\ge3\). The Cartesian-product factorization above is not stated in that paper. It turns the planar obstruction into fixed-cardinality examples in every dimension and gives an exponential upper bound while leaving the exact value open.

The 1998 work of de Berg, Cheong, Devillers, van Kreveld, and Teillaud supplies the planar example whose centroid-aligned overlap approaches \(4/9\) of optimum; Feldman's 2026 result proves that this planar constant is exact. Later overlap papers inspected here are algorithmic and do not supply a higher-dimensional centroid-efficiency tensorization statement.

## Limitations
The result does not settle whether \(c_{n,2}=(2/(n+1))^n\) for any \(n\ge3\). The product examples are decomposable and may be far from extremal. The upper and lower bounds have very different asymptotic scales, so the exact fixed-cardinality decay remains open. No claim is made about rotations, homotheties, nonconvex sets, or other alignment selectors.

## References
1. David Victor Feldman, *Arranging convex bodies for maximum intersection volume: the sharp efficiency of centroid alignment*, arXiv:2608.04516v1, 2026.
2. Mark de Berg, Otfried Cheong, Olivier Devillers, Marc van Kreveld, Monique Teillaud, *Computing the maximum overlap of two convex polygons under translations*, Theory of Computing Systems 31 (1998), 613--628, DOI:10.1007/PL00005845.
3. Hee-Kap Ahn, Siu-Wing Cheng, Iris Reinbacher, *Maximum overlap of convex polytopes under translation*, Computational Geometry 46 (2013), 552--565.
4. Timothy M. Chan, Isaac M. Hair, *A Linear Time Algorithm for the Maximum Overlap of Two Convex Polygons Under Translation*, SoCG 2025, LIPIcs 332, Article 31.
