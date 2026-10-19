# Exact hub-weighted pair sampling on positive-definite star Gram systems

## Finding
For every integer \(n\ge3\) and real \(0<u<1/\sqrt n\), let
\[
G=\begin{pmatrix}1&u\mathbf1_n^{\mathsf T}\\u\mathbf1_n&I_n\end{pmatrix}.
\]
Consider exact two-coordinate minimization of an ordinary full-column-rank least-squares objective whose column Gram matrix equals \(G\). Among **all** fixed probability laws on unordered coordinate pairs, the smallest worst-initial-error conditional expected squared prediction-error contraction factor is \(1-\Lambda\), where
\[
\delta=1-u^2,\quad k=\frac{1-nu^2}{n\delta},\quad t=\frac{(n-1)(1-2u^2)}{n\delta},
\]
\[
\Lambda=\frac{\frac2n+t-\frac{2u(n-1)}{n\sqrt\delta}}{2\bigl(1+\frac{t^2}{4k}\bigr)},\qquad
\theta_*=1-\frac{t\Lambda}{2k}.
\]
An optimal law puts total probability \(\theta_*\) uniformly over the \(n\) hub–leaf pairs and total probability \(1-\theta_*\) uniformly over the \(\binom n2\) leaf–leaf pairs. It is the **unique** optimum among leaf-permutation-invariant laws, and \(0<\theta_*<1\).

The near-singular limit is
\[
\lim_{u\uparrow1/\sqrt n}\theta_* =\frac{2}{1+\sqrt{n-1}}.
\]
As \(n\to\infty\), this mass is of order \(n^{-1/2}\), compared with \(2/(n+1)\) for uniform pair sampling (order \(n^{-1}\)).

## Assumptions and scope
The Gram matrix is real positive definite because its Schur complement is \(1-nu^2>0\). Let \(A\) be any real full-column-rank matrix with \(A^{\mathsf T}A=G\), and let \(b\) be any real vector (consistent or inconsistent). The exact least-squares minimizer is \(x_*\). Each iteration chooses an unordered pair \(J\subset\{0,1,\ldots,n\}\), \(|J|=2\), independently according to the same fixed law, and minimizes \(\|Ax-b\|_2^2\) exactly along those coordinates. The objective is the supremum over nonzero errors \(e=x-x_*\) of \(\mathbb E\|Ae^+\|_2^2/\|Ae\|_2^2\) for one iteration. No specific distribution on \(b\) or initial error is assumed.

## Proof
For a pair \(J\), let \(E_J\) select its coordinates. Exact pair minimization sends \(e\) to \(e-E_J(E_J^{\mathsf T}GE_J)^{-1}E_J^{\mathsf T}Ge\). Setting \(z=G^{1/2}e\), the reduction in squared prediction error is \(z^{\mathsf T}P_Jz\), with orthogonal projector \(P_J=G^{1/2}E_J(E_J^{\mathsf T}GE_J)^{-1}E_J^{\mathsf T}G^{1/2}\). Thus the sharp expected contraction is \(1-\lambda_{\min}(\sum_Jp_JP_J)\).

Every permutation of the leaves preserves \(G\) and conjugates the projectors. Average any candidate law over this permutation group. Concavity and conjugation invariance of the minimum eigenvalue show that symmetrization cannot worsen its sharp contraction. Consequently an optimizer exists among laws assigning total hub–leaf mass \(\theta\in[0,1]\) and the remaining leaf–leaf mass \(1-\theta\), uniformly within each orbit.

Define \(B=\sum_Jp_JE_J(E_J^{\mathsf T}GE_J)^{-1}E_J^{\mathsf T}\). Since \(G\) is positive definite, the projector average \(G^{1/2}BG^{1/2}\) has the eigenvalues of \(BG\). For a symmetric law,
\[
B=\begin{pmatrix}
\theta/\delta&-\theta u\mathbf1_n^{\mathsf T}/(n\delta)\\
-\theta u\mathbf1_n/(n\delta)&[\theta/(n\delta)+2(1-\theta)/n]I_n
\end{pmatrix}.
\]
On the \((n-1)\)-dimensional leaf-contrast subspace, \(BG\) has eigenvalue
\[
L=\frac{\theta}{n\delta}+\frac{2(1-\theta)}n.
\]
On the hub and uniform-leaf subspace its other two eigenvalues are roots of
\[
\lambda^2-T(\theta)\lambda+K(\theta)=0,\quad
T(\theta)=\frac2n+t\theta,\quad K(\theta)=k\theta(2-\theta).
\]
Write the smaller root as \(\lambda_-(\theta)\). Substitution shows
\[
L^2-T(\theta)L+K(\theta)=-\frac{\theta u^2}{n\delta^2}\left(2(n-2)\delta+\theta[(n-4)u^2-(n-3)]\right)<0
\]
for \(0<\theta\le1\): the parenthesis is affine in \(\theta\) and strictly positive at both endpoints, where it equals \(2(n-2)\delta\) and \(n-1-nu^2\). Hence \(\lambda_-(\theta)<L\), and the desired minimum eigenvalue equals \(\lambda_-(\theta)\) throughout; at \(\theta=0\) it is zero.

