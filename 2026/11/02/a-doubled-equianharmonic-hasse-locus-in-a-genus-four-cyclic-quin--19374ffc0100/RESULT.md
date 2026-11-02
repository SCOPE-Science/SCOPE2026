# A doubled equianharmonic Hasse locus in a genus-four cyclic quintic family in characteristic eleven

## Finding
Over \(k=\overline{\mathbb F}_{11}\), let \(C_\lambda\) be the smooth projective normalization of
\[
y^5=x(x-1)(x-\lambda)^2,\qquad \lambda\in k\setminus\{0,1\}.
\]
Set \(Q(\lambda)=\lambda^2-\lambda+1\). For every allowed geometric parameter the Jacobian \(11\)-rank and \(a\)-number are
\[
(f_{11},a)=\begin{cases}(4,0),&Q(\lambda)\ne0,\\(2,2),&Q(\lambda)=0.\end{cases}
\]
In the explicitly normalized differential basis below, the determinant of the eleventh-power Cartier-coefficient matrix is
\[
4\lambda^6(\lambda-1)^6Q(\lambda)^2.
\]
Thus the nonordinary determinant divisor on the **marked** smooth parameter line consists of two geometric points, each with multiplicity exactly two. Both points lie in \(\mathbb F_{121}\setminus\mathbb F_{11}\); the two parameters describe a single configuration after forgetting the ordering of the three branch points with identical inertia.

## Assumptions and scope
All fields have characteristic \(11\); the parameter excludes \(0,1\) and is viewed geometrically over an algebraic closure. The four branch points \(0,1,\lambda,\infty\) have tame inertia exponents \((1,1,2,1)\) modulo five, so Riemann--Hurwitz gives genus \(4\). The family is the cyclic-quintic one-dimensional special family corresponding, after multiplication of the inertia data by a unit modulo five, to the genus-four entry of Moonen's classification. The divisor multiplicity statement is in the displayed equation's parameter coordinate, not on a coarse quotient of the Hurwitz space.

## Proof
Write \(f=x(x-1)(x-\lambda)^2\), so \(y^5=f\). At the three finite tame ramification points, \(\operatorname{ord}(dx)=4\) and \(\operatorname{ord}(y)\) equals \(1,1,2\) respectively; at infinity, \(\operatorname{ord}(x)=-5\), \(\operatorname{ord}(y)=-4\), and \(\operatorname{ord}(dx)=-6\). These give exactly four holomorphic differentials
\[
\omega_2=\frac{dx}{y^2},\quad
\omega_3=\frac{(x-\lambda)dx}{y^3},\quad
\omega_{4,0}=\frac{(x-\lambda)dx}{y^4},\quad
\omega_{4,1}=\frac{x(x-\lambda)dx}{y^4}.
\]
Their orders at infinity are \(2,1,5,0\) respectively, and their orders at the branch point \(x=\lambda\) are \(0,3,1,1\). There are four such independent holomorphic forms, equal to the genus.

Since \(11\equiv1\pmod5\), Cartier preserves the spaces with denominators \(y^j\). The identity \(y^{-j}=y^{-11j}f^{2j}\) reduces the calculation on \(h(x)dx/y^j\) to coefficient extraction from \(h(x)f(x)^{2j}dx\): for each \(i\ge0\), the coefficient of \(x^i dx\) after Cartier is the eleventh root of the coefficient of \(x^{11i+10}dx\). In the chosen basis, define the matrix of *eleventh powers* of Cartier coefficients; it is block diagonal with scalars
\[
A=-5\lambda^2(\lambda-1)^2Q(\lambda),\qquad B=4Q(\lambda),
\]
and the block
\[
M=\begin{pmatrix}
-5\lambda^4(\lambda^2-3\lambda-3)&3\lambda^5(\lambda-2)\\
5(\lambda+5)&4(\lambda^2+\lambda-4)
\end{pmatrix}.
\]
All coefficients are reduced in \(\mathbb F_{11}[\lambda]\). Direct expansion gives
\[
\det M=2\lambda^4(\lambda-1)^4,
\qquad AB\det M=4\lambda^6(\lambda-1)^6Q(\lambda)^2.
\]
The \(2\)-dimensional block is invertible throughout the smooth parameter space. If \(Q\ne0\), both scalar blocks are invertible as well, so the Cartier operator and every semilinear iterate have rank \(4\). If \(Q=0\), both scalar blocks vanish identically under iteration but the two-dimensional block remains invertible; every positive iterate has rank \(2\). The stable image dimension therefore yields the displayed \(11\)-ranks. Since \(a=g-\operatorname{rank}\mathcal C\), the corresponding \(a\)-numbers are \(0\) and \(2\).

