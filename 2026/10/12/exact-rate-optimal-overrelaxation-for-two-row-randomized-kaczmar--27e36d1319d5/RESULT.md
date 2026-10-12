# Exact rate-optimal overrelaxation for two-row randomized Kaczmarz

## Finding
Consider two independently and uniformly sampled, distinct unit-normal equations in the real plane. The optimal **constant** Kaczmarz relaxation for the exact asymptotic expected squared error is uniquely characterized by one scalar root. Except for orthogonal rows, that optimum always **overrelaxes** beyond exact projection; near parallel rows, the optimized asymptotic spectral gap approaches twice the standard-projection gap.

Specifically, write \(c=|a_1^\mathsf Ta_2|\), \(p=(1+c)/2\), \(q=(1-c)/2\), and
\[
S_c(z)=\frac{p^2}{2p-z}+\frac{q^2}{2q-z},\qquad 0<z<2q.
\]
The function
\[
F_c(z)=\frac{p^2(p-z)}{(2p-z)^2}+\frac{q^2(q-z)}{(2q-z)^2}
\]
has exactly one zero \(z_\star\) in that interval. The unique rate-minimizing parameter and its exact contraction factor are
\[
\boxed{\omega_\star(c)=\frac1{S_c(z_\star)},\qquad
\rho_\star(c)=1-\frac{z_\star}{S_c(z_\star)}.}
\]
The special case \(c=0\) gives \(\omega_\star=1\). Every \(0<c<1\) gives \(1<\omega_\star<2\); at nearly parallel rows the ratio of optimal to exact-projection expected-error spectral gaps tends to \(2\).

## Assumptions and scope
Let \(a_1,a_2\in\mathbb R^2\) have unit Euclidean norm and satisfy \(c=|a_1^\mathsf Ta_2|<1\). Let the two equations \(a_i^\mathsf T x=b_i\) be consistent, with their unique common solution denoted \(x_\star\). Choose \(i_k\in\{1,2\}\) independently and uniformly at every step and take a **fixed real** parameter \(\omega\):
\[
x_{k+1}=x_k-\omega a_{i_k}(a_{i_k}^\mathsf T x_k-b_{i_k}),\qquad k\ge0.
\]
The starting vector \(x_0\in\mathbb R^2\) is deterministic. We study mean-square convergence \(\mathbb E\|x_k-x_\star\|_2^2\to0\) and, for \(x_0\ne x_\star\), the exact large-\(k\) \(k\)-th-root factor of this quantity. The contraction-rate formula below is for \(\omega>0\), while the convergence criterion covers all real \(\omega\). There are no measurement errors or extra relaxation schedules.

## Proof
**1. Exact second-moment dynamics.** Up to orthogonal coordinates and a harmless change of sign of one row, the two normals are
\[
a_1=(\sqrt p,\sqrt q)^\mathsf T,\qquad a_2=(\sqrt p,-\sqrt q)^\mathsf T.
\]
This construction realizes the absolute inner product \(c=p-q\). Put \(e_k=x_k-x_\star\). The two possible error maps are
\[
A_\pm=\begin{pmatrix}1-\omega p&\pm\omega\sqrt{pq}\\
\pm\omega\sqrt{pq}&1-\omega q\end{pmatrix},
\]
where the placement of signs is immaterial because both maps have probability one half. For \(U_k=\mathbb E(e_{k,1}^2)\), \(V_k=\mathbb E(e_{k,2}^2)\), and \(W_k=\mathbb E(e_{k,1}e_{k,2})\), direct expansion gives
\[
\begin{pmatrix}U_{k+1}\\V_{k+1}\end{pmatrix}
=M_c(\omega)\begin{pmatrix}U_k\\V_k\end{pmatrix},\qquad
M_c(\omega)=\begin{pmatrix}(1-\omega p)^2&\omega^2pq\\
\omega^2pq&(1-\omega q)^2\end{pmatrix},
\]
and \(W_{k+1}=(1-\omega+2\omega^2pq)W_k\). Thus the covariance off-diagonal does not affect the expected squared norm \(U_k+V_k\).

