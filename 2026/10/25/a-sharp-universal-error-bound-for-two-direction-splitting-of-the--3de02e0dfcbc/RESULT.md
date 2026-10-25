# A sharp universal error bound for two-direction splitting of the first matrix exponential integral

## Finding

Let \(h>0\), let \(A\in\mathbb R^{m\times m}\) and \(B\in\mathbb R^{n\times n}\) be arbitrary real symmetric negative-semidefinite matrices, and define
\[
\varphi_1(X)=\int_0^1e^{tX}\,dt,\qquad K=A\otimes I_n+I_m\otimes B.
\]
For the two-direction product approximation \(S_h=\varphi_1(hA)\otimes\varphi_1(hB)\), define its exact error \(D_h=\varphi_1(hK)-S_h\). Then
\[
0\preceq D_h\preceq C_* I_{mn},\qquad \|D_h\|_2\le C_* =0.06613989397537867\ldots .
\]
This constant is **optimal simultaneously over every pair of finite matrix dimensions, all such generators, and every positive time step**. The equality \(\|D_h\|_2=C_*\) occurs exactly when both spectra contain \(-t_*/h\), where \(t_*=3.2453044817087544\ldots\) is the unique positive zero of
\[
H(t)=(4-t)e^{2t}-(4t+8)e^t+2t^2+5t+4.
\]
When \(A\) and \(B\) are both negative definite, \(D_h\) is positive definite; for negative-semidefinite factors, its kernel is precisely the span of joint tensor eigenvectors on which at least one factor has eigenvalue zero.

In addition, on scalar factors \(A=B=-t/h\), the fraction of the exact \(\varphi_1\) action retained by the product is
\[
\frac{\varphi_1(-t)^2}{\varphi_1(-2t)}=\frac{2(1-e^{-t})}{t(1+e^{-t})}\longrightarrow0\quad(t\to\infty).
\]
Thus there is no strictly positive universal *relative* lower bound for the product approximation, even though its absolute error has the finite sharp ceiling above.

## Assumptions and scope

All matrices are real, finite-dimensional, symmetric, and negative semidefinite. The tensor product is the ordinary Kronecker product; \(\preceq\) is the Loewner order. No commutation of the physical matrices \(A\) and \(B\) is needed because their lifted tensor operators commute. The parameter \(h\) is strictly positive. Matrix functions are exact analytic matrix functions: no quadrature, roundoff, or other implementation error is included. The conclusion is about the isolated \(\varphi_1\)-action approximation, not convergence of an entire nonlinear exponential time-integrator.

## Proof

**1. Spectral reduction and sign.** Write \(-hA=U\operatorname{diag}(a_1,\ldots,a_m)U^{\mathsf T}\) and \(-hB=V\operatorname{diag}(b_1,\ldots,b_n)V^{\mathsf T}\) with \(a_i,b_j\ge0\) and orthogonal \(U,V\). Conjugation by \(U\otimes V\) makes \(D_h\) diagonal, with entry
\[
F(a,b)=\varphi_1(-(a+b))-\varphi_1(-a)\varphi_1(-b),\qquad a,b\ge0.
\]
For a uniform random variable \(T\) on \([0,1]\), the integral defining \(\varphi_1\) gives
\[
F(a,b)=\operatorname{Cov}(e^{-aT},e^{-bT}).
\]
The covariance is nonnegative because both functions of \(T\) are nonincreasing; the identity
\[
2F(a,b)=\int_0^1\!\int_0^1
(e^{-at}-e^{-as})(e^{-bt}-e^{-bs})\,dt\,ds
\]
makes it strictly positive for \(a,b>0\) and zero when either parameter vanishes. This proves the Loewner sign and the kernel description.

**2. Reduction of the sharp constant to one variable.** By Cauchy–Schwarz,
\[
0\le F(a,b)\le\sqrt{W(a)W(b)}\le\sup_{t>0}W(t),
\quad W(t)=\operatorname{Var}(e^{-tT})
=\frac{1-e^{-2t}}{2t}-\left(\frac{1-e^{-t}}{t}\right)^2.
\]
Here \(W(t)\to0\) as \(t\downarrow0\) and as \(t\to\infty\); its maximum is attained at a positive finite point. For \(a=b=t\), equality holds throughout the Cauchy–Schwarz bound, so the global two-parameter supremum is *exactly* \(\max_{t>0}W(t)\). If \(a,b>0\), equality in Cauchy–Schwarz requires the centered functions \(e^{-aT}\) and \(e^{-bT}\) to be proportional. Differentiating this proportionality twice with respect to \(T\) shows \(a=b\). Once uniqueness of the one-variable maximizer is proved, the equality characterization follows.

