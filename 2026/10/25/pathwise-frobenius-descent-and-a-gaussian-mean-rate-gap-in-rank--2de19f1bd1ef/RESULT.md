# Pathwise Frobenius descent and a Gaussian mean-rate gap in rank-one funNyström

## Finding
For a fixed nonzero seed and any nonnegative nondecreasing scalar function \(f\), vanishing at zero and with convex reciprocal profile \(t\mapsto f(1/t)\), the squared Frobenius error of its rank-one power-Nyström approximation decreases monotonically with the power. This applies, in particular, to every nonnegative operator-monotone function \(f\) with \(f(0)=0\). Every seed whose positive-eigenvalue spectral support contains at least two distinct points has strict descent for a nonconstant operator-monotone \(f\).

In the positive-definite two-dimensional Gaussian model, with \(A=\operatorname{diag}(a,b)\), \(a>b>0\), and independent standard normal seed coordinates, the **exact** mean squared Frobenius error for \(f(t)=t\) is
\[
\mathbb E\|A-N_q\|_F^2
=b^2+\frac{r\,c\,(a-b)\,[a+3b+2rc(a+b)]}{2(1+rc)^2},
\quad r=(b/a)^q,\quad c=\sqrt{a/b}.
\]
The mean excess is asymptotic to \(c(a-b)(a+3b)(b/a)^q/2\). By contrast, for almost every fixed Gaussian seed the excess is asymptotic to \(2a(a-b)(\omega_2/\omega_1)^2(b/a)^{2q}\): averaging halves the exponential decay exponent.

Reciprocal convexity is a substantive boundary, not a consequence of scalar monotonicity: an explicit continuous nondecreasing \(f\) and a two-dimensional seed give a strict *increase* of the squared error between powers one and two.

## Assumptions and scope
Let \(A\ne0\) be a real symmetric positive-semidefinite \(n\times n\) matrix, let \(\omega\in\mathbb R^n\) satisfy \(A\omega\ne0\), and take every real \(q\ge1\). Real powers use spectral functional calculus. The rank-one power-Nyström approximation is
\[
N_q=\frac{A^q\omega\omega^{\mathsf T}A^q}{\omega^{\mathsf T}A^{2q-1}\omega},
\qquad F_q=f(N_q).
\]
The denominator is strictly positive; no pseudoinverse ambiguity occurs. Assume \(f:[0,\infty)\to[0,\infty)\) is continuous, nondecreasing, \(f(0)=0\), and \(\phi(t)=f(1/t)\) is convex for \(t>0\). The property includes all continuous nonnegative operator-monotone functions vanishing at zero, but also some functions outside that class, such as \(f(t)=t^2\). Exact arithmetic is assumed.

For strict descent additionally require \(f\) to be nonconstant operator monotone and the seed to meet at least two distinct positive eigenspaces. For the expected-error formula require \(n=2\), \(A=\operatorname{diag}(a,b)\), \(a>b>0\), \(f(t)=t\), and independent \(N(0,1)\) coordinates of \(\omega\).

## Proof
**1. Spectral reduction and a scalar Jensen inequality.** On positive eigenvalues \(a_i\) with nonzero seed weights \(z_i=\omega_i^2\), put
\[
p_i(q)=\frac{a_i^{2q}z_i}{\sum_j a_j^{2q}z_j},\qquad
\lambda_q=\left(\sum_i\frac{p_i(q)}{a_i}\right)^{-1},\qquad
u_q=\frac{A^q\omega}{\|A^q\omega\|_2}.
\]
Terms in the nullspace are absent. Direct substitution gives \(N_q=\lambda_q\nu_q\nu_q^{\mathsf T}\) and \(f(N_q)=f(\lambda_q)\nu_q\nu_q^{\mathsf T}\). Set \(T_q=f(\lambda_q)\), \(U_q=\sum_i p_i(q)f(a_i)\), and \(K=\operatorname{tr}f(A)^2\). The exact error is
\[
\mathcal E_q=\|f(A)-f(N_q)\|_F^2=K+T_q^2-2T_qU_q.
\]
Since \(\lambda_q^{-1}=\sum_i p_i(q)/a_i\), Jensen's inequality for the convex function \(\phi\) yields
\[
T_q=\phi\!\left(\sum_i p_i(q)/a_i\right)
\le\sum_i p_i(q)\phi(1/a_i)=U_q.
\]

