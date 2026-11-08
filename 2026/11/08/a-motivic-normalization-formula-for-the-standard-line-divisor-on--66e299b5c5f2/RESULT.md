# A motivic normalization formula for the standard-line divisor on Fermat surfaces

## Finding

For every field \(k\) of characteristic different from \(2\), every integer \(d\geq3\) invertible in \(k\), and the Fermat surface
\[
X_d:\;X_0^d+X_1^d+X_2^d+X_3^d=0\subset\mathbf P^3_k,
\]
let \(E=\operatorname{Spec}k[t]/(t^d+1)\). Let \(B_d\) be the reduced union of the \(3d^2\) **standard coordinate-pairing lines**: for each of the three partitions of \(\{0,1,2,3\}\) into two pairs, take every line obtained by equating the coordinates in each pair with a scalar from \(E\). Then \(B_d\) has exactly \(6d\) ordinary \(d\)-fold points and \(3d^3\) ordinary nodes over an algebraic closure, and no other singular points. Its reduced multiplicity-\(d\) locus is a disjoint union of six copies of \(E\); its reduced node locus is a disjoint union of three copies of \(E^3\). These statements concern the reduced loci, **not** their nonreduced Jacobian singular schemes.

In the Grothendieck ring of \(k\)-varieties, with \(\mathbb L=[\mathbf A^1_k]\), one has the identity
\[
\boxed{[B_d]=3\mathbb L[E^2]-3[E^2]+6[E]-3[E^3].}
\]
All products of finite schemes here are fiber products over \(k\).

