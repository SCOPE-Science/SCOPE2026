# Marginal multiplicative jump-rate disorder: a sharp three-factor transition in mean first passage

## Finding

A half-line random walk can have a finite physical mean first-passage time at the *marginal* rate-tail exponent \(1/2\) once three independent Pareto rate factors act multiplicatively at every resampling epoch. In contrast, one or two such factors retain an infinite mean, even though the one-factor and three-factor rate distributions have the same algebraic tail index. More generally, a logarithmic factor in the rate tail gives the exact boundary between finite and infinite mean passage.

**Theorem.** Fix an integer \(x\ge1\), a period \(\tau>0\), a tail constant \(k>0\), and \(\beta\in\mathbb R\). Start a nearest-neighbor, symmetric continuous-time random walk \(X\) at \(x\) on the nonnegative integers, with \(0\) absorbing. On each successive period \([j\tau,(j+1)\tau)\), independently sample a strictly positive finite jump rate \(\lambda_j\), and make left or right jumps at half this total rate until absorption. Assume the rates are independent of all symmetric jump directions and satisfy
\[
 \Pr\{\lambda_j>u\}\sim k u^{-1/2}(\log u)^\beta \quad (u\to\infty).
\]
Writing \(T\) for the first hitting time of zero, one has
\[
 \Pr\{T>t\}\sim K_{x,\tau,k,\beta}\,\frac{1}{t[\log(t/\tau)]^\beta},\qquad
 K_{x,\tau,k,\beta}=\frac{2^{3/2-\beta}x\sqrt\tau}{\pi^{3/2}k}.
\]
For every real \(p>0\), \(\mathbb E[T^p]<\infty\) exactly when \(0<p<1\), or \(p=1\) and \(\beta>1\). For \(\beta<1\), the truncated mean satisfies
\[
 \mathbb E[T\wedge t]\sim \frac{K_{x,\tau,k,\beta}}{1-\beta}[\log(t/\tau)]^{1-\beta};
\]
for \(\beta=1\), it is asymptotic to \(K_{x,\tau,k,1}\log\log(t/\tau)\); and for \(\beta>1\),
\[
 \mathbb ET-\mathbb E[T\wedge t]\sim \frac{K_{x,\tau,k,\beta}}{\beta-1}[\log(t/\tau)]^{1-\beta}.
\]

**Concrete multiplicative-rate threshold.** For any integer \(m\ge1\), let every \(\lambda_j\) be a product of \(m\) independent Pareto factors \(U\) with \(\Pr(U>u)=u^{-1/2}\) for \(u\ge1\). Independence holds across periods too. Then
\[
 \Pr(\lambda_j>u)=u^{-1/2}\sum_{\ell=0}^{m-1}\frac{(\log u/2)^\ell}{\ell!}\quad (u\ge1),
\]
and therefore
\[
 \boxed{\Pr(T_m>t)\sim\frac{2^{3/2}x\sqrt\tau\,(m-1)!}{\pi^{3/2}\,t[\log(t/\tau)]^{m-1}}.}
\]
In particular, \(\mathbb E T_m<\infty\) **if and only if** \(m\ge3\). The second and all higher positive moments are infinite for every finite \(m\), despite finite means for \(m\ge3\).

## Assumptions and scope

The walk uses symmetric nearest-neighbor steps with independent exponential holding times conditional on the current rate. Each environmental rate is freshly and independently sampled at deterministic period boundaries; rates are not resampled after every jump. The rate random variables are almost surely strictly positive and finite. The absorption state is irreversible. The start \(x\) is a fixed positive integer as \(t\to\infty\); period \(\tau\) and rate law are fixed. The first asymptotic statement requires the displayed *regularly varying tail equivalence*, not merely two-sided tail bounds. Moment statements refer to physical continuous time, not the number of jumps.

## Proof