The discriminant of \(Q\) is \(-3=8\) in \(\mathbb F_{11}\), a nonsquare. Thus \(Q\) is separable irreducible over \(\mathbb F_{11}\), and its two geometric zeros lie over \(\mathbb F_{121}\) and avoid \(0,1\). On the smooth marked parameter line \(\lambda(\lambda-1)\) is a unit, so the determinant vanishes to order exactly two at each simple zero of \(Q\). For unordered branch configurations, the standard anharmonic transformations of \(\lambda\) leave invariant
\[
J_{\mathrm{br}}=256\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2}.
\]
At \(Q=0\), the two values are exchanged by \(\lambda\mapsto1-\lambda\) and define one inertia-labeled configuration. No assertion on divisor multiplicity after taking a possibly ramified coarse quotient follows from this argument.

## Verification
Two supplied self-contained programs recompute the critical coefficients independently: `verify_cyclic5_11.py` uses exact symbolic polynomial expansion (SymPy), while `verify_binomial_11.py` uses only Python's standard library and the binomial theorem. Both compute the four Cartier blocks, the invertible \(2\)-by-\(2\) determinant, and the full determinant identity. The first also tests the admissible differential orders and anharmonic invariance. Run both with Python 3; the former requires `sympy>=1.11`. Their successful diagnostic lines are recorded in `VERIFICATION.md`.

## Relationship to prior work
Bouw gives general ramified-cover \(p\)-rank and cyclic-cover Cartier-coefficient machinery, and Moonen lists the relevant genus-four cyclic-quintic family and general Hasse-coefficient formulas. Their general statements provide the framework, not this explicit characteristic-eleven determinant factorization and complete geometric parameter locus. Li--Mantovan--Pries--Tang study Newton strata of Moonen's special families and identify the equianharmonic moduli coordinate; later work discusses the equianharmonic distinguished curve and possible Newton polygons. We do **not** claim the family, coefficient-extraction method, branch invariant, distinguished CM configuration, or general Newton-stratum possibilities as new. The additional statement is the complete characteristic-eleven parameterwise ordinary/nonordinary dichotomy and its doubled determinant degeneration on the marked line. The possibility of a historical specialized formula already implying this exact statement remains a priority risk.

## Limitations
This is a characteristic-eleven classification of one specified one-parameter family; it does not classify every cyclic-quintic curve, the full Ekedahl--Oort type, or every Newton slope of the special fiber. The Hasse multiplicities are on the displayed parameter line and are not automatically multiplicities on the coarse quotient. Recomputing coefficients independently supports the arithmetic, but does not constitute an independent external scientific audit. Historical novelty is supported by examined sources and searches, not guaranteed by the failure of database lookup.

## References
- I. Bouw, *The p-Rank of Ramified Covers of Curves*, Compositio Mathematica **126** (2001), 295--322, DOI:10.1023/A:1017513122376. Published online with precisely dated availability 2007-12-04; the journal print edition is earlier.
- B. Moonen, *Special subvarieties arising from families of cyclic covers of the projective line*, arXiv:1006.3400 (first arXiv posting 2010-06-17), particularly Table 1 and the Hasse coefficient formulas.
- W. Li, E. Mantovan, R. Pries, Y. Tang, *Newton polygons arising for special families of cyclic covers of the projective line*, arXiv:1805.06914, particularly the genus-four family and Newton polygon strata.
- W. Li, E. Mantovan, R. Pries, Y. Tang, *Infinitely many primes of basic reduction for some abelian fourfolds*, special-family branch invariant and exceptional CM configuration.
