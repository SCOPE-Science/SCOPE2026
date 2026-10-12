# Parity-character rigidity for the linearized \(x^{2}+6y^{2}\) norm

## Finding

For arbitrary complex functions \(F,G:\mathbb N_{>0}\to\mathbb C\), the equation
\[
F(x^{2}+6y^{2})=G(x)+6G(y)\quad(x,y\ge1)
\]
holds if and only if there are **unique** constants \(A,B,C\in\mathbb C\) such that
\[
G(n)=An^{2}+B+C(-1)^{n}\quad(n\ge1),
\]
and, for every \(t\in\mathcal E_6\),
\[
F(t)=At+7B+C\eta(t\bmod4),\qquad
(\eta(0),\eta(1),\eta(2),\eta(3))=(7,5,-5,-7).
\]
Here \(\mathcal E_6=\{x^{2}+6y^{2}:x,y\ge1\}\). On positive integers outside \(\mathcal E_6\), the function \(F\) is wholly arbitrary. The parity term cannot in general be absorbed into either quadratic or constant terms.

## Assumptions and scope

The form \(x^{2}+6y^{2}\) is the principal positive-definite binary quadratic form of discriminant \(-24\); its two reduced primitive classes are represented by \((1,0,6)\) and \((2,0,3)\). The coefficient is therefore attached to a natural imaginary-quadratic norm, not an arbitrary numerical truncation. All indices \(x,y,n\) are strictly positive integers, the coefficient \(6\) is fixed, and \(F,G\) are completely unconstrained complex-valued functions: no multiplicativity, continuity, boundedness, growth bound, or relation \(G=F^{2}\) is assumed. Equality at an integer with two norm representations is required for both representations. Classification on \(\mathcal E_6\) is exact; no statement is made about its complement beyond freedom of assignment.

## Proof

**Finite rigidity.** For representations \((a,b)\), \((c,d)\) of the same positive integer, the functional equation implies
\[
G(a)+6G(b)-G(c)-6G(d)=0.
\]
The file `check.py` lists seventeen exact such collisions. For each one, form the integer row vector \(R\) of length \(20\), with entries equal to the coefficients of \(G(1),\ldots,G(20)\); repeated indices must be combined. In the given row order, delete columns \(1,2,3\) and take the resulting \(17\times17\) determinant. Exact fraction-free elimination yields **\(432\ne0\)**. Consequently the collision system has rank at least \(17\), leaving nullity at most \(3\).

The three vectors indexed by \(j=1,\ldots,20\), namely \((1)\), \((j^{2})\), and \(((-1)^{j})\), all satisfy these collisions. Indeed equal norms imply equal quadratic sums, and modulo \(4\), the integer \(a^{2}+6b^{2}\) uniquely determines the parities of \(a,b\). Their restriction to \(j\in\{1,2,3\}\) has determinant \(-16\), hence they are independent. Thus every admissible \(G(1),\ldots,G(20)\) is uniquely \(Aj^{2}+B+C(-1)^{j}\) on this range.

**Infinite propagation.** For any integer \(n\ge21\), select the unique \(y\in\{1,\ldots,7\}\) with \(y\equiv n\pmod7\), and define integers
\[
a=\frac{5n-12y}{7},\qquad b=\frac{2n+5y}{7}.
\]
Then \(1\le a,b,y<n\), and expansion of the rational orthogonal transformation gives
\[
 n^{2}+6y^{2}=a^{2}+6b^{2}.
\]
Because \(7\) is odd, \(a\equiv n\pmod2\) and \(b\equiv y\pmod2\). If \(H(n):=G(n)-An^{2}-B-C(-1)^{n}\), both \(G\) and the explicit template satisfy the collision identities, so
\[
H(n)+6H(y)=H(a)+6H(b).
\]
Strong induction from the verified first twenty indices forces \(H(n)=0\) for all \(n\ge1\).

