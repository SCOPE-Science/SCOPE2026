# Exact \(Y_J\) constant of the regular octagonal Banach plane

## Finding
For the real Banach plane \(X_8=(\mathbb R^2,N)\), with
\[
N(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{\sqrt2}\right\},
\]
the centered-triangle constant of Fu, Liu and Li equals
\[
Y_J(X_8)=2\sqrt2-1.
\]
Equivalently, by the Ahmad--Fu--Li identity \(Y_J(X)=2-2\delta_X(1)\),
\[
\delta_{X_8}(1)=\frac{3-2\sqrt2}{2}.
\]

## Assumptions and normalization
All vectors and scalars are real. The constant is
\[
Y_J(X)=\sup\{\|x-y\|: \|x\|=\|y\|=\|x+y\|=1\},
\]
equivalent to the centered-unit-triple definition by using the third vector \(-x-y\). No formula is claimed for other polygonal norms. The precise placement of \(x+y\) in the three unit-norm constraints is essential: a sign reversal of one vector interchanges the constraint and objective.

## Proof
Put \(r=\sqrt2\). The octagonal norm is the maximum of eight linear support functionals
\[
\pm s,\qquad \pm t,\qquad (\pm s\pm t)/r.
\]
The feasible set \(F=\{(x,y):N(x)=N(y)=N(x+y)=1\}\subset\mathbb R^4\) is a finite union of compact polyhedral cells. Each point belongs to at least one cell obtained by selecting an active support equality for each of \(x,y,x+y\), and imposing every support inequality. Where these three equations have rank three, the cell is a bounded segment (possibly a singleton). A linear objective attains its maximum at an endpoint. Such an endpoint has at least one fourth independent active support equality. Rank-deficient choices may be augmented by other simultaneously active constraints to obtain a full-rank endpoint, or their cell lies in a rank-three cell already counted. Consequently every maximum of every support functional of \(x-y\) occurs among the solutions of the three active equalities plus a fourth active support equality, provided all 24 inequalities are checked.

The attached `verify_yj_octagon.py` explicitly forms those candidate linear systems for all eight choices of each of the three unit-sphere constraints and all 24 choices of the fourth equality. It solves each nonsingular system over \(\mathbb Q(\sqrt2)\), tests the 24 support inequalities exactly, and computes each of the eight objective support values using **exact algebraic comparisons**. It finds 96 feasible active systems, representing 48 distinct feasible points, with the exact largest objective \(2\sqrt2-1\). This is an exhaustive finite polyhedral reduction, not inference from a numerical sample.

For an attaining pair use, with the required sign,
\[
x=(1,1-\sqrt2),\qquad
 y=(2-2\sqrt2,\sqrt2-2).
\]
Indeed, direct substitution gives
\[
N(x)=N(y)=N(x+y)=1,
\qquad x+y=(3-2\sqrt2,-1),
\]
whereas
\[
x-y=(2\sqrt2-1,3-2\sqrt2),\qquad N(x-y)=2\sqrt2-1.
\]
The upper-bound enumeration and this exact attaining pair prove the result.

## Verification and limitations
The package verifier carries all coefficients as rational pairs \(a+b\sqrt2\); it uses rational arithmetic and sign tests even to order competing support values. It checks every bounded active-system candidate and the attaining pair, and prints `VERIFY_OK`, 96 feasible systems, 48 distinct points, and the target maximum. No arbitrary-precision or binary floating-point ordering is needed. The checker certifies the stated four-dimensional polyhedral optimization only, not originality or results for other norms. Its finite enumeration is exhaustive because of the active-facet reduction in the proof, rather than because a finite sample of vectors appears representative.

## Relationship to prior work
Fu, Liu and Li introduced the centered-triple constants \(J_L\) and \(Y_J\) in 2021. Ahmad, Fu and Li supplied the present two-vector formulation and the modulus-of-convexity identity. Martini, Papini and Wu study this invariant under the notation \(J_1\) and relate it to other geometric constants; the complete 2024 article was not available for comparison, leaving a stated originality risk. Classical James and Schäffer constants calculated for the octagonal plane by Baronti and Papini, and distinct equilateral-triangle perimeter constants, use different optimization problems and do not by themselves imply this value. The exact octagonal value is a natural finite-dimensional test case for the centered-triangle geometry, but is not a general Banach-space characterization.

## References
1. Y. Fu, Q. Liu and Y. Li, *New Geometric Constants in Banach Spaces Related to the Inscribed Equilateral Triangles of Unit Balls*, Symmetry 13 (2021), 951. DOI: 10.3390/sym13060951.
2. A. Ahmad, Y. Fu and Y. Li, *Some Properties Concerning the \(J_L(X)\) and \(Y_J(X)\) Which Related to Some Special Inscribed Triangles of Unit Ball*, Symmetry 13 (2021), 1285. DOI: 10.3390/sym13071285.
3. H. Martini, P. L. Papini and S. Wu, *Variations of the James and Schäffer constants in Banach spaces*, Annals of Functional Analysis 15 (2024). DOI: 10.1007/s43034-023-00308-7.
4. M. Baronti and P. L. Papini, *Parameters in Banach spaces and orthogonality*, Journal of Analysis 30 (2022), 35--47.