**2. Exact rate and sharp stability interval.** For any \(\omega>0\), \(M_c(\omega)\) has a strictly positive off-diagonal entry. Its strictly positive Perron eigenvector overlaps every nonzero nonnegative vector \((U_0,V_0)^\mathsf T\). Consequently, for **every** nonzero deterministic initial error,
\[
\lim_{k\to\infty}\bigl(\mathbb E\|e_k\|_2^2\bigr)^{1/k}
=\rho_c(\omega)=\lambda_{\max}(M_c(\omega)).
\]
Taking the larger eigenvalue of the displayed symmetric matrix yields the explicit formula
\[
\rho_c(\omega)=1-\omega+\frac{\omega^2}{4}(1+c^2)
+\frac\omega2\sqrt{c^2(\omega-2)^2+\frac{\omega^2}{4}(1-c^2)^2}.
\]
Independently, for any realized row and any real \(\omega\), the unit-normal identity gives
\[
\|e_{k+1}\|_2^2=\|e_k\|_2^2-\omega(2-\omega)(a_{i_k}^\mathsf T e_k)^2.
\]
The sampling-average row Gram matrix is \(D=\operatorname{diag}(p,q)\succ0\). Therefore conditional expected squared norms shrink geometrically for \(0<\omega<2\), grow geometrically for \(\omega<0\) or \(\omega>2\), and are conserved for \(\omega\in\{0,2\}\). Hence convergence for all deterministic starts occurs **if and only if** \(0<\omega<2\). In the permitted interval \(\rho_c(\omega)<1\); otherwise no nonzero deterministic start converges in mean square.

