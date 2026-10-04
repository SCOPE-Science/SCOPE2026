# Sharp smooth Zariski-pair radius and nodal boundary in Example 6.2
## Finding
Let \(E_{{j,s}}\subset\mathbb P^2\) be the projective closures of the affine cubics \(u_{{j,s}}(t,x)=0\) printed in Example 6.2 of Bannai--Kawana--Masuya--Tokunaga. Their singular parameter sets are exactly
\[
\Sigma_1=\left\{{0,84,-\frac12,-\frac1{{10}},-\frac1{{20}}}}\right\},\qquad
\Sigma_2=\left\{{0,14,-18,-\frac25,-\frac9{{20}}}}\right\}.
\]
At \(s=0\), both cubics equal
\[
(x-9t+18)(x-8t+12)(x-5t+6)=0.
\]
Every member with nonzero parameter in \(\Sigma_j\) is an irreducible nodal cubic. In particular,
\[
E_{{1,-1/20}}
\]
has its unique singular point at
\[
(t,x)=\left(\frac{{31}}{{10}},\frac{{45}}{{4}}\right),
\]
and the determinant of its affine Hessian there is \(369/25\neq0\).

The source proves only that there exists some sufficiently small \(\varepsilon>0\) for which its conditions (a)--(c) hold whenever \(0<|s|<\varepsilon\). For the printed families the largest centered disk with this property is explicit:
\[
0<|s|<\frac1{{20}}.
\]
The radius is sharp because condition (a), smoothness, fails at the boundary value \(s=-1/20\).

## Assumptions and scope
The ground field is \(\mathbb C\). Coordinates and the two polynomials \(u_{{1,s}},u_{{2,s}}\) are exactly those of Example 6.2 in arXiv:2103.07639v1. The line called \(L_1\) in that example is \(x=0\), and the quartic is \(Q=C_1+C_2\) with
\[
C_1:x-t^2=0,\qquad C_2:x^2-10tx+25x-36=0.
\]
The three source conditions are: (a) both cubics are smooth; (b) each meets \(L_1\) in three distinct points; (c) each is tangent to \(Q\) at six distinct points. The claim concerns only these printed one-parameter families; it does not classify all deformations of the limiting arrangement.

## Proof
The homogeneous degree-three parts of both \(u_{{j,s}}\) are independent of \(s\) and equal
\[
(x-5t)(x-8t)(x-9t),
\]
so the three points at infinity are distinct and nonsingular for every parameter. Hence singularity can be tested in the affine chart by \(u=u_x=u_t=0\).

Exact lexicographic elimination of \(\langle u_{{1,s}},(u_{{1,s}})_x,(u_{{1,s}})_t\rangle\) contains
\[
s^2(s-84)^2(2s+1)(10s+1)(20s+1),
\]
and the corresponding elimination for \(u_{{2,s}}\) contains
\[
s^2(s-14)^2(s+18)(5s+2)(20s+9).
\]
For every root in these two sets, substitution gives an affine singular point. At \(s=0\) the common fiber factors as the displayed triangle. For the nonzero parameters the reduced fixed-parameter Gröbner bases are respectively
\[
\begin{{array}}{{c|c}}
s & (t,x)\\\hline
84&(-1,1)\\
-1/2&(11/2,27)\\
-1/10&(19/10,1)\\
-1/20&(31/10,45/4)
\end{{array}}
\qquad
\begin{{array}}{{c|c}}
s & (t,x)\\\hline
14&(-1,1)\\
-18&(3,-3)\\
-2/5&(13/5,7)\\
-9/20&(12/5,21/4).
\end{{array}}
\]
Each basis has one linear equation in \(t\) and one in \(x\), so the singular point is unique. The affine Hessian determinants at these eight points are
\[
-2225808,-468,-\frac{{1044}}{{25}},\frac{{369}}{{25}},
-6528,-1728,\frac{{96}}{{25}},-\frac{{459}}{{100}},
\]
all nonzero. Thus every nonzero singular member has an ordinary node. A reducible cubic with a unique singular point would have to be a line plus a conic meeting only at that point; Bézout then forces tangency there, contradicting the nondegenerate quadratic tangent cone. Hence all eight are irreducible nodal cubics.

For condition (b), substituting \(x=0\) gives cubic polynomials in \(t\) whose discriminants are
\[
6718464(80s^3-6431s^2-288s+36)
\]
and
\[
20736(5s-36)^2(s^2+18s+9).
\]
There is no intersection at the point at infinity of \(x=0\), because the leading form restricts there to \(-360t^3\neq0\).

