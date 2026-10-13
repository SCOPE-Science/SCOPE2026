# Conjugate-gradient positivity is dimension-protected exactly through two dimensions
## Finding
Consider exact-arithmetic conjugate gradients for
\[
Ax=b,
\]
started from \(x^0=0\), where \(A\) is a real symmetric positive-definite Stieltjes matrix and \(b\ge 0\) componentwise. In dimensions \(n\le 2\), every iterate produced before termination is componentwise nonnegative. This is sharp jointly in dimension and iteration number: the first CG iterate is nonnegative in every dimension, but dimension \(3\) already permits a negative component at the second iterate.

A concrete irreducible witness is
\[
A=\begin{pmatrix}
2&-2&0\
-2&4&-1\
0&-1&12
\end{pmatrix},
\qquad
b=\begin{pmatrix}2\4\1\end{pmatrix}.
\]
The matrix is Stieltjes because it is symmetric, has nonpositive off-diagonal entries, and its leading principal minors are \(2\), \(4\), and \(46\), all positive. Its inverse is
\[
A^{-1}=
\begin{pmatrix}
47/46&12/23&1/23\
12/23&12/23&1/23\
1/23&1/23&2/23
\end{pmatrix}>0,
\]
so in particular
\[
A^{-1}b=\frac1{23}\begin{pmatrix}96\73\8\end{pmatrix}>0.
\]
Nevertheless, the second CG iterate has a negative third component:
\[
x^{(2)}=\frac1{3219}\begin{pmatrix}9076\9469\-32\end{pmatrix}.
\]
Hence dimension \(3\) and iterate \(2\) are jointly minimal for classical CG to leave the nonnegative cone on this class.

## Assumptions and scope
A Stieltjes matrix here means a real symmetric positive-definite matrix with nonpositive off-diagonal entries. The statement concerns the standard unpreconditioned conjugate-gradient recurrence in exact arithmetic with zero initial vector. It is a componentwise sign statement; it does not contradict CG's usual monotonic decrease of the energy norm of the error. The result does not assert anything about finite-precision rounding, preconditioned CG, nonsymmetric matrices, or nonlinear conjugate-gradient methods.

## Proof
For every dimension, the first CG search direction is \(p_0=b\), and
\[
\alpha_0=\frac{b^{\mathsf T}b}{b^{\mathsf T}Ab}>0.
\]
Therefore
\[
x^{(1)}=\alpha_0 b\ge 0.
\]
So no sign loss can occur at iterate \(1\).

For \(n=1\), CG terminates at the exact solution after the first step, and the solution is nonnegative.

For \(n=2\), write
\[
A=\begin{pmatrix}a&-c\-c&d\end{pmatrix},
\qquad a>0,\quad d>0,\quad c\ge0,\quad ad-c^2>0.
\]
Then
\[
A^{-1}=\frac1{ad-c^2}
\begin{pmatrix}d&c\c&a\end{pmatrix}\ge0.
\]
The classical finite-termination property of exact-arithmetic CG gives the exact solution in at most two steps. Thus the only possible nonterminal iterate is \(x^{(1)}\ge0\), and the terminal iterate is \(A^{-1}b\ge0\). Hence every iterate produced by CG is nonnegative for every two-dimensional Stieltjes system.

For sharpness in dimension \(3\), use the displayed witness. Direct exact arithmetic gives
\[
Ab=\begin{pmatrix}-4\11\8\end{pmatrix},
\qquad
b^{\mathsf T}b=21,
\qquad
b^{\mathsf T}Ab=44,
\]
so
\[
\alpha_0=\frac{21}{44},
\qquad
x^{(1)}=
\begin{pmatrix}21/22\21/11\21/44\end{pmatrix}>0.
\]
The first residual and Fletcher--Reeves coefficient are
\[
r_1=
\begin{pmatrix}43/11\-5/4\-31/11\end{pmatrix},
\qquad
\beta_0=\frac{r_1^{\mathsf T}r_1}{b^{\mathsf T}b}=\frac{2285}{1936}.
\]
Thus
\[
p_1=r_1+\beta_0 b=
\begin{pmatrix}6069/968\420/121\-3171/1936\end{pmatrix},
\]
and the second step length is
\[
\alpha_1=\frac{r_1^{\mathsf T}r_1}{p_1^{\mathsf T}Ap_1}=\frac{20108}{67599}.
\]
Substitution into \(x^{(2)}=x^{(1)}+\alpha_1p_1\) yields exactly
\[
x^{(2)}=\frac1{3219}
\begin{pmatrix}9076\9469\-32\end{pmatrix},
\]
which proves sign loss. Since iterate \(1\) is universally nonnegative and dimensions \(1\) and \(2\) are protected, both minimality assertions follow.

## Verification
The included exact-rational verifier reconstructs the witness using Python's rational arithmetic, checks the three Sylvester minors, computes the inverse and exact solution, replays the first two CG steps, and asserts the negative third component of \(x^{(2)}\). The universal \(n\le2\) statement is proved analytically above; finite computation is used only for the explicit sharpness witness.

## Relationship to prior work
Hestenes and Stiefel's original conjugate-gradient paper gives the finite-termination property and develops the method for symmetric positive-definite systems. Ashby, Manteuffel, and Saylor emphasize CG's Krylov-subspace and norm-minimizing characterization and classify the subject under MSC \(65F10\). Standard Stieltjes-matrix theory supplies inverse positivity, while constrained conjugate-gradient variants explicitly modify directions to enforce nonnegative feasibility.

The present statement is different: it classifies the smallest dimension and smallest iteration at which the unmodified classical CG trajectory itself can leave the nonnegative cone for a Stieltjes system, despite a positive exact solution. Focused searches for componentwise positivity, monotonicity, inverse positivity, Stieltjes or \(M\)-matrix CG iterates, and positive-cone escape did not locate an implication-equivalent theorem. Nearby published results concern norm convergence, finite termination, preconditioning, or explicitly constrained variants rather than this sharp dimension/iteration boundary.

## Limitations
The proof is exact-arithmetic only. It does not claim that the displayed witness is optimally conditioned, nor does it classify all three-dimensional matrices or right-hand sides that preserve positivity. Older literature may contain componentwise monotonicity observations under terminology not recovered by the searches; this is the principal residual originality risk.

## References
1. M. R. Hestenes and E. Stiefel, “Methods of conjugate gradients for solving linear systems,” Journal of Research of the National Bureau of Standards 49 (1952), 409--436. DOI: 10.6028/jres.049.044.
2. S. F. Ashby, T. A. Manteuffel, and P. E. Saylor, “A Taxonomy for Conjugate Gradient Methods,” SIAM Journal on Numerical Analysis 27 (1990). DOI: 10.1137/0727091.
3. J. Huang, R. D. Haynes, and T.-Z. Huang, “Monotonicity of Perturbed Tridiagonal M-Matrices,” SIAM Journal on Matrix Analysis and Applications 33 (2012). DOI: 10.1137/100812483.
4. Q. Li, “A Conjugate Gradient Type Method for the Nonnegative Constraints Optimization Problems,” Journal of Applied Mathematics (2013), Article 986317. DOI: 10.1155/2013/986317.
