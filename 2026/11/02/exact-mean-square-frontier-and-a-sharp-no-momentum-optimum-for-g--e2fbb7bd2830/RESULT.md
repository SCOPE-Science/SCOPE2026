# Exact mean-square frontier and a sharp no-momentum optimum for Gaussian heavy-ball Kaczmarz

## Finding
For every integer \(d\ge 1\), consider the rank-one Gaussian momentum recurrence
\[
x_{k+1}=(1+\omega)x_k-\omega x_{k-1}-\alpha g_kg_k^{\mathsf T}x_k,
\qquad g_k\stackrel{\mathrm{iid}}\sim N(0,I_d),\quad x_{-1}=x_0\ne0,
\]
where \(\alpha>0\) and \(\omega\ge0\) are fixed. The exact exponential mean-square factor is the spectral radius \(\rho_{d,\alpha,\omega}\) of
\[
M_{d,\alpha,\omega}=
\begin{pmatrix}
(1+\omega-\alpha)^2+(d+1)\alpha^2&-2\omega(1+\omega-\alpha)&\omega^2\\
1+\omega-\alpha&-\omega&0\\
1&0&0
\end{pmatrix}.
\]
More precisely,
\[
\lim_{k\to\infty}\bigl(\mathbb E\|x_k\|_2^2\bigr)^{1/k}=\rho_{d,\alpha,\omega}.
\]
Mean-square convergence to zero occurs **exactly** for
\[
\boxed{0\le\omega<1,\qquad 0<\alpha<\frac{2(1-\omega^2)}{d(1+\omega)+2}.}
\]
Globally over all \(\alpha>0\) and \(\omega\ge0\),
\[
\boxed{\rho_{d,\alpha,\omega}\ge\frac{d+1}{d+2},}
\]
with equality **only** at \(\omega=0\), \(\alpha=1/(d+2)\). Thus no strictly positive fixed heavy-ball momentum improves the best asymptotic mean-square factor on this natural isotropic Gaussian instance. In the stepsize parameter \(\eta\) of the rank-one block-Gaussian Kaczmarz specialization in Han--Xie, \(\eta=d\alpha\), so the sharp stability ceiling is \(2d(1-\omega^2)/(d(1+\omega)+2)\).

## Assumptions and scope
All quantities are in exact real arithmetic. The random vectors are mutually independent, independent of the deterministic initial state, and have independent standard-normal components. The linear system is \(I_dx=0\); this is the rank-one, standard-Gaussian specialization of the pseudoinverse-free momentum block-Gaussian Kaczmarz update. The results concern the unaveraged iterate's **expected squared Euclidean norm**, not the squared norm of its expectation; they hold for every deterministic nonzero initialization with zero initial momentum \(x_{-1}=x_0\). The convergence assertion is a strict asymptotic claim: at the boundary the mean-square factor equals one, so convergence to zero does not occur.

## Proof
Set \(u=1+\omega-\alpha\) and define \(a_k=\mathbb E\|x_k\|_2^2\), \(b_k=\mathbb E\langle x_k,x_{k-1}\rangle\), and \(c_k=\mathbb E\|x_{k-1}\|_2^2\). The Gaussian fourth-moment identity
\[
\mathbb E[g_kg_k^{\mathsf T}]=I_d,\qquad
\mathbb E[(g_kg_k^{\mathsf T})^2]=(d+2)I_d
\]
shows, after conditioning on the past, that
\[
\begin{aligned}
a_{k+1}&=\bigl(u^2+(d+1)\alpha^2\bigr)a_k-2\omega u b_k+\omega^2c_k,\\
b_{k+1}&=u a_k-\omega b_k,\\
c_{k+1}&=a_k.
\end{aligned}
\]
Hence \((a_{k+1},b_{k+1},c_{k+1})^{\mathsf T}=M_{d,\alpha,\omega}(a_k,b_k,c_k)^{\mathsf T}\). The \(2\times2\) Gram moment matrix \(G_k=\begin{psmallmatrix}a_k&b_k\\b_k&c_k\end{psmallmatrix}\) is positive semidefinite, and direct subtraction yields the exact identity
\[
\det G_{k+1}=\omega^2\det G_k+(d+1)\alpha^2a_k^2.
\]
For \(\omega>0\), every nonzero positive-semidefinite \(G\) is mapped to a positive-definite matrix within two updates: if its leading entry is positive, this follows at the next step from the determinant formula; otherwise the trailing entry is positive and the leading entry becomes \(\omega^2c>0\) first. The positive linear map is therefore primitive on the cone of symmetric positive-semidefinite matrices. Finite-dimensional Perron--Frobenius theory for a primitive proper-cone-preserving map gives a simple positive dominant eigenvalue, positive left eigenfunctional, and positive leading coefficient for every nonzero positive-semidefinite initial matrix. Taking the leading entry proves the asserted exact factor. For \(\omega=0\), the recurrence reduces directly to \(a_{k+1}=(1-2\alpha+(d+2)\alpha^2)a_k\), again yielding the claimed factor.

