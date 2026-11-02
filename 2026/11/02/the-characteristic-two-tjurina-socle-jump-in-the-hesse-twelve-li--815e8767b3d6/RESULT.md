# The characteristic-two Tjurina socle jump in the Hesse twelve-line arrangement

## Finding

Let \(k\) be an algebraically closed field of characteristic \(p\ne3\), allowing \(p=0\). Let \(\varepsilon\in k\) be a primitive third root of unity. In \(\mathbb P^2_k\), take the **Hesse twelve-line arrangement** \(D\), with lines whose coefficient triples are
\[
\begin{gathered}
(1,0,0),(0,1,0),(0,0,1),\\
(1,1,1),(1,\varepsilon,\varepsilon^2),(1,\varepsilon^2,\varepsilon),\\
(\varepsilon,1,1),(1,\varepsilon,1),(1,1,\varepsilon),\\
(\varepsilon^2,1,1),(1,\varepsilon^2,1),(1,1,\varepsilon^2).
\end{gathered}
\]
Write \(F\) for the product of these twelve linear forms, and define the **intrinsic Tjurina singular scheme**
\[
\Sigma(D)=V(F,F_X,F_Y,F_Z)\subset\mathbb P^2_k.
\]
The equation \(F=0\) is intentionally included: in characteristics dividing twelve, the gradient ideal alone need not be the intrinsic singular scheme.

**Theorem.** For every such \(k\), the scheme \(\Sigma(D)\) has length \(93\), supported at nine ordinary four-line intersections and twelve transverse double intersections. Each double intersection contributes length one. At each four-line intersection, the completed local Tjurina algebra has length nine and Hilbert function \((1,2,3,2,1)\), independent of characteristic. Nevertheless, its socle dimension is exactly two if \(p=2\), and exactly one otherwise. More precisely, it is isomorphic to
\[
\begin{cases}
k[[u,v]]/(u^3,u^2v,v^4),&p=2,\\
k[[u,v]]/(u^2v,u^3+4v^3),&p\ne2,3.
\end{cases}
\]
Consequently, \(\Sigma(D)\) is locally a complete intersection **if and only if** \(p\ne2,3\) (within the family \(p\ne3\)). The characteristic-two reduction preserves every incidence count, the total Tjurina length, and even every local Hilbert function, while destroying the Gorenstein property at exactly nine points.

## Assumptions and scope

All statements concern the reduced twelve-line divisor with the displayed coefficientwise equations after base change to \(k\), and the intrinsic singular scheme defined by the hypersurface and all its partial derivatives. The ground field is algebraically closed, and characteristic three is excluded because the three cube roots of unity coincide. No assertion is made about the gradient-only ideal in characteristic two, or about logarithmic freeness in that characteristic.

## Proof

**1. Incidence is stable away from characteristic three.** Work first in the Eisenstein integers \(\mathbb Z[\varepsilon]\), using \(\varepsilon^2+\varepsilon+1=0\). For the \(\binom{12}{3}=220\) unordered triples of the twelve coefficient vectors, calculate the determinant \(\delta\) and the integer norm \(N(\delta)=\delta\bar\delta\). The exhaustive histogram is
\[
\begin{array}{c|rrrrr}
N(\delta)&0&1&3&9&27\\\hline
\#&36&28&81&72&3.
\end{array}
\]
Every nonzero norm is a power of three. If a determinant vanished after specialization to a field of characteristic other than three, its norm would vanish there too, which is impossible. Thus the complete concurrency pattern is preserved, including characteristic two. The nine distinct base points of the Hesse pencil, obtained by setting one coordinate to zero and solving the other two cubes to sum to zero, each lie on exactly four of the listed lines. Their nine sets of \(\binom43=4\) concurrent triples exhaust the 36 zero determinants. As there are 66 pairs of lines, the remaining \(66-9\binom42=12\) intersections are ordinary nodes. The argument also ensures that the twelve lines remain distinct.