**1. Exact spectral time-change.** Let \(Y_s\) be the unit-total-rate simple symmetric continuous-time random walk on \(\mathbb N_0\), killed at zero, and set \(H_t=\int_0^t\lambda_{\lfloor u/\tau\rfloor}\,du\). Conditional on the rate environment, \(X_t\) has the law of \(Y_{H_t}\), so its survival is \(\mathbb E[q_x(H_t)]\), where \(q_x(h)=\Pr_x(\inf\{s:Y_s=0\}>h)\). Diagonalizing the killed discrete Laplacian via the sine transform and summing the half-line heat kernel over positive endpoints yields the exact identity
\[
 q_x(h)=\frac1\pi\int_0^\pi\sin(x\theta)\cot(\theta/2)e^{-h(1-\cos\theta)}\,d\theta.
\]
For integer \(n\ge1\), \(H_{n\tau}=\tau\sum_{j=0}^{n-1}\lambda_j\). With \(\phi(s)=\mathbb E[e^{-s\lambda_0}]\), independence and Fubini therefore give
\[
 S_n:=\Pr(T>n\tau)=\frac1\pi\int_0^\pi\sin(x\theta)\cot(\theta/2)\bigl[\phi(\tau(1-\cos\theta))\bigr]^n\,d\theta.
\]
There is no exchange of divergent sums: for fixed \(x\), the sine-transform kernel is bounded and integrable on \([0,\pi]\); its limit at zero is \(2x\).

**2. Singular rate transform.** Integration by parts for any nonnegative random variable gives
\[
 1-\phi(s)=s\int_0^\infty e^{-su}\Pr(\lambda_0>u)\,du.
\]
The stated tail has power \(-1/2\) with a slowly varying logarithmic factor. Substitution \(v=su\), followed by the standard Potter domination, gives the explicit Karamata Abelian limit
\[
 1-\phi(s)\sim k\sqrt\pi\,s^{1/2}[\log(1/s)]^\beta\quad(s\downarrow0).
\]
Since \(\tau(1-\cos\theta)\sim\tau\theta^2/2\), this becomes
\[
 d(\theta):=1-\phi(\tau(1-\cos\theta))\sim c\,\theta[\log(1/\theta)]^\beta,
 \qquad c=2^{\beta-1/2}k\sqrt{\pi\tau}.
\]
The factor \(2^\beta\) comes from \(\log(1/(\tau\theta^2/2))\sim2\log(1/\theta)\); it is essential for the constant.

**3. Asymptotic spectral integral.** Set \(b_n=n(\log n)^\beta\) for sufficiently large \(n\), and substitute \(\theta=z/b_n\). For each fixed \(z>0\), regular variation gives \(nd(z/b_n)\to cz\), and hence \(\phi(\tau(1-\cos(z/b_n)))^n\to e^{-cz}\). The prefactor \(\sin(x\theta)\cot(\theta/2)/\pi\) tends to \(2x/\pi\). To justify passage through the integral: for any small \(\epsilon\in(0,1)\), Potter's inequalities bound \(d(\theta)\) below by a positive multiple of \(d(1/b_n)(b_n\theta)^{1-\epsilon}\) for \(1/b_n\le\theta\le\theta_0\); consequently the rescaled integrand is dominated outside \(z\in[0,1]\) by a multiple of \(\exp(-c_0z^{1-\epsilon})\). On \(0\le z\le1\), the bounded kernel supplies an integrable majorant. Finally, for \(\theta\ge\theta_0\), \(\phi(\tau(1-\cos\theta))\le q<1\) uniformly, so that contribution is exponentially small even after multiplying by \(b_n\). Dominated convergence gives
\[
 b_nS_n\longrightarrow\frac{2x}{\pi}\int_0^\infty e^{-cz}\,dz=\frac{2x}{\pi c}.
\]
Putting \(t=n\tau\) and noting \(n=t/\tau\), the constant becomes \(K_{x,\tau,k,\beta}=2^{3/2-\beta}x\sqrt\tau/(\pi^{3/2}k)\). Between two period endpoints, survival is monotone; bounding \(S(t)\) by its neighboring values and using their ratio limit proves the same equivalent for every real \(t\to\infty\).