Let \(P(z)=\det(zI_3-M_{d,\alpha,\omega})\). Exact expansion gives
\[
P(1)=\alpha\left[2(1-\omega^2)-\alpha\bigl(d(1+\omega)+2\bigr)\right],
\qquad\det M_{d,\alpha,\omega}=\omega^3.
\]
If \(\omega\ge1\), the spectral radius is at least \(\omega\), so stability is impossible. If \(0\le\omega<1\), at \(\alpha=0\) the characteristic roots are \(1,\omega,\omega^2\), and the root originating at one has derivative \(-2/(1-\omega)<0\) with respect to \(\alpha\). Thus for small positive steps the spectral radius is below one. Since the spectral radius varies continuously and can cross one only if \(P(1)=0\) (the Perron eigenvalue is positive real), its sole positive threshold is the displayed value. Above this threshold \(P(1)<0\), so a real root greater than one exists because \(P(z)\to+\infty\) as \(z\to+\infty\). At equality, one is an eigenvalue and positivity ensures nondecay. This proves the sharp iff stability interval.

For global optimality set \(r=(d+1)/(d+2)\). If \(\omega>r\), then \(\rho\ge\omega>r\) by \(\det M=\omega^3\). For \(0\le\omega\le r\), define
\[
\alpha_c=\frac{(1+\omega)[d+1-(d+2)\omega]}{(d+2)(d\omega+d+1)}.
\]
Direct polynomial completion of the square yields the exact identity
\[
P(r)=-\frac{(d+1)(d\omega+d+1)}{d+2}(\alpha-\alpha_c)^2
+\frac{\omega^2\bigl[(d+2)^2\omega^2-(d+1)^2\bigr]}{(d+2)^3(d\omega+d+1)}.
\]
Both terms are nonpositive in this range. They vanish simultaneously with \(\alpha>0\) only at \(\omega=0\), \(\alpha=1/(d+2)\): for \(\omega=r\), the unique zero of the second term has \(\alpha_c=0\), excluded. When \(P(r)<0\), the monic cubic has a real root greater than \(r\), and hence \(\rho>r\). At the unique equality case, \(\omega=0\) and \(a_{k+1}/a_k=r\). This proves the sharp bound and uniqueness.

## Verification
The accompanying standalone script `verify.py` symbolically reconstructs the moment matrix, verifies the determinant and characteristic identities, the optimality completion of the square, and the derivative of the critical root. It checks exact rational boundary instances in several dimensions, and directly enumerates the scalar Gaussian fourth-moment identity for polynomial test inputs. It computes representative spectral radii independently. Only the analytical cone argument, not numerical eigenvalue estimates, establishes the infinite-horizon claims.

## Relationship to prior work
Han and Xie (2022, Section 5.6, arXiv:2208.05437) introduced the block Gaussian Kaczmarz method with momentum and supplied global sufficient mean-square convergence estimates; their paper also distinguishes acceleration of the **norm of the expected iterate** from control of the mean-square iterate. Their original construction and Gaussian fourth-moment normalization are explicitly retained here, not claimed as new. The present exact isotropic rank-one result determines the sharp stability region for all fixed nonnegative momentum and the unique globally optimal true mean-square rate.

The qualitative possibility that stochastic heavy-ball acceleration fails on particular one-sample regression distributions was established earlier by Kidambi, Netrapalli, Jain and Kakade (2018, Proposition 3 and Appendix A, arXiv:1803.05591); their construction uses a decoupled, anisotropic two-coordinate mixture and a nonsharp problem-dependent complexity lower bound. The exact isotropic Gaussian moment map and its sharp \((d,\alpha,\omega)\) frontier do not follow as stated from that result. Bollapragada, Chen and Ward (2022, arXiv:2206.07553) analyzed momentum acceleration under minibatching; their conclusions address different batch regimes and do not provide the displayed single-sketch exact parameter optimum. These related mechanisms and overlap risks require independent priority confirmation.

## Limitations
The sharp theorem applies only to identity systems, one independent standard Gaussian rank-one sketch per iteration, nonnegative fixed momentum, and exact arithmetic. It is not a worst-case assertion for every linear system, every sketch law or negative momentum. The finding does not deny acceleration in the mean of iterates, in large minibatches, or under different stochastic acceleration algorithms. The qualitative no-acceleration phenomenon is previously known; the claim of novelty is confined to the quantitative isotropic Gaussian result. Priority against equivalent formulations in broader stochastic-recursion literature remains subject to independent evaluation.

## References
1. D. Han and J. Xie, *On pseudoinverse-free randomized methods for linear systems: Unified framework and acceleration*, arXiv:2208.05437, first posted 2022-08-10, especially Section 5.6, https://arxiv.org/abs/2208.05437.
2. R. Kidambi, P. Netrapalli, P. Jain and S. M. Kakade, *On the insufficiency of existing momentum schemes for stochastic optimization*, arXiv:1803.05591, 2018, Section 3 and Appendix A, https://arxiv.org/abs/1803.05591.
3. R. Bollapragada, T. Chen and R. Ward, *On the fast convergence of minibatch heavy ball momentum*, arXiv:2206.07553, 2022, https://arxiv.org/abs/2206.07553.
