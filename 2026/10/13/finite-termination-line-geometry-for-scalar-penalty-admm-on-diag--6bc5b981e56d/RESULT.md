# Finite-termination line geometry for scalar-penalty ADMM on diagonal quadratic consensus

## Finding
For positive diagonal Hessians \(A=\operatorname{diag}(a_1,\ldots,a_n)\) and \(B=\operatorname{diag}(b_1,\ldots,b_n)\), scalar-penalty over-relaxed ADMM has a complete finite-termination criterion. Define
\[
s_i=a_i+b_i,\qquad p_i=a_ib_i.
\]
There is a scalar penalty \(\rho>0\) and a standard relaxation \(0<\alpha\le2\) that make the method finite for every initialization exactly when all points \((s_i,p_i)\) lie on one line
\[
p=\tau s-\rho^2
\]
with \(0<\tau\le\rho\). The relaxation is then
\[
\alpha=1+\frac{\tau}{\rho}.
\]

More precisely, the fixed-point state \((z,u)\) reaches its exact value in at most two full cycles from arbitrary initialization; the next \(x\)-update is exact. If the initial error already satisfies \(\rho\widetilde u^0=B\widetilde z^0\), one cycle makes \((z,u)\) exact.

## Assumptions and scope
Consider
\[
\min_{x,z\in\mathbb R^n}
\frac12x^{\mathsf T}Ax+c^{\mathsf T}x+
\frac12z^{\mathsf T}Bz+d^{\mathsf T}z
\quad\text{subject to }x=z,
\]
where \(A=\operatorname{diag}(a_i)\), \(B=\operatorname{diag}(b_i)\), and \(a_i,b_i>0\). The augmented term uses the ordinary Euclidean scalar penalty \(\rho I\), not a matrix-valued metric.

With scaled dual variable \(u\), the over-relaxed iteration is
\[
x^{k+1}=\arg\min_x\left(f(x)+\frac{\rho}{2}\|x-z^k+u^k\|_2^2\right),
\]
\[
\widehat x^{k+1}=\alpha x^{k+1}+(1-\alpha)z^k,
\]
\[
z^{k+1}=\arg\min_z\left(g(z)+\frac{\rho}{2}\|\widehat x^{k+1}-z+u^k\|_2^2\right),
\qquad
u^{k+1}=u^k+\widehat x^{k+1}-z^{k+1},
\]
with \(0<\alpha\le2\).

Finite termination for every initialization means that the affine error iteration for \((z,u)\) is nilpotent.

## Proof
Let tildes denote errors from the unique primal-dual solution. For one coordinate with curvatures \(a>0\) and \(b>0\), put
\[
p=\frac{\rho}{a+\rho},\qquad q=\frac{\rho}{b+\rho}.
\]
Then
\[
\widetilde x^+=p(\widetilde z-\widetilde u)
\]
and
\[
\widetilde{\widehat x}
=(\alpha p+1-\alpha)\widetilde z-\alpha p\,\widetilde u.
\]
Thus
\[
\begin{pmatrix}\widetilde z^+\\ \widetilde u^+\end{pmatrix}
=
M(a,b;\rho,\alpha)
\begin{pmatrix}\widetilde z\\ \widetilde u\end{pmatrix},
\]
where
\[
M=
\begin{pmatrix}
q(\alpha p+1-\alpha)&q(1-\alpha p)\\
(1-q)(\alpha p+1-\alpha)&(1-q)(1-\alpha p)
\end{pmatrix}.
\]
The rows are proportional, so \(\det M=0\). Its trace is
\[
\zeta(a,b;\rho,\alpha)
=
1-\frac{\alpha\rho(a+b)}{(\rho+a)(\rho+b)}.
\]
Cayley--Hamilton therefore gives
\[
M^2=\zeta M.
\]
Hence \(M\) is nilpotent exactly when \(\zeta=0\). If \(\zeta\ne0\), the nonzero eigenvalue persists for a suitable initial error and finite termination for every initialization is impossible. Since the diagonal problem is the direct product of these modes, finite termination for every initialization is equivalent to \(\zeta_i=0\) for every \(i\).

Solving \(\zeta_i=0\) gives
\[
\alpha
=
\frac{(\rho+a_i)(\rho+b_i)}{\rho(a_i+b_i)}
=
1+\frac{\rho^2+a_ib_i}{\rho(a_i+b_i)}.
\]
Set \(\tau=\rho(\alpha-1)\). A common \(\alpha\) exists exactly when
\[
a_ib_i=\tau(a_i+b_i)-\rho^2
\]
for every coordinate. Positivity implies \(\tau>0\), while \(\alpha\le2\) is equivalent to \(\tau\le\rho\). This proves the criterion and its converse.

