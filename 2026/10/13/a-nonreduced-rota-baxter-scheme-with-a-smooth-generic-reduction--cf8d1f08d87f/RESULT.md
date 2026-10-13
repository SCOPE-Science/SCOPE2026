# A nonreduced Rota–Baxter scheme with a smooth generic reduction

## Finding

Let \(K\) be **any field**, and consider the three-dimensional associative algebra \(A\) with basis \(e_1,e_2,z\), with multiplication
\[
e_1e_2=z,\qquad e_2e_1=-z,
\]
and every other basis product zero. For \(\lambda\in K\), the weight-\(\lambda\) Rota–Baxter operator scheme \(\mathscr R_\lambda\) parametrizes endomorphisms satisfying
\[
R(x)R(y)=R\bigl(R(x)y+xR(y)+\lambda xy\bigr)
\]
for all \(x,y\in A\).

In column convention write
\[
R=\begin{pmatrix}a&b&h\\c&d&j\\u&v&k\end{pmatrix}.
\]
Then the **reduced** operator scheme has defining ideal
\[
\sqrt{I_\lambda}=\bigl(h,j,ad-bc-k(a+d+\lambda)\bigr),
\]
and therefore is isomorphic to
\[
\boxed{\mathscr R_\lambda^{\mathrm{red}}
\cong \mathbb A^2_{u,v}\times
\{(X,k)\in\mathrm{Mat}_2\times\mathbb A^1:
\det X=k(k+\lambda)\}},
\qquad
X=\begin{pmatrix}a-k&b\\c&d-k\end{pmatrix}.
\]
It is geometrically integral of dimension \(6\).

Its geometry changes sharply with the weight:
\[
\boxed{\mathscr R_\lambda^{\mathrm{red}}\text{ is smooth for }\lambda\ne0,}
\]
while at \(\lambda=0\) its reduced singular locus is the affine plane
\[
\boxed{X=0,\quad k=0,\quad (u,v)\in\mathbb A^2.}
\]
Writing \(\mathbb L=[\mathbb A^1]\) in the Grothendieck ring of \(K\)-varieties,
\[
\boxed{
[\mathscr R_0^{\mathrm{red}}]=\mathbb L^6,\qquad
[\mathscr R_\lambda^{\mathrm{red}}]=\mathbb L^6+\mathbb L^4\quad(\lambda\ne0).
}
\]
Consequently, over every finite field \(\mathbf F_q\), of **either characteristic**,
\[
\boxed{
\#\mathscr R_0(\mathbf F_q)=q^6,\qquad
\#\mathscr R_\lambda(\mathbf F_q)=q^6+q^4\quad(\lambda\ne0).
}
\]
The corresponding point-count zeta functions over \(\mathbf F_q\) are
\[
Z_0(T)=\frac1{1-q^6T},\qquad
Z_\lambda(T)=\frac1{(1-q^6T)(1-q^4T)}\quad(\lambda\ne0).
\]

**The full operator scheme is nonreduced for every weight, even when its reduction is smooth.** In particular, at nonzero weight a first-order deformation exists that provably cannot be extended to order two.

## Assumptions and scope

The source algebra is the nonunital, skew-multiplication algebra denoted \(A_3\) in Abdujabborov–Karimjanov–Kodirova, first publicly issued on 15 July 2021. That paper lists primary MSC \(16W20\) and classifies complex-valued operator matrices for weights zero and one. Those ordinary operator classifications are **prior work**, not claimed here as new.

The result here is scheme-theoretic: it determines the entire defining equations, the radical and geometric fibers, the motivic class, and a nonliftable infinitesimal. It concerns the three-dimensional algebra above, not the four-dimensional unital exterior algebra. Over characteristic \(2\), the signed multiplication still defines the same alternating bilinear product, and all displayed identities continue to hold.

## Proof

