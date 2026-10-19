# Sharp ternary Fourier conditioning for four-point caps

## Finding
Let \(d\ge 2\), \(G=\mathbb F_3^d\), and let \(A\subset G\) consist of four distinct points, no three collinear. For any four-element \(B\subset\widehat G\), let \(M(A,B)=(\chi_b(a))_{a\in A,b\in B}\), where \(\chi_b(a)=e^{2\pi i\langle a,b\rangle/3}\). For invertible \(M\), define its Riesz ratio \(\rho(A,B)=\lambda_{\max}(M^*M)/\lambda_{\min}(M^*M)\), and put \(\rho(A)=\min_B\rho(A,B)\), excluding singular choices.

There are exactly two cases. If the affine span of \(A\) has dimension \(2\) (a four-point affine cap in a plane), then
\[\rho(A)=\frac{7+3\sqrt5}{2},\qquad \#\{B:\rho(A,B)=\rho(A)\}=36\cdot 3^{4(d-2)}.\]
If the affine span has dimension \(3\) (four affinely independent points), then
\[\rho(A)=\frac73,\qquad \#\{B:\rho(A,B)=\rho(A)\}=54\cdot 3^{4(d-3)}.\]
The counts are for unordered four-element sets of distinct ambient characters. Both minima are attained, and the result applies in every indicated dimension without asymptotic qualification.

## Assumptions and scope
The Fourier matrix uses unnormalized unit-modulus character values. The Riesz ratio is the ratio of best upper to best positive lower \(L^2\) exponential-basis bounds; multiplying the entire matrix by a scalar leaves it unchanged. A four-point cap is a four-element set with no three points on an affine line. A rank-two cap is affinely equivalent to \(A_{\rm cap}=\{(0,0),(1,0),(0,1),(1,1)\}\); a rank-three cap is equivalent to \(A_{\rm ind}=\{0,e_1,e_2,e_3\}\). This is an exhaustive dichotomy because the affine span of four points has dimension at most three and noncollinearity excludes dimension one.

## Proof
**Affine reduction and frequency lifts.** Translate one point to the origin and choose an affine basis. In a plane over \(\mathbb F_3\), a fourth point avoiding the lines through the first three forms a parallelogram with them, so every four-point cap of affine dimension two is equivalent to \(A_{\rm cap}\); dimension three gives \(A_{\rm ind}\). An ambient character is determined on \(A\), up to a common column phase, by its restriction to the difference span \(H\) of dimension \(r\in\{2,3\}\). If two chosen characters have equal restriction to \(H\), their columns are proportional and the matrix is singular. Conversely, a four-character set with pairwise distinct restrictions has exactly \(3^{4(d-r)}\) lifts to distinct ambient character sets. Thus the optimizing ratio is determined entirely in \(\mathbb F_3^r\), and optimizer counts multiply by this factor.

**Rank-two cap.** Write \(\omega=e^{2\pi i/3}\). Multiplying each Fourier row by a unit phase shows that translating the frequency set does not change the Gram spectrum. Hence it suffices to inspect the \(\binom83=56\) four-character sets containing the zero character. The exact cyclotomic calculation in `checker.py` works in \(\mathbb Z[\omega]\), representing \(a+b\omega\) by the integer pair \((a,b)\) and using \(\omega^2=-1-\omega\). For \(A_{\rm cap}\), the complete characteristic-polynomial census of \(M^*M\), written in decreasing powers of \(t\), is:

| Polynomial | Number of normalized frequency sets |
| --- | ---: |
| \(t^4-16t^3+81t^2-144t+81\) | 16 |
| \(t^4-16t^3+78t^2-144t+81\) | 4 |
| \(t^4-16t^3+84t^2-162t+81\) | 16 |
| \(t^4-16t^3+78t^2-108t\) | 16 |
| \(t^4-16t^3+84t^2-144t\) | 4 |

The last two polynomials represent singular matrices. The first factors as \((t^2-9t+9)(t^2-7t+9)\); its extreme eigenvalues are \((9-3\sqrt5)/2\) and \((9+3\sqrt5)/2\), giving the claimed ratio. The second factors as \((t-1)(t-3)^2(t-9)\), with ratio \(9\). The third factors as \((t-3)(t^3-13t^2+45t-27)\): the cubic has roots in \((0,1)\), \((4,5)\), and \((7,8)\), so its Riesz ratio exceeds \(7\). Since \((7+3\sqrt5)/2<7\), precisely the 16 frequency sets of the first type minimize the ratio. One such set is \(\{(0,0),(0,1),(1,0),(1,2)\}\). There are 9 frequency translations and every unordered four-set is represented exactly four times when a member is translated to zero, yielding \(16\cdot9/4=36\) minimizing frequency sets in the plane.

**Rank-three cap: universal lower bound.** Fix \(A_{\rm ind}=\{0,e_1,e_2,e_3\}\), and set \(Q=M^*M\). Its diagonal entries are all \(4\). Each off-diagonal entry is the sum of four third roots of unity; if the root multiplicities are \((n_0,n_1,n_2)\) with \(n_0+n_1+n_2=4\), then
\[|n_0+n_1\omega+n_2\omega^2|^2=\tfrac12\big((n_0-n_1)^2+(n_1-n_2)^2+(n_2-n_0)^2\big)\ge1.\]
Consequently \(\operatorname{tr}Q=16\) and \(\operatorname{tr}(Q^2)=64+2\sum_{i<j}|Q_{ij}|^2\ge76\).

Here is a sharp four-eigenvalue inequality. For four positive eigenvalues with largest-to-smallest ratio at most \(7/3\), scale the smallest to \(1\), so every scaled eigenvalue lies in \([1,7/3]\). Keeping three coordinates fixed, the function \((x^2+S)/(x+T)^2\) of the fourth has derivative with the sign of \(xT-S\), and therefore its maximum over the interval is at an endpoint. Iteration shows that the maximum of \(\sum\lambda_i^2/(\sum\lambda_i)^2\) is among the vertices having \(k\) entries equal to \(7/3\) and the other \(4-k\) equal to \(1\). For \(k=0,1,2,3,4\), the five respective values are \(1/4,19/64,29/100,13/48,1/4\). Thus \(\operatorname{tr}(Q^2)/(\operatorname{tr}Q)^2\le19/64\) whenever the Riesz ratio is at most \(7/3\). Together with the lower bound \(76/256=19/64\), this proves \(\rho(A_{\rm ind},B)\ge7/3\) for every invertible \(B\). Equality forces \(\operatorname{tr}(Q^2)=76\), hence every pairwise column inner product has squared modulus one.

**Rank-three sharpness and counting.** The frequency set \(B=\{(0,0,0),(0,1,2),(1,0,2),(2,2,1)\}\) has Gram characteristic polynomial \((t-7)(t-3)^3\), and realizes ratio \(7/3\). A frequency translation again permits normalizing one frequency to zero; there are \(\binom{26}{3}=2600\) normalized sets in the three-dimensional dual. The same exact integer-ring checker exhaustively establishes that exactly eight normalized sets have \(\operatorname{tr}(Q^2)=76\) (equivalently the coefficient of \(t^2\) is \(90\)), and each has characteristic polynomial \((t-7)(t-3)^3\). The equality condition above proves that this finite census is both necessary and sufficient. Because each unordered four-set has four choices of translated-to-zero member, the number of optimizing frequency sets in the three-dimensional dual is \(8\cdot27/4=54\). The frequency-lift factor completes the proof for all \(d\).

## Verification
Run `python3 checker.py` from the package directory. It prints `CHECK_PASS` after enumerating all 56 normalized frequency sets for each of the two plane shapes and all 2600 normalized sets for the affine-independent shape, computing characteristic polynomials with exact integer pairs in \(\mathbb Z[\omega]\). It also checks the three explicit extremizing partners and normalized optimizing counts. All enumerations are exhaustive after the proved affine-span reduction; the universal rank-three lower bound is independently justified by the eigenvalue inequality above. The checker was run successfully on its actual packaged source file.

## Relationship to prior work
Ferguson, Mayeli, and Sothanaphan introduced the Riesz ratio as a quantitative measure of spectrality and proved general exponential-basis existence and bounds in finite abelian groups. Their general conclusions do not determine sharp four-point cap ratios or optimizer multiplicities for ternary vector groups. A prior complete four-by-four Fourier-minor incidence classification for the ternary affine plane counts 81 nonsingular frequency partners per four-point sampling support, but does not rank their condition numbers or distinguish the 36 optimal partners proved here. A prior ternary affine-simplex tight-frame classification proves a minimum tight *frame size* of six and counts 27 such size-six frequency sets; it does not imply an optimum among cardinality-four, necessarily non-tight Riesz bases, or count the 54 such optimal bases. Earlier work on rank/determinant spectra of Boolean Fourier minors concerns characteristic two, not the ternary eigenvalue ratios considered here. The existing exact Riesz-ratio analysis of a subgroup with one extra point addresses a different support geometry, and is not used to claim novelty for that covered family. The result here characterizes the two noncollinear four-point geometries, not four-point sets containing a full affine line.

## Limitations
The theorem is restricted to four distinct sampling points over characteristic three and the unweighted exponential-basis Riesz ratio. It does not classify bases or conditioning for more points, other fields, or weighted Fourier frames. The explicit finite classification is backed by a transparent exhaustive integer calculation rather than a compact hand tabulation of all 56 plane cases. Published equivalence in older Fourier-submatrix or experimental-design literature remains possible, and independent mathematical validation has not been performed.

## References
1. S. Ferguson, A. Mayeli, N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487, originally posted April 9, 2019; Sections 1, 3--5. https://arxiv.org/abs/1904.04487 and https://arxiv.org/html/1904.04487v6 .
2. A. H. Barnett, *How Exponentially Ill-Conditioned Are Contiguous Submatrices of the Fourier Matrix?*, SIAM Review 64 (2022), 105--131, DOI:10.1137/20M1336837. This treats contiguous cyclic Fourier submatrices rather than the ternary affine-cap setting.
