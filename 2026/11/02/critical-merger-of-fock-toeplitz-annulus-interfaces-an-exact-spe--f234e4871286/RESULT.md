# Critical merger of Fock Toeplitz annulus interfaces: an exact spectral and Schatten crossover

## Finding

Two radial jump interfaces of a Fock Toeplitz indicator cease to behave as independent edges when their separation becomes comparable to the coherent-state width. This regime has a complete Gaussian spectral law and an explicit, strictly increasing trace-defect transition function.

Fix \(R>0\) and \(c>0\). For sufficiently small \(t>0\), let
\[
 A_t=\{z\in\mathbb C:R^2-cR\sqrt t<|z|^2<R^2+cR\sqrt t\},
 \qquad Q_t=T_{\mathbf1_{A_t}}^{(t)}.
\]
Here \(T^{(t)}\) is the Toeplitz compression on the Gaussian Fock space defined below. Let \(\Phi\) denote the standard normal distribution function and put
\[
 L_c(x)=\Phi(x+c)-\Phi(x-c),\qquad x\in\mathbb R.
\]
For every continuous \(F:[0,1]\to\mathbb C\) for which \(|F(u)|\le C u^p\) on \([0,1]\) for some \(C>0\) and \(p>0\), the trace is absolutely convergent and
\[
 \boxed{\lim_{t\downarrow0}\sqrt t\,\operatorname{tr}F(Q_t)
   =R\int_{\mathbb R}F(L_c(x))\,dx.}
\]
The complete positive-eigenvalue counting law is, for \(0<\eta<L_c(0)\),
\[
 \boxed{\lim_{t\downarrow0}\sqrt t\,\#\{\lambda\in\sigma(Q_t):\lambda>\eta\}
    =2R\,x_c(\eta),}
\]
with eigenvalues counted with multiplicity, where \(x_c(\eta)>0\) is the unique solution \(L_c(x_c(\eta))=\eta\). Furthermore,
\[
 \lim_{t\downarrow0}\|Q_t\|=L_c(0)=2\Phi(c)-1.
\]
For every \(p>0\) the semi-commutator \(Q_t^2-Q_t\) belongs to the quasi-Schatten class \(\mathcal S_p\), and
\[
 \boxed{\lim_{t\downarrow0}\sqrt t\,\|Q_t-Q_t^2\|_{\mathcal S_p}^p
   =R\int_{\mathbb R}\big[L_c(x)(1-L_c(x))\big]^p\,dx.}
\]
In particular, the Schatten-one constant has the closed form
\[
 \boxed{\lim_{t\downarrow0}\sqrt t\,\operatorname{tr}(Q_t-Q_t^2)
  =R\left[2c\,\operatorname{erfc}(c)
     +\frac{2}{\sqrt\pi}(1-e^{-c^2})\right].}
\]
The bracketed crossover \(B(c)\) satisfies \(B'(c)=2\operatorname{erfc}(c)>0\), \(B(c)\sim2c\) as \(c\downarrow0\), and \(B(c)\to2/\sqrt\pi\) as \(c\to\infty\). Thus the collapsing-shell regime and the additive two-separated-interface regime are connected by an explicit nonlinear transition.

## Assumptions and scope

The Hilbert space is
\[
 \mathcal F_t^2=\left\{f\text{ entire}:\|f\|_t^2=
  \frac1{\pi t}\int_{\mathbb C}|f(z)|^2e^{-|z|^2/t}\,dA(z)<\infty\right\},
\]
with orthonormal basis \(e_n(z)=z^n/\sqrt{t^n n!}\), \(n\in\mathbb N_0\). The Toeplitz operator is \(T_f^{(t)}=P_t M_f|_{\mathcal F_t^2}\), where \(P_t\) is the orthogonal projection and \(M_f\) is multiplication by \(f\). Parameters \(R,c\) are fixed strictly positive real numbers; \(t\downarrow0\) with \(t<(R/c)^2\), so the inner radial square is positive. The two jump interfaces have squared-radius separation \(2cR\sqrt t\). No smoothness is assumed for the indicator. The counting assertion applies only to fixed \(\eta\) strictly between zero and \(2\Phi(c)-1\); it makes no assertion at a threshold depending on \(t\).

## Proof

**1. Exact radial eigenvalues.** Angular orthogonality diagonalizes \(Q_t\) in the monomial basis. With \(N=R^2/t\) and \(a_N=N-c\sqrt N\), \(b_N=N+c\sqrt N\), polar integration and \(s=|z|^2/t\) give
\[
 \lambda_n(t)=\langle Q_te_n,e_n\rangle_t
  =\frac1{n!}\int_{a_N}^{b_N}s^ne^{-s}\,ds,
  \qquad n\ge0.
\]
Hence \(0<\lambda_n(t)<1\); the eigenvalues tend super-exponentially to zero at fixed \(t\). Thus \(Q_t\) and \(Q_t-Q_t^2\) are in \(\mathcal S_p\) for every \(p>0\). Interchanging the nonnegative integral and the exponential series yields the *exact*, not asymptotic, trace identity
\[
 \operatorname{tr}Q_t=\sum_{n\ge0}\lambda_n(t)
 =\int_{a_N}^{b_N}\sum_{n\ge0}\frac{s^n}{n!}e^{-s}\,ds
 =2c\sqrt N=\frac{2cR}{\sqrt t}.
\]

**2. Local normal limit.** The density \(s^ne^{-s}/n!\) is that of the sum of \(n+1\) independent mean-one exponential random variables. Write \(x_{n,N}=(n-N)/\sqrt N\). On every fixed compact interval \(|x_{n,N}|\le M\), Berry--Esseen applied to this sum (with shape \(n+1\asymp N\)) and the convergence of the standardized endpoints gives, uniformly in these indices,
\[
 \lambda_n(t)=\Phi(c-x_{n,N})-\Phi(-c-x_{n,N})+o(1)
  =L_c(x_{n,N})+o(1).
\]
The displayed equality uses \(\Phi(-u)=1-\Phi(u)\).

**3. Tails and global summability.** For \(Y\) Gamma distributed with positive integer shape \(k\), exponential Markov bounds give
\[
 \mathbb P(Y\ge s)\le e^{-kI(s/k)}\ (s>k),\qquad
 \mathbb P(Y\le s)\le e^{-kI(s/k)}\ (0<s<k),
 \quad I(v)=v-1-\log v.
\]
For fixed \(c\), the inequalities with \(k=n+1\), the appropriate endpoint \(a_N\) or \(b_N\), and the elementary lower bound on \(I(v)\) away from \(v=1\), imply constants \(C_c,\gamma_c>0\) and \(N_c\) such that
\[
 \lambda_n(t)\le C_c\exp\!\left(-\gamma_c\left|\frac{n-N}{\sqrt N}\right|\right),
  \qquad N\ge N_c,\ n\ge0.
\]
Indeed, for \(N/2\le n\le2N\) this follows from a Gaussian \(\exp[-\kappa(n-N)^2/N]\) bound outside the fixed central \(O(\sqrt N)\) window; for \(n<N/2\) and \(n>2N\) the same Chernoff exponent is at least of order \(N\) and \(n\), respectively. On the central window enlarge \(C_c\). Consequently \(\lambda_n^p\) has an exponentially summable uniform envelope in \(x_{n,N}\) for each fixed \(p>0\). Combining this with the uniform compact-window normal limit and mesh \(N^{-1/2}\) proves
\[
 N^{-1/2}\sum_{n\ge0}F(\lambda_n(t))
 \longrightarrow\int_{\mathbb R}F(L_c(x))\,dx
\]
for every stated \(F\); the complex-valued case follows by absolute convergence. Multiplication by \(R\) gives the first boxed formula.

**4. Spectral counting and norm.** Differentiation yields
\[
 L_c'(x)=\varphi(x+c)-\varphi(x-c),
\]
where \(\varphi(u)=(2\pi)^{-1/2}e^{-u^2/2}\). Thus \(L_c\) is even, strictly decreases on \((0,\infty)\), and tends to zero at infinity. The uniform convergence on compact \(x\)-intervals, the global exponential tail estimate, and Riemann counting show that the threshold set converges in rescaled counting measure to \(\{x:L_c(x)>\eta\}=(-x_c(\eta),x_c(\eta))\). The same estimates imply convergence of the spectral maxima to \(L_c(0)\).

**5. Schatten semi-commutators.** The indicator obeys \(\mathbf1_{A_t}^2=\mathbf1_{A_t}\), hence \(D_t(\mathbf1_{A_t},\mathbf1_{A_t})=Q_t^2-Q_t\). Its negative has eigenvalues \(\lambda_n(1-\lambda_n)\ge0\). Apply step 3 with \(F(u)=[u(1-u)]^p\) to obtain the Schatten formula, including \(0<p<1\) without using a triangle inequality.

**6. Closed-form trace crossover.** Set \(G,G'\) independent standard Gaussians. Since \(L_c(x)=\mathbb P(x-c<G<x+c)\), Fubini's theorem gives
\[
 \int_{\mathbb R}L_c(x)\,dx=2c,\qquad
 \int_{\mathbb R}L_c(x)^2\,dx
 =\mathbb E(2c-|G-G'|)_+.
\]
Because \(G-G'\) has density \(e^{-u^2/4}/(2\sqrt\pi)\), elementary integration yields
\[
 \int_{\mathbb R}L_c(x)^2\,dx
 =2c\,\operatorname{erf}(c)
   -\frac2{\sqrt\pi}(1-e^{-c^2}).
\]
Subtract this from \(2c\) and multiply by \(R\). Direct differentiation proves the stated crossover monotonicity; its endpoint limits follow from standard Gaussian tails. Every limit above is therefore determined without an unproved infinite-dimensional extrapolation from finite matrices.

## Verification

The accompanying `verify.py` computes the exact incomplete-Gamma eigenvalues of the *defined* Fock operator, compares their rescaled trace and quasi-Schatten defect sums against numerical Gaussian-profile integrals for several widths and exponents, checks the exact trace identity, the closed-form trace constant, and the strict monotonicity of the crossover derivative. All numerical checks are finite and supplementary; the proof above supplies the infinite-dimensional and asymptotic statements. Run with `python verify.py` using Python 3, NumPy and SciPy.

## Relationship to prior work

Jie Qin's October 22, 2026 preprint establishes sharp general criteria for unnormalized Schatten limits of semi-commutators for **fixed bounded symbols** as the Fock scale varies (arXiv:2610.30787v1, Introduction and Theorems 1.1--1.5). The present indicator \(\mathbf1_{A_t}\) moves with \(t\) on the coherent-state scale, so the fixed-symbol classification does not yield its nonvanishing, rescaled interface-interaction constant. The identity \(Q_t^2-Q_t=D_t(\mathbf1_{A_t},\mathbf1_{A_t})\) puts the result in direct dialogue with that work.

Nicola, Riccardi, and Tilli (arXiv:2503.07069) study partial sums and geometric extrema of Fock Toeplitz eigenvalues, including a special annular optimizer; their results do not give the mesoscopic moving-annulus spectral distribution above. Oldfield's two-term Szegő theorem (arXiv:1404.2256, Theorem 2.4 and Corollary 2.5) describes **dilations of a fixed smooth domain** and a sum of boundary corrections. Here the annulus collapses at the same scale as Gaussian smoothing, so the fixed-domain tubular-neighborhood separation cannot be passed uniformly to this limit. The explicit \(B(c)\) quantifies that missing interaction. Standard Gamma Berry--Esseen and exponential Chernoff bounds provide the local probabilistic proof mechanism and are not claimed as new.

## Limitations

This theorem is for one complex dimension, centered circular annuli with a fixed positive half-width parameter \(c\), and Gaussian Fock Toeplitz quantization. It makes no uniform statement when \(c\) itself varies with \(t\), for non-radial moving domains, for general weights, or for higher-order corrections in \(\sqrt t\). The counting theorem concerns thresholds fixed strictly inside the limiting nonzero spectral range. Independent publication-priority verification has not been performed; an equivalent collapsing-annulus formulation in older localization-operator literature is a residual risk.

## References

1. Jie Qin, *Schatten limits for semi-commutators in Toeplitz quantization on Fock space*, arXiv:2610.30787v1 (first posted October 22, 2026), https://arxiv.org/html/2610.30787v1.
2. Fabio Nicola, Federico Riccardi, and Paolo Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space* (arXiv version of the Faber--Krahn manuscript), arXiv:2503.07069, https://arxiv.org/abs/2503.07069.
3. James P. Oldfield, *Two-term Szegő theorem for generalised anti-Wick operators*, arXiv:1404.2256; *Journal of Spectral Theory* 5 (2015), 751--781, https://arxiv.org/abs/1404.2256.
4. Classical central-limit, Berry--Esseen, and Chernoff estimates for sums of independent exponential random variables, used in their standard elementary forms.
