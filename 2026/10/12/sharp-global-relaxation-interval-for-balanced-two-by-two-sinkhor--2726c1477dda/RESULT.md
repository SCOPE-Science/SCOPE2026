# Sharp global relaxation interval for balanced two-by-two Sinkhorn scaling

## Finding
Let \(K\in\mathbb R_{>0}^{2\times2}\) be any strictly positive matrix, including possibly rank-one matrices. Fix the row and column marginals
\[
a=b=(1/2,1/2)^{\mathsf T}.
\]
The standard fixed-parameter, blockwise overrelaxed Sinkhorn iteration is
\[
u_{\ell+1}=u_{\ell}^{\,1-\omega}\circ\left(\frac{a}{Kv_{\ell}}\right)^{\!\omega},
\qquad
v_{\ell+1}=v_{\ell}^{\,1-\omega}\circ\left(\frac{b}{K^{\mathsf T}u_{\ell+1}}\right)^{\!\omega},
\]
with strictly positive initial vectors and componentwise arithmetic. Write
\[
P_{\ell}=\operatorname{diag}(u_{\ell})K\operatorname{diag}(v_{\ell}).
\]
There is a unique positive matrix \(P_*\) diagonally equivalent to \(K\) with prescribed marginals.

**The exact universal global-convergence interval is**
\[
\boxed{0<\omega<2.}
\]
For every strictly positive \(K\) and every strictly positive \((u_0,v_0)\), the actual, unnormalized scaled matrices converge:
\[
P_{\ell}\longrightarrow P_*.
\]
At \(\omega=2\) and at every \(\omega>2\), every nonoptimal initial pair of log scaling ratios fails to converge to those of \(P_*\); thus no such parameter is globally convergent. This sharpness holds for each fixed positive \(K\), not merely for a worst-case matrix family.

The decisive invariant is a two-variable strictly convex potential \(\Phi\). Each relaxation half-step contracts its distance to the corresponding one-variable conditional minimizer by the exact factor \(|1-\omega|\). For \(0<\omega<2\), both half-steps strictly lower \(\Phi\) unless already optimal, which provides global rather than merely local convergence.

For example, take
\[
K=\begin{pmatrix}100&1\\1&100\end{pmatrix}.
\]
The unique balanced scaling is \(P_*=K/202\). Its Birkhoff contraction ratio is \(99/101\). The general sufficient interval supplied by the classic Hilbert-metric contraction argument is only \(0<\omega<101/100\), but every fixed \(\omega\in(0,2)\), including \(\omega=19/10\), is globally convergent for this particular problem.

## Assumptions and scope
The matrix \(K\) has four strictly positive real entries. Rank one is allowed. Both marginals are uniform probability vectors on two atoms. The initial scale factors are strictly positive, but otherwise arbitrary. All statements are in exact arithmetic.

The update is *simultaneous within a scaling block* and *successive between row and column blocks*, with one common fixed parameter \(\omega\). It is not an Anderson-accelerated method or an adaptive rule; no positivity safeguard is imposed beyond positivity of the starting vectors and the kernel.

The convergence assertion concerns the full scaled coupling \(P_{\ell}\), not necessarily the two scaling vectors individually, since the vectors have the natural gauge freedom \((u,v)\sim(cu,c^{-1}v)\).

The equality \(\omega=2\) is excluded. A nonoptimal starting projective state can have nonconvergent iteration even though the row and column updates are individually well-defined and positive.

## Proof
Put
\[
 x=\log(u_1/u_2),\qquad y=\log(v_1/v_2),
\]
and define
\[
\Phi(x,y)=\log\left(
K_{11}e^{(x+y)/2}+K_{12}e^{(x-y)/2}
+K_{21}e^{(-x+y)/2}+K_{22}e^{(-x-y)/2}
\right).
\]
Let
\[
A(y)=K_{11}e^{y/2}+K_{12}e^{-y/2},\quad
B(y)=K_{21}e^{y/2}+K_{22}e^{-y/2}.
\]
The row update gives exactly
\[
x^+=(1-\omega)x+\omega x_*(y),\qquad
x_*(y)=\log(B(y)/A(y)).
\]
The potential has the exact conditional identity
\[
\Phi(x,y)
=\log(2\sqrt{A(y)B(y)})
+\log\cosh\left(\frac{x-x_*(y)}2\right).
\]
Thus \(x_*(y)\) is the unique conditional minimum. Setting
\[
q=|1-\omega|,
\]
we have
\[
|x^+-x_*(y)|=q|x-x_*(y)|.
\]
For \(0<\omega<2\), \(q<1\), and strict monotonicity of \(\log\cosh(t)\) in \(|t|\) shows
\[
\Phi(x^+,y)\le\Phi(x,y),
\]
with equality only when \(x=x_*(y)\).

