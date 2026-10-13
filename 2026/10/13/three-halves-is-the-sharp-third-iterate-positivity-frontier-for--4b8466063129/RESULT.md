# Three halves is the sharp third-iterate positivity frontier for convergent weighted Jacobi
## Finding
Let \(A=A^{\mathsf T}>0\) be a Stieltjes matrix, \(D=\operatorname{diag}(A)\), \(b\ge0\), and start weighted Jacobi from \(x^{(0)}=0\): \[x^{(k+1)}=x^{(k)}+\omega D^{-1}(b-Ax^{(k)}).\] Assume the iteration converges, equivalently \(0<\omega<2/\lambda_{\max}(D^{-1/2}AD^{-1/2})\). Then \(x^{(1)}\ge0\) and \(x^{(2)}\ge0\) for every such system, and the third iterate is nonnegative for every such system and every \(b\ge0\) if and only if \(0<\omega\le3/2\). Thus \(3/2\) is the sharp universal third-iterate positivity frontier. Moreover, iteration three and dimension two are jointly minimal for positivity loss: every convergent one-dimensional weighted-Jacobi orbit from zero stays nonnegative, while for every \(3/2<\omega<2\) there is a convergent two-dimensional SPD Stieltjes system with \(b\ge0\) whose third iterate has a negative component. A concrete witness is \(\omega=8/5\), \(A=\begin{pmatrix}1&-1/5\\-1/5&1\end{pmatrix}\), and \(b=(0,1)^{\mathsf T}\), for which \(x^{(1)}=(0,8/5)^{\mathsf T}\), \(x^{(2)}=(64/125,16/25)^{\mathsf T}\), and \(x^{(3)}=(-64/625,4312/3125)^{\mathsf T}\), even though the iteration converges and \(A^{-1}b=(5/24,25/24)^{\mathsf T}>0\).

## Assumptions and scope
A Stieltjes matrix here means a real symmetric positive definite matrix with nonpositive off-diagonal entries. The diagonal matrix \(D=\operatorname{diag}(A)\) is therefore positive. The statement concerns the classical fixed-weight weighted-Jacobi iteration from the zero initial vector and componentwise nonnegative right-hand sides. Convergence is the usual linear stationary-iteration condition. No claim is made for nonsymmetric \(M\)-matrices, block Jacobi, varying weights, nonzero initial vectors, or iterates after the third except for the one-dimensional minimality statement.

## Proof
Set
\[
C=D^{-1/2}AD^{-1/2},\qquad y^{(k)}=D^{1/2}x^{(k)},\qquad c=D^{-1/2}b.
\]
Then \(C\) is again SPD Stieltjes, has unit diagonal, and \(c\ge0\). The iteration becomes
\[
y^{(k+1)}=y^{(k)}+\omega(c-Cy^{(k)}),\qquad y^{(0)}=0.
\]
Consequently
\[
y^{(k)}=q_k(C)c,
\qquad
q_k(\lambda)=\omega\sum_{j=0}^{k-1}(1-\omega\lambda)^j
=\frac{1-(1-\omega\lambda)^k}{\lambda}.
\]
Convergence is equivalent to \(\rho(I-\omega C)<1\), hence \(0<\omega<2/\lambda_{\max}(C)\). Since \(\operatorname{tr}C=n\), one has \(\lambda_{\max}(C)\ge1\), so every convergent instance has \(0<\omega<2\).

For the first two iterates,
\[
q_1(C)=\omega I,
\qquad
q_2(C)=2\omega I-\omega^2C.
\]
Thus \(q_1(C)\ge0\) entrywise. For \(q_2(C)\), every off-diagonal entry is nonnegative because \(c_{ij}\le0\), and every diagonal entry is \(\omega(2-\omega)>0\). Hence the first two iterates are nonnegative for every convergent instance.

For the third iterate,
\[
q_3(C)=3\omega I-3\omega^2C+\omega^3C^2.
\]
Write \(g_{ij}=-c_{ij}\ge0\) for \(i\ne j\). Since \(c_{ii}=1\),
\[
(C^2)_{ij}=-2g_{ij}+\sum_{\ell\ne i,j}g_{i\ell}g_{\ell j},
\]
and therefore, for \(i\ne j\),
\[
(q_3(C))_{ij}
=\omega^2\left((3-2\omega)g_{ij}+\omega\sum_{\ell\ne i,j}g_{i\ell}g_{\ell j}\right).
\]
If \(0<\omega\le3/2\), this is nonnegative. The diagonal entries are strictly positive because convergence gives \(r=1-\omega\lambda\in(-1,1)\) for every eigenvalue \(\lambda\) of \(C\), while
\[
q_3(\lambda)=\omega(1+r+r^2)>0.
\]
Thus \(q_3(C)\) is SPD and has positive diagonal, so it is entrywise nonnegative. Hence \(y^{(3)}\ge0\), and positive diagonal scaling gives \(x^{(3)}\ge0\).