**3. Uniqueness of the rate-optimal constant relaxation.** Let \(v=(p,q)^\mathsf T\). The second-moment matrix factors as
\[
M_c(\omega)=I-2\omega D+\omega^2vv^\mathsf T.
\]
For \(0<\omega<2\), the spectral gap \(\delta(\omega)=1-\rho_c(\omega)\) is the smallest eigenvalue of \(2\omega D-\omega^2vv^\mathsf T\). Since \(v\) has both entries positive, strict rank-one interlacing gives \(0<\delta(\omega)<2\omega q\). Define \(z=\delta(\omega)/\omega\), so \(0<z<2q\). The rank-one determinant formula gives
\[
1=\omega\biggl(\frac{p^2}{2p-z}+\frac{q^2}{2q-z}\biggr)
=\omega S_c(z).
\]
Conversely, the strictly increasing function \(S_c\) maps \((0,2q)\) onto \((1/2,\infty)\). Thus \(\omega=1/S_c(z)\) bijectively parametrizes the entire \(0<\omega<2\) stability interval, and the spectral gap is \(\delta=z/S_c(z)\). Differentiating this last expression gives
\[
\delta'(z)=\frac{S_c(z)-zS_c'(z)}{S_c(z)^2},\qquad
\bigl(S_c(z)-zS_c'(z)\bigr)'=-zS_c''(z)<0.
\]
The numerator is positive at \(z=0\) and tends to \(-\infty\) as \(z\uparrow2q\). Hence it has one zero, yielding the unique global maximum of the spectral gap. The condition \(S_c-zS_c'=0\) is exactly twice \(F_c(z)=0\). As all unstable or neutral \(\omega\) have \(\rho_c(\omega)\ge1\), this is also the unique global minimizer over all positive \(\omega\).

**4. Strict overrelaxation.** For \(c=0\), the exact eigenvalue formula reduces to \(\rho_0(\omega)=1-\omega+\omega^2/2\) and uniquely minimizes at \(\omega=1\). For \(0<c<1\), at \(\omega=1\), \(M_c(1)\) has largest eigenvalue \(p^2+q^2\), associated with \((q,p)^\mathsf T\). A simple-eigenvalue perturbation calculation gives
\[
\rho_c'(1)=-\frac{2pq(p-q)^2}{p^2+q^2}=-\frac{2pqc^2}{p^2+q^2}<0.
\]
Thus the unique minimizer lies strictly to the right of \(1\), and by Step 3 lies strictly below \(2\).

**5. Nearly parallel rows and a doubled gap.** Take \(q=(1-c)/2\downarrow0\), so \(p=1-q\). The zero \(z_\star\) obeys \(q<z_\star<2q\), because \(F_c(q)>0\). Writing \(h=2q-z_\star>0\), the critical-root equation rearranges to
\[
\frac{q^2(z_\star-q)}{h^2}
=\frac{p^2(p-z_\star)}{(2p-z_\star)^2}\longrightarrow\frac14.
\]
First it implies \(h=O(q^{3/2})\), hence \(z_\star/q\to2\); substituting again gives \(h\sim2q^{3/2}\). Consequently
\[
S_c(z_\star)=\frac12+\frac{\sqrt q}{2}+o(\sqrt q),
\quad \omega_\star=2-2\sqrt q+o(\sqrt q),\quad
1-\rho_\star=\frac{z_\star}{S_c(z_\star)}\sim4q.
\]
At exact projection \(\rho_c(1)=p^2+q^2\), so \(1-\rho_c(1)=2pq\sim2q\). Therefore
\[
\boxed{\lim_{c\uparrow1}\frac{1-\rho_\star(c)}{1-\rho_c(1)}=2.}
\]

## Verification
The accompanying standalone `verifier.py` uses SymPy to verify symbolically the three conditional covariance identities, the rank-one determinant identity, and the critical-root derivative expression. It checks 6,240 positive rational row-weight/relaxation pairs, the characteristic-rate identities for representative angles, and the approach toward the asymptotic gap ratio. Running `python verifier.py` in an environment with SymPy available returned `SYMBOLIC_OK`, `RATIONAL_CASES_OK 6240`, and `VERIFY_OK`. These finite tests corroborate, but do not replace, the fully quantified analytic proof above.

## Relationship to prior work
Strohmer and Vershynin's foundational randomized Kaczmarz paper (arXiv:math/0702226, first publicly submitted 8 February 2007), Section 2, proves an exponential expected-error **bound** for orthogonal row projections and Section 3 examines that method's rate bounds. It does not present the angle-dependent, constant-relaxation rate optimization proved here. Liu and Wright (arXiv:1310.2887) analyze accelerated randomized Kaczmarz using a different momentum mechanism. Wang, Agaskar and Lu (arXiv:1502.00190) derive exact MSE evolution for standard Kaczmarz on inconsistent data, not a closed-form all-angle optimal overrelaxation theorem. Marshall and Mickelin (arXiv:2202.12224) optimize a **scheduled learning-rate bound** in a measurement-noise setting, not the asymptotic spectral radius in the present uniform two-row IID model. Older relaxation and exact-MSE literature warrants continued bibliographic checking; this result claims no novelty for the general randomized Kaczmarz algorithm, its general contraction bounds, or exact second-moment matrix lifting.

## Limitations
The statement assumes two independent unit row normals in \(\mathbb R^2\), consistent equations, independent **with-replacement** uniform sampling, deterministic starts, and constant relaxation. It establishes an exact asymptotic expectation rate, not the optimal finite-horizon parameter, almost-sure Lyapunov exponent, or optimality for arbitrary sampling distributions, more rows, or noisy/inconsistent equations. The general exact-MSE article by Agaskar, Wang and Lu (2014; DOI 10.1109/GlobalSIP.2014.7032145) and Cai, Zhao and Tang's 2012 relaxation article could not be compared in full text; a differently formulated older sharp two-row relaxation result remains a nonzero originality risk. Bibliographic novelty is not logically certified by searches.

## References
1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226 (v1 8 February 2007), https://arxiv.org/pdf/math/0702226.
2. J. Liu and S. J. Wright, *An accelerated randomized Kaczmarz algorithm*, arXiv:1310.2887 (2013), https://arxiv.org/pdf/1310.2887.
3. J. Wang, A. Agaskar and Y. M. Lu, *Randomized Kaczmarz algorithm for inconsistent linear systems: an exact MSE analysis*, arXiv:1502.00190 (2015), https://arxiv.org/pdf/1502.00190.
4. N. F. Marshall and O. Mickelin, *An optimal scheduled learning rate for a randomized Kaczmarz algorithm*, arXiv:2202.12224 (2022), https://arxiv.org/pdf/2202.12224.
5. A. Agaskar, J. Wang and Y. M. Lu, *Randomized Kaczmarz algorithms: exact MSE analysis and optimal sampling probabilities*, 2014, DOI:10.1109/GlobalSIP.2014.7032145 (full text not assessed).
6. Y. Cai, Y. Zhao and Y. Tang, *Exponential convergence of a randomized Kaczmarz algorithm with relaxation*, Advances in Intelligent and Soft Computing 145 (2012), 467–473, DOI:10.1007/978-3-642-28308-6_64 (full text not assessed).
