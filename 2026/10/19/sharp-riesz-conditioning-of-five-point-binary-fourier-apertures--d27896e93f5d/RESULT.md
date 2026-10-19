# Sharp Riesz conditioning of five-point binary Fourier apertures

## Finding

**Theorem.** Let \(d\ge4\), let \(G=\mathbb F_2^d\), and let \(A,B\subset G\) each have five distinct elements. Define the unnormalized Walsh character matrix
\[
H_{A,B}=\big((-1)^{a\cdot b}\big)_{a\in A,\,b\in B},
\]
using the standard nondegenerate dot product. Set \(\rho(A,B)=\lambda_{\max}(H_{A,B}^*H_{A,B})/\lambda_{\min}(H_{A,B}^*H_{A,B})\), with value \(+\infty\) when the matrix is singular. Then
\[
\min_{|A|=|B|=5}\rho(A,B)=\frac94.
\]
A five-point set \(A\) possesses a partner \(B\) attaining \(9/4\) **if and only if** \(A\) is affinely independent over \(\mathbb F_2\). More precisely, order such a set as \(A=\{a_0,a_1,a_2,a_3,a_4\}\), put \(v_i=a_i+a_0\) for \(1\le i\le4\), and define the surjection
\[
U_A:G\longrightarrow\mathbb F_2^4,\qquad
U_A(b)=(v_1\cdot b,v_2\cdot b,v_3\cdot b,v_4\cdot b).
\]
Let \(e_1,\ldots,e_4\) denote the standard basis of \(\mathbb F_2^4\), and set
\[
S=\{e_1,e_2,e_3,e_4,e_1+e_2+e_3+e_4\}.
\]
**All** minimizing frequency sets are exactly the five-point sets \(B\) for which
\[
U_A(B)=S+t\quad\text{for some }t\in\mathbb F_2^4,
\]
with precisely one element of \(B\) above each of the five displayed quotient frequencies. Consequently each independent \(A\) has exactly
\[
16\cdot2^{5(d-4)}
\]
optimal frequency partners. If \(n=2^d\), the number of ordered optimal pairs is
\[
\frac{n(n-1)(n-2)(n-4)(n-8)}{120}\cdot16\cdot\left(\frac n{16}\right)^5.
\]
For \(d=4\), this gives \(43{,}008\) pairs. Every minimizing Gram matrix has eigenvalues \(9,4,4,4,4\); in particular, the optimal Riesz ratio is \(9/4\) rather than an orthogonal value of \(1\).

## Assumptions and scope

All vector operations in the finite groups are over \(\mathbb F_2\). A five-point subset is *affinely independent* when the four differences from one of its points are linearly independent. Such sets exist exactly in dimensions at least four. Singular five-character systems are assigned infinite Riesz ratio. Counting is for **unordered** five-element supports and frequencies; ordered pairs \((A,B)\) distinguish the support from the frequency selection. Normalizing the counting measure or normalizing character columns multiplies all Gram eigenvalues by the same positive factor and leaves \(\rho\) unchanged.

## Proof

**1. Universal determinant and conditioning barrier.** For any \(5\times5\) sign matrix \(M\), row/column sign changes can make its first row and column positive. Subtracting that row from the other four proves \(16\mid\det M\). Hadamard's determinant inequality gives \(|\det M|\le5^{5/2}<56\), so \(|\det M|\in\{0,16,32,48\}\).

