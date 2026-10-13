# Condition nine is the sharp fifth-iterate positivity frontier for spectrally tuned Nesterov acceleration
## Finding
Let \(A\) be a real symmetric positive-definite Stieltjes matrix, so \(A=A^{\mathsf T}\succ0\) and \(a_{ij}\le0\) for \(i\ne j\). For \(b\ge0\), define
\[
f(x)=\frac12x^{\mathsf T}Ax-b^{\mathsf T}x,
\qquad
\mu=\lambda_{\min}(A),\quad L=\lambda_{\max}(A),\quad \kappa=\frac L\mu,
\]
and run constant-parameter look-ahead Nesterov acceleration from \(x_{-1}=x_0=0\):
\[
y_k=x_k+\beta(x_k-x_{k-1}),\qquad
x_{k+1}=y_k-\frac1L(Ay_k-b),\qquad
\beta=\frac{\sqrt\kappa-1}{\sqrt\kappa+1}.
\]
Then \(x_1,x_2,x_3,x_4\ge0\) componentwise for every \(\kappa\ge1\). Moreover, \(x_5\ge0\) for every admissible \(A,b\) if and only if \(\kappa\le9\). Thus iteration five is the first possible universal loss of the nonnegative cone, and condition number nine is the sharp fifth-iterate frontier.

## Assumptions and scope
The statement concerns exact arithmetic, the displayed fixed parameters computed from the exact spectral endpoints, zero initialization, and symmetric positive-definite Stieltjes matrices. The order is componentwise. No claim is made for later iterates, nonzero initial states, variable or restarted momentum, inexact spectral bounds, nonsymmetric \(M\)-matrices, or general constrained acceleration.

The source literature supplies the standard constant-parameter Nesterov method and its strongly convex spectral tuning. The positivity frontier below is a finite-iterate statement specific to inverse-positive/Stieltjes quadratic systems.

## Proof
Put
\[
B=I-\frac AL.
\]
Because \(a_{ii}\le L\), \(a_{ij}\le0\) for \(i\ne j\), and the eigenvalues of \(A/L\) lie in \([1/\kappa,1]\), the matrix \(B\) is both entrywise nonnegative and positive semidefinite. Writing
\[
x_{m+1}=\frac1L p_m(B)b,
\]
the Nesterov recurrence gives
\[
p_m(z)=1+z\bigl((1+\beta)p_{m-1}(z)-\beta p_{m-2}(z)\bigr),
\]
with \(p_{-1}=0\) and \(p_0=1\). Direct induction yields
\[
\begin{aligned}
p_0(z)&=1,\\
p_1(z)&=1+(1+\beta)z,\\
p_2(z)&=1+z+(1+\beta)^2z^2,\\
p_3(z)&=1+z+(1-\beta^2)z^2+(1+\beta)^3z^3,\\
p_4(z)&=1+z+z^2+(1+\beta)^2(1-2\beta)z^3+(1+\beta)^4z^4.
\end{aligned}
\]
All coefficients through \(p_3\) are nonnegative for \(0\le\beta<1\), so entrywise nonnegativity of \(B\) implies \(x_1,x_2,x_3,x_4\ge0\). For \(p_4\), all coefficients are nonnegative exactly when \(\beta\le1/2\), which is equivalent to
\[
\frac{\sqrt\kappa-1}{\sqrt\kappa+1}\le\frac12
\quad\Longleftrightarrow\quad
\kappa\le9.
\]
This proves universal fifth-iterate positivity through condition number nine.