The \(z\)-optimality equation also implies
\[
\rho\widetilde u^{k+1}=B\widetilde z^{k+1}.
\]
Thus one cycle puts any trajectory on the modal error relation, and if all \(\zeta_i=0\) the next modal error vanishes. Equivalently, all coordinate blocks satisfy \(M_i^2=0\).

For
\[
A=\operatorname{diag}(1,2),\qquad
B=\operatorname{diag}(5,6),\qquad
\rho=4,\qquad
\alpha=\frac{15}{8},
\]
the curvature points \((6,5)\) and \((8,12)\) lie on
\[
p=\frac72s-16.
\]
The exact modal matrices are
\[
M_1=
\begin{pmatrix}
5/18&-2/9\\
25/72&-5/18
\end{pmatrix},
\qquad
M_2=
\begin{pmatrix}
3/20&-1/10\\
9/40&-3/20
\end{pmatrix},
\]
and \(M_1^2=M_2^2=0\).

## Verification
The embedded `verify.py` uses exact rational arithmetic. It reconstructs the modal matrices, verifies their squares are zero, checks the line relation and modal factors, and replays the affine witness.

For \(c=(-6,-8)^{\mathsf T}\), \(d=0\), and \(z^0=u^0=0\),
\[
x^\star=z^\star=(1,1)^{\mathsf T},\qquad
u^\star=(5/4,3/2)^{\mathsf T}.
\]
The first \(x\)-update is \(x^1=(6/5,4/3)^{\mathsf T}\), while the first completed cycle gives
\[
z^1=(1,1)^{\mathsf T},\qquad u^1=(5/4,3/2)^{\mathsf T}.
\]
The second \(x\)-update is exactly \(x^\star\).

The computation replays the witness only. The all-dimensional statement is proved by the modal argument above.

## Relationship to prior work
Ghadimi, Teixeira, Shames, and Johansson analyze over-relaxed ADMM for an \(\ell_2\)-regularized quadratic with second Hessian \(\delta I\). Their Theorem 2 and Appendix C give
\[
\zeta_R
=
1-\frac{\alpha\rho(\lambda_i(Q)+\delta)}
{(\rho+\lambda_i(Q))(\rho+\delta)}
\]
and zero factor at \(\rho=\delta\), \(\alpha=2\). This is an isotropic modal-annihilation case. Their Remark 2 also normalizes a general positive-definite second quadratic by a change of variables. In original coordinates that normalization changes the augmented metric, so it does not retain the scalar Euclidean penalty fixed here.

The present result keeps the penalty scalar in the original coordinates and classifies exactly when heterogeneous diagonal curvature pairs can still be annihilated by one common \(\rho\) and \(\alpha\).

Giselsson and Boyd study tight linear rate bounds and metric selection for Douglas--Rachford splitting and ADMM. The inspected text explains why changing the metric can improve conditioning, but it does not state a scalar-Euclidean finite-termination classification for two heterogeneous diagonal Hessians.

## Limitations
The theorem assumes simultaneous diagonal structure in the coordinates where the augmented penalty is scalar Euclidean. It does not classify noncommuting Hessians, singular Hessians, iteration-varying parameters, or matrix-valued penalties. It is also an exact-arithmetic result; near the line condition, cancellation can be sensitive to curvature errors.

Residual originality risk remains that older Douglas--Rachford or quadratic-splitting literature may encode the same scalar-penalty condition under a different spectral parametrization.

## References
1. E. Ghadimi, A. Teixeira, I. Shames, and M. Johansson, “Optimal parameter selection for the alternating direction method of multipliers (ADMM): quadratic problems.” Optimization Online, first public posting 2013-06-10; arXiv:1306.2454; later DOI 10.1109/TAC.2014.2354892.
2. P. Giselsson and S. Boyd, “Linear Convergence and Metric Selection for Douglas-Rachford Splitting and ADMM.” arXiv:1410.8479; later DOI 10.1109/TAC.2016.2564160.
3. Y. Ouyang, Y. Chen, G. Lan, and E. Pasiliao Jr., “An Accelerated Linearized Alternating Direction Method of Multipliers.” SIAM Journal on Imaging Sciences 8 (2015), 644–681, DOI 10.1137/14095697X; primary MSC 90C25.