Suppose \(M\) is nonsingular and its Gram eigenvalues satisfy \(0<m\le\lambda_i\le M_0\), with ratio \(r=M_0/m\le9/4\). Their mean is \(5\) because each of the five sign columns has squared norm \(5\). Taylor's inequality for \(\log x\), whose second derivative on this interval is at least \(-1/m^2\), and Popoviciu's variance bound give
\[
\begin{aligned}
\log\det(M^*M)
&=\sum_{i=1}^5\log\lambda_i\\
&\ge5\log5-\frac1{2m^2}\sum_{i=1}^5(\lambda_i-5)^2\\
&\ge5\log5-\frac{5}{8}(r-1)^2\\
&\ge5\log5-\frac{125}{128}.
\end{aligned}
\]
It follows that
\[
|\det M|^2\ge3125e^{-125/128}>3125/3>1024,
\]
using \(e<3\). Since a sign determinant is divisible by \(16\) and at most \(48\), **any** sign matrix with \(\rho\le9/4\) necessarily has \(|\det M|=48\). This implication does not use any special property of Walsh matrices.

**2. Five-point sets inside a three-dimensional affine space cannot be extremal.** Every affinely dependent five-point \(A\) has affine dimension exactly three, since an affine plane over \(\mathbb F_2\) has only four points. After an affine change of coordinates, the restrictions of all characters to \(A\) are columns from the order-eight Walsh matrix, up to column signs. A repeated restricted column gives zero determinant. For five distinct restricted columns, Jacobi's complementary minor identity for an \(8\times8\) Walsh matrix gives the magnitude of the five-minor as \(8\) times the magnitude of a complementary three-minor. Every \(3\times3\) sign determinant has magnitude at most \(4\) (Hadamard bound plus divisibility by four). Thus \(|\det H_{A,B}|\le32\), and step 1 rules out \(\rho\le9/4\).

**3. Exact classification of maximal five-character determinants.** Now suppose \(A\) is affine independent, so \(U_A\) is onto. Multiplying rows and columns by signs makes the first row and one chosen column of \(H_{A,B}\) positive. For any \(b_0\in B\), subtract the top row from each other row. Expanding in the first column yields
\[
|\det H_{A,B}|=16\,|\det Q|,
\]
where \(Q\) is the binary \(4\times4\) matrix whose columns are the coordinate vectors \(U_A(b+b_0)\) for \(b\in B\setminus\{b_0\}\).

The following finite lemma is exhaustive and has a standalone exact certificate: among the \(\binom{16}{4}=1820\) unordered four-subsets of \(\mathbb F_2^4\), the determinant magnitude of the corresponding four-column binary matrix is distributed as
\[
0:880,\qquad1:835,\qquad2:100,\qquad3:5.
\]
The five maximizers, written as four hexadecimal-free integer bit masks with the low bit first, are
\[
\begin{gathered}
(3,5,9,14),\ (3,6,10,13),\ (5,6,11,12),\\
(7,9,10,12),\ (7,11,13,14).
\end{gathered}
\]
Each is exactly \((S+t)\setminus\{0\}\) for one of the five shifts \(t\in S\). The proof of the lemma evaluates every four-subset with two different exact determinant formulas, fraction-free elimination and the \(24\)-term permutation expansion, in the included `checker.py`. All \(1820\) cases are exhaustively covered, without floating-point tolerances.

Thus \(|\det H_{A,B}|=48\) precisely when \(U_A(B)=S+t\) for some \(t\in\mathbb F_2^4\). Every such translate contains five different quotient frequencies. The \(16\) translates are distinct: a nonzero translation in a characteristic-two group acts in disjoint pairs, so cannot preserve the odd-size set \(S\). Each quotient vector has \(2^{d-4}\) preimages, giving \(16\cdot2^{5(d-4)}\) independent five-frequency sets for each \(A\).

**4. Exact Gram spectrum at equality.** For a canonical independent set \(A=\{0,e_1,e_2,e_3,e_4\}\) and the canonical partner \(B=S\), the five-by-five Gram matrix equals \(4I+ss^*\), where \(s=(1,1,1,1,-1)^T\). Its eigenvalues are \(9,4,4,4,4\). Affine changes of row coordinates, frequency translations, and arbitrary choices of lifts in \(\ker U_A\) alter the synthesis matrix only by row/column sign changes or permutations, leaving singular values invariant. Hence every determinant-maximizing pair has \(\rho=9/4\), and step 1 shows no other pair does.

