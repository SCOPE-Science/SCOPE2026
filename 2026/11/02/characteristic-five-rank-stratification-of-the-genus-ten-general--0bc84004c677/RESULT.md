# Characteristic-five rank stratification of the genus-ten generalized Fermat family

## Finding
Let \(k=\overline{\mathbb F}_5\). For \(\lambda\in k\setminus\{0,1\}\), consider the genus-ten curve
\[
C_\lambda:\quad X_0^3+X_1^3+X_2^3=0,\qquad
\lambda X_0^3+X_1^3+X_3^3=0
\quad\subset\mathbb P^3_k.
\]
The geometric \(5\)-rank and the \(a\)-number of its Jacobian are exactly
\[
(f,a)(\operatorname{Jac}(C_\lambda))=
\begin{cases}
(4,6),&\lambda\in\{-1,2,3\},\\
(6,4),&\lambda\notin\{0,1,-1,2,3\}.
\end{cases}
\]
The three exceptional marked parameters form a single orbit under the anharmonic transformations of the four branch points \(\{\infty,0,1,\lambda\}\). There are no other geometric jump parameters.

## Assumptions and scope
All claims hold over the algebraic closure of \(\mathbb F_5\); the parameter restriction ensures a smooth complete intersection. Here the \(p\)-rank is \(\dim_{\mathbb F_p}\operatorname{Jac}(C)[p](k)\), and \(a=\dim_k\operatorname{Hom}(\alpha_p,\operatorname{Jac}(C)[p])\). Equivalently, \(a\) is the dimension of the kernel of the Cartier operator on holomorphic differentials. The numbers count marked parameters, not isomorphism classes of curves.

## Proof
**Smoothness and genus.** In characteristic five, the two Jacobian rows, up to the invertible factor \(3\), are \((X_0^2,X_1^2,X_2^2,0)\) and \((\lambda X_0^2,X_1^2,0,X_3^2)\). A rank drop forces \(X_2=X_3=0\); the two defining cubics then force \((\lambda-1)X_0^3=0\) and \(X_1=0\), impossible projectively. Thus the complete intersection is smooth. Its canonical class is \(\mathcal O_C(2)\), and its degree is \(9\); by adjunction its genus is \(1+9=10\).

**Hasse–Witt calculation.** Put \(F_1=X_0^3+X_1^3+X_2^3\), \(F_2=\lambda X_0^3+X_1^3+X_3^3\). The Koszul sequence identifies \(H^1(C,\mathcal O_C)\) with \(H^3(\mathbb P^3,\mathcal O(-6))\). Index its standard inverse-monomial basis by the ten positive tuples \(\mathbf a=(a_0,a_1,a_2,a_3)\) with \(\sum a_i=6\). For the ordered list
\[
\begin{split}
&(1,1,1,3),(1,1,2,2),(1,1,3,1),(1,2,1,2),(1,2,2,1),\\
&(1,3,1,1),(2,1,1,2),(2,1,2,1),(2,2,1,1),(3,1,1,1),
\end{split}
\]
use zero-based matrix indices \(0,\ldots,9\). The Frobenius matrix entry in row \(\mathbf b\), column \(\mathbf a\) is the coefficient of \(X_0^{5a_0-b_0}\cdots X_3^{5a_3-b_3}\) in \((F_1F_2)^4\); coefficients with negative exponents are zero. This is the standard Koszul/Frobenius multiplier construction, not a finite-field interpolation.

Exactly six entries are nonzero:
\[
\begin{array}{lll}
H_{1,8}=(\lambda+1)(\lambda-1)^2,& H_{8,1}=\lambda+1,\\
H_{3,7}=\lambda^2(\lambda-2),&H_{7,3}=\lambda-2,\\
H_{4,6}=3(\lambda-3),&H_{6,4}=3(\lambda-3).
\end{array}
\]
All other entries vanish identically. In particular, indices \(0,2,5,9\) are zero rows and columns, while \((1,8),(3,7),(4,6)\) are independent two-dimensional Frobenius-stable blocks. On the smooth parameter space, each block is either invertible or zero: the first is zero exactly at \(\lambda=-1\), the second at \(\lambda=2\), and the third at \(\lambda=3\). These three values are distinct in characteristic five.

An invertible semilinear Frobenius block contributes its full dimension to the stable image, while a zero block contributes none. Therefore the stable Frobenius rank, equal to the \(5\)-rank, is \(6\) generically and \(4\) at the three exceptional parameters. The \(a\)-number is the dimension of the kernel of the Hasse–Witt/Cartier map, namely \(10-\operatorname{rank}H\), so it equals \(4\) generically and \(6\) exceptionally. These computations hold for every algebraically closed parameter, proving geometric completeness.

**The marked orbit.** Permuting the four branch points acts by anharmonic substitutions, including \(\lambda\mapsto1-\lambda\) and \(\lambda\mapsto1/\lambda\). Starting with \(\lambda=2\), these produce \(4=-1\) and \(3=1/2\) in characteristic five. Thus the three exceptional marked values form a single orbit.

## Verification
The self-contained script `verify.py` expands \((F_1F_2)^4\) over \(\mathbb F_5[\lambda]\), reconstructs the full ten-by-ten coefficient matrix, and asserts all six displayed entries and the vanishing of the remaining entries. It additionally checks ranks at the three smooth \(\mathbb F_5\)-parameters. Its output `verify_output.txt` ends with `VERIFY_OK`. The factorization and invertibility arguments above prove the result for all algebraically closed parameters; finite-field enumerations are not used as infinite proofs.

## Relationship to prior work
Carvacho, Hidalgo, and Quispe (2015, arXiv:1507.02903v1, Section 6.3) supply the genus-ten generalized Fermat model and a Jacobian decomposition into lower-genus quotient factors; this is not asserted to be new. Hidalgo (2017 preprint, arXiv:1710.01349, Section 5.3) develops Cartier-operator techniques and explicitly computes the \(2\)-rank for this family. His inspected treatment does not provide the above characteristic-five exceptional parameters or this characteristic-five Hasse–Witt matrix: the explicit general-prime specialization there concerns exponents dividing \(p-1\), which does not include exponent three at \(p=5\). Earlier investigations of the same type of cover in characteristic seven involve a different Frobenius congruence and do not determine the present strata.

## Limitations
The claim determines the geometric \(5\)-rank and \(a\)-number, not the full Newton polygon, Ekedahl–Oort type, or zeta functions. The orbit assertion concerns marked branch configurations and does not independently classify automorphism groups or all isomorphism classes. Historical priority is provisional: the searched literature and indexed records may omit an equivalent, unpublished, or differently phrased computation. There has been no independent scientific audit.

## References
1. M. Carvacho, R. Hidalgo, S. Quispe, *Isogenous decomposition of the Jacobian of generalized Fermat curves*, arXiv:1507.02903v1 (first posted 10 July 2015), especially Section 6.3.
2. R. Hidalgo, *Holomorphic differentials of generalized Fermat curves*, arXiv:1710.01349 (first posted October 2017; inspected later revision), especially Sections 5.2–5.3.