**2. Monotonicity and strictness.** Differentiation of the finite exponential weights gives
\[
\frac{d}{dq}\sum_i p_i(q)h(a_i)
=2\operatorname{Cov}_{p(q)}(h(a),\log a).
\]
The covariance is nonnegative when \(h\) is nondecreasing, and nonpositive when \(h\) is nonincreasing, by the pairwise identity \(2\operatorname{Cov}(h,g)=\sum_{i,j}p_ip_j(h_i-h_j)(g_i-g_j)\). It follows that \(U_q\) and \(\lambda_q\), hence \(T_q\), are nondecreasing. The composition with a convex reciprocal profile is locally Lipschitz on the relevant positive spectral interval, so for almost every \(q\),
\[
\mathcal E_q'=2T_q'(T_q-U_q)-2T_qU_q'\le0.
\]
Absolute continuity on compact \(q\)-intervals proves the assertion for every real \(q\ge1\). For a nonconstant operator-monotone function on the positive half-line, \(f\) is strictly increasing there; if the seed meets two distinct positive eigenvalues then \(U_q'>0\), \(T_q>0\), proving strict descent. For one supported positive eigenvalue, \(p_i\) and \(\lambda_q\) do not vary, so the error is constant. Continuous nonnegative operator-monotone functions vanishing at zero have a positive linear-plus-resolvent integral representation; on substituting \(1/t\), the constituent terms are \(c/t\) and \(1/(1+st)\), each convex. This proves inclusion of that class.

**3. Sharp fixed-seed spectral rate.** Let \(a>b\) be the largest and next-largest distinct positive eigenvalues meeting the seed, with squared spectral-projection weights \(\alpha,\beta>0\). For nonconstant operator-monotone \(f\), the ratio of the second weight to the top weight is \((\beta/\alpha)(b/a)^{2q}\); all lower supported eigenspaces contribute smaller orders. Therefore
\[
f(a)-U_q\sim(f(a)-f(b))(\beta/\alpha)(b/a)^{2q},
\quad f(a)-T_q=O((b/a)^{2q}).
\]
Using the exact identity
\[
\mathcal E_q-[K-f(a)^2]=(f(a)-T_q)^2+2T_q(f(a)-U_q)
\]
gives
\[
\mathcal E_q-[K-f(a)^2]
\sim2f(a)(f(a)-f(b))(\beta/\alpha)(b/a)^{2q}.
\]

**4. Exact Gaussian expectation and the mean-rate gap.** In dimension two with \(f(t)=t\), put \(z=(a/b)^q|\omega_1/\omega_2|\). The absolute ratio of independent standard Gaussians has density \(2/[\pi(1+t^2)]\); hence \(z\) has density \(2r/[\pi(1+r^2z^2)]\) on \((0,\infty)\), where \(r=(b/a)^q\). One has
\[
\lambda_q=\frac{ab(1+z^2)}{a+bz^2},\qquad
\mathcal E_q-b^2
=\frac{a^2(a-b)^2}{(a+bz^2)^2}
+\frac{2ab(a-b)}{a+bz^2}.
\]
The elementary integrals used to average these rational functions are
\[
I_1=\int_0^\infty\!\frac{dz}{(1+r^2z^2)(a+bz^2)}
=\frac\pi{2(\sqrt{ab}+ar)},
\]
\[
I_2=\int_0^\infty\!\frac{dz}{(1+r^2z^2)(a+bz^2)^2}
=\frac\pi2\frac{r+\frac12\sqrt{b/a}}{(\sqrt{ab}+ar)^2}.
\]
(The second follows by differentiating the first with respect to \(a\), holding \(b,r\) fixed.) Multiplication by the density and simplification yields precisely
\[
\mathbb E\mathcal E_q=b^2+\frac{rc(a-b)[a+3b+2rc(a+b)]}{2(1+rc)^2}.
\]
Dividing the excess by \(r\) and taking \(r\downarrow0\) proves its stated asymptotic. The fixed-seed formula in Step 3, with \(\alpha=\omega_1^2\), \(\beta=\omega_2^2\), proves almost-sure rate \((b/a)^{2q}\). The Gaussian coefficient has infinite mean because \(\mathbb E(\omega_2/\omega_1)^2=\infty\), consistently with the slower exact expected-error rate.

**5. A monotone-function boundary.** Set \(A=\operatorname{diag}(4,1)\), \(\omega=(1,28)^{\mathsf T}\), and define the continuous nondecreasing function
\[
f(t)=\begin{cases}0,&0\le t\le21/20,\\ (20t-21)/3,&21/20<t<6/5,\\1,&t\ge6/5.\end{cases}
\]
Here \(f(A)=\operatorname{diag}(1,0)\). Direct rational arithmetic yields \(\lambda_1=200/197<21/20\) and \(\lambda_2=65/53>6/5\), so \(F_1=0\), while \(F_2\) is the rank-one orthogonal projection with first diagonal entry \(16/65\). Thus \(\mathcal E_1=1\) but \(\mathcal E_2=2-32/65=98/65>1\). Therefore scalar monotonicity alone does not suffice.

## Verification
The self-contained Python 3 standard-library file `verify_rankone_funnystrom.py` checks the full matrix \(f(N_q)\) against the independently derived scalar formula, finite-step monotonicity for six reciprocal-convex examples, the exact rational boundary example, the two-dimensional Gaussian angular integral against the closed form, and its small-ratio asymptotics. Run `python3 verify_rankone_funnystrom.py`. Its recorded execution returned `PASS: 18081 independent full-matrix, reduced-form, rational, and Gaussian-integral checks`.

The infinite-dimensional parameter quantifiers (arbitrary finite matrix size and arbitrarily large real \(q\)) follow from the analytical identities above; randomized or quadrature tests cannot independently establish them. All statements are in exact arithmetic.

## Relationship to prior work
Persson and Kressner introduced funNyström as \(f\) of a power-Nyström approximation of \(A\), and obtained probabilistic norm estimates for operator-monotone matrix functions [1]. Persson, Meyer, and Musco developed algorithm-independent near-optimality transfer and discussed monotonic improvement of the **untransformed** low-rank approximation under power iteration [2]. Neither fact alone implies the present pathwise Frobenius descent for the nonlinear transform \(f(N_q)\), nor its exact Gaussian expected-error formula and the one-half rate-exponent difference. Classical Nyström structural approximation work [3] provides broader context without these claims. This is a novelty comparison, not proof that no equivalent result exists in other literature.

## Limitations
The pathwise theorem is rank one and uses a fixed seed and powers of one PSD matrix, not varying sketches, block rank, finite precision, or spectral-norm descent. Convexity of the reciprocal profile is sufficient, not asserted to be necessary. The sharp rate assumes two distinct positive seed-supported eigenvalues and a nonconstant operator-monotone function. The exact Gaussian expectation concerns only a two-eigenvalue positive-definite matrix and \(f(t)=t\); no general-dimensional expected-risk rate is claimed. An equivalent unpublished or differently formulated monotonicity argument might predate this statement. No independent audit has been performed.

## References
[1] D. Persson and D. Kressner, *Randomized low-rank approximation of monotone matrix functions*, arXiv:2209.11023 (first public 2022-09-22), https://arxiv.org/abs/2209.11023.

[2] D. Persson, R. A. Meyer, and C. Musco, *Algorithm-agnostic low-rank approximation of operator monotone matrix functions*, arXiv:2311.14023 (first public 2023-11-23), https://arxiv.org/abs/2311.14023.

[3] A. Gittens and M. W. Mahoney, *Revisiting the Nyström method for improved large-scale machine learning*, arXiv:1303.1849, https://arxiv.org/abs/1303.1849.