Finally, the number of affine independent five-point sets is \(n(n-1)(n-2)(n-4)(n-8)/120\): choose one starting point and four successive independent differences, then divide by \(5!\). Multiplying by the number of partners proves the ordered-pair count. This completes the theorem.

## Verification

Run `python3 checker.py` using Python 3 with no external packages. The checker enumerates all \(1820\) unordered binary four-column sets, tests each determinant with two independent integer algorithms, verifies the five distinguished maximizers, their translation orbit, and the canonical order-sixteen Walsh-minor counts. It reports `CHECK_PASS` on success. Its canonical independent-row enumeration returns determinant-magnitude frequencies \(0:1360\), \(16:2672\), \(32:320\), \(48:16\); the dependent-row model returns \(0:3344\), \(32:1024\). The infinite-dimensional statement is proved by the character-quotient reduction and does not extrapolate a finite scan.

The strict conditioning barrier is analytic; in particular, \(3125/3>1024\) is exact arithmetic. For a canonical optimal set, the Gram matrix has the explicit rank-one perturbation of \(4I\) given in the proof.

## Relationship to prior work

Ferguson, Mayeli, and Sothanaphan introduced the Riesz ratio as a quantitative invariant of exponential bases on finite abelian groups; their theory supplies the natural question but not this five-point binary value or equality classification. Seberry and Mitrouli established the order-five D-optimal sign matrix and its non-embedding in the order-eight Hadamard matrix. Brent and Osborn tabulated absolute minor values, including the **previously known total of \(43{,}008\)** determinant-48 five-minors in the order-sixteen Sylvester matrix. This pre-existing total is used as an external consistency check, not claimed as a new result. Huckle and Kravvaritis study spectra of leading principal Sylvester submatrices, a different restriction from arbitrary row/frequency selections.

The finding here is the **exact Riesz conditioning optimum**, its equivalence to determinant maximization for these five-character Fourier systems, and the **complete geometric description of all optimal frequency partners in every dimension \(d\ge4\)**. Published determinant totals, general existence/inequality results, and principal-submatrix spectra do not alone provide this spectral-ratio theorem. The originality comparison is subject to the bibliographic limitations below.

## Limitations

The theorem concerns five distinct support positions, five distinct frequencies, and the specified binary groups. It does not classify arbitrary other five-by-five sign-matrix Riesz extremizers, larger Fourier apertures, or continuous-phase Fourier systems. The exact finite lemma is proved computationally by a complete bounded enumeration; neither a symbolic classification of all four-by-four binary matrices nor independent external validation is claimed. The full text of Huckle and Kravvaritis was unavailable; its abstract concerns principally leading-principal submatrices, but this limits the bibliographic comparison. Other historical sources may contain an equivalent statement.

## References

1. S. Ferguson, A. Mayeli, and N. Sothanaphan, *Riesz bases of exponentials and multi-tiling in finite abelian groups*, arXiv:1904.04487 (first posted 9 April 2019), especially definitions and bounds on quantitative spectrality.
2. J. Seberry and M. Mitrouli, *Some remarks on Hadamard matrices*, *Cryptography and Communications* **2** (2010), 293–306. DOI: 10.1007/s12095-010-0036-9 (D-optimal five-minors and non-embedding in order eight).
3. R. P. Brent and J. H. Osborn, *On minors of maximal determinant matrices*, *Journal of Integer Sequences* **16** (2013), Article 13.4.2, arXiv:1208.3819 (known determinant-magnitude tables; order-sixteen data).
4. T. K. Huckle and C. D. Kravvaritis, *Properties of submatrices of Sylvester Hadamard matrices*, *Linear and Multilinear Algebra* **65** (2017), 1629–1642, DOI: 10.1080/03081087.2016.1250863 (first online 26 October 2016; abstract inspected).