Sharpness is already two-dimensional. Fix any \(3/2<\omega<2\) and choose
\[
C_a=\begin{pmatrix}1&-a\\-a&1\end{pmatrix},
\qquad
0<a<\min\left\{1,\frac{2}{\omega}-1\right\}.
\]
Then \(C_a\) is SPD and \(\lambda_{\max}(C_a)=1+a<2/\omega\), so weighted Jacobi converges. The path sum in the preceding off-diagonal formula is empty, and
\[
(q_3(C_a))_{12}=a\omega^2(3-2\omega)<0.
\]
Taking \(b=e_2\) produces a negative first component at the third iterate. In one dimension, convergence means \(0<\omega<2\) and
\[
q_k(1)=1-(1-\omega)^k>0
\]
for every \(k\ge1\), so no one-dimensional counterexample exists. This proves both sharpness and joint minimality.

For the concrete rational witness \(\omega=8/5\), \(a=1/5\), the eigenvalues of \(A\) are \(4/5\) and \(6/5\), so the iteration eigenvalues are \(-7/25\) and \(-23/25\), both strictly inside the unit disk. Exact substitution yields the iterates and positive exact solution stated above.

## Verification
The accompanying `verify.py` uses only exact rational arithmetic. It reconstructs the rational witness, verifies the iteration matrix has spectral radius below one, reproduces \(x^1\), \(x^2\), \(x^3\), and \(A^-1b\), and checks the polynomial coefficient identity behind the universal off-diagonal formula. The finite checker is supplementary: the universal claim is proved by the displayed algebra and inequalities, not by enumeration.

## Relationship to prior work
Weighted Jacobi, also called damped or relaxed Jacobi, is classical. Imakura, Sakurai, Sumiyoshi, and Matsufuru explicitly write the recurrence \(x_{k+1}=x_k+\omega D^-1(b-Ax_k)\), identify the weight parameter, and analyze convergence through the spectral radius of \(I-\omega D^-1A\). Li and Sun study Jacobi-type iterations for \(Z\)-matrices and \(M\)-matrices, with convergence and spectral-radius comparisons as their stated focus. De Sterck et al. explicitly note that underrelaxed weighted Jacobi with weight in \((0,1)\) preserves positivity for a singular \(M\)-matrix because its update is a nonnegative combination.

Those results supply the classical method, matrix-splitting setting, and the familiar underrelaxed positivity mechanism. They do not imply the present overrelaxed finite-iterate statement: the exact universal \(3/2\) threshold arises from the third-degree polynomial and the length-two path term in \(C^2\). Searches under the equivalent diagonally preconditioned Richardson formulation and against published weighted-Jacobi norm-safety results likewise found no implication-equivalent third-iterate coordinatewise threshold.

## Limitations
The theorem is a finite-iterate order-preservation statement, not a claim that all weighted-Jacobi iterates remain nonnegative for \(\omega\le3/2\). The counterexample proves failure of a universal third-iterate guarantee above \(3/2\), not failure for every matrix. The proof relies on symmetry, positive definiteness, and the Stieltjes sign pattern after diagonal normalization. A residual literature risk remains that an older matrix-iteration or nonnegative-splitting source states the same finite-iterate threshold under different terminology.

## References
1. A. Imakura, T. Sakurai, K. Sumiyoshi, and H. Matsufuru, “A parameter optimization technique for a weighted Jacobi-type preconditioner,” *JSIAM Letters* 4 (2012), 41–44. DOI: 10.14495/jsiaml.4.41. Publicly available on J-STAGE on 2012-12-24.
2. W. Li and W. Sun, “Modified Gauss–Seidel type methods and Jacobi type methods for Z-matrices,” *Linear Algebra and its Applications* 317 (2000), 227–240. DOI: 10.1016/S0024-3795(00)00140-3.
3. H. De Sterck, T. A. Manteuffel, S. F. McCormick, K. Miller, J. Pearson, J. Ruge, and G. Sanders, “Smoothed aggregation multigrid for Markov chains,” accepted manuscript for *SIAM Journal on Scientific Computing* (2009), especially the weighted-Jacobi positivity observation in its Section 3.