For condition (c), restriction to \(C_1\) is a square:
\[
u_{{1,s}}(t,t^2)=(st-t^3+11t^2-36t+36)^2,
\]
\[
u_{{2,s}}(t,t^2)=(st-5s-t^3+11t^2-36t+36)^2.
\]
The discriminants of the square roots are
\[
4s^3-311s^2-288s+144,
\qquad
4(s^3+s^2+103s+36).
\]
Eliminating \(x\) against \(C_2\) gives
\[
-36(s^2-10st^2+37st-47s-10t^3+110t^2-360t+360)^2
\]
and
\[
-(6s^2+10st^2-63st+203s+60t^3-660t^2+2160t-2160)^2.
\]
The discriminants of the cubic square roots are
\[
40(s-10)^2(100s^3-980s^2+133s+360)
\]
and
\[
-20(s+60)^2(1200s^3+18235s^2-42924s-25920).
\]
The only possible overlaps between the \(C_1\)- and \(C_2\)-supports are the four points \(C_1\cap C_2\), with \(t=3,2,6,-1\). The first square root takes values \(3s,2s,6s,84-s\) there, and the second takes values \(-2s,-3s,s,-6(s-14)\). Hence there is no overlap for \(0<|s|<1/20\).

For \(C_2\), use the rational parametrization
\[
t=-\frac{q^2+27q-10}{q(q-10)},\qquad x=-\frac{36q}{q-10}.
\]
After clearing the cubic denominator, the two restrictions become
\[
-36\bigl(sq^3-10q^3-10sq^2+80q^2-170q+100\bigr)^2
\]
and
\[
-\bigl(sq^3+60q^3-20sq^2-480q^2+100sq+1020q-600\bigr)^2.
\]
Their cubic discriminants are
\[
4000(100s^3-980s^2+133s+360)
\]
and
\[
-72000(1200s^3+18235s^2-42924s-25920).
\]
The omitted parameter values \(q=0,10\) are never roots of these two cubics, and neither corresponding point at infinity lies on \(E_{{j,s}}\). Thus a nonzero discriminant gives three distinct points on \(C_2\), each with intersection multiplicity two. Together with the direct square restrictions on \(C_1\), and the no-overlap test above, this gives exactly six distinct tangencies to \(Q=C_1+C_2\).

It remains only to show that none of the displayed obstruction polynomials vanishes in \(0<|s|<1/20\). For every polynomial not already split into linear factors, Rouché's theorem on \(|s|=1/20\) applies with the constant term dominant. For example,
\[
\frac{{80}}{{20^3}}+\frac{{6431}}{{20^2}}+\frac{{288}}{{20}}<36,
\]
and the analogous exact inequalities for the other five cubic factors are replayed by the verifier. The split singular factors have no nonzero root of modulus below \(1/20\). Thus (a)--(c) hold throughout the punctured disk. At \(s=-1/20\), \(E_{{1,s}}\) has the node above, so no larger centered disk can work.

## Verification
Run `python artifacts/verify.py` with Python and SymPy. It reconstructs the two printed cubics, recomputes the two lexicographic elimination factors, checks every singular point and Hessian determinant, verifies the line-intersection and conic-intersection discriminants, checks the four possible cross-component overlaps, and verifies the exact Rouché inequalities at radius \(1/20\). The expected final line is `VERIFY_OK`.

## Relationship to prior work
Example 6.2 of Bannai--Kawana--Masuya--Tokunaga gives the two explicit cubic families and proves only that there exists a sufficiently small \(\varepsilon>0\) for which conditions (a)--(c) hold for \(0<|s|<\varepsilon\). The same source uses those conditions to obtain a family of Zariski pairs degenerating to one conic-line arrangement. The inspected preprint and searchable published copy do not give the singular parameter sets, classify their singular fibers, or determine a sharp centered value of \(\varepsilon\). Targeted searches for the exact formulas, parameter values, discriminant language, and equivalent smoothness-radius formulations found no covering result.

## Limitations
The calculation is specific to Example 6.2 and to the centered disk in its printed parameter \(s\). A nonlinear reparameterization changes the numerical radius. No claim is made about a maximal connected subset of the parameter line beyond the centered disk, nor about the topology of arrangements at every exceptional parameter outside that disk. Literature noncoverage is limited to the inspected and searched sources; an unindexed computation under different terminology remains a residual risk.

## References
1. S. Bannai, N. Kawana, R. Masuya, H. Tokunaga, *Trisections on Certain Rational Elliptic Surfaces and Families of Zariski Pairs Degenerating to the same Conic-line Arrangement*, arXiv:2103.07639v1, 13 March 2021; published in *Geometriae Dedicata* 216 (2022), Paper 8, DOI:10.1007/s10711-021-00672-5.