**2. Uniform local model.** The nine fourfold points are permuted transitively by coordinate permutations and diagonal cube-root scalings preserving the pencil. Consider \(P=(1:-1:0)\). Its four lines are \(Z=0\) and \(X+Y+\varepsilon^j Z=0\) for \(j=0,1,2\). In the affine chart \(X=1\), put \(u=Y+1\) and \(v=Z\). After dividing the local equation of \(D\) by a unit, its germ is
\[
f=v\prod_{j=0}^2(u+\varepsilon^jv)=v(u^3+v^3).
\]
Multiplication of a reduced equation by a unit does not change the ideal \((f,f_u,f_v)\). Hence this model describes the completed Tjurina algebra at every fourfold point.

**3. The characteristic-two algebra.** In characteristic two the derivatives are \(f_u=u^2v\), \(f_v=u^3\), and therefore
\[
(f,f_u,f_v)=(u^3,u^2v,v^4).
\]
The quotient has basis \(1,v,v^2,v^3,u,uv,uv^2,uv^3,u^2\), length nine, graded Hilbert function \((1,2,3,2,1)\), and socle with basis \(u^2,uv^3\). A zero-dimensional local complete intersection is Gorenstein, but this algebra has two-dimensional socle; hence it is not a local complete intersection.

**4. All other permitted characteristics.** When \(p\ne2,3\), the Euler identity \(4f=u f_u+v f_v\) makes \(f\) redundant in the Tjurina ideal, and the nonzero constants three and four can be divided out:
\[
(f,f_u,f_v)=(u^2v,u^3+4v^3).
\]
These two cubic forms have no common projective zero, so they constitute a homogeneous regular sequence. The quotient is a length-nine Artin complete intersection, whose Hilbert series is \((1-t^3)^2/(1-t)^2\) and whose socle dimension is one. This proves the claimed Hilbert function and the Gorenstein property.

**5. The global scheme.** At an ordinary transverse node, the local equation is a unit times \(uv\), so the Tjurina algebra has length one and is a complete intersection in every characteristic. The 21 support points are pairwise distinct by Step 1. The total length is \(9\cdot9+12\cdot1=93\), and local complete-intersection failure occurs precisely at the nine fourfold points in characteristic two.

## Verification

The companion `verify_hesse.py` script is executable with the Python standard library alone. It recomputes all 220 Eisenstein determinants and their norm histogram; independently forms the twelve lines and enumerates their 21 crossings over \(\mathbb F_4\) and \(\mathbb F_7\); checks the nine monomial normal forms and Hilbert functions; and computes the common kernels of multiplication by \(u\) and \(v\) on the Artin algebras in characteristic two and several odd characteristics. Its expected final line is `VERIFY_OK`. The infinite-characteristic assertion follows from Steps 1–5, not the finite-field examples.

## Relationship to prior work

Artebani and Dolgachev describe the Hesse pencil, its nine base points, twelve lines, and four triangular fibers [1]. Vallès proves characteristic-zero freeness results for unions of singular pencil members and explicitly identifies the twelve-line Hesse arrangement as a free divisor; local complete intersection of the Jacobian scheme is central to his criterion [2]. These geometric and characteristic-zero facts are not presented here as new. The result isolates the positive-characteristic local-algebra boundary: in characteristic two the intrinsic Tjurina scheme retains all numerical data but acquires a non-Gorenstein socle. The characteristic-zero freeness theorem is not asserted to extend or fail as a theorem in positive characteristic; only its local complete-intersection premise is evaluated. Later work on arithmetic Hesse pencils [3] studies Galois representations on elliptic three-torsion, not the Tjurina local algebra of the twelve-line union.

## Limitations

This is an explicit calculation for the Hesse arrangement, not a classification of all arrangements with fourfold points. The projective gradient-only scheme in characteristic two is not identified here, and no statement is made for characteristic three. The literature-priority comparison is limited to inspected sources and available searchable records; an unindexed positive-characteristic Jacobian computation could overlap. No independent scientific audit has been performed.

## References

[1] M. Artebani and I. Dolgachev, *The Hesse pencil of plane cubic curves*, first arXiv submission 2006-11-19, arXiv:math/0611590, https://arxiv.org/abs/math/0611590.

[2] J. Vallès, *Free divisors in a pencil of curves*, first arXiv submission 2015-02-09, arXiv:1502.02416, https://arxiv.org/abs/1502.02416.

[3] A. S. I. Anema, J. Top and A. Tuijp, *Hesse Pencils and 3-Torsion Structures*, first arXiv submission 2017-08-31, arXiv:1708.09745, https://arxiv.org/abs/1708.09745.