Put \(s=a+d\) and
\[
f=ad-bc-k(s+\lambda).
\]
Every Rota–Baxter defect is skew bilinear in its two inputs. Direct substitution on the basis pairs \((e_1,e_2)\), \((e_1,z)\), and \((e_2,z)\) yields exactly these coordinate triples:
\[
D_{12}=\bigl(-h(s+\lambda),\;-j(s+\lambda),\;f\bigr),
\]
\[
D_{13}=\bigl(-hj,\;-j^2,\;(a-k)j-ch\bigr),
\]
\[
D_{23}=\bigl(h^2,\;hj,\;bj+(k-d)h\bigr).
\]
These nine polynomials generate the **full** scheme ideal \(I_\lambda\) in the polynomial ring in all nine entries of \(R\); none of the original scheme equations is discarded at this stage.

Because \(h^2,j^2\in I_\lambda\), every field-valued point has \(h=j=0\). Conversely, setting \(h=j=0\) eliminates all equations except \(f=0\). Consequently
\[
\sqrt{I_\lambda}=\sqrt{(h,j,f)}.
\]
The ideal \((h,j,f)\) is prime. Indeed, under the invertible change of variables
\[
X=\begin{pmatrix}a-k&b\\c&d-k\end{pmatrix},
\]
one has \(f=\det X-k(k+\lambda)\). This polynomial is primitive and irreducible: treating it as a linear polynomial in the lower-right entry of \(X\), its leading coefficient is the upper-left entry, which is relatively prime to its constant coefficient \(-x_{12}x_{21}-k(k+\lambda)\). This argument works over every field, including algebraic closures. Hence \((h,j,f)\) is geometrically prime, proving the radical formula and dimension \(2+(5-1)=6\).

For smoothness, the four partial derivatives of
\[
\det X-k(k+\lambda)
\]
with respect to the entries of \(X\) vanish simultaneously precisely when \(X=0\). Then the equation becomes \(k(k+\lambda)=0\), and its remaining derivative in \(k\) is \(-2k-\lambda\). If \(\lambda\ne0\), this derivative is nonzero at both roots \(k=0,-\lambda\), even in characteristic \(2\). If \(\lambda=0\), the only singular solution is \(X=0,k=0\). The arbitrary variables \(u,v\) give the stated affine-plane singular stratum.

For the Grothendieck class, fix \(\delta\in K\) and consider the determinant fiber
\[
F_\delta=\{X\in\mathrm{Mat}_2:\det X=\delta\}.
\]
Choosing the first column first gives
\[
[F_\delta]=\begin{cases}
\mathbb L^3-\mathbb L,&\delta\ne0,\\
\mathbb L^3+\mathbb L^2-\mathbb L,&\delta=0.
\end{cases}
\]
For nonzero determinant, the first column is nonzero, and the second column ranges over an affine line. For zero determinant, the first column may be zero (giving an affine plane of second columns) or nonzero (again giving an affine line). These are algebraic bundle decompositions valid in the Grothendieck ring over any \(K\).

Since \(k(k+\lambda)\) vanishes at **one** \(K\)-rational value of \(k\) when \(\lambda=0\), but at **two distinct** values when \(\lambda\ne0\), the five-dimensional determinant hypersurface has class
\[
\mathbb L(\mathbb L^3-\mathbb L)+
 r\mathbb L^2
=\mathbb L^4+(r-1)\mathbb L^2,
\]
where \(r=1\) or \(r=2\), respectively. Multiplication by the free \(\mathbb A^2_{u,v}\) gives the announced \(\mathbb L^6\) and \(\mathbb L^6+\mathbb L^4\). Point counts, extension-field counts, and zeta functions follow by evaluating \(\mathbb L\) at \(q^m\).

To see why the **full scheme** is nonreduced, retain rather than discard the original square equations \(h^2=j^2=0\). When \(\lambda\ne0\), the point
\[
R_*(e_1)=0,\quad R_*(e_2)=-\lambda e_2,\quad R_*(z)=0
\]
has Zariski tangent dimension \(7\) in the full operator scheme, while the reduced smooth variety has tangent dimension \(6\). (These dimensions follow from the Jacobians of the nine displayed generators and of \((h,j,f)\), respectively.) In fact the first-order family
\[
R_\epsilon(e_1)=0,\qquad R_\epsilon(e_2)=-\lambda e_2,\qquad
R_\epsilon(z)=\epsilon e_2,
\quad \epsilon^2=0
\]
satisfies all nine defects over \(K[\epsilon]/(\epsilon^2)\). However any lift to \(K[t]/(t^3)\) retaining the first-order coefficient \(j=t\) would have \(j^2=t^2\ne0\), contradicting the defining equation \(j^2=0\). Thus this infinitesimal is obstructed at second order. At \(\lambda=0\), the zero operator has full-scheme tangent dimension \(9\), while the reduced locus has tangent dimension \(7\). The nonreducedness is therefore present for all weights.

