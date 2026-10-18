# Complete Kodaira-fiber stratification of the conic-line cubic pencil

## Finding
Work over \(\mathbb C\). For every parameter \(a\) satisfying \(a\ne0,1\) and \(a^2-a+1\ne0\), let \(S_a\to\mathbb P^1\) be obtained by blowing up the nine base points of the plane cubic pencil
\[
C_{a,t}:\quad (x-ay)(x^2+y^2-z^2)+t(x-y)(x^2-xy+y^2-z^2)=0,
\qquad t\in\mathbb P^1.
\]
Write \(I_n\), \(II\), and \(III\) for standard Kodaira fiber types. Define three disjoint finite subsets of the allowed \(a\)-line:
\[
\begin{aligned}
T&=\{a:a^2+1=0\}\cup\{2,\tfrac12\},\\
R&=\{a:(4a^2-12a+7)(7a^2-12a+4)=0\},\\
K&=\{a:71a^2-196a+71=0\}.
\end{aligned}
\]
The complete singular-fiber classification is
\[
\begin{array}{c|c}
\text{Parameter class}&\text{Singular-fiber basket}\\\hline
 a\notin T\cup R\cup K&4I_2+4I_1\\
 a\in T&III+3I_2+3I_1\\
 a\in R&I_3+3I_2+3I_1\\
 a\in K&II+4I_2+2I_1.
\end{array}
\]
All entries count geometric fibers (not just plane-curve factorization types). On \(T\), a line and conic become tangent; on \(R\), a conic splits to make a triangle; and on \(K\), two ordinary nodal fibers coalesce into one irreducible cuspidal fiber.

## Assumptions and scope
The source of the pencil is Suluyer's four-conic-line-member construction. We restrict to parameters with nine distinct simple base points; no assertion is made at \(a=0,1\) or \(a^2-a+1=0\). The parameter at infinity \(t=\infty\) means the second generating cubic. The ground field is algebraically closed of characteristic zero. The surfaces are relatively minimal rational elliptic surfaces with sections; no claim concerns their Mordell–Weil groups or isomorphism classes.

## Proof
**1. Base scheme and fibration.** Let the generating members be \(L_1Q_1\) and \(L_2Q_2\), with \(L_1=x-ay\), \(L_2=x-y\), \(Q_1=x^2+y^2-z^2\), and \(Q_2=x^2-xy+y^2-z^2\). Their nine intersections are
\[
[0:0:1],\ [a:1:\pm\sqrt{a^2-a+1}],\ [1:1:\pm\sqrt2],\ [0:1:\pm1],\ [1:0:\pm1].
\]
They are distinct on the stated domain; Bézout implies that all intersections are transverse. Blowing them up yields a smooth rational surface with \(K^2=9-9=0\), fiber class \(3H-\sum E_i=-K\), and nine exceptional sections. Every component of each reducible fiber is a rational curve of self-intersection \(-2\) (a line goes through three base points; a conic through six). The pencil is thus a relatively minimal genus-one fibration with section. Its topological Euler characteristic is \(12\).

**2. Exact discriminant.** On the chart \(y=1\) put \(u=x/y\), \(v=z/y\). For finite \(t\) the cubic becomes
\[
P(u)-v^2L(u)=0,\quad
P=(u-a)(u^2+1)+t(u-1)(u^2-u+1),\quad
L=(1+t)u-(a+t).
\]
The birational double-cover model is \(w^2=P(u)L(u)\), with \(w=vL(u)\). Exact polynomial identities over \(\mathbb Z[a,t]\) give
\[
\operatorname{Res}_u(P,L)=t(a-1)(a+t)(t+1)
\]
and
\[
\operatorname{Disc}_u(PL)=-t^2(a-1)^2(t+a)^2(t+1)^2D_a(t),
\]
where
\[
\begin{aligned}
D_a(t)={}&3t^4+(10a+10)t^3+(59a^2-70a+59)t^2\\
&+(28a^3-4a^2-4a+28)t+4(a^2+1)^2.
\end{aligned}
\]
The quartic is \(-\operatorname{Disc}_u(P)\), and its leading coefficient is \(3\). The only potentially singular values away from the four reducible members \(t=0,-1,-a,\infty\) are therefore the roots of \(D_a\). For such a value, \(\operatorname{Res}_u(P,L)\ne0\), so a double root of \(P\) produces exactly one ordinary node and a triple root produces a cusp. The plane chart \(y=0\) can only contribute the already-listed reducible member \(t=-1\): when \(t\ne-1\), the leading cubic coefficient of \(P\) is nonzero and the corresponding point at infinity of the hyperelliptic quartic is unramified/smooth. At the base point \([0:0:1]\), the two generators have independent differentials since \(a\ne1\), so each strict transform meets its exceptional section smoothly. Thus no additional singularities are omitted by this model.