Similarly define
\[
C(x)=K_{11}e^{x/2}+K_{21}e^{-x/2},\quad
D(x)=K_{12}e^{x/2}+K_{22}e^{-x/2}.
\]
The column update is
\[
y^+=(1-\omega)y+\omega y_*(x^+),\qquad
y_*(x)=\log(D(x)/C(x)),
\]
and it obeys
\[
\Phi(x^+,y^+)\le\Phi(x^+,y),
\]
with equality only when \(y=y_*(x^+)\). In particular, a full step decreases \(\Phi\) strictly unless the current point is a simultaneous conditional minimizer.

To show existence and uniqueness of that minimizer, observe first that, since \(K_{ij}>0\),
\[
 e^{\Phi(x,y)}
\ge4(\min_{i,j}K_{ij})\cosh(x/2)\cosh(y/2).
\]
So \(\Phi\) is coercive, with compact sublevel sets. Its Hessian is the covariance of the four points
\[
(1/2,1/2),\quad(1/2,-1/2),\quad(-1/2,1/2),\quad(-1/2,-1/2)
\]
under the strictly positive Gibbs weights proportional to the four summands in \(e^{\Phi}\). For every nonzero vector, its dot products with these four points are not all equal. Hence the Hessian is positive definite everywhere, so \(\Phi\) is strictly convex with a unique minimizer \((x_\infty,y_\infty)\).

Let \(T\) denote the continuous full-step map on \(\mathbb R^2\). When \(0<\omega<2\), the function
\[
\Delta(x,y)=\Phi(x,y)-\Phi(T(x,y))
\]
is continuous, nonnegative, and vanishes precisely at the simultaneous conditional minimizer, i.e. the unique minimizer of \(\Phi\). Since the sequence stays in its compact initial sublevel set, \(\Phi\) decreases to a finite limit and the consecutive decreases tend to zero. Every cluster point therefore has \(\Delta=0\), so every cluster point equals \((x_\infty,y_\infty)\). Thus
\[
(x_\ell,y_\ell)\longrightarrow(x_\infty,y_\infty).
\]
At that point, the gradient of \(\Phi\) vanishes. Normalizing the positive entries
\[
\widehat P_{ij}(x,y)
=\frac{K_{ij}e^{(\sigma_i x+\sigma_j y)/2}}
{\sum_{r,s}K_{rs}e^{(\sigma_r x+\sigma_s y)/2}},
\qquad \sigma_1=1,\quad\sigma_2=-1,
\]
we have
\[
\partial_x\Phi=\tfrac12(\widehat P_{11}+\widehat P_{12}-\widehat P_{21}-\widehat P_{22}),
\]
and similarly for the column difference. Hence \(\widehat P(x_\infty,y_\infty)\) has both row and column marginals equal to \((1/2,1/2)\), and must be the unique balanced scaling of \(K\).

It remains to prove convergence of the *unnormalized* \(P_\ell\). Write
\[
s_u=\tfrac12(\log u_1+\log u_2),\quad
s_v=\tfrac12(\log v_1+\log v_2),\quad w=s_u+s_v.
\]
The coupling has entries
\[
(P_\ell)_{ij}=e^{w_\ell}K_{ij}e^{(\sigma_i x_\ell+\sigma_j y_\ell)/2}.
\]
Averaging the two log-row updates, and then the two log-column updates, yields the exact recursions
\[
 w^{\mathrm{row}}=(1-\omega)w+\omega g_r(y),
\qquad
w^+=(1-\omega)w^{\mathrm{row}}+\omega g_c(x^+),
\]
where
\[
 g_r(y)=-\log2-\tfrac12\log(A(y)B(y)),
\qquad
 g_c(x)=-\log2-\tfrac12\log(C(x)D(x)).
\]
At the limiting balanced scaling,
\[
g_r(y_\infty)=g_c(x_\infty)=w_\infty
\]
for its uniquely determined scalar \(w_\infty\). Combining the recursions gives
\[
 w_{\ell+1}=(1-\omega)^2w_\ell
 +\omega(1-\omega)g_r(y_\ell)
 +\omega g_c(x_{\ell+1}).
\]
Since \((1-\omega)^2<1\) and the forcing tends to
\[
\omega(2-\omega)w_\infty,
\]
the elementary stable affine-recursion lemma implies \(w_\ell\to w_\infty\). The actual scaled matrices \(P_\ell\) therefore converge entrywise to \(P_*\).

**Sharpness.** For \(\omega=2\), \(q=1\). The conditional \(\cosh\) identity makes both half steps preserve \(\Phi\) *exactly*. Starting at any nonminimizing \((x_0,y_0)\), one has \(\Phi(x_\ell,y_\ell)=\Phi(x_0,y_0)>\min\Phi\), hence no convergence to the unique balanced scaling. For every \(\omega>2\), \(q>1\) makes both half steps nondecreasing in \(\Phi\) (strict whenever the corresponding coordinate is nonoptimal); the same nonconvergence conclusion follows. At \(\omega=0\) the scale factors remain unchanged. Thus \((0,2)\) is exactly the parameter interval giving convergence from every strictly positive initialization.

