# Four cusps and a genus-six Kummer normalization in characteristic three

## Finding
Let \(k\) be algebraically closed of characteristic \(3\). Consider Kawakita's plane sextic family
\[
 S_{a,b}:\quad x^6+y^6+z^6+a(x^4y^2+y^4z^2+z^4x^2)+b(x^2y^4+y^2z^4+z^2x^4)=0.
\]
For every \((a,b)\in k^2\) such that
\[
 a+b\ne0,\qquad a\ne b,\qquad (ab)^2-(a+b)^3\ne0,
\]
the curve \(S_{a,b}\) is geometrically integral and has exactly four geometric singular points
\[
 [1:\epsilon:\eta],\qquad \epsilon,\eta\in\{1,-1\}.
\]
Each is a unibranch ordinary cusp, with local semigroup \(\langle2,3\rangle\) and delta invariant \(1\). Its normalization is a smooth geometrically connected curve of genus \(6\), with a tame Galois map of group \((\mathbf Z/2\mathbf Z)^2\) to \(\mathbf P^1_k\), branched at nine distinct points in three groups of three, each of inertia order \(2\). If \(a,b\) belong to \(\mathbf F_{3^m}\), then for every \(r\ge1\), the normalization and the singular plane sextic have the same number of \(\mathbf F_{3^{mr}}\)-rational points.

## Assumptions and scope
The inequalities define a nonempty Zariski-open parameter space; the theorem applies to every geometric parameter on it, not just general parameters, and to any algebraically closed field of characteristic three. The last displayed point-count equality requires parameters over the stated finite field. We study the literal reduction of the displayed integral sextic equation, not a stable reduction of a characteristic-zero curve. Parameters violating the three inequalities are outside the classification, and no general assertion is made for those boundary strata.

## Proof
**1. The cubic quotient.** In characteristic three, set \(X=x^2\), \(Y=y^2\), \(Z=z^2\). Then the sextic is exactly the inverse image under the degree-four coordinate squaring map \(\pi:\mathbf P^2\to\mathbf P^2\) of
\[
G_{a,b}:\ X^3+Y^3+Z^3+a(X^2Y+Y^2Z+Z^2X)+b(XY^2+YZ^2+ZX^2)=0.
\]
Away from the coordinate triangle, \(\pi\) is a finite etale Galois map with group \((\mathbf Z/2\mathbf Z)^2\).

**2. The cubic is integral with one ordinary cusp.** The point \(P=[1:1:1]\) lies on \(G_{a,b}\). In the affine chart \(Z=1\), write \(X=1+t\), \(Y=1+w-t\). Direct expansion in characteristic three gives the exact local equation
\[
G_{a,b}=(a+b)w^2+(b-a)t^3+(a+b)t^2w+btw^2+w^3.
\]
The tangent cone is \((a+b)w^2\), and the coefficient of \(t^3\) is nonzero. Weierstrass preparation in \(w\), followed by completing the square (permitted since \(2\) is invertible), gives a quadratic equation with discriminant of \(t\)-adic order exactly three. Thus the completed local ring has normalization parameter with valuations \(2,3\), is unibranch, and has delta invariant one. More explicitly its analytic form is a unit times \(w'^2-t^3u(t)\), with \(u(0)\ne0\), and its square root can be absorbed into \(w'\).

This cusp also implies geometric irreducibility: if a plane cubic were reducible and singular with doubled tangent \(w=0\) at \(P\), a component line through \(P\) would have to be this tangent line (if another factor were itself singular, it would split into lines over \(k\)). But the restriction \(G_{a,b}|_{w=0}=(b-a)t^3\) is not identically zero. Since the arithmetic genus of a plane cubic is one and the cusp already contributes delta one, there are no other singularities; the smooth normalization is \(\mathbf P^1_k\).

**3. Transverse coordinate intersections.** On \(Z=0\), \(X=1\), the cubic cuts the axis in the roots of \(T^3+bT^2+aT+1\); on the other axes the corresponding cubic coefficients are cyclically permuted. In characteristic three the discriminant of either orientation is \((ab)^2-(a+b)^3\). The discriminant hypothesis makes each axis intersection consist of three distinct transverse geometric points. All coordinate vertices lie off the cubic (its value there is one), so the nine points are distinct and the cusp \(P\) lies off all axes.