The function \(\lambda_-(\theta)\) is concave because it is the minimum eigenvalue of an affine family of symmetric matrices. It is analytic on \((0,1)\), has strictly positive right derivative at zero and strictly negative left derivative at one: at \(\theta=1\) the two roots are \(1,k\), with \(k<1\), and implicit differentiation gives derivative \(tk/(k-1)<0\). Concavity, analyticity, and unequal endpoint values rule out a plateau of maximizers, so the maximizer is unique and interior.

Differentiating \(\lambda^2-T(\theta)\lambda+K(\theta)=0\) at that maximum yields \(t\lambda=2k(1-\theta)\). Eliminate \(\theta=1-t\lambda/(2k)\) to obtain
\[
\left(1+\frac{t^2}{4k}\right)\lambda^2-
\left(\frac2n+t\right)\lambda+k=0.
\]
Its smaller root is \(\Lambda\), because the discriminant simplifies exactly to \(4u^2(n-1)^2/(n^2\delta)\). The maximizer is therefore \(\theta_*\), as stated. This proves global optimality by the symmetrization reduction, without requiring uniqueness of nonsymmetric laws.

Finally, expand \(\Lambda/k\) as \(k\downarrow0\) with \(u\uparrow1/\sqrt n\) and substitute in \(\theta_*=1-t\Lambda/(2k)\); elementary cancellation yields \(2/(1+\sqrt{n-1})\). Uniform sampling assigns hub–leaf mass \(n/\binom{n+1}{2}=2/(n+1)\). The respective large-\(n\) orders follow immediately.

## Verification
The accompanying standalone Python program compares the explicit spectral formulas with direct \((n+1)\)-dimensional projector averages for 108 independently chosen star matrices, checks 432 spectral evaluations and 108 numerical optimum comparisons (540 assertions in all), and checks the near-singular limiting formula numerically. These are finite tests supporting the algebra, not proofs of the quantified theorem. Exact symbolic substitutions also give, for \(n=3\), \(u=1/2\),
\[
\Lambda=\frac{5-2\sqrt3}{13},\qquad \theta_* =\frac{3+4\sqrt3}{13},
\]
while uniform pairs give \(\lambda_{\min}=(8-\sqrt{37})/18\), strictly smaller than \(\Lambda\).

## Relationship to prior work
Xie and Yang's 2026 framework permits arbitrary static coordinate-batch laws and offers scale-invariant convergence bounds and learned sampling designs. The present result solves analytically the sharp one-step spectral probability-design problem for a symmetric star Gram family; it is not a general convergence bound or a claim of optimal long-run sampling. General sketch-and-project and coordinate-sampling theory gives the projector representation but does not by itself state this closed-form hub-mass law or its near-singular large-star scaling. Closely related explicit optimal *single-coordinate* sampling results do not imply the optimal *pair-coordinate* design without a separate analysis of rank-two projectors.

## Limitations
This is an exact-arithmetic, one-step, fixed-iid-law result for star Gram matrices. There is no claim that every optimal law must be permutation invariant, no extension to general Gram matrices, and no implication that minimizing one-step worst-case error minimizes runtime or asymptotic convergence exponents. Full-text comparison with every plausible source has not been possible; bibliographic overlap remains a risk.

## References
Xie, D.-Y. and Yang, X., *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685, first public October 3, 2026.

Gower, R. M. and Richtárik, P., *Randomized iterative methods for linear systems*, SIAM Journal on Matrix Analysis and Applications 36 (2015), 1660–1690.