## Verification
The embedded `verify.py` implements the *log-ratio* form of precisely the displayed row/column updates, checks conditional potential descent for \(\omega=19/10\), and checks the endpoint invariance for \(\omega=2\) on
\[
K=\begin{pmatrix}100&1\\1&100\end{pmatrix}.
\]
For this matrix the unique balanced coupling is \(K/202\). The checker evaluates the classical Birkhoff contraction ratio \(99/101\), and verifies that its published sufficient upper endpoint is \(101/100\), strictly below \(19/10\). It also verifies a non-symmetric positive kernel example, and checks that projective gradient/marginal residuals approach zero.

The checker is finite numerical corroboration. The convergence and sharpness assertions for all positive matrices, all positive initializations, and all parameters in the asserted ranges are established analytically above.

## Relationship to prior work
Entropic optimal transport and ordinary alternating diagonal scaling are classical. Peyré's archive-era treatment of entropic Wasserstein flows explains the link between regularized transport, Gibbs kernels, and Sinkhorn/iterative proportional fitting and provides a general diagonal-scaling framework; the public preprint lists primary MSC \(90C25\).

Thibault, Chizat, Dossal, and Papadakis introduced overrelaxed Sinkhorn--Knopp scaling and proved convergence using **adaptive** relaxation parameters chosen to enforce descent of a KL-type Lyapunov function. Their full original work states that a naive *fixed* overrelaxation can fail globally in general; the full paper does not present a two-by-two equal-marginal unconditional parameter classification.

Lehmann, von Renesse, Sambale, and Uschmajew prove that for general positive kernels fixed \(\omega\in(0,2)\) is **locally** convergent. Their general **global** theorem requires
\[
0<\omega<\frac{2}{1+\Lambda(K)},
\]
where \(\Lambda(K)<1\) is the Birkhoff contraction factor. The paper does not supply a sharp all-start fixed-parameter global interval for two-by-two equal-marginal matrices.

For
\[
K=\begin{pmatrix}100&1\\1&100\end{pmatrix},
\]
one has
\[
\Lambda(K)=\frac{99}{101},
\qquad
\frac{2}{1+\Lambda(K)}=\frac{101}{100}.
\]
The theorem above therefore strictly enlarges the published general-purpose sufficient range on this natural smallest nontrivial family to every \(\omega<2\), and shows that the endpoint cannot be included. Its additional mechanism is the *conditional log-cosh symmetry* of the projective dual objective when both marginals are uniform and there are exactly two alternatives. Neither generic local spectral analysis nor an adaptive safety rule implies this specific unconditional global result.

## Limitations
Uniform two-point row and column marginals are essential to the exact conditional \(\cosh\) reflection symmetry. The theorem does not claim an all-start \((0,2)\) interval for unequal marginals, larger matrices, kernels with zero entries, asynchronous component updates, varying relaxation parameters, or finite-precision implementations.

The proof gives convergence but no uniform geometric rate independent of the entries of \(K\); matrices approaching degeneracy can converge very slowly. Gauge-related scaling factors need not individually converge even when their product coupling does.

The novelty assessment remains subject to the possibility of older nonlinear SOR or matrix-scaling literature deriving this special case under alternate terminology.

## References
1. G. Peyré, “Entropic Wasserstein Gradient Flows,” arXiv:1502.06216v1, first public 2015-02-22. Revised arXiv manuscript (2015), primary MSC 90C25; published as “Entropic Approximation of Wasserstein Gradient Flows,” SIAM Journal on Imaging Sciences 8 (2015), 2323–2351, DOI 10.1137/15M1010087.
2. A. Thibault, L. Chizat, C. Dossal, and N. Papadakis, “Overrelaxed Sinkhorn--Knopp Algorithm for Regularized Optimal Transport,” arXiv:1711.01851v1, first public 2017-11-06; Algorithms 14 (2021), article 143, DOI 10.3390/a14050143.
3. T. Lehmann, M.-K. von Renesse, A. Sambale, and A. Uschmajew, “A note on overrelaxation in the Sinkhorn algorithm,” arXiv:2012.12562v1, first public 2020-12-23; Optimization Letters 16 (2022), 2209–2220, DOI 10.1007/s11590-021-01830-0.
4. P. A. Knight, “The Sinkhorn--Knopp Algorithm: Convergence and Applications,” SIAM Journal on Matrix Analysis and Applications 30 (2008), 261–275, DOI 10.1137/060659624.
