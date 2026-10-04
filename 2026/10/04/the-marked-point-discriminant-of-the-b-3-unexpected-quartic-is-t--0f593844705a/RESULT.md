# The marked-point discriminant of the \(B_3\) unexpected quartic is the non-Fano arrangement
## Finding
Over \(\mathbb C\), let \(Q_B\subset\mathbb P^2\) be the \(B_3\) unexpected quartic of Dumnicki--Farnik--Harbourne--Malara--Szpond--Tutaj-Gasińska, with marked point \(B=[a:b:c]\) and the nine fixed points \(Z=\{[1:0:0],[0:1:0],[0:0:1],[1:\pm1:0],[1:0:\pm1],[0:1:\pm1]\}\). The reduced parameter locus where the cubic tangent cone of \(Q_B\) at \(B\) is nonreduced is exactly the seven-line arrangement \(\Delta_{\mathrm{red}}=V(abc(a+b+c)(a+b-c)(a-b+c)(-a+b+c))\). This is the non-Fano arrangement: it has six triple and three double intersection points, and those nine singular points are exactly \(Z\). If \(B\notin\Delta_{\mathrm{red}}\), then \(B\) is an ordinary triple point of \(Q_B\). At a smooth point of one of the three coordinate components of \(\Delta_{\mathrm{red}}\), the tangent cone is a triple line; at a smooth point of one of the four remaining components, it is a double line plus a distinct simple line. At every \(B\in Z\), the cubic tangent term vanishes, the multiplicity jumps to four, and \(Q_B\) is a union of four distinct concurrent lines, so \(B\) is an ordinary quadruple point.

## Assumptions and scope
Work over \(\mathbb C\). The family is the explicit bihomogeneous family from the cited source,
\[
Q_B(x,y,z)=3a(b^2-c^2)x^2yz+3b(c^2-a^2)xy^2z+3c(a^2-b^2)xyz^2
+a^3y^3z-a^3yz^3+b^3xz^3-b^3x^3z+c^3x^3y-c^3xy^3.
\]
The claim concerns only the singularity at the marked point \(B=[a:b:c]\) as \(B\) varies in parameter space. It does not classify other singularities of each quartic.

## Proof
On the affine parameter chart \(c=1\), write \(B=[a:b:1]\) and use local curve coordinates \(x=a+u\), \(y=b+v\), \(z=1\). Direct expansion gives no terms of total degree below three and gives
\[
T_3=-(bu-av)^3+bu^3-av^3,
\]
while the degree-four term is
\[
T_4=uv(u-v)(u+v).
\]
The discriminant of the binary cubic \(T_3\), after setting \(u=1\), factors as
\[
-27a^2b^2(a-b-1)(a-b+1)(a+b-1)(a+b+1).
\]
The analogous exact calculations on the charts \(a=1\) and \(b=1\) give the cyclically corresponding factorizations. Hence the reduced global locus of repeated tangent directions is
\[
\Delta_{\mathrm{{red}}}=V\!\left(abc(a+b+c)(a+b-c)(a-b+c)(-a+b+c)\right).
\]

The factorization of \(T_3\) determines the generic type on each component. For example, on \(a=0\) in the chart \(c=1\),
\[
T_3=-b(b-1)(b+1)u^3,
\]
so away from component intersections the tangent cone is a triple line. On \(a+b+1=0\),
\[
T_3=a(a+1)(u+v)^2(au+av+2u-v),
\]
so away from component intersections it is a double line plus a distinct simple line. The other components follow by the displayed symmetric factorizations verified in the checker.

The seven parameter lines have precisely six triple and three double intersection points. Exact projective intersection enumeration gives
\[
\{[1:0:0],[0:1:0],[0:0:1],[1:\pm1:0],[1:0:\pm1],[0:1:\pm1]\},
\]
which is exactly the source configuration \(Z\). A seven-line arrangement with six triple and three double points is the non-Fano arrangement. At each of these nine points the cubic term \(T_3\) vanishes identically. The first nonzero local term is degree four and splits into four distinct linear factors; for example, at \(B=[0:0:1]\),
\[
Q_B=xy(x-y)(x+y).
\]
Since \(Q_B\) has degree four, multiplicity four at \(B\) forces the whole curve to be the union of those four distinct lines through \(B\). Thus each such marked point is an ordinary quadruple point.

## Verification
The accompanying exact symbolic checker reconstructs \(Q_B\), verifies the vanishing of all local terms of degree below three, computes the three affine-chart discriminants, checks the componentwise tangent-cone factorizations, enumerates all intersections of the seven parameter lines, identifies them with the nine source points, and verifies a squarefree product of four linear factors at every one of the nine multiplicity-four specializations. It returns `VERIFY_OK`.

## Relationship to prior work
Dumnicki, Farnik, Harbourne, Malara, Szpond, and Tutaj-Gasińska give the displayed \(B_3\) quartic family, the nine fixed points, and BMSS duality: the marked quartic and the swapped cubic have the same tangent cone at the marked point. Their accessible full text does not state the parameter discriminant, its non-Fano identification, the triple-line versus double-plus-simple stratification, or the multiplicity-four specializations. Farnik, Galuppi, Sodomaco, and Trok prove that the nine-point configuration is, up to projective equivalence, the unique configuration admitting an unexpected quartic, but the inspected article does not supply this marked-point degeneration stratification. Standard line-arrangement literature identifies a seven-line arrangement with six triple and three double points as the non-Fano arrangement.

## Limitations
Only the reduced support of the tangent-cone discriminant is asserted; scheme-theoretic multiplicities of the discriminant divisor are not claimed. The result is characteristic-zero and concerns this explicit \(B_3\) family. No claim is made about the full singular locus of every specialized quartic away from the marked point.

## References
1. M. Dumnicki, Ł. Farnik, B. Harbourne, G. Malara, J. Szpond, H. Tutaj-Gasińska, *A matrixwise approach to unexpected hypersurfaces*, arXiv:1907.04832; Linear Algebra Appl. 592 (2020), 113–133.
2. T. Bauer, G. Malara, T. Szemberg, J. Szpond, *Quartic unexpected curves and surfaces*, arXiv:1804.03610; Manuscripta Math. 161 (2020), 283–292.
3. Ł. Farnik, F. Galuppi, L. Sodomaco, W. Trok, *On the unique unexpected quartic in \(\mathbb P^2\)*, J. Algebraic Combin. 53 (2021), 131–146.
4. M. DiPasquale, J. Sidman, W. Traves, *Logarithmic derivations associated to line arrangements*, J. Algebra 588 (2021), 197–225.