For \(k=\mathbb F_q\), write \(Q=q^n\) and \(s_n=\#\{t\in\mathbb F_Q:t^d=-1\}\). For **every** \(n\geq1\), the number of \(\mathbb F_Q\)-points lying on exactly \(j\) *geometric standard lines* is
\[
\boxed{N_1=3s_n^2(Q-1-2s_n),\quad N_2=3s_n^3,\quad N_d=6s_n,}
\]
with all other positive multiplicities absent. Thus
\[
\boxed{\#B_d(\mathbb F_Q)=3s_n^2Q-3s_n^2+6s_n-3s_n^3.}
\]
If \(g_n=\gcd(d,Q-1)\), then \(s_n=g_n\) if \((Q-1)/g_n\) is even and \(s_n=0\) otherwise. In particular, \(B_d(\mathbb F_Q)\) is empty precisely when \(-1\) is not a \(d\)-th power in \(\mathbb F_Q\).

For the Hasse–Weil zeta function, writing \(Z(Y,T)=\exp(\sum_{n\geq1}\#Y(\mathbb F_{q^n})T^n/n)\), one has the finite-étale factorization
\[
\boxed{Z(B_d,T)=\frac{Z(E^2,qT)^3Z(E,T)^6}{Z(E^2,T)^3Z(E^3,T)^3}.}
\]
The formula is computable from the finite Frobenius permutation on the roots of \(t^d+1\) and does not require computing the zeta function of the ambient Fermat surface.

## Assumptions and scope

The characteristic is odd and does not divide \(d\). The surface is then smooth, and \(E\) is finite étale of degree \(d\). The divisor \(B_d\) is explicitly the reduced union of the \(3d^2\) coordinate-pairing lines. It need not coincide with the union of **all** geometric lines on the Fermat surface in special positive characteristics; no such equality is assumed. Geometric incidences are counted over an algebraic closure, even when a component line is not defined over the ground field. The Grothendieck-ring assertion is valid over arbitrary fields satisfying the assumptions; point counts and zeta function require a finite field.

## Proof

**1. Components and normalization.** Put \(R=\{a\in\overline{k}:a^d=-1\}\). For example, for the pairing \((01)(23)\), define
\[
L^{01|23}_{a,b}=\{X_0=aX_1,\;X_2=bX_3\}\qquad(a,b\in R).
\]
The other two families are obtained by pairing \((02)(13)\) and \((03)(12)\). Every such line lies on \(X_d\). The lines are distinct, and all are smooth. Their disjoint parameter space is \(\coprod_3 E^2\). A simultaneous parameterization \(([u:v],a,b)\mapsto[au:u:bv:v]\), and the analogous parameterizations for the other pairings, identify the normalization \(\widetilde B_d\) with \(\coprod_3(E^2\times\mathbf P^1)\).

**2. Same-family intersections.** Two lines of the displayed pairing meet precisely when they have the same first parameter or the same second parameter. The common point is respectively \([a:1:0:0]\) or \([0:0:b:1]\). Thus each family has two disjoint kinds of high-multiplicity points, indexed by \(E\), and exactly \(d\) component lines through each. The other pairing families do not meet these points. Across all three families, the reduced high-multiplicity support is six copies of \(E\), and its inverse image in \(\widetilde B_d\) is six copies of \(E^2\).

**3. Different-family intersections.** Take an \((01)(23)\)-line with parameters \((a,b)\), and an \((02)(13)\)-line with parameters \((c,e)\). They intersect if and only if \(ae=bc\); when they do, their unique intersection point is
\[
[ae:e:b:1],\qquad c=ae/b.
\]
For each \((a,b,e)\in E^3\) this defines a unique pair of meeting lines, because \((ae/b)^d=-1\). Conversely every cross-family intersection is of this form. Each coordinate is nonzero. The third pairing family cannot contain the point: its required ratio \(X_0/X_3=ae\) has \(d\)-th power \(+1\), not \(-1\), because \(\operatorname{char}k\ne2\). Thus the points are ordinary double points. There are three unordered pairs of pairing families, so their reduced support is three copies of \(E^3\); its normalization preimage is six copies of \(E^3\). No cross-family point equals a same-family point. This exhausts all intersections.

**4. Local type.** At any intersection the lines are distinct smooth branches inside the smooth surface \(X_d\), and distinct projective lines through a point have different tangent directions. Hence each same-family intersection is an ordinary \(d\)-fold point and each cross-family intersection an ordinary node, also in positive odd characteristic prime to \(d\).

**5. Scissor identity.** Let \(S\) denote the reduced finite singular support. The normalization is an isomorphism over the complement of \(S\). Its inverse image of the high-multiplicity support is \(6E^2\), while the support itself is \(6E\). Its inverse image of the node support is \(6E^3\), while the support itself is \(3E^3\). Scissors therefore give
\[
[B_d]=3(\mathbb L+1)[E^2]-6[E^2]+6[E]-6[E^3]+3[E^3],
\]
which simplifies to the claimed identity. In particular it is **not** legitimate over a nonsplit field to replace \(6[E^2]-6[E]\) by \(6(d-1)[E]\): that replacement forgets nonrational branches above rational multiple points.

**6. Arithmetic and zeta.** For any finite extension \(\mathbb F_Q\), \(\#E(\mathbb F_Q)=s_n\), \(\#E^j(\mathbb F_Q)=s_n^j\), and \(\#\mathbf A^1(\mathbb F_Q)=Q\). Point counting applied to the scissor identity yields the total count. The reduced high and node strata contribute respectively \(6s_n\) and \(3s_n^3\) rational points. All remaining rational points lie on exactly one geometric standard line, giving \(N_1\). Finally the zeta identity follows by exponentiating the point-count identity for all \(n\), using the definition of \(Z\). The explicit expression for \(s_n\) is the standard cyclic-group solvability criterion for \(t^d=-1\) in \(\mathbb F_Q^\times\).

## Verification

The accompanying `verify.py` independently enumerates every normalized projective point over each of the eight odd prime fields \(\mathbb F_3,\mathbb F_5,\ldots,\mathbb F_{23}\) listed in the script, for all degrees \(3\leq d\leq8\) coprime to the characteristic. It tests the three pairing equations directly, including the high-multiplicity cases where two coordinates vanish; it compares every observed positive incidence count with the closed formulas. All 44 admissible prime-degree cases pass. These finite checks are supporting evidence only; Steps 1–6 prove the claim for every admissible field and all finite extensions.

## Relationship to prior work

The line equations and intersection criteria are classical and appear in Schütt–Shioda–van Luijk, *Lines on Fermat surfaces* (2009/2010), and in Andria–Rojas–Mangueira, *Maximal number of skew lines on Fermat surfaces* (first public preprint March 23, 2024, Proposition 1.2). Salberger, *Counting rational points on projective varieties* (2023), identifies the union of the coordinate-pairing lines as an auxiliary divisor. These prior statements give the geometric building blocks, **not** the finite-étale singular-stratum identifications, general Grothendieck-ring formula, or all-extension arithmetic incidence spectrum displayed above. Previously available small-degree point counts (including the Fermat cubic and split Fermat quartic) are subsumed and are not separately claimed as new.

## Limitations

The claim concerns the standard \(3d^2\) lines only; extra lines may exist in exceptional characteristics. Characteristic two and characteristics dividing \(d\) are excluded. The equality of Grothendieck classes is a scissors calculation, not an isomorphism of \(B_d\) with a disjoint union of the displayed schemes. Ordinary multiple points have nonreduced Jacobian singular schemes when \(d>2\); only the reduced singular support is identified. No full zeta function for \(X_d\) is asserted. The exact motivic identity has not been independently audited, and an unlocated equivalent older computation remains possible.

## References

1. S. Andria, J. Rojas, W. Mangueira, *Maximal number of skew lines on Fermat surfaces*, arXiv:2403.15666 (initial public preprint March 23, 2024), especially §1 and Proposition 1.2.
2. M. Schütt, T. Shioda, R. van Luijk, *Lines on Fermat surfaces*, arXiv:0812.2377 (2008; journal 2010), especially the standard line construction and pairwise intersection framework.
3. P. Salberger, *Counting rational points on projective varieties*, Proc. London Math. Soc. (2023), §9, DOI:10.1112/plms.12508.
