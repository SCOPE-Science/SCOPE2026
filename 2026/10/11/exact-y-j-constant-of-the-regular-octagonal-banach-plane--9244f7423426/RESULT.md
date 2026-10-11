# Exact \(Y_J\) constant of the regular octagonal Banach plane
## Finding
For the real Banach plane \(X_8=(\mathbb R^2,N)\) with
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\},
\]
the centered-triangle constant introduced by Fu, Liu and Li is
\[
Y_J(X_8)=2\sqrt2-1.
\]
Equivalently, using the identity \(Y_J(X)=2-2\delta_X(1)\) from Ahmad, Fu and Li,
\[
\delta_{X_8}(1)=\frac{3-2\sqrt2}{2}.
\]

## Assumptions and scope
All spaces and vectors are real. The constant is
\[
Y_J(X)=\sup\left\{\|x-y\|:\ \|x\|=\|y\|=\|x+y\|=1\right\},
\]
which is equivalent to the original centered-triple definition by taking the three unit vectors \(x\), \(y\), and \(-x-y\). The result concerns only the displayed regular-octagonal norm; it does not assert a formula for arbitrary regular polygons or arbitrary Banach planes.

## Proof
Put \(r=\sqrt2\). The octagonal norm is the maximum of the eight linear support functionals
\[
\pm s,\qquad \pm t,\qquad \frac{\pm s\pm t}{r}.
\]
Hence the feasible set
\[
F=\{(x,y)\in\mathbb R^2\times\mathbb R^2:N(x)=N(y)=N(x+y)=1\}
\]
is a finite union of compact polyhedral cells. On a cell where one support functional is active for each of \(x\), \(y\), and \(x+y\), the three active equalities have rank at most three. If the rank is three, the cell is a point or a line segment after the remaining support inequalities are imposed. For each of the eight support functionals \(h\), maximizing \(h(x-y)\) over such a cell is a linear program, so its maximum occurs either at the unique point or at an endpoint of the segment; an endpoint is obtained when one additional support inequality is active. Rank below three contributes only cells already represented by a rank-three active choice after choosing another active facet on the same boundary face.

The accompanying exact checker therefore enumerates every triple of active support facets and every possible fourth active inequality. All arithmetic is carried out exactly in \(\mathbb Q(\sqrt2)\), all twenty-four support inequalities for \(x\), \(y\), and \(x+y\) are checked, and the objective \(N(x-y)\) is evaluated at every feasible endpoint. It finds ninety-six feasible active systems representing forty-eight distinct vertices, and the largest objective is exactly
\[
2\sqrt2-1.
\]

For attainment, take
\[
x=(1,1-\sqrt2),\qquad y=(2\sqrt2-2,2-\sqrt2).
\]
Direct substitution gives \(N(x)=N(y)=N(x+y)=1\), while
\[
x-y=(3-2\sqrt2,-1),
\]
so \(N(x-y)=2\sqrt2-1\). This matches the exhaustive upper bound and proves the formula.

## Verification
The file `verify_yj_octagon.py` implements the exact polyhedral enumeration described above with rational-pair arithmetic for \(a+b\sqrt2\). A successful replay prints `VERIFY_OK`, the feasible-system count, the distinct-vertex count, the exact maximum, and the explicit maximizing pair. No floating-point comparison is used in the certificate.

## Relationship to prior work
Fu, Liu and Li introduced \(J_L\) and \(Y_J\) for centered unit triples in 2021. Ahmad, Fu and Li gave the two-vector formulation used here and identified \(Y_J(X)=2-2\delta_X(1)\). A later paper of Martini, Papini and Wu studies the same invariant under the notation \(J_1\), together with related James--Schäffer parameters. The accessible abstract does not state an exact regular-octagon value, so that paper remains a literature-access risk rather than evidence of coverage.

A 2022 paper of Baronti and Papini computes the classical James and Schäffer constants for the regular octagonal plane, but those objectives are different from the centered-triangle supremum here. A separate result on equilateral triangles in regular \(4n\)-gonal norms proves constancy of a perimeter parameter; its feasible triangles are norm-equilateral and its conclusion does not determine the centered-triple quantity \(Y_J\).

## Limitations
The originality assessment is based on direct searches for \(Y_J\), its \(J_1\) alias, the unit-separation modulus-of-convexity formulation, the exact radical, and regular-octagon tables, plus inspection of the most relevant available sources. The full text of the 2024 \(J_1\) paper was not available in the inspected sources, so an unlocated equivalent table remains a residual risk. The result is an exact value for one canonical two-dimensional polyhedral norm, not a general classification theorem.

## References
1. Y. Fu, Q. Liu and Y. Li, *New Geometric Constants in Banach Spaces Related to the Inscribed Equilateral Triangles of Unit Balls*, Symmetry 13 (2021), 951. DOI: 10.3390/sym13060951. First public date verified here: 2021-05-27.
2. A. Ahmad, Y. Fu and Y. Li, *Some Properties Concerning the \(J_L(X)\) and \(Y_J(X)\) Which Related to Some Special Inscribed Triangles of Unit Ball*, Symmetry 13 (2021), 1285. DOI: 10.3390/sym13071285.
3. H. Martini, P. L. Papini and S. Wu, *Variations of the James and Schäffer constants in Banach spaces*, Annals of Functional Analysis 15 (2024). DOI: 10.1007/s43034-023-00308-7.
4. M. Baronti and P. L. Papini, *Parameters in Banach spaces and orthogonality*, Journal of Analysis 30 (2022), 35--47.