**Recovering \(F\) and sufficiency.** At \(t=x^{2}+6y^{2}\), substitute the formula for \(G\) to obtain
\[
F(t)=A(x^{2}+6y^{2})+7B+C\bigl((-1)^{x}+6(-1)^{y}\bigr).
\]
Squares modulo \(4\) are \(0\) or \(1\), so \(t\bmod4\) uniquely fixes the ordered parity pair \((x\bmod2,y\bmod2)\). The weighted parity expression takes values \(7,5,-5,-7\) for residues \(0,1,2,3\), respectively, proving the stated well-defined formula. Conversely the displayed formulas satisfy the equation for all positive \(x,y\), regardless of how \(F\) is assigned outside \(\mathcal E_6\). The finite independence gives uniqueness of \(A,B,C\).

## Verification

The standalone Python 3 script `check.py` validates the seventeen representations as integer identities, constructs the exact \(17\times20\) matrix, computes its determinant \(432\) after removing the first three columns by integer Bareiss elimination, checks the three predicted kernel vectors, and checks their \(3\times3\) independence determinant \(-16\). It also tests the induction step on \(4980\) successive indices and the modulo-\(4\) parity decoder on \(10{,}000\) pairs. It prints `EXACT_CERTIFICATE_OK`. The infinite induction and the parity claim are separately proved above, not inferred from finite tests.

Run from the directory containing both files: `python3 check.py`. The certificate uses only the Python standard library. No externally sourced code, generated tables, or numerical tolerances are required.

## Relationship to prior work

Kátai and Phong (2014) studied general additive two-set equations under a difference-set hypothesis; their stated main condition is not the present weighted square-pair system. Their 2015 open-problems paper formulates a **nonlinear** arithmetic-function equation on \(x^{2}+Dy^{2}\). You, Chen, Yuan, and Shen (2016) address that nonlinear equation under additional conditions and solve the cases \(D\in\{2,3,4,5\}\). Khanh (2017) treats the nonlinear equation for all \(D\); her Lemma 2 supplies a general, necessary quadratic-plus-periodic expression for the auxiliary \(G\) in \(F(x^{2}+Dy^{2})=G(x)+UG(y)\), but not this exact parity-character sufficiency/classification for \((D,U)=(6,6)\). Kátai and Phong (2021) obtain a parity character for a different equation involving **three independently varying squares**, not a two-variable anisotropic norm with a coefficient of 6. Neither that independent-three-square theorem, the nonlinear classification, nor a necessary finite-periodic envelope logically implies the complete three-dimensional solution space here. These are scope and implication comparisons, not a claim of a comprehensive novelty guarantee.

## Limitations

The result is specialized to the natural quadratic norm with coefficient \(6\); no analogous classification is asserted for other coefficients or independently varying weights. It does not solve a new nonlinear squared-function identity (those have prior classifications), and it does not compute the density of \(\mathcal E_6\). Although the identified literature lacks the explicit stated linearized classification, earlier unindexed or differently formulated arguments remain possible. The finite certificate is reproducible but not independent external validation.

## References

1. I. Kátai and B. M. Phong, *The functional equation \(f(A+B)=g(A)+h(B)\)*, Annales Univ. Sci. Budapest., Sect. Comp. **43** (2014), 287–301, DOI: 10.71352/ac.43.287.
2. I. Kátai and B. M. Phong, *Some unsolved problems on arithmetical functions*, Annales Univ. Sci. Budapest., Sect. Comp. **44** (2015), 233–235, DOI: 10.71352/ac.44.233.
3. L. You, Y. Chen, P. Yuan, and J. Shen, *A characterization of arithmetic functions satisfying \(f(u^{2}+kv^{2})=f^{2}(u)+kf^{2}(v)\)*, arXiv:1606.05039v1 (first submitted 2016-06-16).
4. B. M. M. Khanh, *On conjecture concerning the functional equation*, Annales Univ. Sci. Budapest., Sect. Comp. **46** (2017), 123–135, DOI: 10.71352/ac.46.123.
5. I. Kátai and B. M. Phong, *Arithmetical functions commutable with sums of squares II*, Mathematica Pannonica New Series **27** (2021), 179–190, DOI: 10.1556/314.2021.00016.