**3. Uniqueness of the maximizer.** Direct differentiation, valid for \(t>0\), gives
\[
2t^3W'(t)=e^{-2t}H(t),\qquad
H(t)=(4-t)e^{2t}-(4t+8)e^t+2t^2+5t+4.
\]
The function \(H\) and its first two derivatives vanish at zero, and
\[
H'''(t)=-4e^t J(t),\qquad
J(t)=(2t-5)e^t+t+5.
\]
Moreover,
\[
J(0)=0,\quad J'(0)=-2,\quad
J'(t)=(2t-3)e^t+1,\quad J''(t)=(2t-1)e^t.
\]
Since \(J''\) changes sign exactly once, from negative to positive at \(t=1/2\), and \(J'\to+\infty\), the derivative \(J'\) has exactly one positive zero. Hence \(J\), initially decreasing from zero and eventually tending to \(+\infty\), has exactly one positive zero. Therefore \(H'''\) is positive and then negative, changing sign once. Since \(H''(0)=H'(0)=H(0)=0\), while each of \(H'',H',H\) tends to \(-\infty\) as \(t\to\infty\), successively integrating this single-change sign pattern proves that each of \(H'',H'\), and \(H\) has precisely one positive zero and is positive before, negative after that zero. Consequently \(W'\) changes from positive to negative at exactly one positive point \(t_*\). Thus \(t_*\) is the unique global maximizer.

**4. Sharpness and asymptotics.** Choosing scalar \(A=B=-t_*/h\) gives \(\|D_h\|_2=W(t_*)=C_*\). The same equality is attainable in dimensions at least two by placing \(-t_*/h\) in the spectrum of each factor. The displayed scalar relative ratio follows by cancellation of \(\varphi_1(-t)=(1-e^{-t})/t\). Finally, for *fixed* \(A\) and \(B\), Taylor expansion under the integral yields
\[
D_h=\frac{h^2}{12}(A\otimes B)+O(h^3)\quad(h\downarrow0)
\]
in operator norm. The uniform ceiling does not decay with \(h\) if the generators themselves vary with \(h\): \(A_h=B_h=-t_*/h\) gives the same error \(C_*\) at every \(h>0\).

## Verification

The independent standard-library script `verify.py` provides exact-rational Taylor-series interval arithmetic for \(e^t\). It rigorously brackets the unique positive zero of \(H\) between \(3.245304481708\) and \(3.245304481710\), and the sharp constant between \(0.066139893974\) and \(0.066139893977\). Its stronger printed enclosures are reproduced by running `python3 verify.py`. It also runs a supplementary scalar parameter-grid comparison of positivity and the Cauchy–Schwarz inequality. These finite checks do not replace the all-parameter proof above; the uniqueness, global inequality, and equality cases are analytical.

## Relationship to prior work

Caliari and Cassini introduced direction splitting of matrix \(\varphi\)-functions for Kronecker-sum exponential integrators [1]. Their Theorem 1, equation (14), establishes the \(O(h^2)\) approximation \(\varphi_1(hK)=\varphi_1(hA)\otimes\varphi_1(hB)+O(h^2)\) for fixed generators; Sections 3–5 develop efficient implementations and numerical experiments. The present result does **not** claim that approximation or its local order as new. Instead it determines, in the self-adjoint dissipative class, the global sign, **sharp stiffness-uniform absolute norm constant and equality spectra**, and the unrestricted relative underestimation limit. Neither the global sharp constant nor the equality characterization appears in the inspected full text of [1].

Muñoz-Matute, Pardo, and Calo [2] recover \(\varphi\)-actions via a Sylvester-equation method built from Kronecker products. Caliari, Cassini, and Zivcovich [3] and Croci and Muñoz-Matute [4] use quadrature of the integral formula, not the uncorrected two-factor product whose worst-case error is bounded here. Their accessible bibliographic summaries do not resolve the precise sharp bound; their full papers were not examined in this review. The key covariance and Cauchy–Schwarz inequalities are classical tools, not new claims.

## Limitations

The universal constant is proved only for **two** symmetric negative-semidefinite factor matrices and the first \(\varphi\)-function; it is not a bound for three or more tensor factors, other \(\varphi_\ell\), nonsymmetric generators, a full numerical solution, or relative error for arbitrary forcing vectors. Loewner ordering of the two matrix-function operators does not imply entrywise ordering in an arbitrary basis. The theorem gives a worst-case operator-error bound rather than an assertion that a given time integrator attains it. Priority over all literature, including independently formulated probability inequalities, has not been independently established.

## References

[1] M. Caliari and F. Cassini, “Direction splitting of \(\varphi\)-functions in exponential integrators for \(d\)-dimensional problems in Kronecker form,” arXiv:2304.02327 (first publicly posted 2023-04-05); Journal of Approximation Software 1(1), 2024. https://arxiv.org/abs/2304.02327 ; https://doi.org/10.13135/3103-1935/10813 .

[2] J. Muñoz-Matute, D. Pardo, and V. M. Calo, “Exploiting the Kronecker product structure of \(\varphi\)-functions in exponential integrators,” International Journal for Numerical Methods in Engineering 123 (2022), 2142–2161. https://doi.org/10.1002/nme.6929 .

[3] M. Caliari, F. Cassini, and F. Zivcovich, “A \(\mu\)-mode approach for exponential integrators: actions of \(\varphi\)-functions of Kronecker sums,” arXiv:2210.07667. https://arxiv.org/abs/2210.07667 .

[4] M. Croci and J. Muñoz-Matute, “Exploiting Kronecker structure in exponential integrators: fast approximation of the action of \(\varphi\)-functions of matrices via quadrature,” arXiv:2211.00696. https://arxiv.org/abs/2211.00696 .