## Verification

Run `python artifacts/verify.py` using Python and SymPy. The bundled verifier reconstructs each basis-pair defect symbolically and compares it to the complete nine-polynomial scheme ideal, including signs in every characteristic. It differentiates both the full and reduced equations at the specified points and verifies the stated tangent dimensions and the first-order deformation's nonliftable square obstruction.

As finite replay evidence, the checker exhaustively tests **every endomorphism** over \(\mathbf F_2\) and \(\mathbf F_3\), without assuming the reduced form, at weights zero and one. It obtains \(64,80\) operators over \(\mathbf F_2\) and \(729,810\) over \(\mathbf F_3\). It additionally enumerates every matrix fiber of the reduced hypersurface over \(\mathbf F_3,\mathbf F_5,\mathbf F_7,\mathbf F_{11}\), matching the formula for weights zero, one, and two. It prints `VERIFY_OK`.

The finite experiments are checks, **not** the infinite-field proof; the latter is given by the exact equations, primality, Jacobian criterion, and determinant-fiber stratification.

## Relationship to prior work

Abdujabborov–Karimjanov–Kodirova (2021), especially its algebra \(A_3\) and its weight-zero and weight-one Rota–Baxter tables, covers the ordinary complex-valued operator classification. The field-point reduction \(h=j=0\) is consistent with that result, and by itself is not an originality claim. The **new statement** is that the unreduced representing scheme still retains nilpotent normal-direction coordinates and obstructed first-order deformations, while its reduced geometry has an exact smoothness and motivic weight transition.

Benito–Gubarev–Pozhidaev treat Rota–Baxter operators on the related but different **unital four-dimensional exterior algebra**, including its full unital operations. Their operator classification does not determine the functor of schemes on the **three-dimensional augmentation ideal**, nor its nonreduced directions. Das–Mishra develop general deformation theory of associative Rota–Baxter algebras; the explicit nonliftable direction and determinant-fiber calculations for this algebra are not stated there.

The closest published semantic research result computes a finite-field count and conjugacy orbits of weight-zero Rota–Baxter operators on the **four-dimensional** unital exterior algebra over \(\mathbf F_2\). The changed ambient algebra and omission of nonzero weights mean it neither states nor implies the scheme geometry above. Searches under equivalent names, exact equations, finite-field counts, and nonreduced/infinitesimal terminology found no dominating or identical statement.

## Limitations

Only this natural three-dimensional skew-nilpotent associative algebra is treated. The weight is fixed in each fiber of the parameter family; no claim is made about a joint total space over the weight line.

The motivic identities concern the **reduced** variety; Grothendieck classes of usual varieties do not record nilpotent scheme structure. Rational-point counts also cannot see nonreduced directions.

The primary literature already classifies complex-valued Rota–Baxter operators; that portion is not new. The originality analysis cannot rule out an equivalent scheme calculation under a different name for the augmentation ideal. Self-review is not independent certification.

## References

1. N. G. Abdujabborov, I. A. Karimjanov, and M. A. Kodirova, “Rota-type operators on 3-dimensional nilpotent associative algebras,” *Communications in Mathematics* 29 (2021), 227–241, DOI `10.2478/cm-2021-0020`, first publicly issued 15 July 2021.
2. P. Benito, V. Gubarev, and A. Pozhidaev, “Rota–Baxter Operators on Quadratic Algebras,” *Mediterranean Journal of Mathematics* (2018), DOI `10.1007/s00009-018-1234-5`, especially the unital Grassmann-algebra sections.
3. A. Das and S. K. Mishra, “The \(L_\infty\)-deformations of associative Rota–Baxter algebras and homotopy Rota–Baxter operators,” arXiv:2008.11076v1.