**3. Collision formulas.** Direct calculation yields
\[
\begin{aligned}
D_a(0)&=4(a^2+1)^2,\\
D_a(-1)&=(a-2)^2(4a^2-12a+7),\\
D_a(-a)&=(2a-1)^2(7a^2-12a+4),\\
\operatorname{Disc}_t(D_a)&=512(a-1)^4(a^2-a+1)(71a^2-196a+71)^3.
\end{aligned}
\]
The resultant of any pair of distinct factors defining the excluded parameters and the sets \(T,R,K\) is nonzero, so these loci are disjoint. Moreover, each collision with \(t=0,-1,-a\) involves exactly one simple root of \(D_a\): \(\operatorname{Disc}_t(D_a)\ne0\) at \(a\in T\cup R\). Hence precisely three nodal fibers remain in those cases. Outside \(T\cup R\cup K\), the quartic has four distinct roots avoiding the reducible parameters, giving four \(I_1\) fibers.

**4. Reducible-fiber types.** The four distinguished cubics (at \(0,\infty,-1,-a\)) are respectively a line times a smooth conic, except that the last two conics may split. For \(t=0\), the conic is tangent to its line exactly when \(a^2+1=0\). For \(t=-1\), the conic is
\[
(2-a)x^2-xy+(1-a)y^2+(a-1)z^2=0,
\]
which meets \(y=0\) tangentially exactly when \(a=2\), and factors as two distinct lines exactly when \(4a^2-12a+7=0\). For \(t=-a\), the conic is
\[
(1-a)x^2+axy+(1-2a)y^2+(a-1)z^2=0,
\]
which is tangent to \(x=0\) exactly when \(a=\tfrac12\), and factors as two distinct lines exactly when \(7a^2-12a+4=0\). Each factored conic has its node away from the additional line, so the three distinct lines make a triangle. Thus every generic reducible member has type \(I_2\), every tangent case has type \(III\), and every triangular case has type \(I_3\).

**5. Cuspidal locus and completeness.** A cubic \(P=(1+t)u^3-(a+2t)u^2+(1+2t)u-(a+t)\) has a triple root only if
\[
(a+2t)^2-3(1+t)(1+2t)=0,\qquad
(a+2t)^3-27(1+t)^2(a+t)=0.
\]
Their resultant with respect to \(t\) is \(-27(a-2)^3(a-1)(71a^2-196a+71)\). The apparent factor at \(a=2\) corresponds to the already-listed reducible parameter \(t=-1\); the factor \(a=1\) is excluded. At either root of \(71a^2-196a+71\), substituting
\[
 a=\frac{98+39r}{71},\quad t_0=\frac{-52-12r}{71},\quad r\in\{\sqrt3,-\sqrt3\}
\]
gives \(P(u)=(1+t_0)(u+2+r)^3\) and \(L(-2-r)\ne0\). Hence \(C_{a,t_0}\) has exactly an ordinary cusp (Kodaira \(II\)), and \(D_a\) has exactly a double root there and two other simple roots. All cases are exhausted by the discriminant factorization. The Euler-number sum in each row is \(12\), providing an independent global completeness consistency check. \(\square\)

## Verification
The standalone script `kodaira_suluyer_checker.py` uses exact polynomial arithmetic in SymPy to verify the discriminant, resultants, pairwise separation of parameter loci, and cubic triple-root specializations. It prints `SULUYER_KODAIRA_DISCRIMINANT_EXACT_OK` on success. Its symbolic identities hold for indeterminates; classification of the analytic singularities and fibers is established by the geometric argument above, not finite sampling.

## Relationship to prior work
Suluyer constructs the family and proves that it has four conic-line members; Example 4.2 treats the specialization \(a=2\) and identifies three remaining nodal fibers. The present result classifies all singular fibers for every simple-basepoint parameter and locates all exceptional parameter values algebraically. Kodaira's singular-fiber classification and Miranda's elliptic-surface framework are standard prior results. Persson's catalog includes possible fiber configurations abstractly; the point here is the complete parameter stratification for this explicit family. No claim is made to those general techniques or to the four initial reducible cubics.

## Limitations
Only the nine-distinct-basepoint locus is treated. The 2024 thesis cited by Suluyer is bibliographically relevant; its full text could not be checked, so possible earlier overlap and earlier presentation of the particular cubic family remain residual risks. The first verified public date for the explicit pencil in an accessible primary abstract is the arXiv submission of 9 December 2024, not the May 2026 journal date. The theorem gives geometric fiber types, not arithmetic reduction types or a classification of all rational elliptic surfaces.

## References
1. H. Suluyer, *Pencils of Conic-Line Curves*, arXiv:2412.06928, first posted 9 December 2024, https://arxiv.org/abs/2412.06928.
2. H. Suluyer, *On the Number of Conic-Line Curves in a Pencil*, Mediterr. J. Math. 23 (2026), article 127, https://doi.org/10.1007/s00009-026-03125-z, especially Section 4, Theorem 4.1 and Example 4.2.
3. H. Suluyer, *Classification Problems of Multinets and Conic-Line Arrangements*, PhD thesis, Middle East Technical University (2024), https://hdl.handle.net/11511/110938; full text not inspected.
4. R. Miranda, *The Basic Theory of Elliptic Surfaces*, ETS, Pisa (1989).
5. R. Miranda, *Persson's list of singular fibers for a rational elliptic surface*, Math. Z. 205 (1990), 191–211.