It remains to prove sharpness for every \(\kappa>9\), rather than only to exhibit one condition number. Let
\[
C=\begin{pmatrix}
1&1&0&0\\
1&2&1&0\\
0&1&2&1\\
0&0&1&1
\end{pmatrix}.
\]
The factorization \(C=V^{\mathsf T}V\), with columns \(e_1,e_1+e_2,e_2+e_3,e_3\), shows \(C\succeq0\); the alternating vector lies in its nullspace. Also \(\lambda_{\max}(C)<4\) by the maximum row-sum bound. Put \(r=1-1/\kappa\) and
\[
B_\varepsilon=\operatorname{diag}(\varepsilon C,r).
\]
Choose \(\varepsilon>0\) so that
\[
4\varepsilon<r,
\qquad
\varepsilon<\frac{2\beta-1}{6(1+\beta)^2}.
\]
Then \(B_\varepsilon\) is entrywise nonnegative and positive semidefinite, with minimum eigenvalue \(0\) and maximum eigenvalue \(r\). Therefore \(A=L(I-B_\varepsilon)\) is SPD Stieltjes with exact condition number \(\kappa\). Taking \(b=e_4\), the path structure gives \((C^j)_{14}=0\) for \(j=0,1,2\), while \((C^3)_{14}=1\) and \((C^4)_{14}=6\). Hence
\[
(x_5)_1=\frac{\varepsilon^3}L
\left[(1+\beta)^2(1-2\beta)+6(1+\beta)^4\varepsilon\right]<0.
\]
Because \(\kappa>9\) is equivalent to \(\beta>1/2\), the required positive \(\varepsilon\) always exists. This proves sharpness for every condition number above nine and completes the iff statement.

## Verification
A standalone exact-rational checker accompanies this result. It reconstructs the rational witness at \(\kappa=16\), verifies the Stieltjes sign pattern and positive definiteness by exact leading principal minors, replays five Nesterov iterates, checks the negative first component of \(x_5\), solves the linear system exactly to confirm a nonnegative true solution, and independently evaluates the degree-four matrix polynomial.

For the witness
\[
A=\begin{pmatrix}
398/25&-2/25&0&0&0\\
-2/25&396/25&-2/25&0&0\\
0&-2/25&396/25&-2/25&0\\
0&0&-2/25&398/25&0\\
0&0&0&0&1
\end{pmatrix},
\quad b=e_4,
\quad \kappa=16,
\]
the parameters are \(L=16\) and \(\beta=3/5\), and exact arithmetic gives
\[
(x_5)_1=-\frac{77}{31250000000}<0.
\]
The finite witness check supports the sharpness construction but is not used as a substitute for the quantified proof above.

## Relationship to prior work
Ghadimi, Feyzmahdavian, and Johansson state the constant-step Nesterov recurrence for strongly convex smooth objectives and the parameter
\[
\beta=\frac{\sqrt L-\sqrt\mu}{\sqrt L+\sqrt\mu}.
\]
Their analysis concerns convergence rates, not componentwise cone preservation. The closest published-finding-index match located in the overlap search concerns objective-value spikes for exact-parameter Nesterov acceleration; objective monotonicity does not imply, and is not implied by, entrywise nonnegativity of the iterates. A prior heavy-ball positivity result has the same numerical condition threshold nine but uses a different two-step recurrence; it does not imply the four safe Nesterov iterates, the degree-four Nesterov polynomial, or the fifth-iterate iff statement here.

## Limitations
The proof identifies the earliest iterate at which universal positivity can fail under this fixed Nesterov tuning, but it does not classify positivity at iterations six and later. The counterexample family is five-dimensional; minimal counterexample dimension is not asserted. The result is exact-arithmetic and depends on exact spectral endpoints. Older literature on monotone inertial iterations or positive systems could use terminology not recovered by the searches performed, so a residual bibliographic risk remains despite the statement-level comparisons.

## References
1. E. Ghadimi, H. R. Feyzmahdavian, and M. Johansson, “Global convergence of the Heavy-ball method for convex optimization,” arXiv:1412.7457, first public version 2014-12-23. Equation (4) states the constant-step Nesterov scheme; the paper lists primary MSC 90C26.
2. Y. Nesterov, *Introductory Lectures on Convex Optimization: A Basic Course*, Springer, 2004. Cited by the first reference for the strongly convex accelerated method.