**4. Connectedness and ramification.** On the normalization \(\widetilde G=\mathbf P^1_k\), adjoining \(\sqrt{X/Z}\) and \(\sqrt{Y/Z}\) gives the function field of the inverse-image curve. The square classes are independent: at any of the three points of \(\widetilde G\) lying over \(X=0\), the valuation of \(X/Z\) is odd and that of \(Y/Z\) is zero; likewise for \(Y=0\). This yields extension degree four and establishes geometric integrality of the sextic. At each of the three points over \(X=0\) only the first Kummer character ramifies, at each over \(Y=0\) only the second does, and over \(Z=0\) both have a common simple pole, giving one diagonal inertia character. There are nine branch points, each with inertia of order two. The entire extension is tame.

**5. Singularities and geometric genus.** The map \(\pi\) is etale at all four points above \(P\) (the coordinates are nonzero). Consequently the four inverse-image germs are exactly the four ordinary cusps displayed in the finding. Elsewhere away from the axes, the pullback of the smooth cubic is smooth; at the axes, transverse intersection with the branch divisor makes the Kummer pullback smooth. Thus there are no other geometric singularities. The arithmetic genus of the plane sextic is \((6-1)(6-2)/2=10\). Subtracting the four cusp delta invariants gives geometric genus \(6\). Independently Riemann--Hurwitz on the degree-four tame cover gives
\[
 2g-2=4(-2)+9\cdot 2=10,\qquad g=6.
\]

**6. Rational-point bijection.** The four singular points are defined over \(\mathbf F_3\). Each ordinary cusp is unibranch and its unique normalization point has the same residue field. At smooth points normalization is an isomorphism. Thus the normalization map is a bijection on rational points over every finite extension of every finite definition field for \(a,b\), proving the final statement.

## Verification
The included standalone `verify.py` computes the polynomial and all three partial derivatives using exact arithmetic in \(\mathbf F_3\) and \(\mathbf F_9\). For all four parameter pairs satisfying the hypotheses over \(\mathbf F_3\) and all 58 such pairs over \(\mathbf F_9\), its exhaustive projective-point enumeration finds precisely the four rational sign-point singularities. The observed sextic point-count distributions are \(\{4:2,10:2\}\) and \(\{4:16,10:10,16:22,22:4,28:6\}\), respectively. Its successful terminal output is `VERIFY_OK`. The computations check concrete examples and are not used to infer the general theorem; the symbolic cubic, Kummer and genus arguments above do the latter.

## Relationship to prior work
Kawakita introduced the sextic family in *Certain sextics with many rational points* (2017), and Iezzi--Kawakita--Timpanella (arXiv:2306.01928, June 2023) treated its genus-six and genus-ten arithmetic under their positive-characteristic assumptions, including the exclusion of characteristic three. Giulietti--Kawakita--Lia--Montanucci (arXiv:1805.06317) discussed a special symmetric Wiman sextic, which is reducible in characteristic three; the present hypotheses explicitly exclude its symmetric parameter locus. The current theorem instead classifies a nonempty nonsymmetric open family of characteristic-three reductions, identifying an integral four-cuspidal boundary and a genus-six normalization. It is not implied by the special symmetric reducibility statement or by results established only in characteristics at least five.

## Limitations
This is a statement for the indicated parameter open subset. It does not classify singularities when \(a+b=0\), \(a=b\), or \((ab)^2=(a+b)^3\), or supply the zeta functions of individual normalizations. The finite verification does not enumerate geometric points over an algebraic closure. The literature comparison may miss older, unpublished or unindexed characteristic-three computations; the precise earliest day of Kawakita's May 2017 online publication is not established by the cited page.

## References
1. M. Q. Kawakita, *Certain sextics with many rational points*, Advances in Mathematics of Communications **11** (2017), 289--292. DOI: https://doi.org/10.3934/amc.2017020 (published online May 2017; the source does not specify a day).
2. A. Iezzi, M. Q. Kawakita, M. Timpanella, *New sextics of genus 6 and 10 attaining the Serre bound*, arXiv:2306.01928v1, first posted 2023-06-02, https://arxiv.org/abs/2306.01928.
3. M. Giulietti, M. Q. Kawakita, M. Lia, M. Montanucci, *An \(\mathbf F_{p^2}\)-maximal Wiman's sextic and its automorphisms*, arXiv:1805.06317v1, first posted 2018-05-15, https://arxiv.org/abs/1805.06317, especially Remark 3.1.