**4. Moments and the exact product model.** For \(p>0\), the layer-cake identity \(\mathbb E[T^p]=p\int_0^\infty t^{p-1}\Pr(T>t)\,dt\) converts the proved survival equivalent into comparison with \(\int^\infty t^{p-2}(\log t)^{-\beta}\,dt\). At \(p=1\) this converges exactly for \(\beta>1\). The truncated-mean equivalents follow by integrating the survival asymptotic; in the \(\beta>1\) case integrate from \(t\) to infinity. For the Pareto product, \(V_i=\log U_i\) are independent exponential random variables of rate \(1/2\), so \(\log\lambda_j\) is Gamma with integer shape \(m\). Its Erlang survival function gives the exact polynomial-tail identity, with \(k=1/[2^{m-1}(m-1)!]\) and \(\beta=m-1\). Substituting these values produces the displayed constant and shows the mean-finiteness transition occurs precisely between two and three independent rate factors.

## Verification

The included standalone Python 3 program `verify.py` uses no third-party packages. Execute `python3 verify.py` to check the Gamma-product tail against independent density quadrature, its low-frequency Laplace transform, the killed-walk spectral kernel and an independent modified-Bessel identity for a deterministic rate, and selected exact finite-epoch spectral integrals against the predicted large-time scaling. The program reports 71 deterministic assertions. All numerical tests are finite checks, not a proof of the infinite-time asymptotic; the proof above supplies that conclusion.

## Relationship to prior work

Levit and Reuveni (2026, arXiv:2609.26925) derive the rate-mixed half-line first-passage transform and identify a finite/infinite mean transition for pure algebraic rate tails, using a constant multiple of \(s^\alpha\) at small Laplace argument. Their analysis supplies the natural starting point and the fundamental spectral method. The present theorem isolates the **marginal** exponent \(1/2\), where a slowly varying logarithmic factor changes mean integrability; the pure-power hypothesis and strict-index dichotomy alone do not determine this boundary. The exact three-factor construction is a specific mechanism for generating the logarithmic factor.

Arutkin and Reuveni (2023, arXiv:2302.07041) introduce the doubly stochastic continuous-time random walk and its time-change framework. Their first-passage discussion includes bounded-domain settings and does not provide this stated marginal log-Pareto half-line integrability classification in the inspected material. Angstmann and collaborators (2025, arXiv:2511.18256) analyze space-fractional first-passage exponents for different subordinated dynamics; this is relevant fractional-process context, not a claim of priority for the same period-resampled product-rate model. The Abelian step is standard regular-variation theory and is not itself presented as novel.

## Limitations

This is an asymptotic result for fixed \(x\), fixed \(\tau\), and independent rate blocks; no uniformity in these parameters, in \(\beta\), or in the number of factors is claimed. The survival law alone does not give full hitting-time distributional convergence under different scalings. The environment changes at deterministic times, not at jumps; ergodic or correlated rate environments are outside scope. The result is accompanied by an internal best-knowledge literature comparison, not an independent publication-priority audit. Earlier literature on borderline random time changes may contain equivalent general statements, and this residual risk should be considered before publication.

## References

- Levit and Reuveni, *First Passage in the Presence of Jump Rate Fluctuations: A Transition from Infinite to Finite Mean*, arXiv:2609.26925, first publicly submitted 2026-09-22. https://arxiv.org/abs/2609.26925
- Arutkin and Reuveni, *Doubly Stochastic Continuous Time Random Walk*, arXiv:2302.07041 (2023). https://arxiv.org/abs/2302.07041
- Angstmann et al., *First-Passage Times for the Space-Fractional Spectral Fokker-Planck Equation*, arXiv:2511.18256 (2025). https://arxiv.org/abs/2511.18256
- Bingham, Goldie and Teugels, *Regular Variation*, Cambridge University Press (1987), for standard slowly varying and Potter-bound methods.
